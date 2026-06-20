# Meghalaya Constituency Data Analysis

## Overview
This project analyses constituency level development data in Meghalaya using Microsoft Excel. The analysis focuses on regional disparities, infrastructure, scheme delivery, and fund utilisation patterns across constituencies.

---

## Tools Used
- Microsoft Excel for data analysis, visualisations, and dashboard creation

---

## Project Sections

### Section 1: Data Audit
- Generated summary statistics for key indicators  
- Identified data quality issues such as outliers and scale differences  
- Created derived metrics:
  - Infrastructure Index
  - Welfare Dependency  
  - Low Fund Utilisation Flag
---

### Section 2: Analytical Insights
- Compared regional disparities across Khasi Hills, Jaintia Hills, Garo Hills, and Ri Bhoi  
- Identified gaps in scheme delivery for JJM and PM Awas Yojana  
- Analysed fund utilisation patterns  
- Highlighted key relationships and anomalies across indicators  

---

### Section 3: Profile Generator
- Not implemented in Python 

---

### Section 4: Interactive Dashboard
An interactive dashboard was created in Excel using pivot tables and slicers to allow easy exploration of the data.

Filters available:
- Region  
- District  
- Primary Occupation

Key indicators displayed:
- Voter Turnout percentage  
- BPL Households percentage  
- PM Awas Completion percentage  
- JJM Functional Tap Connections percentage  
- Pucca Road percentage  
- Fund Utilisation percentage  

Features:
- Side by side comparison of key indicators  
- Identification of top and bottom performing constituencies  
- Dynamic filtering based on region and district  

---

## How to Use

1. Open the Excel file in `notebooks/Boanerjes_Wann_finished_report_meghalaya_constituency_data.xlsx`  
2. Navigate through the sheets:
   - Summary statistics
   - Section1 to S2-Q4 analysis
   - Dashboard  
3. Use the slicers in the dashboard to filter by region and district and Primary Occupation

---

## Assumptions
- Infrastructure Index gives equal weight to roads, water access, and connectivity  
- Welfare Dependency combines poverty levels with MGNREGS intensity  
- Regional averages are used for overall comparison  

---

## Limitations
- Analysis is fully Excel based and semi automated by converting raw data into table 
- Limited to the indicators available in the dataset  
- No advanced statistical or predictive modelling has been applied  

---

## Future Improvements
- Develop a Python based profile generator  
- Build a more advanced dashboard using Power BI or Streamlit  
- Include more socio economic indicators for deeper insights  
- Apply statistical methods or machine learning for predictive analysis  