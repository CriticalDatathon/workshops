# MIT Critical Datathon Workshops 

## Useful Links:

1. [Google Colab Notebooks Folder](https://drive.google.com/drive/folders/1ddnh2SmqkeWrg0Zs1S6fRmOQm11Yx3Hg?usp=share_link) - As soon as they get concluded, let's create a copy to this repository.

2. [Submitted Paper with Initial Work](https://drive.google.com/file/d/1Y5jp0P0HWWLh7Xq497wlkchc-EfaZxOV/view?usp=share_link)

3. [Code for the Initial Work with ML](https://github.com/joamats/mit-sao2-spo2)

4. [Code for the Data Extraction](https://github.com/CriticalDatathon/data-prep)

5. [Google Slides with Rationale](https://docs.google.com/presentation/d/16PJ193CkKOUvkyUBb16Tpwme93aOOwhKAPo11NNurDs/edit?usp=sharing)

## Working Teams

| Team | Members | Notebook |
|------|---------|----------|
| 1    | Luca, Nikita, João, Luis | [Notebook 1](https://colab.research.google.com/drive/1cMRVGYtUSEoYNWWw_0SOLJqEjGKxZ_vO?usp=sharing) |
| 2    | David, Adrien, Jack | [Notebook 2](https://colab.research.google.com/drive/1LK6ctRzOjxT50Wn9t3M68KxnvqPrL4zk?usp=sharing) |
| 3    | Skyler, Maria, Tristan | [Notebook 3](https://colab.research.google.com/drive/1W2xke2uf-Kmt1YAndQFuyJMD6GSkKSCe?usp=sharing) |


## Variable Dictionary:
| name                           | type    | description                                                                        |
|:-------------------------------|:--------|:-----------------------------------------------------------------------------------|
| subject_id                     | int64   | Unique identifier for each patient                                                 |
| stay_id                        | int64   | Unique identifier for each hospital stay                                           |
| SaO2_timestamp                 | object  | Timestamp for SaO2 measurement                                                     |
| SaO2                           | float64 | Arterial oxygen saturation                                                         |
| delta_SpO2                     | int64   | Change in peripheral oxygen saturation from the previous measurement               |
| SpO2                           | int64   | Peripheral oxygen saturation                                                       |
| hidden_hypoxemia               | int64   | Indicates if the patient had hypoxemia without clinical signs                      |
| hadm_id                        | int64   | Unique identifier for each hospital admission                                      |
| gender                         | object  | Gender of the patient                                                              |
| sex_female                     | int64   | Indicates if the patient is female                                                 |
| anchor_age                     | int64   | Age of the patient at the time of admission                                        |
| race                           | object  | Race of the patient                                                                |
| race_group                     | object  | Grouping of race into broader categories                                           |
| language                       | object  | Primary language spoken by the patient                                             |
| insurance                      | object  | Type of insurance of the patient                                                   |
| weight                         | float64 | Weight of the patient in kilograms                                                 |
| height                         | float64 | Height of the patient in centimeters                                               |
| BMI                            | float64 | Body Mass Index of the patient                                                     |
| anchor_year_group              | object  | Grouping of admission year into broader categories                                 |
| first_hosp_stay                | bool    | Indicates if this is the first hospital stay for the patient                       |
| first_icu_stay                 | bool    | Indicates if this is the first ICU stay for the patient                            |
| icustay_seq                    | int64   | Sequence number of ICU stay for the patient                                        |
| admittime                      | object  | Timestamp for hospital admission                                                   |
| dischtime                      | object  | Timestamp for hospital discharge                                                   |
| icu_intime                     | object  | Timestamp for ICU admission                                                        |
| icu_outtime                    | object  | Timestamp for ICU discharge                                                        |
| los_hospital                   | int64   | Length of hospital stay in days                                                    |
| los_icu                        | float64 | Length of ICU stay in days                                                         |
| CCI                            | int64   | Charlson Comorbidity Index                                                         |
| SOFA_admission                 | int64   | Sequential Organ Failure Assessment (SOFA) score at admission                      |
| mortality_in                   | int64   | Indicates if the patient died during the hospital stay                             |
| delta_vent_start               | float64 | Time since ventilation started (in hours) at the time of the measurement           |
| ventilation_status             | object  | Indicates if the patient was on mechanical ventilation                             |
| invasive_vent                  | int64   | Indicates if the patient was on invasive mechanical ventilation                    |
| delta_FiO2                     | float64 | Change in fraction of inspired oxygen (FiO2) from the previous measurement         |
| FiO2                           | float64 | Fraction of inspired oxygen                                                        |
| delta_rrt                      | float64 | Time since renal replacement therapy (in hours) at the time of the measurement     |
| rrt                            | int64   | Indicates if the patient was on renal replacement therapy                          |
| delta_vp_start                 | float64 | Time since vasopressor therapy started (in hours) at the time of the measurement   |
| norepinephrine_equivalent_dose | float64 | Dose of norepinephrine equivalent to other vasopressors (in mcg/kg/min)            |
| delta_sofa_coag                | float64 | Change in SOFA score for coagulation from the previous measurement                 |
| sofa_coag                      | float64 | SOFA score for coagulation                                                         |
| delta_sofa_liver               | float64 | Change in SOFA score for liver from the previous measurement                       |
| sofa_liver                     | float64 | SOFA score for liver                                                               |
| delta_sofa_cv                  | int64   | Change in SOFA score for cardiovascular from the previous measurement              |
| sofa_cv                        | int64   | Cardiovascular component of Sequential Organ Failure Assessment (SOFA) score       |
| delta_sofa_cns                 | float64 | Change in central nervous system component of SOFA score from previous measurement |
| sofa_cns                       | float64 | Central nervous system component of SOFA score                                     |
| delta_sofa_renal               | float64 | Change in renal component of SOFA score from previous measurement                  |
| sofa_renal                     | float64 | Renal component of SOFA score                                                      |
| delta_sofa_resp                | float64 | Change in respiratory component of SOFA score from previous measurement            |
| sofa_resp                      | float64 | Respiratory component of SOFA score                                                |
| delta_hemoglobin               | float64 | Change in hemoglobin level from previous measurement                               |
| hemoglobin                     | float64 | Hemoglobin level                                                                   |
| delta_hematocrit               | float64 | Change in hematocrit level from previous measurement                               |
| hematocrit                     | float64 | Hematocrit level                                                                   |
| delta_mch                      | float64 | Change in mean corpuscular hemoglobin from previous measurement                    |
| mch                            | float64 | Mean corpuscular hemoglobin                                                        |
| delta_mchc                     | float64 | Change in mean corpuscular hemoglobin concentration from previous measurement      |
| mchc                           | float64 | Mean corpuscular hemoglobin concentration                                          |
| delta_mcv                      | float64 | Change in mean corpuscular volume from previous measurement                        |
| mcv                            | float64 | Mean corpuscular volume                                                            |
| delta_platelet                 | float64 | Change in platelet count from previous measurement                                 |
| platelet                       | float64 | Platelet count                                                                     |
| delta_rbc                      | float64 | Change in red blood cell count from previous measurement                           |
| rbc                            | float64 | Red blood cell count                                                               |
| delta_rdw                      | float64 | Change in red cell distribution width from previous measurement                    |
| rdw                            | float64 | Red cell distribution width                                                        |
| delta_wbc                      | float64 | Change in white blood cell count from previous measurement                         |
| wbc                            | float64 | White blood cell count                                                             |
| delta_d_dimer                  | float64 | Change in D-dimer level from previous measurement                                  |
| d_dimer                        | float64 | D-dimer level                                                                      |
| delta_fibrinogen               | float64 | Change in fibrinogen level from previous measurement                               |
| fibrinogen                     | float64 | Fibrinogen level                                                                   |
| delta_thrombin                 | float64 | Change in thrombin time from previous measurement                                  |
| thrombin                       | float64 | Thrombin time                                                                      |
| delta_inr                      | float64 | Change in international normalized ratio (INR) from previous measurement           |
| inr                            | float64 | International normalized ratio (INR)                                               |
| delta_pt                       | float64 | Change in prothrombin time (PT) from previous measurement                          |
| pt                             | float64 | Prothrombin time (PT)                                                              |
| delta_ptt                      | float64 | Change in partial thromboplastin time (PTT) from previous measurement              |
| ptt                            | float64 | Partial thromboplastin time (PTT)                                                  |
| delta_alt                      | float64 | Change in alanine transaminase (ALT) level from previous measurement               |
| alt                            | float64 | Alanine transaminase (ALT) level                                                   |
| delta_alp                      | float64 | Change in alkaline phosphatase (ALP) level from previous measurement               |
| alp                            | float64 | Alkaline phosphatase (ALP) level                                                   |
| delta_ast                      | float64 | Change in aspartate transaminase (AST) level from previous measurement             |
| ast                            | float64 | Aspartate transaminase (AST) level                                                 |
| delta_bilirubin_total          | float64 | Change in total bilirubin level from previous measurement                          |
| bilirubin_total                | float64 | Total bilirubin level                                                              |
| delta_bilirubin_direct         | float64 | Change in direct bilirubin level                                                   |
| bilirubin_direct               | float64 | Direct bilirubin level                                                             |
| delta_bilirubin_indirect       | float64 | Change in indirect bilirubin level                                                 |
| bilirubin_indirect             | float64 | Indirect bilirubin level                                                           |
| delta_ck_cpk                   | float64 | Change in creatine kinase (CPK) level                                              |
| ck_cpk                         | float64 | Creatine kinase (CPK) level                                                        |
| delta_ck_mb                    | float64 | Change in creatine kinase MB (CK-MB) level                                         |
| ck_mb                          | float64 | Creatine kinase MB (CK-MB) level                                                   |
| delta_ggt                      | float64 | Change in gamma-glutamyl transferase (GGT) level                                   |
| ggt                            | float64 | Gamma-glutamyl transferase (GGT) level                                             |
| delta_ld_ldh                   | float64 | Change in lactate dehydrogenase (LDH) level                                        |
| ld_ldh                         | float64 | Lactate dehydrogenase (LDH) level                                                  |
| delta_albumin                  | float64 | Change in albumin level                                                            |
| albumin                        | float64 | Albumin level                                                                      |
| delta_aniongap                 | float64 | Change in anion gap                                                                |
| aniongap                       | float64 | Anion gap                                                                          |
| delta_bicarbonate              | float64 | Change in bicarbonate level                                                        |
| bicarbonate                    | float64 | Bicarbonate level                                                                  |
| delta_bun                      | float64 | Change in blood urea nitrogen (BUN) level                                          |
| bun                            | float64 | Blood urea nitrogen (BUN) level                                                    |
| delta_calcium                  | float64 | Change in calcium level                                                            |
| calcium                        | float64 | Calcium level                                                                      |
| delta_chloride                 | float64 | Change in chloride level                                                           |
| chloride                       | float64 | Chloride level                                                                     |
| delta_creatinine               | float64 | Change in creatinine level                                                         |
| creatinine                     | float64 | Creatinine level                                                                   |
| delta_glucose_lab              | float64 | Change in glucose level from laboratory measurement                                |
| glucose_lab                    | float64 | Glucose level from laboratory measurement                                          |
| delta_sodium                   | float64 | Change in sodium level                                                             |
| sodium                         | float64 | Sodium level                                                                       |
| delta_potassium                | float64 | Change in potassium level                                                          |
| potassium                      | float64 | Potassium level                                                                    |
| delta_ph                       | float64 | Change in pH level                                                                 |
| ph                             | float64 | pH level                                                                           |
| delta_lactate                  | float64 | Change in lactate level                                                            |
| lactate                        | float64 | Lactate level                                                                      |
| delta_heart_rate               | int64   | Change in heart rate                                                               |
| heart_rate                     | float64 | Heart rate                                                                         |
| delta_mbp                      | int64   | Change in mean blood pressure (MBP)                                                |
| mbp                            | float64 | Mean blood pressure (MBP)                                                          |
| delta_resp_rate                | float64 | Change in respiratory rate                                                         |
| resp_rate                      | float64 | Respiratory rate                                                                   |
| delta_temperature              | float64 | Change in body temperature                                                         |
| temperature                    | float64 | Body temperature                                                                   |
| delta_glucose                  | float64 | Change in glucose level                                                            |
| glucose                        | float64 | Glucose level                                                                      |
| delta_heart_rhythm             | float64 | Change in heart rhythm                                                             |
| heart_rhythm                   | object  | Heart rhythm                                                                       |
