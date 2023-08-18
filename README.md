
# Premier League Relegation predictor

I created a Logistic regression model from Premier League standing data from 1996-2022 to predict whether a team would be relegated based on wins,losses, draws and goal differential.




## Exploratory Data Analysis(EDA)

When I first apporached the data, I first wanted to check for any discrepencies . The data covered Premier League standings from 1992-2022. From 1992-1995, the Premier League hads 23 teams. After the 1995 season, they reduced the teams to 20. Therefore, data from 1992-1995 needed to be removed.

Next I wanted to see the relationships that exist in the data. The follwoing graphs show realtionships between  wins,losses, draws and goal differential. Orange points represent teams that were relegated.



<p align="center">
  <img src="/Users/anshulprasad/Desktop/1bce132b-885d-4349-9d62-ca3c7eeb7499.png" width="350" >
  <img src="/Users/anshulprasad/Desktop/ca56e9aa-f903-4ab7-9d30-28370a024f0e.png" width="350" >
</p>


Loooking at this data, I realized that there exists a linear boundry between relegated teams and teams that survived. From this, I realized that for my use case, a logistic regression model would be best. In order to prep the data for training. I needed to label teams that finished 18-20th as relegated.

## Model

I used the scikit-learn libary to create a logistic regression model. I spilt the data 80:20 with 80% being used for training and 20% being used for testing to avoid overfiting.

Accuracy is around 95-99%

I stored the model in an object where it could be easliy delpoyed on any application

This is how you import and initalize the model:
```
from logistic_model import PremierLeagueRelegationPredictor


model = PremierLeagueRelegationPredictor()
model.train()

```