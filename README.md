# SectionC_G3_Salary_Visualization

> **Newton School of Technology | Data Visualization & Analytics**  
> A data visualization and analytics project using Python, GitHub, and Tableau to analyze socio-economic factors influencing income levels.

---

## Project Overview

| Field | Details |
|---|---|
| **Project Title** | Salary Visualization |
| **Sector** | Social Impact / Socio-Economic Analytics |
| **Team ID** | G3 |
| **Section** | C |
| **Faculty Mentor** | Archit Raj |
| **Institute** | Newton School of Technology |
| **Submission Date** | 29 April 2026 |

### Team Members

| Role | Name | GitHub Username |
|---|---|---|
| Project Lead, PPT and Quality Lead | Atharva Tiwari | `Atharva20041809` |
| Analysis Lead | Rachit Gupta | `Rachitt19` |
| Visualization Lead | Agrima Gusain | `slayplayagrima` |
| Data Lead | Tanmay Singh | `tanmay-7706` |
| ETL Lead | R Ashrith | `ashrith-07` |
| Strategy Lead | Ashish Kushwaha | `N/A` |

---

## Business Problem

Income inequality is influenced by socio-economic factors such as education, occupation, workclass, demographics, and financial conditions. Understanding these patterns helps identify which groups are more likely to earn above $50K and which factors support income mobility. This project uses the Adult Census Income dataset to analyze income patterns and provide data-driven insights for workforce planning, policy targeting, and social development.

**Core Business Question**

> Which demographic, educational, occupational, and financial factors influence high-income status?

**Decision Supported**

> This analysis helps stakeholders identify income gaps, high-income drivers, and target areas for education, workforce development, and financial literacy programs.

---

## Dataset

| Attribute | Details |
|---|---|
| **Source Name** | Adult Census Income Dataset |
| **Direct Access Link** | https://archive.ics.uci.edu/dataset/2/adult |
| **Row Count** | 16,281 |
| **Column Count** | 15 |
| **Time Period Covered** | Census-based adult income records |
| **Format** | CSV |

**Key Columns Used**

| Column Name | Description | Role in Analysis |
|---|---|---|
| `income` | Income category of the individual, either `<=50K` or `>50K` | Target variable / KPI split |
| `education_num` | Numeric representation of education level | Income predictor |
| `occupation` | Job role of the individual | Segmentation and high-income analysis |
| `hours_per_week` | Weekly working hours | Work effort analysis |
| `capital_gain` | Profit from investments or asset sales | Financial wealth indicator |

For full column definitions, see [`docs/data_dictionary.md`](docs/data_dictionary.md).

---

## KPI Framework

| KPI | Definition | Formula / Computation |
|---|---|---|
| High Income Rate | Percentage of individuals earning above $50K | Count of `>50K` earners / Total records |
| Gender Income Gap | Difference in high-income rate between males and females | Male high-income rate - Female high-income rate |
| Top Earning Occupation | Occupation with the highest percentage of high-income individuals | `% >50K` grouped by occupation |
| People with Capital Gains | Percentage of individuals with investment gains | Count of `capital_gain > 0` / Total records |

---

## Tableau Dashboard

| Item | Details |
|---|---|
| **Dashboard URL** | https://public.tableau.com/app/profile/agrima.gusain5797/viz/IncomePredictionAnalysisDashboard_17773823940220/Dashboard3 |
| **Executive View** | Shows high-level KPIs such as high income rate, gender income gap, top earning occupation, and people with capital gains |
| **Operational View** | Enables detailed income analysis across education, occupation, workclass, demographics, and financial indicators |
| **Main Filters** | Education Group, Age Group, Sex, Income Label, Occupation Group |

---

## Key Insights

1. Higher education increases the likelihood of earning above $50K, showing that education is a strong income driver.
2. Occupation plays a major role in income level, with executive and professional roles having the highest high-income rates.
3. High-income patterns vary across demographic and job groups, showing the role of social and career factors.
4. Education, occupation, and capital gains influence high-income status more strongly than working hours alone.
5. Income is strongly linked to education, occupation, and capital gains.
6. Financial indicators like capital gain explain income differences more clearly than basic work-effort measures.
7. Gender and marital status strongly influence earning potential.
8. Income is not driven by one factor alone; it is shaped by education, occupation, demographics, workclass, and financial indicators.

