import subprocess
import sys
import os

# Ensure pandas is installed, try to install via pip if missing
try:
    import pandas as pd
except ImportError:
    print(" 'pandas' not found. Attempting to install...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
        import pandas as pd
        print(" Successfully installed pandas.")
    except Exception as e:
        print(" Failed to install pandas. Please install it manually and re-run the script.")
        sys.exit(1)

import argparse

# Argument parser to accept external input file
parser = argparse.ArgumentParser(description="Extract species-level abundance from Kraken2 report.")
parser.add_argument("-i", "--input", required=True, help="Path to the Kraken2 report file")
args = parser.parse_args()

# Extract sample name from the parent directory of the input file
sample_name = os.path.basename(os.path.dirname(args.input))

# Define column names based on Kraken2 report structure
columns = ["Percentage", "Reads_covered", "Reads_assigned", "Taxonomic_rank", "NCBI_ID", "Taxon_name"]

try:
    # Read the file while handling multiple spaces
    df = pd.read_csv(args.input, sep="\t", header=None, names=columns, engine='python')

    # Clean taxon names by stripping unnecessary spaces
    df["Taxon_name"] = df["Taxon_name"].str.strip()

    # Filter for species-level data only
    df_species = df[df["Taxonomic_rank"] == "S"]

    # Summarize species-level abundance
    species_abundance = df_species.groupby("Taxon_name")[["Percentage", "Reads_covered"]].sum().reset_index()


    # Sort by highest abundance
    species_abundance = species_abundance.sort_values(by="Reads_covered", ascending=False)

    # Print the top 10 species with their abundance
    print(f"\nTop 10 Most Abundant Species in Sample: {sample_name}")
    print(species_abundance.head(10).to_string(index=False))

    # Dynamically name the output CSV file using the sample name
    output_file = f"{sample_name}_species_abundance_summary.csv"
    species_abundance.to_csv(output_file, index=False)
    print(f"\n Species-level abundance summary saved as '{output_file}'.")
except Exception as e:
    print(f" An error occurred during processing: {e}")
    sys.exit(1)

