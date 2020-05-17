# -*- coding: utf-8 -*-

#kalan quiz

def kalan_quiz(liste):
    if len(liste)==0:
        return 14
    elif liste[-1]=="G":
        return kalan_quiz(liste[:-1])
    elif liste[-1]!="G":
        return 14- len(liste)

#kalan vize

def kalan_vize(liste):
    if liste[2]!=0:
        return 0
    elif liste[2]==0 and liste[1]==0 and liste[0]==0:
        return 3
    elif  liste[1]==0 and liste[2]==0:
        return 2
    elif liste[2]==0:
        return 1
    else:
        return 0
      
        

# quiz icerik ayristirna
def saf_quiz(a):
 # hepsi str
    key=set(list("0123456789G"))
    a=a.split('''<table class='bordered-table zebra-striped'><tr><th> Quiz No </th><th>''')[1]
    a=a.split('''</td></tr></table><br />''')[0]
    a=a.replace('/','').replace("<tr>",'').split("<td>")
    aa=[]
    for i in a:
        if i:
            aa.append(i)
    b=[]
    for i in aa:
        if '.' in i or i=='G':
            b.append(i)
    
    if len(b) !=28:
        print("quiz ayristirma hatasj")
    return b
    
# topla
def topla(liste,k=0):
    ii=0
    if k==0:
        for i in liste:
            try:
                ii+=float(i)
            except:
                pass
        return ii
    if k==1:
        for i in liste:
            try:
                ii+=float(i)
            except:
                print ("listede sayi olmayan var")
                
    
# vize icerik ayristirma
def saf_vize(a):
    a=a.split('''<table class='bordered-table zebra-striped'><tr><th>Ders</th><th>Vize No</th><th>Dinleme</th><th>Okuma</th><th>Yazılı</th><th>Sözlü</th><th>Ortalama</th></tr><tr><td>''')[1]
    a=a.split('''</td></tr><tr></table>''')[0]
    a=a.replace("/","").split("<td>")
    aa=[]
    sira=0
    for i in a:
        if i!="":
            try:
                aa.append(float(i))
            except:
                pass
    b=[]
    b.append(aa[5]*4)
    b.append(aa[11]*4)
    b.append(aa[17]*4)
    b.append(aa[23]*4)
    b.append(aa[29]*4)
    b.append(aa[35]*4)
    return b