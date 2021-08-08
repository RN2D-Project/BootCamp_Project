
CREATE TABLE "demographics" (
    "patient_female_id" int   NOT NULL,
    "age" int   NOT NULL,
    "education" float   NOT NULL,
    CONSTRAINT "pk_demographics" PRIMARY KEY (
        "patient_female_id"
     )
);

CREATE TABLE "habits" (
    "patient_female_id" int   NOT NULL,
    "current_smoker" int   NOT NULL,
    "cigs_per_day" float   NOT NULL,
    CONSTRAINT "pk_habits" PRIMARY KEY (
        "patient_female_id"
     )
);

CREATE TABLE "pre_existing_conditions" (
    "patient_female_id" int   NOT NULL,
    "bp_meds" float   NOT NULL,
    "prevalent_stroke" int   NOT NULL,
    "prevalent_hyp" int   NOT NULL,
    "diabetes" int   NOT NULL,
    CONSTRAINT "pk_pre_existing_conditions" PRIMARY KEY (
        "patient_female_id"
     )
);

CREATE TABLE "parameters" (
    "patient_female_id" int   NOT NULL,
    "tot_chol" float   NOT NULL,
    "tc_key" varchar   NOT NULL,
    "sys_bp" float   NOT NULL,
    "dial_bp" float   NOT NULL,
    "bp_key" varchar   NOT NULL,
    "bmi" float   NOT NULL,
    "bmi_key" varchar   NOT NULL,
    "heart_rate" float   NOT NULL,
    "glucose" float   NOT NULL,
    "glucose_key" varchar   NOT NULL,
    "ten__year_chd" int   NOT NULL,
    CONSTRAINT "pk_parameters" PRIMARY KEY (
        "patient_female_id"
     )
);

CREATE TABLE "blood_pressure" (
    "bp_key" varchar   NOT NULL,
    "bp_category" varchar   NOT NULL,
    "systolic_mmhg" varchar   NOT NULL,
    "and_or" varchar   NOT NULL,
    "diastolic_mmhg" varchar   NOT NULL,
    CONSTRAINT "pk_blood_pressure" PRIMARY KEY (
        "bp_key"
     )
);

CREATE TABLE "glucose_test" (
    "glucose_key" varchar   NOT NULL,
    "fasting_blood_sugar_test" varchar   NOT NULL,
    "results" varchar   NOT NULL,
    CONSTRAINT "pk_glucose_test" PRIMARY KEY (
        "glucose_key"
     )
);

CREATE TABLE "bmi" (
    "bmi_key" varchar   NOT NULL,
    "bmi" varchar   NOT NULL,
    "description" varchar   NOT NULL,
    CONSTRAINT "pk_bmi" PRIMARY KEY (
        "bmi_key"
     )
);

CREATE TABLE "tot_chol" (
    "tc_key" varchar   NOT NULL,
    "total_cholesterol_mg_dl" varchar   NOT NULL,
    "total_cholesterol_mmo_dl" varchar   NOT NULL,
    "chol_results" varchar   NOT NULL,
    CONSTRAINT "pk_tot_chol" PRIMARY KEY (
        "tc_key"
     )
);


SELECT * FROM complete_parameters;

--join tot_chol results to parameters
SELECT pa.patient_female_id, 
	   pa.tot_chol,
	   tc.chol_results
INTO para_1
FROM parameters as pa
LEFT JOIN tot_chol as tc
ON pa.tc_key = tc.tc_key;

--join bp category to parameters
SELECT pa.patient_female_id, 
	   pa.sys_bp,
	   pa.dial_bp,
	   bp.bp_category
INTO para_2
FROM parameters as pa
LEFT JOIN blood_pressure as bp
ON pa.bp_key = bp.bp_key;

--join description to parameters
SELECT pa.patient_female_id, 
	   pa.bmi,
	   bm.description
INTO para_3
FROM parameters as pa
LEFT JOIN bmi as bm
ON pa.bmi_key = bm.bmi_key;

--join heart_rate and glucose results to parameters
SELECT pa.patient_female_id, 
	   pa.heart_rate,
	   pa.glucose,
	   glt.results,
	   pa.ten__year_chd
INTO para_4
FROM parameters as pa
LEFT JOIN glucose_test as glt
ON pa.glucose_key = glt.glucose_key;

--Join para1 and para2
SELECT p1.patient_female_id, 
	   p1.tot_chol,
	   p1.chol_results,
	   p2.sys_bp,
	   p2.dial_bp,
	   p2.bp_category
INTO para_5
FROM para_1 as p1
RIGHT JOIN para_2 as p2
ON p1.patient_female_id = p2.patient_female_id;

--Join para1, para2 & p3
SELECT p5.patient_female_id, 
	   p5.tot_chol,
	   p5.chol_results,
	   p5.sys_bp,
	   p5.dial_bp,
	   p5.bp_category,
	   p3.bmi,
	   p3.description
INTO para_6
FROM para_5 as p5
RIGHT JOIN para_3 as p3
ON p5.patient_female_id = p3.patient_female_id;

--Join para1, para2, p3 & p4
SELECT p6.patient_female_id, 
	   p6.tot_chol,
	   p6.chol_results,
	   p6.sys_bp,
	   p6.dial_bp,
	   p6.bp_category,
	   p6.bmi,
	   p6.description,
	   p4.heart_rate,
	   p4.glucose,
	   p4.results,
	   p4.ten__year_chd
INTO complete_parameters
FROM para_6 as p6
RIGHT JOIN para_4 as p4
ON p6.patient_female_id = p4.patient_female_id;

--join demographics to habits
SELECT d.patient_female_id, 
	   d.age,
	   d.education,
	   h.current_smoker,
	   h.cigs_per_day
INTO dh
FROM demographics as d
LEFT JOIN habits as h
ON d.patient_female_id = h.patient_female_id;

SELECT * FROM dhp;

--join demographics, habits to Pre-existing Conditions
SELECT dh.patient_female_id, 
	   dh.age,
	   dh.education,
	   dh.current_smoker,
	   dh.cigs_per_day,
	   px.bp_meds,
	   px.prevalent_stroke,
	   px.prevalent_hyp,
	   px.diabetes
 
INTO dhp
FROM dh 
LEFT JOIN pre_existing_conditions as px
ON dh.patient_female_id = px.patient_female_id;

--join complete datasets
SELECT dhp.patient_female_id, 
	   dhp.age,
	   dhp.education,
	   dhp.current_smoker,
	   dhp.cigs_per_day,
	   dhp.bp_meds,
	   dhp.prevalent_stroke,
	   dhp.prevalent_hyp,
	   dhp.diabetes,
	   cp.tot_chol,
	   cp.chol_results,
	   cp.sys_bp,
	   cp.dial_bp,
	   cp.bp_category,
	   cp.bmi,
	   cp.description,
	   cp.heart_rate,
	   cp.glucose,
	   cp.results,
	   cp.ten__year_chd
 
INTO complete_datasets
FROM dhp
LEFT JOIN complete_parameters as cp
ON dhp.patient_female_id = cp.patient_female_id;

SELECT * FROM complete_datasets;
