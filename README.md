### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [Dataset](#dataset)
4. [File Descriptions](#files)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python.  The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

For this project, I used HackerEarth data to better understand the factors that leads to employee fatigue [here](https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-predict-burnout-rate/). The task was to understand and observe the mental health of all the employees in the company by predicting the burn rate of employees based on the provided features. Prediction of the employee burn rate is based on factors such as WFH setup, resources, mental fatigue score.

Questions to be answered:
- How remote work affect burn rate?
- How well can we predict an individual's burn rate? 
- What aspects correlate well to burn rate?
+1 What are the costs of work related stress at the organizational level? 

## Dataset<a name="dataset"></a>

Employee ID: The unique ID allocated for each employee (example: fffe390032003000)
Date of Joining: The date-time when the employee has joined the organization (example: 2008-12-30)
Gender: The gender of the employee (Male/Female)
Company Type: The type of company where the employee is working (Service/Product)
WFH Setup Available: Is the work from home facility available for the employee (Yes/No)
Designation: The designation of the employee of work in the organization. In the range of [0.0, 5.0] bigger is higher designation.
Resource Allocation: The amount of resource allocated to the employee to work, ie. number of working hours. In the range of [1.0, 10.0] (higher means more resource)
Mental Fatigue Score: The level of fatigue mentally the employee is facing. In the range of [0.0, 10.0] where 0.0 means no fatigue and 10.0 means completely fatigue.
Burn Rate: The value we need to predict for each employee telling the rate of Bur out while working. In the range of [0.0, 1.0] where the higher the value is more is the burn out.


## File Descriptions <a name="files"></a>

- 1 jupyter notebook to showcase work related to the above questions. Markdown cells were used to assist in walking through the thought process for individual steps.  
- 3 data files (train, test, clean_df_train)
- 1 `.py` file for interactive scenario analysis with ActiveGraf through excel. I use xlwings library and VBA to run Python script from a Power Point presentation file (license is necessary for ActiveGraf, see my presentation at the post [here](https://medium.com/...)
- 1 `.actg` file. It is a special ActiveGraf zip file that contains the excel and powerpoint files for interactive scenario analysis.

## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://medium.com/...).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to HackerEarth for the data.  You can find the Licensing for the data and other descriptive information at the Kaggle link available [here](https://www.kaggle.com/blurredmachine/are-your-employees-burning-out/metadata).
For Excel and PowerPoint you need a Microsoft Office license. 
For Interactive Scenario Analysis you need an ActiveGraf license, you can try it with a 1 month free trial link available [here](https://activegraf.com/get-activegraf).
 
