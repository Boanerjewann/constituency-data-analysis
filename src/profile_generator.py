import pandas as pd
import argparse

# Load dataset
df = pd.read_csv("data/sample_meghalaya_constituency_data.csv")

# ----------- FUNCTIONS -----------

def get_benchmark(value, state_avg, region_avg):
    result = ""
    
    if value > state_avg:
        result += "↑ above state avg "
    elif value < state_avg:
        result += "↓ below state avg "
    else:
        result += "= at state avg "

    if value > region_avg:
        result += "| ↑ above regional avg"
    elif value < region_avg:
        result += "| ↓ below regional avg"
    else:
        result += "| = at regional avg"

    return result


def generate_profile(row):
    region = row['Region']

    # State averages
    state_avg = df.mean(numeric_only=True)

    # Regional averages
    region_df = df[df['Region'] == region]
    region_avg = region_df.mean(numeric_only=True)

    profile = "\n===== CONSTITUENCY PROFILE =====\n"

    # Snapshot
    profile += f"\n--- Snapshot ---\n"
    profile += f"Name: {row['Constituency_Name']}\n"
    profile += f"Region: {row['Region']}\n"
    profile += f"District: {row['District']}\n"
    profile += f"Electorate: {row['Electorate_2023']}\n"
    profile += f"Primary Occupation: {row['Primary_Occupation'].replace('&amp;', '&')}\n"
    profile += f"Literacy Rate: {row['Literacy_Rate_Pct']}%\n"

    # Scheme Status
    profile += f"\n--- Scheme Status ---\n"
    profile += f"MGNREGS Person Days: {row['MGNREGS_Person_Days_FY2425']}\n"
    profile += f"PM Awas Completion: {row['PM_Awas_Completion_Pct']}%\n"
    profile += f"JJM Coverage: {row['JJM_Functional_Tap_Connections_Pct']}%\n"
    profile += f"PM-KISAN Beneficiaries: {row['PM_KISAN_Beneficiaries']}\n"

    # Infrastructure
    profile += f"\n--- Infrastructure ---\n"
    profile += f"Road Length: {row['Road_Length_Km']} km\n"
    profile += f"Pucca Road: {row['Pucca_Road_Pct']}%\n"
    profile += f"4G Coverage: {row['Internet_4G_Coverage_Pct']}%\n"
    profile += f"Health Centres: {row['Primary_Health_Centres']}\n"
    profile += f"Schools: {row['Govt_Primary_Schools']}\n"

    # Benchmarking
    profile += f"\n--- Benchmarking ---\n"

    profile += f"Literacy: {get_benchmark(row['Literacy_Rate_Pct'], state_avg['Literacy_Rate_Pct'], region_avg['Literacy_Rate_Pct'])}\n"
    profile += f"JJM: {get_benchmark(row['JJM_Functional_Tap_Connections_Pct'], state_avg['JJM_Functional_Tap_Connections_Pct'], region_avg['JJM_Functional_Tap_Connections_Pct'])}\n"
    profile += f"PM Awas: {get_benchmark(row['PM_Awas_Completion_Pct'], state_avg['PM_Awas_Completion_Pct'], region_avg['PM_Awas_Completion_Pct'])}\n"
    profile += f"Pucca Road: {get_benchmark(row['Pucca_Road_Pct'], state_avg['Pucca_Road_Pct'], region_avg['Pucca_Road_Pct'])}\n"

    # Fund utilisation warning
    if row['Constituency_Fund_Utilized_Pct'] < 60:
        profile += "\n⚠ WARNING: Fund utilisation below 60%\n"

    return profile

# ----------- MAIN PROGRAM -----------

parser = argparse.ArgumentParser()
parser.add_argument('--constituency', type=str)
parser.add_argument('--id', type=str)
parser.add_argument('--output', type=str)

args = parser.parse_args()

# Find row
if args.constituency:
    result = df[df['Constituency_Name'] == args.constituency]
elif args.id:
    result = df[df['Constituency_ID'] == args.id]
else:
    print("Error: Provide --constituency or --id")
    exit()

if result.empty:
    print("Error: Constituency not found")
    exit()

row = result.iloc[0]

profile = generate_profile(row)

print(profile)

if args.output:
   with open(args.output, "w", encoding="utf-8") as file:
    file.write(profile)
