import os.path
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class LinReg:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Obtain R2 score 
    def r_sq(self):
        model = LinearRegression().fit(x, y)
        r_sq = model.score(x, y)  
        print('coefficient of determination:', r_sq)

    # Obtain intercept b0
    def intc(self):
        model = LinearRegression().fit(x, y)        
        print('intercept:', model.intercept_)

    # Obtain coefficient b1, b2, bi
    def coef(self):
        model = LinearRegression().fit(x, y)
        print('coefficient(s):', model.coef_)

    # Obtain estimated responses         (Same: y_pred = model.intercept_ + np.sum(model.coef_ * x, axis=1))
    def pred(self, dat):
        model = LinearRegression().fit(x, y)
        y_pred = model.predict(dat)
        print('predicted response:', y_pred, sep='\n')


# Get actuals into dataframe
location = 'C:\\Users\\970jwillems\\OneDrive - Sonova\\Development-Data Analysis\\Forecast Model\\'
file =  'data_actuals.xlsx'
filepath = os.path.join(location, file)
df = pd.read_excel(filepath)

# Define and shape model data
x1 = df['marketing_costs'].to_numpy()           # Regressor 1 = Marketing spend
x2 = df['marketing_costs_facebook'].to_numpy()  # Regressor 2 = Marketing spend Facebook
x3 = df['marketing_costs_taboola'].to_numpy()   # Regressor 3 = Marketing spend Taboola
x4 = df['marketing_costs_gdn'].to_numpy()       # Regressor 4 = Marketing spend GDN (Google Display)
#x5 = df['seasonality_period'].to_numpy()       # Regressor 5 = Seasonality period
x6 = df['low_season'].to_numpy()                # Regressor 6 = Low season (dummy)
x7 = df['high_season'].to_numpy()               # Regressor 7 = High season (dummy)
x = np.vstack((x1, x2, x3, x4, x6, x7)).T       # Shape into 6D horizontal array (.T -> transpose)
y = df['total_qualified_leads'].to_numpy()      # Dependent variable = Qualfied leads

# Model outcome/attributes
fcm = LinReg(x,y)
fcm.r_sq()
fcm.intc()
fcm.coef()

# Check against actuals
x_act = [[431704, 231545, 98884, 16600, 1, 0],     #2021-02
         [469335, 256048, 126209, 0, 1, 0],        #2021-01
         [364162, 211179, 52152, 32908, 0, 0],     #2020-11
         [215840, 124512, 36559, 0, 0, 0]]         #2020-09
fcm.pred(x_act)

# Forecast
x_fc = [[568000, 125000, 130000, 62000, 0, 1],     #2021-03
        [475000, 100000, 100000, 50000, 0, 0]]     #2021-04
fcm.pred(x_fc)

##Add comment






