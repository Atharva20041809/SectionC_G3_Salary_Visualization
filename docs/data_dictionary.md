# Adult Census Income - Data Dictionary

## Overview
This document serves as the official data dictionary for the **Adult Census Income** dataset (often referred to as the "Census Income" dataset) utilized in this project. The original dataset originates from the UC Irvine Machine Learning Repository and was extracted from the 1994 US Census database. 

During the ETL pipeline process (`etl_pipeline.py`), the dataset schema was transformed for machine learning readiness resulting in the `/data/processed/adult_cleaned.csv` file. 

---

## Processed Schema Mapping

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| **`age`** | Integer / Continuous | The age of the individual. Expected range is 17 to 90. |
| **`workclass`** | Categorical | The generalized employment division. Values include: `Private`, `Self-emp-not-inc`, `Self-emp-inc`, `Federal-gov`, `Local-gov`, `State-gov`, `Without-pay`, `Never-worked`. |
| **`education`** | Categorical | The highest achieved level of education. Values include: `Bachelors`, `Some-college`, `11th`, `HS-grad`, `Prof-school`, `Assoc-acdm`, `Assoc-voc`, `9th`, `7th-8th`, `12th`, `Masters`, `1st-4th`, `10th`, `Doctorate`, `5th-6th`, `Preschool`. |
| **`education_num`** | Integer / Continuous | The numerical proxy for the maximum education level attained. Ranging from 1 to 16. |
| **`marital_status`** | Categorical | Demographic marital status. Values include: `Married-civ-spouse`, `Divorced`, `Never-married`, `Separated`, `Widowed`, `Married-spouse-absent`, `Married-AF-spouse`. |
| **`occupation`** | Categorical | The general classification of the individual's employment role. Values include: `Tech-support`, `Craft-repair`, `Other-service`, `Sales`, `Exec-managerial`, `Prof-specialty`, `Handlers-cleaners`, `Machine-op-inspct`, `Adm-clerical`, `Farming-fishing`, `Transport-moving`, `Priv-house-serv`, `Protective-serv`, `Armed-Forces`. |
| **`relationship`** | Categorical | Social/household relationship status. Values include: `Wife`, `Own-child`, `Husband`, `Not-in-family`, `Other-relative`, `Unmarried`. |
| **`race`** | Categorical | Ethnicity identification. Values include: `White`, `Asian-Pac-Islander`, `Amer-Indian-Eskimo`, `Other`, `Black`. |
| **`sex`** | Categorical | The gender of the individual: `Female`, `Male`. |
| **`capital_gain`** | Integer / Continuous | Registered capital gains recorded for the individual. |
| **`capital_loss`** | Integer / Continuous | Registered capital losses recorded for the individual. |
| **`hours_per_week`** | Integer / Continuous | Total recorded working hours committed by the individual per week. |
| **`native_country`** | Categorical | The individual's country of functional origin (e.g., `United-States`, `Cambodia`, `England`, `Puerto-Rico`, etc.). |
| **`income`** | Binary / Encoded | The target modeling variable determining if the individual generates more than 50K annually. Originally categorical (`>50K`, `<=50K`), transformed internally to Binary states (`1`: >50K classification, `0`: <=50K classification). |

---

## Engineered / Pipeline Features
Features strictly created exclusively via our analytical `etl_pipeline.py`.

| Feature Name | Data Type | Engineering Logic |
| :--- | :--- | :--- |
| **`age_group`** | Categorical Bins | Demographic binning derived strictly from the `age` column via standard discrete segments: `[16-25, 25-45, 45-65, 65-100]`. Labeled logically as: `Youth`, `YoungAdult`, `Adult`, `Senior` to isolate cohort trends visually. |

---

## Omitted Features
Features excluded from pipeline transit parameters out of the raw state.

| Original Column Name | Omission Rationale |
| :--- | :--- |
| **`fnlwgt`** | Represents the sociological final demographic weight estimate evaluated by the Census Bureau. Given standard predictive configurations devoid of systemic population estimations logic, this metric proves irrelevant and possesses minimal predictive power, hence it was completely dropped across the dataset. |

---

## Data Quality Assurance (ETL Mappings)
- **Column Standardization**: All original column labels featuring dashes (e.g., `education-num`, `hours-per-week`) were strictly redefined mapping directly into a python-compliant `snake_case` structural layout (e.g. `education_num`, `hours_per_week`).
- **Null Value Enforcement**: Unrecorded structural entries spanning the categorical mappings utilizing the string placeholder `?` were comprehensively located, overwritten universally into programmatic `NaN`, and accurately back-filled via a statistical modal average derivation logic eliminating system leakage points. None are present in the completed processed repository architecture.
