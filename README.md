# Kraken2 species-level abundance extractor

This script extracts **species-level abundance** from a Kraken2 report file and provides a summary of species names, their percentage abundance, and the number of reads assigned.

## **Features**
- Filters **species-level (S)** classifications from Kraken2 reports.
- Summarizes **percentage abundance** and **reads covered**.
- Sorts by the **most abundant species**.
- Outputs the results to **console** and **saves a CSV file**.

---

## **Installation**

### **1. Install python dependencies**
Ensure you have `pandas` installed. If not, install it using:

```sh
pip install pandas
```

If using **Python 3**, run:

```sh
pip3 install pandas
```

---

## **Usage**

### **1. Run the script**
```sh
python extract_species_abundance.py -i <kraken2_report_file>
```

For example:
```sh
python extract_species_abundance.py -i D392_S7_L001.report.txt
```

---

## **Example output**
```
Top 10 Most Abundant Species:
         Taxon_name  Percentage  Reads_covered
   Escherichia coli       17.56         207170
   Klebsiella pneumoniae        0.12           1373
   Escherichia albertii        0.07            804
   Escherichia fergusonii        0.06            655
   Shigella dysenteriae        0.05            613
```

### **2. Output file**
The script saves the full species-level abundance summary as:
```
species_abundance_summary.csv
```

---

## **Troubleshooting**

### **1. "ModuleNotFoundError: No module named 'pandas'"**
Install pandas:
```sh
pip install pandas
```

### **2. "FileNotFoundError"**
Ensure you provide the correct path to the Kraken2 report file.

---

## **License**
This script is open-source and free to use.

---

## **Author**
Gerald Mboowa 
