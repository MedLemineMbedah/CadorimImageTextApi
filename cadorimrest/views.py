from operator import imod
from unittest import result
from django.shortcuts import render
from django.http import JsonResponse
from numpy import save
from rest_framework.decorators import api_view
from rest_framework.response import Response
import easyocr
import sys
import re
from .models import Cart
from .models import BackCart
from .models import Book
from .models import PassePort
from .serializers import BookSerial
from .models import Documents


from django.contrib.auth.forms import UserCreationForm 


# Create Rest pour la lecture de texte dans les image


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        data = {'texte': "Hello World"}
        return JsonResponse(data)
    elif request.method == 'POST':
        return 1


@api_view(['GET', 'POST'])
def detectTextPassport(request):


    if request.method == 'GET':
        
        data = {'text': "Aucune Image"}
        b = Book(title='Beatles Blog', author='All the latest Beatles news.')
        b.save()

    #  sys.stdout = open("textjsontest.txt", "w")
        return JsonResponse(data)

    elif request.method == 'POST':
        text = ""
        data = request.data
        
        chemin = data['chemin']
        print(chemin)

        reader = easyocr.Reader(['en', 'ar'])
        results = reader.readtext(chemin)
        for result in results:
            text += result[1] + ","
            print(text)
        
        engText = re.sub(r'[^\x00-\x7f]', r'', text)
        imageTexte = {'data': engText}




        
        b=imageTexte['data']
        a=[]
        a  = b.split(',')
        c=[]
        j=0
        k=0
        #affichage
        p=0
        for i in a:
            if(a[j] and not a[j].isspace()):
              print("a[",p,"] = ",a[j])
              c.append(a[j])
              j=j+1
              p=p+1
            else:
              j=j+1

        # cr = Cart(NNI=c[3],Nom=c[9],Prenom=c[7],Sex=c[12],date_naiss=c[15],lieu_de_nai=c[17],Pays='Mauritanie',typeDocument="Carte d'identification",Path=chemin)
        # cr.save()
        pas = PassePort(NNI=c[16],Nom=c[10],Prenom=c[12],Sex=c[20],date_naiss=c[19],lieu_de_nai=c[23],Pays='Mauritanie',dateEmission=c[26],dateValidie=c[27],typeDocument="Passe Port",Path=chemin) 
        pas.save()
      
        print("####################### C #########################")
        with open('PassPort.txt', 'w') as filehandle:
         for listitem in c:
            filehandle.write('%s\n' % listitem)
        y=0
        for l in c :
            print("c[",y,"] = ",c[y])
            y=y+1
            
            
        engText = re.sub(r'[^\x00-\x7f]', r'', text)
        imageTexte = {'data': engText}


        
        return JsonResponse(imageTexte)


@api_view(['GET', 'POST'])
def detectTextCart(request):

  
    if request.method == 'GET':
        
        data = {'text': "Aucune Image"}
        b = Book(title='Beatles Blog', author='All the latest Beatles news.')
        b.save()

    #  sys.stdout = open("textjsontest.txt", "w")
        return JsonResponse(data)

    elif request.method == 'POST':
        text = ""
        data = request.data
        
        chemin = data['chemin']
        print(chemin)

        reader = easyocr.Reader(['en', 'ar'])
        results = reader.readtext(chemin)
        for result in results:
            text += result[1] + ","
            print(text)
        
        engText = re.sub(r'[^\x00-\x7f]', r'', text)
        imageTexte = {'data': engText}




        
        b=imageTexte['data']
        a=[]
        a  = b.split(',')
        c=[]
        j=0
        k=0
        #affichage
        p=0
        for i in a:
            if(a[j] and not a[j].isspace()):
              print("a[",p,"] = ",a[j])
              c.append(a[j])
              j=j+1
              p=p+1
            else:
              j=j+1
       # cr = Cart(NNI=c[3],Nom=c[9],Prenom=c[7],Sex=c[12],date_naiss=c[15],lieu_de_nai=c[17],Pays='Mauritanie',typeDocument="Carte d'identification",Path=chemin)
       # cr.save()
       
      
        print("####################### C #########################")
        with open('cart.txt', 'w') as filehandle:
         for listitem in c:
            filehandle.write('%s\n' % listitem)
        y=0
        for l in c :
            print("c[",y,"] = ",c[y])
            y=y+1
            
            
        engText = re.sub(r'[^\x00-\x7f]', r'', text)
        imageTexte = {'data': engText}


        
        return JsonResponse(imageTexte)


