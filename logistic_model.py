import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

class PremierLeagueRelegationPredictor:
    
    '''
    Reads in data for model stored in league_tables.csv
    '''
    def __init__(self):
        self.epl_results = pd.read_csv("league_tables.csv")

    '''
    This cleans data for preparation
    '''
    def data_preparation(self):

        #Remnove data samples when premier league had 23 teams. This ended the year 1995
        self.epl_results = self.epl_results[self.epl_results['Season_End_Year'] > 1995]


        altered_data_set =  self.epl_results[['W','D','L','GD','Rk']]
        altered_data_set['Status'] = ["Relegated" if x > 17 else "Survived" for x in altered_data_set['Rk'] ]
        altered_data_set['Class'] = [ 0 if x == "Relegated" else 1 for x in altered_data_set['Status'] ]

        return altered_data_set
    

    
    '''
    creates a Logistic regression model that anaylsizes Wins, Losses , Draws and Goal difference to see where a 
    team would be relegated or not. 

    classes are resembled with1 being survived and being relegated.

    data is also split into training set and testing set with 80:20 training to test ratio.

    returns a scikit-learn logistic regression model 
    '''
    def train(self):
        preped_data = self.data_preparation()
        training,test = train_test_split(preped_data,test_size=0.2)
        model = LogisticRegression()
        model.fit(training[['W','D','L','GD']],training['Class'])   
        score = model.score(test[['W','D','L','GD']], test['Class'])
        print("Model accuracy : " + str(score))        
        return model
    

