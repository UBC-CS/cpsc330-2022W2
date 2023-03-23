import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, colorConverter

cm3 = ListedColormap(['#0000aa', '#ff2020', '#50ff50'])
cm2 = ListedColormap(['#0000aa', '#ff2020'])


def plot_2d_separator(classifier, X, fill=False, ax=None, eps=None, alpha=1,
                      cm=cm2, linewidth=None, threshold=None,
                      linestyle="solid"):
    # binary?
    if eps is None:
        eps = X.std() / 2.

    if ax is None:
        ax = plt.gca()

    x_min, x_max = X[:, 0].min() - eps, X[:, 0].max() + eps
    y_min, y_max = X[:, 1].min() - eps, X[:, 1].max() + eps
    xx = np.linspace(x_min, x_max, 1000)
    yy = np.linspace(y_min, y_max, 1000)

    X1, X2 = np.meshgrid(xx, yy)
    X_grid = np.c_[X1.ravel(), X2.ravel()]
    
    try:
        decision_values = classifier.decision_function(X_grid)
        levels = [0] if threshold is None else [threshold]
        fill_levels = [decision_values.min()] + levels + [
            decision_values.max()]
    except AttributeError:
        # no decision_function
        decision_values = classifier.predict_proba(X_grid)[:, 1]
        levels = [.5] if threshold is None else [threshold]
        fill_levels = [0] + levels + [1]
    if fill:
        ax.contourf(X1, X2, decision_values.reshape(X1.shape),
                    levels=fill_levels, alpha=alpha, cmap=cm)
    else:
        ax.contour(X1, X2, decision_values.reshape(X1.shape), levels=levels,
                   colors="black", alpha=alpha, linewidths=linewidth,
                   linestyles=linestyle, zorder=5)

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(())
    ax.set_yticks(())




def discrete_scatter(x1, x2, y=None, markers=None, s=10, ax=None,
                     labels=None, padding=.2, alpha=1, c=None, markeredgewidth=None):
    """Adaption of matplotlib.pyplot.scatter to plot classes or clusters.
    Parameters
    ----------
    x1 : nd-array
        input data, first axis
    x2 : nd-array
        input data, second axis
    y : nd-array
        input data, discrete labels
    cmap : colormap
        Colormap to use.
    markers : list of string
        List of markers to use, or None (which defaults to 'o').
    s : int or float
        Size of the marker
    padding : float
        Fraction of the dataset range to use for padding the axes.
    alpha : float
        Alpha value for all points.
    """
    if ax is None:
        ax = plt.gca()

    if y is None:
        y = np.zeros(len(x1))

    unique_y = np.unique(y)

    if markers is None:
        markers = ['o', '^', 'v', 'D', 's', '*', 'p', 'h', 'H', '8', '<', '>'] * 10

    if len(markers) == 1:
        markers = markers * len(unique_y)

    if labels is None:
        labels = unique_y

    # lines in the matplotlib sense, not actual lines
    lines = []

    current_cycler = mpl.rcParams['axes.prop_cycle']

    for i, (yy, cycle) in enumerate(zip(unique_y, current_cycler())):
        mask = y == yy
        # if c is none, use color cycle
        if c is None:
            color = cycle['color']
        elif len(c) > 1:
            color = c[i]
        else:
            color = c
        # use light edge for dark markers
        if np.mean(colorConverter.to_rgb(color)) < .4:
            markeredgecolor = "grey"
        else:
            markeredgecolor = "black"

        lines.append(ax.plot(x1[mask], x2[mask], markers[i], markersize=s,
                             label=labels[i], alpha=alpha, c=color,
                             markeredgewidth=markeredgewidth,
                             markeredgecolor=markeredgecolor)[0])

    if padding != 0:
        pad1 = x1.std() * padding
        pad2 = x2.std() * padding
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        ax.set_xlim(min(x1.min() - pad1, xlim[0]), max(x1.max() + pad1, xlim[1]))
        ax.set_ylim(min(x2.min() - pad2, ylim[0]), max(x2.max() + pad2, ylim[1]))

    return lines

