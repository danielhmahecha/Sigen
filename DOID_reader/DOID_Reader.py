import csv
def main():
    hpos=readFile()
    
    toCSV(hpos)
    print ('CHECK THE CSV FILE')

def readFile():
    f=open("/home/daniel/Documents/SIGEN/DATABASE/HumanDO.obo" ,"r")
    f1= f.readlines()
    doids=list()
    for i in range(len(f1)):
        x = f1[i]
        if x.startswith("id: DOID:"):
            id = x.replace("id: DOID:","").rstrip()
            y=f1[i+1]
            name = y.replace("name: ","").rstrip()
            doid = {"name": name,"DOID": id, "ai": ""}
            doids.append(doid)
    return doids 

def toCSV(doids):
    toCSV = doids
    with open('DOID.csv','w',encoding='utf8', newline='') as output_file:
        fc = csv.DictWriter(output_file, fieldnames=toCSV[0].keys())
        fc.writeheader()
        fc.writerows(toCSV)

if __name__=="__main__":
    main()