# ASV Renamer

ASV Renamer is a Python script for renaming amplicon sequence variant (ASV) identifiers in ASV tables and corresponding representative sequence files. The script is developed with the help of OpenAI's GPT-4 language model and modified by human developers to ensure its functionality and usability.

## Requirements

- Python 3.6 or higher
- pandas
- BioPython

You can install the required packages using the following command:

```bash
pip install pandas biopython
```

## Usage

1. Clone this repository or download the `rename_asv_ids.py` script.
2. Prepare your input ASV table file (tab-separated) and representative sequences file (FASTA format).
3. Run the script with the appropriate input and output file paths:

```bash
python rename_asv_ids.py --asv_table_file input_asv_table.tsv \
                         --rep_seq_file input_rep_seq.fasta \
                         --output_asv_table_file output_asv_table.tsv \
                         --output_rep_seq_file output_rep_seq.fasta
```

The script will generate updated ASV table and representative sequence files with renamed ASV identifiers.

## Functionality

The script performs the following tasks:

- Reads the input ASV table and representative sequence files.
- Renames ASV identifiers in the ASV table and representative sequence files to a standard format (e.g., ASV1, ASV2, ...).
- Keeps the original sample names in the ASV table unchanged.
- Saves the updated ASV table and representative sequence files to the specified output file paths.

## Acknowledgments

This script was initially generated using OpenAI's GPT-4 language model and later modified by human developers to ensure its functionality and usability. We would like to thank OpenAI for providing access to their powerful language model and the open-source community for their continuous support and contributions.
