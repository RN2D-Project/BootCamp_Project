# __BootCamp_Project__

## __Overview:__
The group identified Heart Disease Risk Disease 4238 records to perform the analysis and use machine learning to predict the heart  disease risk in next 10 years for female population of dataset. It was found that the data was poorly correlated and the accuracy score was very low. Hence, the group switched the project to a different dataset (Heart Disease).

In this current dataset which is related to Heart Disease, our  objective is to identify the the weightage for each feature i.e. preexisting condition, medication, age group and other parameters to predict whether a patient is at heart disease risk or not.  

### __Dataset selection:__
A number of datasets were reviewed before finalizing the Heart Disease Dataset from source - Kaggle.com and additional secondary datasets were extracted from CDC, American Heart Association and Mayo Clinic.

Heart Disease is one of the leading cause of death for men and women in the United States. It is said that women are at a greater risk for Heart Disease than men. About 1 in every 5 female deaths is due to heart disease(www.cdc.gov). The dataset comprises of demographic details, habits, existing health conditions and parameters for each patient record, along with their heart disease risk. This project analyzes the risk of Heart Disease for female patients only.

### __Reason for selection:__

A) General Reasons
1. A relevant topic that is relatable to a wide audience.
2. Beneficial to a number of stakeholders such as Patients at risk, hospitals and health systems, insurance companies
3. A robust automated system to predict heart Disease may enable an increased accuracy of diagnosis.
4. It could enable Health Systems to provide better quality of care.
5. It will especially be beneficial in taking timely preventive action especially in female patients as they present atypical symptoms when compared to males leading to difficulties and delays in diagnosis.

B) Project specific reasons
1. Availability of the dataset
2. Availability of number of records for the data required to perform the analysis.
3. Applicability of tools and technologies learnt during the course to meet the deliverables.

## Description of source of the data
This dataset has been sourced from Kaggle. 

- Primary Data Source: https://www.kaggle.com/dileep070/heart-disease-prediction-using-logistic-regression
It contains details such as patient age, medication, test results,smoking pattern to predict whether the patient is at risk or not.

- Secondary Data Source: It includes the data required for Analysis and Vizualisation

- Glucose Levels: https://www.cdc.gov/diabetes/basics/getting-tested.html
- Blood Pressure: https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings
- BMI details:  https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html


### __Purpose of Analysis:__
For the purpose of our analysis, we will use data related to heart disease to predict whether the patient has heart disease risk or not.

The following actions will be performed:
- Perform analysis for current BP and cholestrol level, current smoking pattern,age group, any current BP medication, glucose level.
- Use Machine learning models to predict the patients risk for heart disease

## __Presentation:__
- Provisional Machine learning Model - Neeraja and Nisha
- Provisional Database - Dixie & Richelle

The presentation can be viewed at the following link: 

Segment 1 - https://drive.google.com/file/d/1jBHAhm4AzAVBi5AUHJoCA3l3yXS9wJuA/view?usp=sharing

Segment 2 - https://docs.google.com/presentation/d/13ICAp0w_pGawtcIiCHCIWfkRKR1s869B/edit?rtpof=true

Final_Presentation

![UCB_Capstone_Project_Final.ppt](/Presentation/UCB_Capstone_Project_Final.ppt)

- Flow Diagram
__Segment 3__

![Flow_Diagram_Segment_3.PNG](/Tableau_Dashboard_files/Flow_Diagram_Segment_3.PNG)


## __Tools and technologies used:__

- Microsoft Excel - To view the data once csv file is downloaded
- Postgress SQL - To create a database
- Python (Jupyter Notebook)
- QDB - To create ERD diagram
- SCIKIT learn machine learning Library 
- Tableau for Visualizations
- Github
- Google Drive - To keep all the documents at one central location

For more details, please refer to the Technology documentation.
![technology.md](technology.md)

## __Machine Learning Model Description:__

