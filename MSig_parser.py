import sys 
import fnmatch 
# Overlap file from MSigDB is the input file, Results the output 
def parse_overlaps(overlap_file, include_non_hallmarks=False): 
  fh = open(overlap_file, "r") 
  lines = fh.read() 
  fh.close() 
  split = lines.split("\n") 
  overlaps_shown = int(split[4].split('\t')[1]) 
  header_length = overlaps_shown + 15 result = [] 
  for gene in split[header_length:-1]: 
    elements = gene.split("\t") 
    entrez = elements[0] 
    GENE_NAME = elements[1]
    Description = elements[2] 
    Hallmarks = elements[3:] 
    filtered = fnmatch.filter(Hallmarks, 'HALLMARK*') 
    if filtered: 
      result.append([entrez, GENE_NAME, str(filtered), Description]) 
    elif include_non_hallmarks: 
      result.append([entrez, GENE_NAME, "No Hallmark hits", Description])
     
  return result
  
 
 
 def parse_header(overlap_file): 
   fh = open(overlap_file, "r") 
   lines = fh.read() fh.close() 
   split = lines.split("\n") 
   overlaps_shown = int(split[4].split('\t')[1]) 
   header_length = overlaps_shown + 10 
   header = split[0:header_length] 
   return header
   
def unique_entrez_filter(parsed_overlaps): 
overlaps_by_entrez = {} 
for overlap_row in parsed_overlaps: 
  entrez = overlap_row[0] 
  overlaps_by_entrez[entrez] = overlap_row 
return [overlaps_by_entrez[k] for k in overlaps_by_entrez]

def main(): 
  infile = sys.argv[1] # overlap file 
  outfile = sys.argv[2] 
  result = parse_overlaps(infile) 
  lines = ['\t'.join(gene) for gene in result] 
  all_text = '\n'.join(lines) 
  print('writing %i lines to %s' % (len(lines), outfile)) 
  with open(outfile, 'w') as fo: 
    fo.write(all_text + '\n')
 
if __name__ == '__main__': 
  main()
 