@api_view(['GET', 'POST'])
def test(request):

    if request.method == 'GET':
        
        # string1 = 'CARTE'
        
        # # opening a text file
        # file1 = open("cart.txt", "r")
        
        # # read file content
        # readfile = file1.read()
        
        # # checking condition for string found or not
        # if string1 in readfile: 
        #     #print('String', string1, 'Found In File')
        #     data = {'resultat': "Document est une carte"}
        # else: 
        #     #print('String', string1 , 'Not Found') \
        #     data = {'resultat': "Not Found"}
        
        # # closing a file
        # file1.close()
        #file1 = open("doc.txt", "r")
        # Program to show various ways to read and
        # write data in a file.
       
        print("################### Start GetInfo Fonction ##################")
        #print(getData("Prenom"))
        cr = Cart(NNI=getNNI(),Nom=getData("Nom"),Prenom=getData("Prenom"),Sex=getData("Sexe"),date_naiss=getData("Date de naissance"),lieu_de_nai=getData("Lieu de naissance"),Pays=getData("Nom"),typeDocument=getTypeDocument())
        cr.save()
        # print("################### End GetInfo Fonction ##################")
        #print("NNI size :",len(str(180777250102)))    
        # txt = "180777250102m"

        # x = txt.isnumeric()

        # print("IS number : ",x)
        
        data={'Domcuments':'parfait'}
       
        # b = Book(title='Beatles Blog', author='All the latest Beatles news.')
        # b.save()

    #  sys.stdout = open("textjsontest.txt", "w")
        return JsonResponse(data)

    elif request.method == 'POST':
        text = ""
        data = request.data
        
        chemin = data['chemin']
        print(chemin)

        reader = easyocr.Reader(['en', 'ar'])
        results = reader.readtext(chemin)
        for result in results:
            text += result[1] + ","
            print(text)
        
        engText = re.sub(r'[^\x00-\x7f]', r'', text)
        imageTexte = {'data': engText}




        
        b=imageTexte['data']
        a=[]
        a  = b.split(',')
        c=[]
        j=0
        k=0
        #affichage
        p=0
        for i in a:
            if(a[j] and not a[j].isspace()):
              print("a[",p,"] = ",a[j])
              c.append(a[j])
              j=j+1
              p=p+1
            else:
              j=j+1
        # cr = Cart(NNI=c[3],Nom=c[9],Prenom=c[7],Sex=c[12],date_naiss=c[15],lieu_de_nai=c[17],Pays='Mauritanie',typeDocument="Carte d'identification",Path=chemin)
        # cr.save()
       
      
        print("####################### C #########################")
        with open('data.txt', 'w') as filehandle:
         for listitem in c:
            filehandle.write('%s\n' % listitem)
        y=0
        for l in c :
            print("c[",y,"] = ",c[y])
            y=y+1

        print("###################### Type de Document ######################")
       # print(typeDocument())

        # cr = Cart(NNI=getNNI(),Nom=getData("Nom"),Prenom=getData("Prenom"),dateValidie=getData("date Validie"),dateEmission=getData("date Emission"),codePostale=getData("code Postale"),Ville=getData("Ville"),Rue=getData("Rue"),Sex=getData("Sexe"),date_naiss=getData("Date de naissance"),lieu_de_nai=getData("Lieu de naissance"),NumeroDocument=getNNI(),Pays=getData("Pays"),typeDocument=getTypeDocument(),Path=chemin)
        # cr.save()
            
        # engText = re.sub(r'[^\x00-\x7f]', r'', text)
        # imageTexte = {'data': engText}


        
        return JsonResponse(imageTexte)
       


@api_view(['GET', 'POST'])
def CartBack(request):

    if request.method == 'GET':
        
        data = {'text': "Aucune Image"}
        b = Book(title='Beatles Blog', author='All the latest Beatles news.')
        b.save()

    #  sys.stdout = open("textjsontest.txt", "w")
        return JsonResponse(data)

    elif request.method == 'POST':
        text = ""
        data = request.data
        
        chemin = data['chemin']
        print(chemin)

        reader = easyocr.Reader(['en', 'ar'])
        results = reader.readtext(chemin)
        for result in results:
            text += result[1] + ","
            print(text)
        
        engText = re.sub(r'[^\x00-\x7f]', r'', text)
        imageTexte = {'data': engText}


        b=imageTexte['data']
        a=[]
        a  = b.split(',')
        c=[]
        j=0
        k=0
        #affichage
        p=0
        for i in a:
            if(a[j] and not a[j].isspace()):
              print("a[",p,"] = ",a[j])
              c.append(a[j])
              j=j+1
              p=p+1
            else:
              j=j+1
        # cr = Cart(NNI=c[3],Nom=c[9],Prenom=c[7],Sex=c[12],date_naiss=c[15],lieu_de_nai=c[17],Pays='Mauritanie',typeDocument="Carte d'identification",Path=chemin)
        # cr.save()
        Bcr = BackCart(dateEmission=c[6],dateValidie=c[2],Path=chemin)
        Bcr.save()
      
        print("####################### C #########################")
        with open('BackCart.txt', 'w') as filehandle:
         for listitem in c:
            filehandle.write('%s\n' % listitem)
        y=0
        for l in c :
            print("c[",y,"] = ",c[y])
            y=y+1
            
            
        engText = re.sub(r'[^\x00-\x7f]', r'', text)
        imageTexte = {'data': engText}


        
        return JsonResponse(imageTexte)


def getTypeDocument():
    
    file1 = open("data.txt", "r")
    
    readfile = file1.read()
    data_db = Documents.objects.all()
    for d in data_db:
        if d.type in readfile: 
            if d.nationalite in readfile:
                return d.type
    return "Not Found"
        
   

def getData(name):

    file1 = open("data.txt", "r")
    lines = []
    with file1 as f:
        lines = f.readlines()
    count = 0
    pos=0
    for line in lines:
        if name in line:
            break
        pos+=1
    for line in lines:
        if count == pos +1 :
           return line
        count+=1

    return "vide"


def getNNI():

    file1 = open("data.txt", "r")
    lines = []
    with file1 as f:
        lines = f.readlines()
    for line in lines:
        try:
            value=int(line)
        except:
            value =0
        if value !=0 :
            return line
      
    return "Acun NNI dans la fichier"











    # # checking condition for string found or not
    # if "PASSEPORT" in readfile: 
    #     if "FRA" in readfile:
    #         return "passeport francaise"
    #     else:
    #          return "passeport mauritanienne"
    # elif "CARTE" in readfile:
    #     if "CARTE NATIONALE" in readfile:
    #         return "carte francaise"
    #     else:
    #          return "carte mauritanienne"
    # else: 
    #     #print('String', string1 , 'Not Found') \
    #     return "Not Found"
    
    # # closing a file
    # file1.close()

