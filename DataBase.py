import mysql.connector

databaseName='sigenDB'
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Sigen100%",buffered=True)
mycursor=mydb.cursor()

'''
FUNCTIONS
'''

'''
    Variants Finders
'''

'''
Finds a variant by rsID
'''
def identifyVariantRsid(rsID):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Variant WHERE rsID = \'{}\''.format(rsID))
    ans = mycursor.fetchall()
    return ans

'''
Finds a variant by clinvar identifier
'''
def identifyVariantClinvar(clinvar):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Variant WHERE clinvar = \'{}\''.format(clinvar))
    ans = mycursor.fetchall()
    return ans

'''
Finds variants with a given Clinical Significance
'''

def identifyVariantClinsig(clinSig):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Variant WHERE clinSig = \'{}\''.format(clinSig))
    ans = mycursor.fetchall()
    return ans

'''
Finds variants for a given Gene Symbol
'''
def identifyVariantGeneSymbol(geneSymbol):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Variant WHERE geneSymbol = \'{}\''.format(geneSymbol))
    ans = mycursor.fetchall()
    return ans

'''
Finds variants on a given position (range)
'''
def identifyVariantPosition(chromosome, initPos, finalPos):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Variant WHERE chromosome = \'{}\' AND initPos >= \'{}\' AND finalPos <= \'{}\''.format(chromosome, initPos, finalPos))
    ans = mycursor.fetchall()
    return ans

'''
    Genes Finders
'''

'''
Finds a gene by its gene symbol
'''
def identifyGeneSymbol(symbol):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Gene WHERE symbol = \'{}\''.format(symbol))
    ans = mycursor.fetchall()
    return ans

'''
Finds a gene by its ENSEMBL identifier
'''
def identifyGeneEnsembl(ensembl):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Gene WHERE ensembl = \'{}\''.format(ensembl))
    ans = mycursor.fetchall()
    return ans

'''
Finds genes on a given position (range)
'''
def identifyGenePosition(chromosome, initPos, finalPos):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Gene WHERE chromosome = \'{}\' AND initPos >= \'{}\' AND finalPos <= \'{}\''.format(chromosome, initPos, finalPos))
    ans = mycursor.fetchall()
    return ans

'''
    Transcripts Finder
'''

'''
Finds transcript by stable ID
'''
def identifyTranscriptStableID(stableID):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Transcript WHERE stableID = \'{}\''.format(stableID))
    ans = mycursor.fetchall()
    return ans

'''
Finds transcripts by gene symbol
'''
def identifyTranscriptGeneSymbol(geneSymbol):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Transcript WHERE geneSymbol = \'{}\''.format(stableID))
    ans = mycursor.fetchall()
    return ans

'''
Finds transcripts on a given position (range)
'''
def identifyTranscriptPosition(chromosome, initPos, finalPos):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Transcript WHERE chromosome = \'{}\' AND initPos >= \'{}\' AND finalPos <= \'{}\''.format(chromosome, initPos, finalPos))
    ans = mycursor.fetchall()
    return ans

'''
    Patients finder
'''

'''
Finds a patient by sigen ID
'''
def identifyPatientID(sigenID):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Patient WHERE sigenID = \'{}\''.format(sigenID))
    ans = mycursor.fetchall()
    return ans

'''
Finds patients by given sex
'''
def identifyPatientSex(sex):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Patient WHERE sex = \'{}\''.format(sex))
    ans = mycursor.fetchall()
    return ans

'''
    Diseases Finders
'''

'''
Finds Disease by Name
'''
def identifyDiseaseName(name):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Disease WHERE name = \'{}\''.format(name))
    ans = mycursor.fetchall()
    return ans

'''
Finds Disease by DOID
'''
def identifyDiseaseDOID(DOID):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Disease WHERE DOID = \'{}\''.format(DOID))
    ans = mycursor.fetchall()
    return ans

'''
    Symptoms Finders
'''

'''
Finds Symptom by Name
'''
def identifySymptomName(name):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Symptom WHERE name = \'{}\''.format(name))
    ans = mycursor.fetchall()
    return ans

'''
Finds Symptom by HPO
'''
def identifySymptomHPO(HPO):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Symptom WHERE HPO = \'{}\''.format(HPO))
    ans = mycursor.fetchall()
    return ans

'''
    CREATORS
'''

'''
Creates a variant with the info given by parameter
'''
def createVariant(rsIDp, clinvarp, clinSigp, chromosomep, initPosp, finalPosp, geneSymbolp):
    mycursor.execute("USE "+ databaseName)
    mycursor.execute("INSERT INTO Variant (rsID, clinvar, clinSig, chromosome, initPos, finalPos, geneSymbol) VALUES (\'{rsID}\', \'{clinvar}\', \'{clinSig}\', {chromosome}, {initPos}, {finalPos}, \'{geneSymbol}\')".format(rsID = rsIDp, clinvar = clinvarp, clinSig = clinSigp, chromosome = chromosomep, initPos = initPosp, finalPos = finalPosp, geneSymbol = geneSymbolp))
    mydb.commit()

'''
Creates a patient with the info given by parameter
'''
def createPatient(sigenIDp, sexp):
    mycursor.execute("USE "+ databaseName)
    mycursor.execute("INSERT INTO Patient (sigenID, sex) VALUES (\'{sigenID}\', \'{sex}\')".format(sigenID = sigenIDp, sex = sexp))
    mydb.commit()

