# __BootCamp_Project__

## __Overview:__
The objective of this project is to analyze a dataset consisting of 6,000 Youtube Video records to discover a pattern in the list of trending videos. Once analysis is done, a machine learning model will be developed to predict how long a videpo features in the YouTube trending list based on  features/variables.

### __Dataset selection:__
A number of datasets were reviewed before finalizing the Youtube Video Dataset from source - Kaggle.com, namely:
- Youtube trending Video 
- Dataset to predict preferences to opt for Travel insurance
- Reading Habits prediction in US adults
- Walmart sales Retail data set
- House Sale Price prediction
- Fuel vs Electric vehicle preference prediction

A decision was made to analyze the dataset for YouTube trending videos. 

### __Reason for selection__

A) General Reasons
1. A useful topic for Youtube content creators. 
2. Youtube is a global platform with over 2 billion users
3. The analysis will be useful for promotional and marketing purpose.
4. Youtubers/Business/Professionals can use this model as an input before uploading their videos to make their videos popular/ trending.


B) Project specific reasons
1. Availability of the dataset
2. Availability of number of records for the data required to perform the analysis.
3. Applicability of tools and technologies learnt during the course to meet the deliverables.

## Description of source of the data
This dataset is available on Kaggle where the publisher has extracted it from the Youtube API.This dataset is a daily record of the top trending YouTube videos available in a CSV format. It contains details such as video title, channel title, publish time, tags, views, likes and dislikes, description, and comment count. The Category_id which represents video category is available in an associated JSON file. Source:  https://www.kaggle.com/datasnaek/youtube-new?select=USvideos.csv


### __Purpose of Analysis:__
For the purpose of our analysis, we will use data related to trending videos in the US.

The following actions will be performed:

- Perform analysis of trending videos by each feature (category, Tags, Likes, comments,title etc.) 
- Use Machine learning models to predict the length of video trending on YouTube.


## __Team and Roles:__
- Square - Dixie Peralta
- Triangle - Neeraja Jayaraman & Nisha Bharakhada
- Circle - Dixie Peralta & Richelle Long
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

The presentation can be viewed at the following link: https://drive.google.com/file/d/1jBHAhm4AzAVBi5AUHJoCA3l3yXS9wJuA/view?usp=sharing

## __Tools and technologies used in Segment 1:__

- Microsoft Excel - To view the data once csv file is downloaded
- Postgress SQL - To create a database
- Python (Jupyter Notebook)
- QBD - To create ERD diagram
- Github
- Google Drive - To keep all the documents at one central location
For more details, please refer to the Technology documentation.
[technology.md](technology.md)

## __Machine Learning Model Description:__

The machine learning model proposed for this project is Multiple regression model in order to predict the trending duration of different videos based on criteria such as Views, Likes, Dislikes and comment count. 

For more details, please refer to the Machine Learning Documentation.
[MachineLearningModel_proposal_Seg1.docx](/MachineLearningModel/MachineLearningModel_proposal_Seg1.docx)

## __Database Description:__

For details on Data ETL process and database setup, please refer to the Database documentation.
[ETLProcess.docx](/ETL/ETLProcess.docx)

The schema of the database can be viewed below:

Quick Database Diagram:
![ETL/ERD.png](/ETL/ERD.png)

It has been proposed that our database will be created in 
PostgreSQL – Relational Database System, as seen in the screenshot below:
![DB_ERD_SQL_posGres.png](/ETL/DB_ERD_SQL_posGres.png)