---

## Recommendations

| # | Insight | Recommendation | Expected Impact |
|---|---|---|---|
| 1 | Higher education improves high-income probability | Invest in education access and upskilling programs | Improved economic mobility |
| 2 | Executive and professional roles show higher income rates | Focus skill development on high-paying career paths | Better workforce readiness |
| 3 | Capital gains strongly indicate wealth-building potential | Promote financial literacy and investment awareness | Improved wealth-building opportunities |
| 4 | Gender and marital income gaps are visible | Support fair pay and targeted inclusion programs | Reduced income inequality |
| 5 | Working more hours does not guarantee high income | Prioritize skill quality and career mobility | Sustainable income growth |

---

## Analytical Pipeline

The project follows a structured workflow:

1. **Define** - Social impact sector selected and income inequality problem scoped.
2. **Extract** - Adult Census Income dataset sourced from UCI Machine Learning Repository.
3. **Clean and Transform** - Missing values handled, categorical values standardized, and derived fields created.
4. **Analyze** - EDA and statistical analysis performed using Python.
5. **Visualize** - Interactive Tableau dashboard created and published.
6. **Recommend** - Data-backed recommendations developed for education, workforce, and policy planning.
7. **Report** - Final report and presentation prepared for submission.

---

## Tech Stack

| Tool | Status | Purpose |
|---|---|---|
| Python + Jupyter Notebooks | Mandatory | ETL, cleaning, analysis, and KPI computation |
| Tableau Public | Mandatory | Dashboard design and publishing |
| GitHub | Mandatory | Version control and collaboration |
| Pandas, NumPy, Matplotlib, Seaborn, SciPy | Used | Data processing, visualization, and statistical analysis |

---

## Impact & Value

**Social Impact**

**Income Mobility**  
Education and upskilling can increase the share of high-income individuals.

**Workforce Development**  
Training for high-paying occupations can help workers move toward better income groups.

**Inequality Reduction**  
Gender and marital income gaps highlight unequal earning patterns.

**Financial Growth**  
Capital gains strongly increase high-income probability.

**Policy Efficiency**  
Income patterns help identify groups needing support.

---

## Limitations & Next Steps

**Limitations**

Limited explanatory power of model:  
Income is influenced by many hidden factors, so the model cannot explain every income outcome.

Missing key variables:  
Data does not include family background, location cost, industry type, experience, or personal wealth.

External factors not fully captured:  
Economic conditions, labor market trends, and policy changes are not directly included.

Dataset limitation:  
Analysis is based on census records and may not capture all modern income patterns.

**Future Scope**

Build advanced predictive models:  
Use machine learning models to improve high-income prediction accuracy.

Incorporate richer datasets:  
Add location, experience, industry, family income, and cost-of-living data.

Apply advanced segmentation:  
Cluster individuals by education, occupation, workclass, and financial characteristics.

Use causal analysis techniques:  
Move beyond correlation to understand the true drivers of high-income status.

---

## Contribution Matrix

| Team Member | Dataset and Sourcing | ETL and Cleaning | EDA and Analysis | Statistical Analysis | Tableau Dashboard | Report Writing | PPT and Viva |
|---|---|---|---|---|---|---|---|
| Atharva Tiwari |  |  |  |  |  | | Owner |
| Rachit Gupta |  |  |  | |  | Owner |  |
| Agrima Gusain |  |  | Owner |  | Owner |  |  |
| Tanmay Singh | Owner |  |  |  |  |  |  |
| R Ashrith |  | Owner |  |  |  |  |  |
| Ashish Kushwaha |  |  |  | Owner |  |  |  |


_Declaration: We confirm that the above contribution details are accurate and verifiable through GitHub Insights, PR history, and submitted artifacts._

**Team Lead Name:** Atharva Tiwari

**Date:** 29 April 2026

---

## Academic Integrity

All analysis, code, and recommendations in this repository are the original work of the team listed above. The project uses the Adult Census Income dataset for academic analysis and visualization.

---

*Newton School of Technology - Data Visualization & Analytics | Capstone 2*