The machine learning model proposed for this project is a Binary Classification Model in order to predict the risk of female patients for heart disease based on existing features and parameters. Classification models such as Logistic regression, Support vector Model, Random Forest Classifier, Decision Tree Classifier and Gradient Boosting Model have been used. Each model’s accuracy score and Classification report have been recorded.
For more details, please refer to the Machine Learning Documentation.

![MachineLearningModel_proposal.docx](/Machine_Learning_Model/MachineLearningModel_proposal.docx)

The code for Exploratory Data Analysis and Machine Learning Model can be viewed here:
[FINALHeartDiseasePredictor_MLM.ipynb](/JupyterNotebook_Dataset_and_MLM/FINALHeartDiseasePredictor_MLM.ipynb)

## __Database Description:__

For details on Data ETL process and database setup, please refer to the Database documentation.
![Database.md](/Database/Database.md)

The code for ETL can be viewed here: [predicting_heart_disease_in_females.ipynb](/JupyterNotebook_DatasetandMLM/predicting_heart_disease_in_females.ipynb)

The schema of the database can be viewed below:
Quick Database Diagram:
![Database/FHD_Predictor_ERD.png](/Database/FHD_Predictor_ERD.png)

It has been proposed that our database will be created in 
PostgreSQL – Relational Database System, as seen in the screenshot below:
![SQL_Python_Connection_String.png](/Database/SQL_Python_Connection_String.png)

- Different tables were joined using 'join' query
![FHD_predictor_SQLCode.py](Database/FHD_predictor_SQLCode.py)


## __Dashboard Visualization__:
It has been proposed that Tableau will be used to create visualizations for this project. For the completeness and transparency with more detail oriented visualization for the purpose of understanding the datapoint, below charts and tables were added. This is helpful in decision making process for the Prediction Model and understand the data itself based on the domain.

For Dashboard, please refer to the below link:
https://public.tableau.com/authoring/FemaleHeartDiseasePredictor/Story_Board#1


## __Project Learnings and Challenges__

- Understanding dataset is imperative before performing data cleaning or  data analysis.
- Knowledge of Domain/Subject Matter helps to understand the significance and weightage for each value present in the dataset.
- From the dataset, it is important to analyze whether the dataset alone will suffice the requirement to achieve the target or objective to resolve any problem/ question we are hoping to answer. 
- Selection of dataset is a key to address the issue/problem in terms of feature available, datatype, validity and authenticity of the datasource. 
- In case the data is incomplete, it has risk of inaccurate analysis and incorrect prediction based on the machine learning model selected.

## __Recommendations__

### Database

- Connecting to cloud Database
- Maintaining a backup of data
- Understanding correct datatype
- Data cleaning based on key feature requirement

### Git Hub

- Knowledge of basic functions of Git hub for eg: commit, merge, clean up the repository is important to save time on working on core deliverables of the project
- Maintaining a clean repository helps to avoid any duplication and confusion while working on large dataset and with a bigger team of developers delivering feature for the same application
- To make sure any upgrades in infrastructure required has been done and getting the information from authetic source
- Ensuring any changes/modification have been commited and merged wheneever applicable to avoid bug/break 

### Machine Learning Model

- Decision for selecting Model
- Understanding input data
- Comparison to achieve outcome
- Understanding Pros and Cons for different ML model
- Adding more dimension to the analysis
- Addressing Class Imbalance issues
- Attempt to get a better Recall score along with Accuracy 
- Consider other machine learning Models such as simple Neural networks

### Dashboard

- Accuracy in reading the value of each data point in the graph
- Understanding datapoint value significance based on domain of dataset
- Weightage for each feature
- Understanding statistical significance for each data point
- Data analysis and visualization correlation with prediction models


## __Final Results__ 

As per data analysis performed and different ML model, it has  been identified that the best accuracy score was achieved by using Logistic Regression Model. However, considering the dataset is relevant to heart disease, better precision and recall score along with accuracy score is imperative, hence it was concluded that Decision Tree Model to be more relevant model for this dataset to predict whether the patient has risk for coronary heart disease in the  next 10 years. 






