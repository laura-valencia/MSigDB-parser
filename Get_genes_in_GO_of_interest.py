def get_genes_in_goterm(goterms_of_interest_fn, gene_descriptions_fn, matrix_fns_by_goi, outfile_fn):
  goterms_of_interest = []
  
  with open(goterms_of_interest_fn, "r") as goterms_of_interest_handler:
    goterms_of_interest = [goterm.replace("\n", "") for goterm in goterms_of_interest_handler.readlines()]

  gene_descriptions = {}

  with open(gene_descriptions_fn, "r") as gene_descriptions_handler:
    for gene_line in gene_descriptions_handler.readlines():
      (entrez_gene_id, desc) = gene_line.replace("\n", "").split("\t")
      gene_descriptions[entrez_gene_id] = desc

  gois = [key for key in matrix_fns_by_goi]

  genes_in_goterm_by_goterm = {}
  
  for goterm in goterms_of_interest:
    genes_in_goterm = {}

    for goi, matrix_fn in matrix_fns_by_goi.items():
      matrix_header = []
      gene_matrix_body = [[]]

      with open(matrix_fn, "r") as matrix_file_handler:
        matrix_header = matrix_file_handler.readline().replace("\n", "").split("\t")
        gene_matrix_body = [gene_line.replace("\n", "").split("\t") for gene_line in matrix_file_handler.readlines()]

      for gene_line in gene_matrix_body:
        entrez = gene_line[0]
        symbol = gene_line[1]
        desc = gene_descriptions[entrez]

        if goterm in matrix_header:
          goterm_index = matrix_header.index(goterm)
          is_gene_in_goterm = gene_line[goterm_index] == "1"
          
          if is_gene_in_goterm:
            if not symbol in genes_in_goterm:
              genes_in_goterm[symbol] = { "entrez": entrez, "desc": desc }

            genes_in_goterm[symbol][goi] = 1
    
    if len(genes_in_goterm) > 0:    
      genes_in_goterm_by_goterm[goterm] = genes_in_goterm  
      
  matched_genes_header = ["Goterm", "Gene", "Entrez", "Description"]

  for goi in gois:
    matched_genes_header.append(goi)

  matched_genes = []

  for goterm, genes_in_goterm in genes_in_goterm_by_goterm.items():
    for symbol, data in genes_in_goterm.items():
      data_line = [goterm, symbol, data["entrez"], data["desc"]]

      for goi in gois:
        data_line.append(data[goi] if goi in data else 0)

      matched_genes.append(data_line)

  with open(outfile_fn, "w") as outfile_fh:
    outfile_fh.write("\t".join(matched_genes_header) + "\n")
    
    for row in matched_genes:
      outfile_fh.write("\t".join([str(col) for col in row]) + "\n")

  return 0

if __name__ == "__main__":
  get_genes_in_goterm(
    goterms_of_interest_fn="GO_of_interest_G2M.txt", 
    matrix_fns_by_goi={"EIF2AK4": ".\data\G2M_GO_and_genes_EIF2AK4.csv", "GCN1L1": ".\data\G2M_GO_and_genes_GCN1L1.csv"}, 
    gene_descriptions_fn="gene_descriptions.tsv", 
    outfile_fn=".\out\G2M_genes_in_goterm.txt")
