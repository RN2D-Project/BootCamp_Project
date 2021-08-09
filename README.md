# __BootCamp_Project__

## __Overview:__
Originally - The group identified YouTube videos with 6000 records to performn the analysis and use machine learning to understand which feature contributes the most to make the video trending. Using the regression model, the accuracy score was very low, hence, the group switched the project to a different dataset (Heart Disease).

In this current dataset which is related to Heart Disease, our  objective is to identify the the weightage for each feature i.e. preexisting condition, medication, age group and other parameters to predict whether a patient is at heart disease risk or not.  

### __Dataset selection:__
A number of datasets were reviewed before finalizing the Youtube Video Dataset from source - Kaggle.com, namely:
- Youtube trending Video 
- Dataset to predict preferences to opt for Travel insurance
- Reading Habits prediction in US adults
- Walmart sales Retail data set
- House Sale Price prediction
- Fuel vs Electric vehicle preference prediction
- Heart Disease

A decision was made to analyze the dataset for Heart Disease for female patients only.

### __Reason for selection__

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
Source: https://www.kaggle.com/dileep070/heart-disease-prediction-using-logistic-regression

It contains details such as patient age, medication, test results,smoking pattern to predict whether the patient is at risk or not.


### __Purpose of Analysis:__
For the purpose of our analysis, we will use data related to heart disease to predict whether the patient has heart disease risk or not.

The following actions will be performed:

- Perform analysis for current BP and cholestrol level, current smoking pattern,age group, any current BP medication, glucose level.
- Use Machine learning models to predict the patients risk for heart disease


## __Team and Roles:__
- Square - Neeraja Jayaraman
- Triangle -  Dixie Peralta, Richelle Long
- Circle - Nisha Bharakhada
- X - Dixie Peralta, Richelle Long, Neeraja Jayaraman & Nisha Bharakhada


## __Commmunication protocol:__
The following modes of communication will be used by the team.
1. Git Hub - Coding, ReadMe, Commits and Final Project Results  
2. Slack - Team's main communication  
3. Google Drive  - For Assignments, Documents and Notes  
4. Zoom - Daily / Weekly meetups
For more details, please refer to the communication protocol document.
[CommunicationProtocol.docx](CommunicationProtocol.docx)

## __Presentation:__
- Provisional Machine learning Model - Neeraja and Nisha
- Provisional Database - Dixie & Richelle

The presentation can be viewed at the following link: 

Segment 1 - https://drive.google.com/file/d/1jBHAhm4AzAVBi5AUHJoCA3l3yXS9wJuA/view?usp=sharing

Segment 2 - https://drive.google.com/drive/folders/14KQiHRpSGZYOli-9ZkKgPc7hI9MZ7THd

- Flow Diagram
[Segment_2_Flow_Diagram.PNG](Segment_2_Flow_Diagram.PNG)

## __Tools and technologies used in Segment 1:__

- Microsoft Excel - To view the data once csv file is downloaded
- AWS and S3 - Database hosting on the cloud
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

The machine learning model proposed for this project is a Logistic regression model in order to predict the risk of patient for heart disease based on existing features and parameters. Other Classification models such as Support vector Model, Random Forest Classifier and Decision Tree Classifier may also be used to build a robust Machine Learning Model.

For more details, please refer to the Machine Learning Documentation.
![MachineLearningModel_proposal_Seg2.docx](/Machine_Learning_Model/MachineLearningModel_proposal_Seg2.docx)

The code for Machine Learning Model can be viewed here:
[HeartDiseasePredictor_MLM.ipynb](HeartDiseasePredictor_MLM.ipynb)
## __Database Description:__

For details on Data ETL process and database setup, please refer to the Database documentation.
![HD_ETL_AWS_and_S3_documentation.docx](/ETL/HD_ETL_AWS_and_S3_documentation.docx)

The code for ETL can be viewed here: [predicting_heart_disease_in_females.ipynb](predicting_heart_disease_in_females.ipynb)

The schema of the database can be viewed below:
Quick Database Diagram:
![ETL/FHD_Predictor_ERD.png](/ETL/FHD_Predictor_ERD.png)

It has been proposed that our database will be created in 
PostgreSQL – Relational Database System, as seen in the screenshot below:
- Connection String (AWS to PostgressSQL)

![pgAdmin_AWS_connection.png](/Database/pgAdmin_AWS_connection.png)


- File on AWS - S3 bucket

![AWS_S3_Bucket.png](Database/AWS_S3_Bucket.png)


## Dashboard Visualization:
It has been proposed that Tableau will be used to create visualizations for this project. For Dashboard blueprint, please refer to the below files:

1) Risk by BP and  Agegroup 

![HeartDiseaseRisk_basedon_BP and AgeGroup.PNG](/Tableau_Dashboard_files/HeartDiseaseRisk_basedon_BP_and_AgeGroup.PNG)

2) Risk by Agegroup 

![HeartDiseaseRisk_by_AgeGroup.PNG](/Tableau_Dashboard_files/HeartDiseaseRisk_by_AgeGroup.PNG)

3) Risk by Cholestrollevel

![Heartatrisk_basedon_Cholestrol_level.PNG](/Tableau_Dashboard_files/Heartatrisk_basedon_Cholestrol_level.PNG)

4) Risk by SmokingPattern.PNG

![Heartatrisk_basedon_SmokingPattern.PNG](/Tableau_Dashboard_files/Heartatrisk_basedon_SmokingPattern.PNG)