def plot_2d_classification(classifier, X, fill=False, ax=None, eps=None,
                           alpha=1, cm=cm3):
    # multiclass
    if eps is None:
        eps = X.std() / 2.

    if ax is None:
        ax = plt.gca()

    x_min, x_max = X[:, 0].min() - eps, X[:, 0].max() + eps
    y_min, y_max = X[:, 1].min() - eps, X[:, 1].max() + eps
    xx = np.linspace(x_min, x_max, 1000)
    yy = np.linspace(y_min, y_max, 1000)

    X1, X2 = np.meshgrid(xx, yy)
    X_grid = np.c_[X1.ravel(), X2.ravel()]
    decision_values = classifier.predict(X_grid)
    ax.imshow(decision_values.reshape(X1.shape), extent=(x_min, x_max,
                                                         y_min, y_max),
              aspect='auto', origin='lower', alpha=alpha, cmap=cm)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_xticks(())
    ax.set_yticks(())


def plot_logistic_regression_graph():
    import graphviz
    lr_graph = graphviz.Digraph(node_attr={'shape': 'circle', 'fixedsize': 'True'},
                                graph_attr={'rankdir': 'LR', 'splines': 'line'})
    inputs = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_0")
    output = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_2")

    for i in range(4):
        inputs.node("x[%d]" % i, labelloc="c")
    inputs.body.append('label = "inputs"')
    inputs.body.append('color = "white"')

    lr_graph.subgraph(inputs)

    output.body.append('label = "output"')
    output.body.append('color = "white"')
    output.node("y")

    lr_graph.subgraph(output)

    for i in range(4):
        lr_graph.edge("x[%d]" % i, "y", label="w[%d]" % i)
    return lr_graph



def plot_single_hidden_layer_graph():
    import graphviz
    nn_graph = graphviz.Digraph(node_attr={'shape': 'circle', 'fixedsize': 'True'},
                                graph_attr={'rankdir': 'LR', 'splines': 'line'})

    inputs = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_0")
    hidden = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_1")
    output = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_2")

    for i in range(4):
        inputs.node("x[%d]" % i)

    inputs.body.append('label = "inputs"')
    inputs.body.append('color = "white"')

    hidden.body.append('label = "hidden layer"')
    hidden.body.append('color = "white"')

    for i in range(3):
        hidden.node("h%d" % i, label="h[%d]" % i)

    output.node("y")
    output.body.append('label = "output"')
    output.body.append('color = "white"')

    nn_graph.subgraph(inputs)
    nn_graph.subgraph(hidden)
    nn_graph.subgraph(output)

    for i in range(4):
        for j in range(3):
            nn_graph.edge("x[%d]" % i, "h%d" % j)

    for i in range(3):
        nn_graph.edge("h%d" % i, "y")
    return nn_graph

def plot_two_hidden_layer_graph():
    import graphviz
    nn_graph = graphviz.Digraph(node_attr={'shape': 'circle', 'fixedsize': 'True'},
                                graph_attr={'rankdir': 'LR', 'splines': 'line'})

    inputs = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_0")
    hidden = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_1")
    hidden2 = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_2")

    output = graphviz.Digraph(node_attr={'shape': 'circle'}, name="cluster_3")

    for i in range(4):
        inputs.node("x[%d]" % i)

    inputs.body.append('label = "inputs"')
    inputs.body.append('color = "white"')

    for i in range(3):
        hidden.node("h1[%d]" % i)

    for i in range(3):
        hidden2.node("h2[%d]" % i)

    hidden.body.append('label = "hidden layer 1"')
    hidden.body.append('color = "white"')

    hidden2.body.append('label = "hidden layer 2"')
    hidden2.body.append('color = "white"')

    output.node("y")
    output.body.append('label = "output"')
    output.body.append('color = "white"')

    nn_graph.subgraph(inputs)
    nn_graph.subgraph(hidden)
    nn_graph.subgraph(hidden2)

    nn_graph.subgraph(output)

    for i in range(4):
        for j in range(3):
            nn_graph.edge("x[%d]" % i, "h1[%d]" % j, label="")

    for i in range(3):
        for j in range(3):
            nn_graph.edge("h1[%d]" % i, "h2[%d]" % j, label="")

    for i in range(3):
        nn_graph.edge("h2[%d]" % i, "y", label="")

    return nn_graph
