# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 10:02:51 2023

@author: Pr.TAC_MACHINO
"""
#import time
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import glob
symptomes_patient = []
a = []
avc = []
palu = []
typhoide = []
vih = []
meningite = []
hepatite = []
grippe = []
ebola = []
drepanocytose = []
diabete = []
covid = []
cholera = []
chlamedia = []
cancer = []
liste = []
liste_symptomes = []


app = Flask(__name__)

liste_maladie = glob.glob("*.txt")
t_symptome = 0

liste.append(avc),liste.append(cancer),liste.append(chlamedia),liste.append(cholera),liste.append(covid)
liste.append(diabete),liste.append(drepanocytose),liste.append(ebola),liste.append(grippe),liste.append(hepatite)
liste.append(meningite),liste.append(palu),liste.append(typhoide),liste.append(vih)
for file,i in zip(liste_maladie,range(0,len(liste_maladie))):
    nom = liste[i]
    with open(file,"r") as f:
        symptome = f.read().splitlines()
        for alpha in symptome :
            if alpha not in liste_symptomes :
                liste_symptomes.append(alpha)
b = len(liste_symptomes)
numéros = [(i+1) for i in range(b)]
dic_maladie = {numéro:maladie for numéro,maladie in zip(numéros,liste_symptomes)}

def control(a):
    for file,i in zip(liste_maladie,range(0,len(liste_maladie))):
        nom = liste[i]
        with open(file,"r") as f:
            symptome = f.read().splitlines()
        for j in symptome:
            for l in a:
                if l == j:
                    nom.append(l)
    x = stat()
    return x

def stat():
    min = 0
    for i in range(0,len(liste)):
        if len(liste[i])>min:
            malade = i
            min = len(liste[i])
        else :
            min = min
    stat = str((len(liste[malade])/len(a))*100)
    print(stat)
    result = str(liste_maladie[malade][:-4])
    r="vous avez " + stat + "% de chance d'avoir la maladie nomée " + result
    return r
    
    
@app.route("/")
def hello():
    return "Hello sipsio, word!"

@app.route("/bot",methods=['POST'])




def bot():
    """Respond to incoming calls with a simple text message."""
    #Fetch th message
    usr_msg = request.form.get('Body')
    
    # création de la reponse
    resp = MessagingResponse()
    msg = resp.message()
    if 'salut' in usr_msg:
        msg.body("salut!! comment puis je t'aider???\n")
        #time.sleep(1)
        msg.body(" c'est pour une consultation ou pour le bilan de santé??\n")
    elif 'consultation' in usr_msg:
        msg.body("ok, nous allons vous consulté.                  \n")
        #time.sleep(3)
        msg.body("Parmi les symptomes suivants, lesquels présentez vous??(entrer juste les numéros des symptomesséparés de la vigule")
        #prenoms = ['pierre','jean','julie','sophie']
        #ages = [24,54,56,65,25,98,35]
        #dico_2 = {prenom:age for prenom,age in zip(prenoms,ages) if age>30}
        for i in range(10) :
            h = str(i+1)
            msg.body(h + dic_maladie[i+1])
        for i in range(10) :
            h = str(i+11)
            msg.body(h + dic_maladie[i+11])
        for i in range(10) :
            h = str(i+21)
            msg.body(h + dic_maladie[i+21])
        for i in range(10) :
            h = str(i+31)
            msg.body(h + dic_maladie[i+31])
        symptomes_patient = usr_msg.split(",")
        #msg.body(symptomes_patient)
    elif 'bilan' in usr_msg:
        msg.body("vous pouvez trouver votre bilan de santé à cette addres :   \n")
        #time.sleep(1)
        msg.body("https://www.youtube.com/@H2esInstitute")
    elif symptomes_patient(0) in numéros :
        for num in symptomes_patient:
            de = dic_maladie[num]
            a.append(de)
        message = control(a)
        msg.body(message)
    return str(resp)


if __name__ =="__main__":
    app.run(debug=True)