import gzip

def parse_gene_info(file_path):
    with gzip.open(file_path, 'rt') as f:
        headers = f.readline().strip().split("\t")
        tax_col = headers.index("#tax_id")
        type_col = headers.index("type_of_gene")

        total_genes = 0
        human_genes = 0
        gene_types = []

        for line in f:
            total_genes += 1
            parts = line.strip().split("\t")
            if len(parts) <= max(tax_col, type_col):
                continue
            tax_id = parts[tax_col]
            gene_type = parts[type_col]
            gene_types.append(gene_type)
            if tax_id == "9606":
                human_genes += 1

        return total_genes, human_genes, gene_types
