import csv
from collections import OrderedDict
def main():
    omim = readOMIM()
    genes=readFile(omim)
    nodups=deleteDuplicates(genes)
    toCSV(nodups)
    #print ('CHECK THE CSV FILE')

def readFile(omim):
    genes = list()
    genesfile = '/home/daniel/Documents/SIGEN/DATABASE/GENES_LIST.txt'
    dialect = csv.excel()
    dialect.delimiter=','
    with open(genesfile,encoding="utf8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            for o in omim:
                if row['Gene name'] in o:
                    gene = {"symbol": row['Gene name'], "ensembl": row['Gene stable ID'], "chromosome": row['Chromosome/scaffold name'], "initPos": row['Gene start (bp)'], "finalPos": row['Gene end (bp)'], "idGene":""}
                    genes.append(gene)
    
    return genes

def deleteDuplicates (genes):
    l=genes

    clean=[dict(t) for t in {tuple(d.items()) for d in l}]
    return clean

def readOMIM():
    omim = list()
    f=open("/home/daniel/Documents/SIGEN/DATABASE/OMIM-MENDELIAN.txt" ,"r")
    f1= f.readlines()
    for x in f1:
        omim.append(x)

    return omim 

def toCSV(genes):
    toCSV = genes
    with open('Genes.csv','w',encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file, fieldnames=toCSV[0].keys())
        fc.writeheader()
        fc.writerows(toCSV)


if __name__=="__main__":
    main()



