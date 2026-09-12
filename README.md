# MSBA 265 – Module 1 Assignment

## Exploratory Data Analysis, Data Quality Verification, Data Dictionaries, and Outlier Pipelines

**Course:** MSBA 265 – Business Analytics Topics  
**Semester:** Fall 2026  
**Student:** Nu Quynh Chau Nguyen  
**Dataset:** French Motor Third Party Liability Claims  
**Source:** OpenML

---

## Project Overview

This project performs exploratory data analysis, data quality verification, business data dictionary construction, correlation analysis, distribution analysis, and outlier filtering on the French Motor Third Party Liability Claims dataset.
The project is designed to be fully reproducible from the command line and Jupyter Notebook environment.

---

## Repository Structure

msba265_module1_workshop/
│
├── .gitignore
├── README.md
├── requirements.txt
├── Module1_Homework_Report.pdf
│
├── data/
│   ├── download_data.py
│   ├── raw_business_data.csv
│   └── cleaned_business_data.csv
│
├── notebooks/
│   └── 01_eda_and_data_dictionary.ipynb
│
├── src/
│   └── clean_outliers.py
│
└── reports/
    ├── data_dictionary.csv
    └── figures/
        ├── correlation_heatmap.png
        ├── feature_distributions.png
        └── outlier_filtering_comparison.png

---    

## Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Nuquynhchaunguyen/msba265_module1_workshop.git
cd msba265_module1_workshop

### 2. Create a Virtual Environment

python3 -m venv venv

### 3. Activate the Virtual Environment

#### macOS / Linux

source venv/bin/activate

#### Windows

venv\Scripts\activate

### 4. Install Project Dependencies

pip install -r requirements.txt

---

## Reproduce the Project

### Step 1 – Download the Raw Dataset

Run:

python data/download_data.py

This script downloads the **French Motor Third Party Liability Claims** dataset from OpenML and saves it as:

data/raw_business_data.csv

Expected dataset size:

678,013 rows × 12 columns

---

### Step 2 – Run the Jupyter Notebook

Open:

notebooks/01_eda_and_data_dictionary.ipynb

Run all notebook cells from top to bottom.

The notebook performs:

- Structural data type and null-value inspection
- Summary statistics
- Raw boundary audits
- Business data dictionary generation
- Skewness diagnostics
- Pearson correlation analysis
- Correlation heatmap generation
- Feature distribution analysis
- Outlier diagnostics
- Tukey IQR and Z-score comparison

The notebook generates the following artifacts:
reports/data_dictionary.csv
reports/figures/correlation_heatmap.png
reports/figures/feature_distributions.png
reports/figures/outlier_filtering_comparison.png

---

### Step 3 – Run the Production Outlier-Cleaning Pipeline

From the project root, run:

python src/clean_outliers.py

The script applies **Tukey 1.5 × IQR filtering** to the `Density` feature. The cleaned dataset is saved as:

data/cleaned_business_data.csv

Expected output:

Initial Dataset Records: 678,013
Tukey IQR Valid Range: [-2,257.00, 4,007.00]
Outlier Records Removed: 77,566
Final Cleaned Records: 600,447

---

## Main Findings

- `DrivAge` ranges from 18 to 100 years.
- `Exposure` ranges from approximately 0.0027 to 2.01.
- `BonusMalus` ranges from 50 to 230.
- `ClaimNb` is highly right-skewed and contains many valid zero-claim observations.
- A standard logarithmic transformation should not be applied directly to `ClaimNb` because `log(0)` is undefined.
- `Density` is strongly right-skewed and contains many statistically extreme observations.
- Some high-density observations may represent legitimate metropolitan policyholders rather than data-entry errors.
- The strongest numerical Pearson relationship is between `DrivAge` and `BonusMalus`, approximately **r = -0.48**.
- Tukey IQR filtering on `Density` removes **77,566 records**.
- The final cleaned dataset contains **600,447 records**.

---

## Business Interpretation

`Exposure` represents the amount of time a policy is active. For count-based claim-frequency modeling, log(Exposure) should be incorporated as an offset rather than treating Exposure as a standard predictor.

`Density` and categorical `Area` represent overlapping geographic risk information. Including both in the same linear regression model may introduce redundancy and multicollinearity, so they should be evaluated carefully during modeling.

`ClaimNb` is a discrete count variable. Zero-claim observations are legitimate business observations and should be preserved rather than removed or transformed using a standard logarithmic transformation. ClaimNb should remain in raw count units and be modeled using a Poisson rate framework with log(Exposure) as an offset.

---

## Generated Artifacts

### Business Data Dictionary

reports/data_dictionary.csv

### Pearson Correlation Heatmap

reports/figures/correlation_heatmap.png

### Feature Distribution Plots

reports/figures/feature_distributions.png

### Outlier Filtering Comparison

reports/figures/outlier_filtering_comparison.png

### Cleaned Dataset

data/cleaned_business_data.csv

### Final Homework Report

Module1_Homework_Report.pdf

---

## Final Deliverables

This repository includes:

- Jupyter Notebook
- Data download script
- Raw dataset
- Business data dictionary CSV
- Pearson correlation heatmap
- Feature distribution plots
- Outlier filtering comparison
- Cleaned dataset
- Production outlier filtering script
- Requirements file
- Final homework PDF report

---

## Reproduction Summary

A reviewer can reproduce the project by following these steps:

1. Create and activate the virtual environment.
2. Install the required dependencies.
3. Download the raw dataset.
4. Open and run the Jupyter Notebook from top to bottom.
5. Run the production outlier-cleaning pipeline.

Commands:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python data/download_data.py

Then open:
notebooks/01_eda_and_data_dictionary.ipynb
Run all cells from top to bottom.

Finally, run:
python src/clean_outliers.py

---

## Final Report

The completed assignment report is available at:

Module1_Homework_Report.pdf


