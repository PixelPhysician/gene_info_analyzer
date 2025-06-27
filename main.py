import os
import urllib.request
from collections import Counter
from tqdm import tqdm
from utils import parse_gene_info

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_file_with_progress(url, filename):
    with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=filename) as t:
        urllib.request.urlretrieve(url, filename, reporthook=t.update_to)
    print(f"\nDownloaded: {filename}")

def main():
    print("Gene Info Analyzer (FHNW Medical Software Dev)")

    choice = input("Download from NCBI or use local file? [D/U]: ").strip().upper()

    if choice == 'D':
        filename = input("Enter filename to save as (e.g. gene_info.gz): ").strip()
        url = "https://ftp.ncbi.nlm.nih.gov/gene/DATA/gene_info.gz"
        download_file_with_progress(url, filename)
    elif choice == 'U':
        filename = input("Enter path to your local .gz file: ").strip()
    else:
        print("Invalid option.")
        return

    if not os.path.isfile(filename):
        print(f"File '{filename}' not found.")
        return

    print("\nAnalyzing data...\n")
    total, human, types = parse_gene_info(filename)
    type_counts = Counter(types)

    print(f"1. Total genes listed: {total}")
    print(f"2. Genes listed for Homo sapiens: {human}")
    print(f"3. Unique gene types: {sorted(set(types))}")
    most_common_type, count = type_counts.most_common(1)[0]
    print(f"4. Most common gene type: {most_common_type} ({count} occurrences)")

if __name__ == "__main__":
    main()
