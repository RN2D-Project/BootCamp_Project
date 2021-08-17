# __BootCamp_Project__

## __Datasets__

Topic: 		Female Heart Disease

Resources:	Framingham.csv (Kaggle)		                    ~ 2,419 rows 16 columns

ETL:        used Jupyter Notebook to extract and clean data
-   checked columns
-   checked datatypes
-   dropped null values
-   filtered data to only view females

### __First Dataset__ 
ETL Clean data set :    ~ heart_disease_females.csv       ~ 2,034 rows 16 columns

From the first dataset, heart_disease_females.csv columns were broken down into 4 groups
-   Demographics.csv                                      ~ age and education
-   Habits.csv                                            ~ currentSmoke and cigsPerDay
-   Pre-existing_conditions.csv                           ~ BP_meds, prevalentStroke, prevalentHypertension and diabetes
-   Parameters.csv                                        ~ totChol, sysBP, diaBP, BMI, heart_rate and glucose

For the purpose of joining datasets from different source other than the Kaggle datasets we extracted, additional datasets were added.
-   bmi_pks.csv
-   bp_pks.csv
-   glucose_pks.csv
-   totChol_pks.csv

### __Second Dataset__    
Clean data set :       ~ clean_FHD_predictor_dataset.csv  ~ 2,034 rows 20 columns
