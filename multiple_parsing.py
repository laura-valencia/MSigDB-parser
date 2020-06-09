import msigdb_parser 
import MatchFiles 

def multiple_parsing(overlap_infile, correlations_infile, outfile): 
  overlaps = msigdb_parser.parse_overlaps(overlap_infile) 
  correlations = MatchFiles.parse_correlations(correlations_infile) 
  matched_genes_by_entrez_id = MatchFiles.match_gene_lists(overlaps, correlations) 
  
  with open(outfile, 'w') as out: 
    out.write('IlluminaID' + '\t' + 'ENTREZ_GENE_ID' + '\t' + 'SYMBOL' + '\t' + 'Duplicates' + '\t' + 'cor1' + '\t' + 'PADJ1' + '\t' + 'cor2' + '\t' + 'PADJ2' + '\t' + 'ATF4 target' + '\t' + 'Description' + '\t' + 'Hallmark' + '\n') 
    out.write('\n'.join(['\t'.join([str(col) for col in line]) for line in matched_genes_by_entrez_id])) 
    
  return outfile 
  
  #multiple_parsing('overlap.txt', 'correlations.csv', 'outfile')
  
  #Example: 
  
  multiple_parsing('overlap_positive_GCN1.txt', 'main_GCN1L1_positive_ATF4_.csv', 'main2_pos_GCN1_matched.csv')
