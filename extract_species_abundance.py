import argparse
import pandas as pd

# Argument parser to accept external input file
parser = argparse.ArgumentParser(description="Extract species-level abundance from Kraken2 report.")
parser.add_argument("-i", "--input", required=True, help="Path to the Kraken2 report file")
args = parser.parse_args()

# Define column names based on Kraken2 report structure
columns = ["Percentage", "Reads_covered", "Reads_assigned", "Taxonomic_rank", "NCBI_ID", "Taxon_name"]

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
print("\nTop 10 Most Abundant Species:")
print(species_abundance.head(10).to_string(index=False))

# Save to CSV for further analysis
species_abundance.to_csv("species_abundance_summary.csv", index=False)
print("\nSpecies-level abundance summary saved as 'species_abundance_summary.csv'.")
