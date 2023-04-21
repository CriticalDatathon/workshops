# Data and Algorithmic Bias Workshop
## Use Case: The peril of inaccurate Sp02 measurements in the EHR
by Leo Anthony Celi on some airplane from somewhere to somewhere, originally to be applied in the Australian Datathon

### 1. Talk: Introduction 
* Pulse oximetry has been found to be a poor proxy of arterial oxygen saturation among individuals of color
* A certain value means different depending on the skin tone
* How would this issue impact the development of algorithms in healthcare where Sp02 is one of the features?
* Specific aim: To determine whether the issue of poor accuracy of pulse oximeters also affects indigenous patients in Australia
### 2.	Breakout session #1: Design the study to address the research question
* Inclusion and exclusion criteria: pros and cons of focusing on a specific condition
* Outcome: Sp02 – Sa02 gap 
  - Definition of Sp02 – Sa02 gap
  - Representation: first pair? mean of pairs across the entire ICU LOS? mean of pairs during the first 24 hours? standardized based on number of pairs? 
* Features including confounders affecting Sp02 (e.g., hemoglobin, bilirubin, vasopressor use) and those affecting the relationship of So02 and outcome (e.g., age, illness severity, comorbidities)
* Methodology: traditional regression, causal inference
### 3.	Flow diagram and Table 1, distribution of outcome and features across indigenous vs. non-indigenous patients
### 4.	Breakout sessions #2: Sources of bias in the study design
* Sampling selection bias as regards who have access to ICU care (look at literature)
* Sampling selection bias as regards the hospital’s ICU admission criteria (look at literature)
* Sampling selection bias based on study inclusion and exclusion criteria 
* Measurement bias from irregular sampling 
* Data imbalance: indigenous vs non-indigenous, outcome imbalance
*	Unmeasured confounding: patient-provider sex and race concordance, other drivers of clinical decision-making that are not captured by EHR
### 5.	Exploratory data analysis
* Look at proportion of indigenous vs indigenous patients of every cohort that is excluded
* Number of blood gases indigenous vs non-indigenous
  - during the first 24 hours standardized based on illness severity
  - during the entire ICU length of stay standardized based on ICU length-of-stay
* If only the first pair is considered, time to the first arterial blood gas indigenous vs non-indigenous patients
### 6.	Breakout session #3: How to address the different sources of data bias
* Irregular sampling of arterial blood gases
* Imbalance in the number of indigenous vs. indigenous patients
### 7.	Talk: What is the effect of indigenous status being embedded on the data?
### 8.	Breakout sessions #4: What are the potential consequences of the inaccuracy of the pulse oximetry on indigenous patients on the development of decision-support algorithms? Provide use cases.
### 9.	Breakout sessions #5: How should we evaluate whether a decision-support algorithm will not harm indigenous patients further?
