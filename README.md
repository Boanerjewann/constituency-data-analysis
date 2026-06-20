# Meghalaya Constituency Data Analysis

## Overview
This project analyses constituency level development data in Meghalaya using Microsoft Excel and Python. The analysis focuses on regional disparities, infrastructure, scheme delivery, and fund utilisation patterns across constituencies.

---

## Tools Used
- Microsoft Excel for data analysis, visualisations, and dashboard creation  
- Python (pandas, argparse) for the constituency profile generator  

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
A Python based command line script was developed to generate structured constituency reports.

**Script location:** `src/profile_generator.py`

**Features:**
- Accepts input using:
  - Constituency name
  - Constituency ID  
- Generates a formatted profile including:
  - Constituency snapshot (region, district, electorate, occupation, literacy)
  - Scheme performance (MGNREGS, PM Awas, JJM, PM-KISAN)
  - Infrastructure indicators (roads, connectivity, health, education)
- Performs benchmarking:
  - Compares each indicator with state and regional averages
  - Uses clear indicators (↑ above, ↓ below, = at average)
- Flags low fund utilisation (below 60%)
- Supports saving output to a text file

**Example usage:**

python src/profile_generator.py --constituency "Jowai"
python src/profile_generator.py --id MH029
python src/profile_generator.py --constituency "Jowai" --output reports/jowai_profile.txt


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
- Dynamic filtering based on region, district, and occupation  

---

## How to Use

1. Open the Excel file in  
   `notebooks/Boanerjes_Wann_finished_report_meghalaya_constituency_data.xlsx`  

2. Navigate through sheets:
   - Summary statistics  
   - Section 1 to S2-Q4 analysis  
   - Dashboard  

3. Use slicers to interactively filter data  

4. For Python script:
   - Run from project root using command line  
   - Provide constituency name or ID  

---

## Assumptions
- Infrastructure Index gives equal weight to roads, water access, and connectivity  
- Welfare Dependency combines poverty levels with MGNREGS intensity  
- Regional averages are used for comparative benchmarking  

---

## Limitations
- Analysis is primarily Excel based with limited automation  
- Limited to available indicators in the dataset  
- No advanced statistical or predictive modelling  

---

## Future Improvements
- Extend the Python script for automated batch profile generation  
- Build an interactive web based dashboard using Streamlit or Power BI  
- Include additional socio economic and governance indicators  
- Apply predictive modelling and advanced analytics  
