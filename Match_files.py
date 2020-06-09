import sys 
#compare entrez ID in both files and write only the genes with hallmarks 
def parse_correlations(correlations_filename): 
  fh = open(correlations_filename, "r") 
  lines = fh.read() 
  fh.close() 
  list_of_lines = lines.split("\n") 
  result_genes = [] 
  for gene in list_of_lines[1:-1]: 
    elements = gene.split(",") 
    IlluminaID = elements[0] 
    entrez = elements[1] 
    duplicates = elements[3] 
    PADJ1 = elements[5] 
    PADJ2 = elements[7] 
    cor1 = elements[4] 
    cor2 = elements[6] 
    ATF4 = elements[8] 
    gene_tuple = (IlluminaID, entrez, duplicates, cor1, float(PADJ1), cor2, float(PADJ2), ATF4) #ATF4 was used as positive control for a cell stress pathway test we were studyng
    result_genes.append(gene_tuple) 
 return result_genes 
 
def match_gene_lists(overlaps, correlations): 
  result = [] 
  for correlation_elements in correlations: 
    IlluminaID = correlation_elements[0] 
    Corr_entrez = int(correlation_elements[1]) 
    duplicates = correlation_elements[2] 
    cor1 = correlation_elements[3] 
    PADJ1 = float(correlation_elements[4]) 
    cor2 = correlation_elements[5] 
    PADJ2 = float(correlation_elements[6]) 
    ATF4 = correlation_elements[7] 
    for gene_elements in overlaps: 
      Res_entrez = int(gene_elements[0]) 
      GENE_NAME = gene_elements[1] 
      Hallmarks_temp = gene_elements[2] 
      Hallmarks = Hallmarks_temp[1:-1].replace(",", "\t") 
      Description = gene_elements[3]
      if Res_entrez==Corr_entrez: 
        result.append([IlluminaID, Res_entrez, GENE_NAME, duplicates, cor1, str(PADJ1), cor2, str(PADJ2), ATF4, Description, Hallmarks]) 
 return result
 
 def match_gene_lists(overlaps, correlations): 
    result = [] for correlation_elements in correlations: 
    IlluminaID = correlation_elements[0] 
    Corr_entrez = int(correlation_elements[1]) 
    duplicates = correlation_elements[2] 
    cor1 = correlation_elements[3] 
    PADJ1 = float(correlation_elements[4]) 
    cor2 = correlation_elements[5] 
    PADJ2 = float(correlation_elements[6]) 
    ATF4 = correlation_elements[7] 
    for gene_elements in overlaps: 
      Res_entrez = int(gene_elements[0]) 
      GENE_NAME = gene_elements[1] 
      Hallmarks_temp = gene_elements[2] 
      Hallmarks = Hallmarks_temp[1:-1].replace(",", "\t") 
      Description = gene_elements[3] 
      if Res_entrez==Corr_entrez: 
        result.append([IlluminaID, Res_entrez, GENE_NAME, duplicates, cor1, str(PADJ1), cor2, str(PADJ2), ATF4, Description, Hallmarks]) 
  return result

def main(): 
  overlaps_file = sys.argv[1] 
  correlations_file = sys.argv[2] 
  outfile = sys.argv[3] 
  #Open first input file 
  fh = open(overlaps_file, "r") 
  overlap_lines = fh.read() 
  fh.close() 
  #Open second input file 
  fh = open(correlations_file, "r") 
  correlation_lines = fh.read() 
  fh.close() 
  #Get each line of Results file and the PAdjusted correlation file 
  overlap_split = overlap_lines.split("\n") 
  correlation_split = correlation_lines.split("\n") 
  correlations = [gene.split('\t') for gene in correlation_split[0:-1]] 
  overlaps = [gene.split('\t') for gene in overlap_split[0:-1]] 
  matched = match_gene_lists(overlaps, correlations) 
  with open(outfile, "w") as fo: 
    matched.sort(key=lambda cols: cols[0]) 
    print('Number of lines: %i' % len(matched)) 
    print('Number of unique genes: %i' % len(set([cols[0] for cols in result]))) 
    fo.write('\n'.join(['\t'.join([str(col) for col in cols]) for cols in result])) 
    
    
 if __name__ == '__main__': 
   main()
