import csv
def main():
    omim = readOMIM()
    genes=readFile(omim)
    toCSV(genes)
    #print ('CHECK THE CSV FILE')

def readFile(omim):
    genes = list()
    genesfile = '/home/daniel/Documents/SIGEN/DATABASE/Transcripts-biomart.txt'
    dialect = csv.excel()
    dialect.delimiter=','
    with open(genesfile,encoding="utf8") as csvfile:
        spamreader = csv.DictReader(csvfile, dialect=dialect)
        for row in spamreader:
            for o in omim:
                if row['Gene name'] in o:
                    gene = {"stableID": row['Transcript stable ID'], "chromosome": row['Chromosome/scaffold name'], "initPos": row['Transcript start (bp)'], "finalPos": row['Transcript end (bp)'], "geneSymbol": row['Gene name'], "idTranscript":""}
                    genes.append(gene)
    
    return genes

def readOMIM():
    omim = list()
    f=open("/home/daniel/Documents/SIGEN/DATABASE/OMIM-MENDELIAN.txt" ,"r")
    f1= f.readlines()
    for x in f1:
        omim.append(x)

    return omim 

def toCSV(genes):
    toCSV = genes
    with open('Transcripts.csv','w',encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file, fieldnames=toCSV[0].keys())
        fc.writeheader()
        fc.writerows(toCSV)


if __name__=="__main__":
    main()



