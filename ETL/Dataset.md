# __BootCamp_Project__

## __Datasets__

Topic: 		Female Heart Disease

Resources:	Framingham.csv (Kaggle)		                    ~ 2,419 rows 16 columns

![Framingham](https://user-images.githubusercontent.com/87670915/129682836-55eed5c2-4193-4567-93fa-e6b23dd4e668.png)


## ETL:        used Jupyter Notebook to extract and clean data
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

Clean data set :       ~ clean_FHD_predictor_dataset.csv  ~ 2,034 rows 20 columns


For the purpose of joining datasets from different source other than the Kaggle datasets we extracted, additional datasets were added.

-   bmi_pks.csv
-   bp_pks.csv
-   glucose_pks.csv
-   totChol_pks.csv


#### bmi_pks.csv

![bmi_pks](https://user-images.githubusercontent.com/87670915/129682833-7fd5cf43-e014-454b-ac53-97dcd4283d28.png)

#### bp_pks.csv
  
![bp_pks](https://user-images.githubusercontent.com/87670915/129682835-449e5766-613c-4750-99d9-0da59164ab18.png)

#### glucose_pks.csv
   
![glucose_pks](https://user-images.githubusercontent.com/87670915/129682839-33e50c5d-ac1f-442a-9eb4-b41580999d0b.png)

#### totChol_pks.csv
  
![totChol_pks](https://user-images.githubusercontent.com/87670915/129682838-4970eb38-4e71-45fa-a1e7-1fe8071ccbde.png)


### __Second Dataset__    
Clean data set :       ~ clean_FHD_predictor_dataset.csv  ~ 2,034 rows 20 columns

![Clean_FHD_dataset](https://user-images.githubusercontent.com/87670915/129683504-6b9ba100-9684-4988-896f-41311438721e.png)




