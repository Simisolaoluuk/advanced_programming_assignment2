import pandas as pd

# Path to your original dataset
input_file = "data/full_companies_data.csv"

# Path to your smaller sample file
output_file = "data/companies_sample.csv"

def extract_sample():
    # Read the full dataset
    df = pd.read_csv(input_file)

    # Take the first 7000 rows
    sample_df = df.head(7000)

    # Save the sample to a new CSV file
    sample_df.to_csv(output_file, index=False)

    print("Sample of 7000 records saved to:", output_file)

if __name__ == "__main__":
    extract_sample()
