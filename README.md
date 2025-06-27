# V1.1 - GeneAnalyzer

A lightweight Python command-line tool to analyze the official NCBI `gene_info.gz` dataset. 

---

## Features

- Download or load a local `gene_info.gz` file
- Parse large compressed TSV files using `gzip`
- Extract statistics:
  - Total gene entries
  - Number of *Homo sapiens* genes (TaxID 9606)
  - Unique gene types
  - Most frequent gene type
- Progress bar for downloads
- Unit tested with `unittest`

---

## Project Structure

<pre><code> ``` gene_info_analyzer/ ├── main.py # CLI: user interaction, download, display stats ├── utils.py # Core function to parse gene_info.gz ├── test_utils.py # Unit tests using unittest ├── requirements.txt # External dependencies ├── .gitignore # Files excluded from Git └── README.md # Project documentation ``` </code></pre>

## Getting Started
### Installation

```bash
# Clone or download this folder
cd gene_info_analyzer

# Optional: Create a virtual environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
# .\venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt

<pre><code> ### Running the App ```bash python main.py ``` You will be prompted to either: - **Download** the official NCBI file, or - **Upload** your own local `.gz` file </code></pre>

Sample output:
Analyzing data...

1. Total genes listed: 60056804
2. Genes listed for Homo sapiens: 193439
3. Unique gene types: [...]
4. Most common gene type: protein-coding (47777560 occurrences)



<pre><code> ### Running Unit Tests ```bash python test_utils.py ``` </code></pre>

Sample output:
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK



# Source File
Official dataset:
NCBI gene_info.gz
(https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene_info.gz)


Versioning
v1.0: Initial working version (CLI + parser + test suite)
v1.1: README and folder structure finalized

by Sarah Deckarm, 2025
