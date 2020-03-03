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
def identifyVariantGene(geneSymbol):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Variant WHERE geneSymbol = \'{}\''.format(geneSymbol))
    ans = mycursor.fetchall()
    return ans

'''
Finds variants on a given position
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

def identifyGeneEnsembl(ensembl):
    mycursor.execute("USE " + databaseName)
    mycursor.execute('SELECT * FROM Gene WHERE ensembl = \'{}\''.format(ensembl))
    ans = mycursor.fetchall()
    return ans

