import numpy as np 
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import xlwings as xw 

# Code for Interactive decision-making dashboard

def main():

    '''
    Input: Imported Data from Excel sheet cells
    Scenario calculation: Rewrite the dataset with the new input
    Output: Result of new prediction
    '''

    # ----> SCENARIO ANALYSIS <----
    # let's connect python with excel through xlwings in order to connect the data with ActiveGraf, an interactive scenario analysis tool
    # xlwings caller
    sht = xw.Book.caller().sheets['Sheet1']

    # import cleaned dataset
    df = pd.read_csv(r"C:\Users\BernadettKepenyes\Documents\GitHub\employee-burnout\clean_df_train.csv")
    
    # mean of MFS
    MFS_mean = df['Mental Fatigue Score'].mean()

    # Effect of Company Health Program on "Mental Fatigue Score"
    MFS_effect = 1 - sht.range('C3:C3').value

    # change data
    df_copy = df.copy()
    df_copy['Mental Fatigue Score'] = df_copy['Mental Fatigue Score']*MFS_effect

    # new mean of MFS
    MFS_mean_new = df_copy['Mental Fatigue Score'].mean()

    # linear regression
    X = df[['Gender','Company Type','WFH Setup Available','Designation','Resource Allocation','Mental Fatigue Score','days_count']]
    y = df['Burn Rate']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    lm_model = LinearRegression(normalize=True)
    lm_model.fit(X_train, y_train)

    y_preds = lm_model.predict(X_test)
    mean = y_preds.mean()

    X_test = df_copy[['Gender','Company Type','WFH Setup Available','Designation','Resource Allocation','Mental Fatigue Score','days_count']]
    X_test_train, X_test_test, y_test_train, y_test_test = train_test_split(X_test, y, test_size=0.2, random_state=42)

    y_preds_test = lm_model.predict(X_test_test)
    mean_test = y_preds_test.mean()

    # Return the output to excel
    sht.range('C5:C5').value = mean
    sht.range('C6:C6').value = mean_test
    sht.range('C8:C8').value = MFS_mean
    sht.range('C9:C9').value = MFS_mean_new
