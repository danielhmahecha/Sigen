import csv
def main():
    hpos=readFile()
    
    toCSV(hpos)
    print ('CHECK THE CSV FILE')

def readFile():
    f=open("/home/daniel/Documents/SIGEN/DATABASE/hp.obo" ,"r")
    f1= f.readlines()
    hpos=list()
    for i in range(len(f1)):
        x = f1[i]
        if x.startswith("id: HP:"):
            id = x.replace("id: HP:","").rstrip()
            y=f1[i+1]
            name = y.replace("name: ","").rstrip()
            hpo = {"HPO": id, "name": name, "idSymptom":""}
            hpos.append(hpo)
    return hpos 

def toCSV(hpos):
    toCSV = hpos
    with open('HPO.csv','w',encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file, fieldnames=toCSV[0].keys())
        fc.writeheader()
        fc.writerows(toCSV)

if __name__=="__main__":
    main()