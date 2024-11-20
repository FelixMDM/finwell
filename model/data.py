import pandas as pd

input_files = [
    "../data/Fall2024.csv",
    "../data/Spring2024.csv",
    "../data/Summer2024.csv"
]

output_file = "../data/clean_data/data.csv"
na_values=["", " ", "N/A", "NA"]

for i in range(3):
    input_file = input_files[i]
    df = pd.read_csv(input_file, header=None)

    # Process the data
    extracted_data = []
    for i in range(len(df)):
        row = df.iloc[i].tolist()
        if len(row) >= 2:
            decision = row[41]
            inquiry = row[40]

            decision_label = "Y" if decision != "N" else "N"

            if isinstance(inquiry, str) and inquiry not in na_values:
                extracted_data.append([inquiry.lower(), decision_label])

    # Save to a new file
    with open(output_file, "a", encoding="utf-8") as f:
        for inquiry, decision in extracted_data:
            f.write(f"{inquiry},,, {decision}\n")

print(f"Extracted data has been saved to {output_file}")