# MSigDB parsing codes
-------------------
## MSig_parser.py
When exploring molecular signatures in the MSig database (Hallmarks), one can download a text file with results. This Python code is useful to change the text format into a table with a format that can be read in another program. 

## Match_files.py
This code is used to match Entrez IDs of a gene with correlation information to a table with Hallmarks obtained from MSigDB

## Multiple parsing code
Here both MSig_parser.py and Match_files.py are used to parse multiple files

## GO_term_arrays_and_counts.py
When exploring GO terms in MSigDB, one can retrieve a results file with multiple GO terms that matched to the input gene set. This code parses the text into a table with a format readable by another program.

## Get_genes_in_GO_of_interest.py
This code needs several input files and uses handles to work with them. A list of GO terms of interest are matched to gene descriptions and the GO term array produced in the previous step. The code generates a list with genes that have any of the GO terms of interest and include ENTREZ IDs and descriptions.
