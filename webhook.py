from flask import Flask, jsonify, request, make_response, render_template
import DataBase as DataBase
import random

'''
Variables
'''
#Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/patientsearch", methods=['GET','POST'])
def patientSearch():
 
  return render_template("patientSearch.html")

@app.route("/variantsearch")
def variantSearch():
  return render_template("variantSearch.html")

@app.route("/clinicalsearch")
def clinicalSearch():
  return render_template("clinicalSearch.html")

@app.route("/patientcreation", methods=['GET','POST'])
def patientCreation():
  data=''
  if 'sigenID' and 'sex' in request.args.keys():
    sigenID = request.args['sigenID']
    sex = request.args['sex']
    DataBase.createPatient(sigenID,sex)
    data = 'Patient Created: '+sigenID
  return render_template("patientCreation.html",data=data)

@app.route("/variantcreation")
def variantCreation():
  return render_template("variantCreation.html")

@app.route("/genotypecreation")
def genotypeCreation():
  return render_template("genotypeCreation.html")

@app.route("/diseaseInfo", methods=['GET','POST'])
def diseaseInfo():
    #print(request.args)
    #print(request.path)

    if 'diseasename' in request.args.keys():
      diseasename=request.args['diseasename']
      info = DataBase.identifyDiseaseName(diseasename) 
    elif 'doid' in request.args.keys():
      doid=request.args['doid']
      info = DataBase.identifyDiseaseDOID(doid) 


    data={'info': info, 'symptoms': None, 'variants': None, 'patients':None}
    return render_template('diseaseInfo.html',data=data)

@app.route("/symptomInfo", methods={'GET','POST'})
def symptomInfo():

    if 'symptomname' in request.args.keys():
      symptomname = request.args['symptomname']
      info = DataBase.identifySymptomName(symptomname)
    elif 'hpo' in request.args.keys():
      hpo = request.args['hpo']
      info = DataBase.identifySymptomHPO(hpo)
    print('INFO',info)
    data={'info': info, 'diseases': None, 'patients': None}
    return render_template('symptomInfo.html',data=data)

@app.route("/patientInfo", methods=['GET','POST'])
def patientInfo():
    #print(request.args)
    #print(request.path)

    if 'sigenID' in request.args.keys():
      sigenID=request.args['sigenID']
      info = DataBase.identifyPatientID(sigenID)
    elif 'doid' in request.args.keys():
      doid=request.args['doid']
      info = DataBase.identifyDiseaseDOID(doid) 


    data={'info': info, 'diseases': None, 'symptoms': None, 'variants':None}
    return render_template('patientInfo.html',data=data)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)