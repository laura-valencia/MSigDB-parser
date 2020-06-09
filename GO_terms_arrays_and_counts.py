import fnmatch 
from tabulate import tabulate 

# Returns the number of genes per GO term (count_outfile) 
# Returns an array with whether each GO term is present in each gene (0=not, 1=yes) 

def main(input_file, array_outfile, counts_outfile): 
  fh = open(input_file, "r") 
  lines = fh.read() fh.close() 
  split = lines.split("\n") 
  overlaps_shown = int(split[4].split('\t')[1]) 
  header_length = overlaps_shown + 10 
  gene_start = header_length + 5 
  GO_Header = [] 
  for gene in split[10:header_length]:
    elements = gene.split("\t") 
    GO_test = elements[0] 
    GO_description = elements[2] 
    GO_Header.append([GO_test, GO_description])
  GO_gene = [] 
  all_genes = [] 
  for gene in split[gene_start:-1]: 
  elements = gene.split("\t") 
  entrez = elements[0] 
  SYMBOL = elements[1] 
  GO_terms_raw = elements[3:] 
  GO_terms = fnmatch.filter(GO_terms_raw, 'GO*') 
  if GO_terms: 
    GO_gene.append(GO_terms)
  all_genes.append((entrez, SYMBOL, GO_terms))
  
Matches = [] 
for GO_list in GO_Header: 
  GO_test = GO_list[0] 
  Match_count = 0
  
  for GO_terms in GO_gene: 
    Match_count += GO_terms.count(GO_test)
  
  Matches.append([GO_test, Match_count])  
  
# Returns the array of GO terms with genes (arrays) 

with open(array_outfile, 'w') as genes_file: 
  all_go_terms = [] 
  for header_line in GO_Header: 
    GO_test = header_line[0] 
    all_go_terms.append(GO_test) 
  # use all_go_terms to write top_line_go_terms on the file 
  top_line_go_term_names = [] 
  for g_name in all_go_terms: 
    top_line_go_term_names.append(g_name) 
  genes_file.write("Entrez\tSymbol\t" + "\t".join(top_line_go_term_names) + "\n") 
  for (entrez, symbol, GO_terms) in all_genes: 
    gene_line = [entrez, symbol] 
    for term in all_go_terms: 
      gene_line.append(str(GO_terms.count(term))) # either 1 or 0 
    genes_file.write("\t".join(gene_line) + "\n") 
    
    # Returns the number of genes per GO term (counts) 
with open(counts_outfile, 'w') as counts_file: 
  counts_file.write("GO_Term\tCount\n") 
  for match in Matches: 
    counts_file.write("\t".join([str(m) for m in match]) + "\n")
    
if __name__ == "__main__": 
  main("GCN1.txt", "GCN1_array2.csv", "GCN1_count2.csv")
