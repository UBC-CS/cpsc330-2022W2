# UBC CPSC 330: Applied Machine Learning (2022W2)

## Introduction

This is the course homepage for CPSC 330: Applied Machine Learning at the University of British Columbia. You are looking at the current version (Jan-Apr 2023). Earlier versions can be found at these links:
* [from Sep-Dec 2020 taught by Mike Gelbart](https://github.com/UBC-CS/cpsc330/tree/v2.0)
* [from Jan-April 2022 taught by Giulia Toti](https://github.com/UBC-CS/cpsc330-2021W2)
* [from May-June 2022 taught by Mehrdad Oveisi](https://github.com/UBC-CS/cpsc330-2022s)
* [from Sep-Dec 2022 taught by Varada Kolhatkar](https://github.com/UBC-CS/cpsc330)


Instructors: Giulia Toti (201), Mathias Lecuyer (202), Amir Abdi (203)

## Important links

* [Course GitHub page](https://github.com/UBC-CS/cpsc330-2022W2)
* [Course Jupyter book](https://ubc-cs.github.io/cpsc330/README.html). **Important:** this is a static version of the lecture notebooks developed by a previous instructor of the course. It can be used as reference for the content, but not for anything related to the particular course instance (due dates, setup steps, etc.)
* [Course videos YouTube channel](https://www.youtube.com/playlist?list=PLHofvQE1VlGtZoAULxcHb7lOsMved0CuM)
* [Canvas link](https://canvas.ubc.ca/courses/106375)
* [Syllabus / administrative info](docs/course_info.md)
* [Piazza](https://piazza.com/ubc.ca/winterterm22023/cpsc3302012022032022w2/home) (this is where all announcements will be made). [Click here to enroll](https://piazza.com/ubc.ca/winterterm22023/cpsc3302012022032022w2).
* [Other course documents](https://github.com/UBC-CS/cpsc330-2022W2/tree/main/docs)
* [Past exams](https://github.com/UBC-CS/cpsc330/tree/master/exams)

## Deliverable due dates (tentative)
Usually the homework assignments will be due on Mondays and will be released on Tuesdays.

|Assessment  | Due date |  Where to find? | Where to submit? | Weight (%) |
|-------|-----------|-----------|-----------|-----|
| Syllabus quiz | Jan 16, 11:59pm  | [Canvas](https://canvas.ubc.ca/courses/106375/quizzes/584868) | [Canvas](https://canvas.ubc.ca/courses/106375/quizzes/584868) |  1% |
| hw1 | Jan 16, 11:59pm |  [Github repo](https://github.com/UBC-CS/cpsc330-2022W2/tree/main/hw) | [Gradescope](https://www.gradescope.ca/courses/9483)| 3% | 
| hw2 | Jan 23, 11:59pm |   [Github repo](https://github.com/UBC-CS/cpsc330-2022W2/tree/main/hw) | [Gradescope](https://www.gradescope.ca/courses/9483)| 3% |
| hw3 | Feb 1, 11:59pm |   [Github repo](https://github.com/UBC-CS/cpsc330-2022W2/tree/main/hw) | [Gradescope](https://www.gradescope.ca/courses/9483)| 4% | 
| hw4 | Feb 10, 11:59pm  |   [Github repo](https://github.com/UBC-CS/cpsc330-2022W2/tree/main/hw) | [Gradescope](https://www.gradescope.ca/courses/9483)| 4% |
| **Midterm** | Feb 15 **Wednesday** | TBD | TBD | 19 % |
| hw5 | March 1, 11:59pm |   [Github repo](https://github.com/UBC-CS/cpsc330-2022W2/tree/main/hw) | [Gradescope](https://www.gradescope.ca/courses/9483)| 4% | 
| hw6 | Mar 15, 11:59pm |   [Github repo](https://github.com/UBC-CS/cpsc330-2022W2/tree/main/hw) | [Gradescope](https://www.gradescope.ca/courses/9483)| 5% | 
| hw7 | Mar 22, 11:59pm  |   [Github repo](https://github.com/UBC-CS/cpsc330-2022W2/tree/main/hw) | [Gradescope](https://www.gradescope.ca/courses/9483)| 4% |  
| hw8 | TBD, 11:59pm |   [Github repo](https://github.com/UBC-CS/cpsc330-2022W2/tree/main/hw) | [Gradescope](https://www.gradescope.ca/courses/9483)|  3% |
| **Final exam** | Apr 20, 7:00pm | TBD | TBD | 50% |



## Lecture schedule (tentative)

Lectures will be on Tuesday and Thursday. Exact time and location change according to your section:
| Section  | Day  | Time   | Location |
|----------|----------|--------|------|
| 201 | Tue/Thu  |  2:00 - 3:30 | Geography 100 |
| 202 | Tue/Thu  |  3:30 - 5:00 | P. A. Woodward Instructional Resources Centre 3 |
| 203 | Tue/Thu  |  5:00 - 6:30 | Hugh Dempster Pavilion 310 |


**Lectures**: 
- Watch the "Pre-watch" videos before each lecture. 
- You will find lecture notes from each instructor in this repository. Lectures will be posted as they become available. 

| Date  | Topic | Assigned videos and datasets                                                                                                                                                                                                                                                                        | vs. CPSC 340 |
|-------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Jan 10 | Course intro | 📹 <li>Pre-watch: None</li><li>Recap video (after lecture): [1.0](https://youtu.be/-1hTcS5ZE4w)</li>                                                                                                                                                                                                | n/a|
|  | **Part I: ML fundamentals and preprocessing**  |                                                                                                                                                                                                                                                               
|  | | **Week 1 datasets:** <li>[grade prediction toy dataset](lectures/data/quiz2-grade-toy-classification.csv)</li><li>[Canada USA cities toy dataset](lectures/data/canada_usa_cities.csv)</li><li>[Housing Prices](https://www.kaggle.com/harlfoxem/housesalesprediction)</li>                         | |                                                                                                                                                                                                                                                                                                
| Jan 12 | Decision trees | 📹 <li>Pre-watch: [2.1](https://youtu.be/YNT8n4cXu4A), [2.2](https://youtu.be/6eT5cLL-2Vc)</li> <li>After lecture: [2.3](https://youtu.be/Hcf19Ij35rA), [2.4](https://youtu.be/KEtsfXn4w2E)</li>                                                                                                    |   less depth| 
| Jan 17 | ML fundamentals | 📹  <li> Pre-watch: [3.1](https://youtu.be/iS2hsRRlc2M), [3.2](https://youtu.be/h2AEobwcUQw)</li> <li>After lecture: [3.3](https://youtu.be/4cv8VYonepA), [3.4](https://youtu.be/Ihay8yE5KTI)</li>                                                                                                  | similar |
|        |     | **Week 2 datasets:** <li>[California housing](https://www.kaggle.com/harrywang/housing)</li><li>[Spotify Song Attributes](https://www.kaggle.com/geomack/spotifyclassification/home)</li>                                                                                                           | |
| Jan 19 | $k$-NNs and SVM with RBF kernel | 📹  <li> Pre-watch: [4.1](https://youtu.be/hCa3EXEUmQk), [4.2](https://youtu.be/bENDqXKJLmg)</li> <li>After lecture: [4.3](https://youtu.be/IRGbqi5S9gQ), [4.4](https://youtu.be/ic_zqOhi020)</li>                                                                                                  | less depth |
| Jan 24 | Preprocessing, `sklearn` pipelines | 📹  <li> Pre-watch: [5.1](https://youtu.be/xx9HlmzORRk), [5.2](https://youtu.be/G2IXbVzKlt8)</li><li>After lecture: [5.3](https://youtu.be/nWTce7WJSd4), [5.4](https://youtu.be/2mJ9rAhMMl0)</li>                                                                                                   |  more depth|
|        |     | **Week 3 dataset:** <li>[California housing](https://www.kaggle.com/harrywang/housing)</li>                                                                                                                                                                                                         | |
| Jan 26 | More preprocessing, `sklearn` `ColumnTransformer`, text features | 📹  <li> Pre-watch: [6.1](https://youtu.be/to2mukSyvLk), [6.2](https://youtu.be/hteVvLwrWZ4)</li>                                                                                                                                                                                                   | more depth |
|        |     | **Week 4 datasets**: <li>[IMDB movie review](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)</li>                                                                                                                                                                         | |
| Jan 31 | Linear models | 📹  <li> Pre-watch: [7.1](https://youtu.be/HXd1U2q4VFA), [7.2](https://youtu.be/56L5z_t22qE), [7.3](https://youtu.be/_OAK5KiGLg0)</li>                                                                                                                                                              |   less depth |
|        |     | **Week 5 datasets**: <li>[Spotify Song Attributes](https://www.kaggle.com/geomack/spotifyclassification/home)</li><li>[Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)</li>                                                                                            | |
| Feb 2 | Hyperparameter optimization, overfitting the validation set | 📹  <li> Pre-watch: [8.1](https://youtu.be/lMWdHZSZMk8),[8.2](https://youtu.be/Z9a9XZ0vQv0)</li>                                                                                                                                                                                                    |   different|
| Feb 7 | Evaluation metrics for classification  | 📹  <li> Pre-watch: [9.2](https://youtu.be/ZCuCErW5lI8),[9.3](https://youtu.be/XkCTUuoH23c),[9.4](https://youtu.be/jHaKRCFb6Qw)</li>                                                                                                                                                                | more depth |
|        |     | **Week 6 datasets**: <li>[Kaggle House Prices data set](https://www.kaggle.com/c/home-data-for-ml-course/)</li> <li>[Adult Census Income](https://www.kaggle.com/uciml/adult-census-income#)</li>                                                                                                   | |
| Feb 9 | Regression metrics | 📹 <li>Pre-watch: [10.1](https://youtu.be/lgGTKLwNgkQ)</li>                                                                                                                                                                                                                                         |   more depth on metrics less depth on regression|
| Feb 14 | Midterm review |                                                                                                                                                                                                                                                                                                     |
| Feb 15 | **Midterm**  | **On Wednesday! Note the different time!** More details will be posted on Piazza                                                                                                                                                                                                                    | 
| Feb 16 | No lecture |                                                                                                                                                                                                                                                                                                     | 
| Feb 19-25 | **Reading week (no classes)**  |                                                                                                                                                                                                                                                                                                     | 
|        |     | **Week 7 datasets**: <li>[Adult Census Income](https://www.kaggle.com/uciml/adult-census-income#)</li> <li>[Credit Card Dataset for Clustering](https://www.kaggle.com/arjunbhasin2013/ccdata)</li>                                                                                                 | |
| Feb 28 | Ensembles | 📹 <li>Pre-watch: [11.1](https://youtu.be/8litm1H7DLo),[11.2](https://youtu.be/EkFkY9QB2Hw)</li>                                                                                                                                                                                                    | similar |
| Mar 2 | Feature importances, model interpretation | 📹 <li>Pre-watch: [12.1](https://youtu.be/xfICsGL7DXE),[12.2](https://youtu.be/tiSN18OmZOo)</li>                                                                                                                                                                                                    | feature importances is new, feature engineering is new |
| Mar 7 |   Feature engineering and feature selection | None                                                                                                                                                                                                                                                                                                | less depth |
|  | **Part II: Unsupervised learning, transfer learning, different learning settings**  |                                                                                                                                                                                                                                                                                                     | 
| Mar 9 |   Clustering | 📹 <li>Pre-watch: [14.1](https://youtu.be/caAuUAXwpb8),[14.2](https://youtu.be/s6AvSZ1_l7I),[14.3](https://youtu.be/M5ilrhcL0oY)</li>                                                                                                                                                               | less depth |
| Mar 14 |   More clustering | <li> Post-lecture: [15.1](https://youtu.be/1ZwITQyWpkY), [15.2](https://youtu.be/T4NLsrUaRtg), [15.3](https://youtu.be/NM8lFKFZ2IU), [201 lecture recording](https://ubc.zoom.us/rec/share/w5u5E2wogGUTcwYvRbHd-TH7ix4WwY1JXrlvd7WvqD6ERjg7eYOApKcvsn0uZkom.QVa__I6MgP-d4ji_?startTime=1678844657000)</li>                                                                                                                                                                                                                                                                                               | less depth |
|        |  | **Week 9 datasets**: <li>[Jester 1.7M jokes ratings dataset](https://www.kaggle.com/vikashrajluhaniwal/jester-17m-jokes-ratings-dataset)</li>                                                                                                                                                       |
| Mar 16 |   Simple recommender systems |      None                                                                                                                                                       | less depth ||
| Mar 21 |  Text data, embeddings, topic modeling  | 📹 <li>Pre-watch: [16.1](https://youtu.be/GTC_iLPCjdY),[16.2](https://youtu.be/7W5Q8gzNPBc)</li>                                                                                                                                                                                                    |   new |
| Mar 23 | Neural networks and computer vision |                                                                                                                                                                                                                                                                                                     |   less depth |
| Mar 28 | Time series data | (Optional) [Humour: The Problem with Time & Timezones](https://www.youtube.com/watch?v=-5wpm-gesOY)                                                                                                                                                                                                 | new |
| Mar 30 | Survival analysis | 📹 (Optional but highly recommended)[Calling Bullshit 4.1: Right Censoring](https://www.youtube.com/watch?v=ITWQ5psx9Sw)                                                                                                                                                                            |   new |
|  | **Part III: Communication, ethics, deployment**  |                                                                                                                                                                                                                                                                                                     |
| April 4  |  Ethics | 📹 (Optional but highly recommended) <li>[Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 5 (6 short videos, 50 min total)</li> <li>[The ethics of data science](http://jtleek.com/ads2020/week-15.html)</li>                                  | new |
| Apr 6 | Communication | 📹 (Optional but highly recommended) <li>[Calling BS videos](https://www.youtube.com/playlist?list=PLPnZfvKID1Sje5jWxt-4CSZD7bUI4gSPS) Chapter 6 (6 short videos, 47 min total)</li> <li>[Can you read graphs? Because I can't.](https://www.youtube.com/watch?v=vbDObzI-CTc) by Sabrina (7 min)</li> |   new |
| Apr 11 | Model deployment |                                                                                                                                                                                                                                                                                                     |  new |
| Apr 13 | Conclusions - TBD |                                                                                                                                                                                                                                                                                                     |  new |

