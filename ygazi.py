# -*- coding: utf-8 -*-
import requests, time 
from total import *
G = '\033[32;1m'
R = '\033[31;1m'
kmavi="\033[94m"
S="\033[33m"
norm="\033[1;37;40m"+"\033[92m"
url='http://ydyosistem.gazi.edu.tr/LoginScript.php'
url_vize='http://ydyosistem.gazi.edu.tr/admin.php?Process=VizeBilgi'
url_quiz='http://ydyosistem.gazi.edu.tr/admin.php?Process=QuizBilgi'



while True:
    no=raw_input("""  
        OGRENCI NUMARANIZ: """).strip()
    if no=="g" or no=="G" or no=="q" or no=="Q":
        exit()
    try:
        no=int(no)
        no=str(no)
        assert len(no)==9, "fhata"
    except:
        print(R+"\n  [!] hatali giris\n"+G)
        continue
    break
data={"username":no,"password":no[-6:],'ogr':'1'}
with requests.Session() as ses:
    print(S+"\n siteye giris yapiliyor..")
    try:
       r = ses.post(url, allow_redirects=True, data=data)
    except:
        print(R+"\n [!] bu islem icin internet baglantisi gerekir\n"+G)
        time.sleep(6)
        exit()
    
    if not """<meta http-equiv="Refresh" content="0; URL=admin.php">""" in r.text:
        print(R+"\n  [!] boyle bir ogrenci bulunamadi\n")
        time.sleep(5)
        exit()
    print(G+" siteye giris basarili  [%15]")
    print(S+'\n quiz notlari aliniyor..')
    rrr=ses.get(url_quiz, allow_redirects=True , headers=r.headers)
    
    print(G+' quiz notlari alindi   . %60')
    icerik_quiz=rrr.text.encode('utf-8')
    print(S+'\n vize notlari aliniyor..')
    rr=ses.get(url_vize, allow_redirects=True , headers=r.headers)
    print(G+" vize notlari alindi  %100")
    
    icerik_vize=rr.text.encode('utf-8')

    


quiz_liste=saf_quiz(icerik_quiz)

#vize ixerik hesaplama

vize_liste=saf_vize(icerik_vize)

  
###  ilkd notunu hesplayak  ######
ilkdv=[]

ilkdv.append(vize_liste[0])
ilkdv.append(vize_liste[1])
ilkdv.append(vize_liste[2])

ilkdq=[]
for i in range(14):
    ilkdq.append(quiz_liste[i])

ilkdq=topla(ilkdq)

ilkdv=topla(ilkdv)
ilkd=ilkdq/14*3.0/10 + float(ilkdv/3)*7/10
######################

# vize

del vize_liste[0]
del vize_liste[0]
del vize_liste[0]
kalan_v=kalan_vize(vize_liste)

vize_t=topla(vize_liste)


# quiz

for i in range(14):
    del quiz_liste[0]

    
quiz_t=topla(quiz_liste)

    
kalan_q=kalan_quiz(quiz_liste)



if kalan_v==3 and kalan_q==14:
    ort_2=ilkd
elif kalan_v==3:
    
    ort_2=float(quiz_t)/(14-kalan_q)
elif kalan_q==14:
    ort_2=float(vize_t)/(3-kalan_v)
else: 
    ort_2=float(vize_t)/float(3-kalan_v)*7.0/10 + float(quiz_t)/float(14-kalan_q)*3.0/10

ort_net=ilkd*4.0/10 + ort_2*6.0/10



if kalan_q==0 and kalan_v==0:
    if  ort_2>=75:
        print(kmavi+"""

                 ##############################################
   		#				               #
		#"""+G+'''       HELAL OLSUN LAN FINALSIZ GECTIN!'''+kmavi+'''       #
                # '''+G+'''         QOPEK GIBI CALISTIN DIMI LAN  '''+kmavi+'''      #
		#     '''+G+'''           SENI HAYVAN HERIF   '''+kmavi+'''          #
		#                       		       #
		#   '''+G+'''            CONGRATULATIONS	'''+kmavi+'''	       #
		#	'''+G+'''                  	NOTUN: {}  '''.format(str(ort_net)[:4])+kmavi+'''  #
		#					       #
		 ##############################################

'''+G)
        raw_input("[ent]")
        exit()
    elif ort_net>=45 :
        print(kmavi+"""

                 ##############################################
   		#				               #
		#"""+G+"""    KANKA IPIN UCUNDASIN HEMEN AC KITABINI   """+kmavi+""" #
                #"""+G+"""      BASLA DERS CALISMAYA KAYBEDECEK """+kmavi+"""        #
		#   """+G+"""        1 SANIYEN YOK ARTIK.  """+kmavi+"""             #
		#                       		       #
		# """+G+"""               NOTUN: {}	 """.format(str(ort_net)[:4])+kmavi+"""            #
		#_____________________________    	       #
		√"""+G+"""finalden en az {} almalisin""".format(str(float(300-2*ort_net)/3)[:4])+kmavi+"""|                #
		 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#################

"""+G)
        raw_input("[ent]")
        exit()
    else:
        print(kmavi+"""

                 ###############################################
   		#						#
		#  """+G+"""  aptal herif bosa yasiyosun keske olsen   """+kmavi+"""  #
                #  """+G+"""    finale kaldin derdim ama sen direk   """+kmavi+"""    #
		#  """+G+"""        hazirlikta kaldin agla   """+kmavi+"""            #
		#                       			#
		#  """+G+"""              NOTUN: {}	   """.format(str(ort_net)[:4])+kmavi+"""           #
		#____________________________  			#
		√ """+G+"""finalden en az {} almalisin""".format(str(float(300-2*ort_net)/3)[:2])+kmavi+"""|			#
                √ """+G+"""tabi boyle bisi mumkunse   """+kmavi+"""|			#
		 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~|##################

"""+G)
        raw_input("[ent]")
        exit()
    
    
#Sinavlar Bitmemis İse
if ort_2>71:
    print(kmavi+"""

                 ###############################################
   		#						#
		#   """+G+"""   2.DONEME SUPER BASLAMİSSİN AFERİM      """+kmavi+"""  #
                # """+G+""" EGER BU DONEM ORTALAMANİ 75 USTUNDE TUTMAYİ  #
		#   """+G+"""        BASARİRSAN FİNALSİZ GECERSİN  """+kmavi+"""      #
		#                       			#
		#      """+G+"""          NOTUN: {}	 """.format(str(ort_net)[:4])+kmavi+"""             #
		#    			  			#
		|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
                |"""+G+""" BU DONEMKİ SİNAVLARDAN MİNİMUM {} alsan yeter""".format(str((750 - float(vize_t*7)/3 - float(quiz_t*3)/14) / (float(kalan_v*7)/3 + float(kalan_q)/14*3))[:4])+kmavi+"""
		|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

"""+G)
    raw_input("[ent]")
    exit()
    

else:
    while True:
        try:
            hdf=raw_input("""
            yil sonu genel basari
            puani hedefin kac   = """).replace(",",".").replace(" ","")
            if hdf=="":
                print("""
                
              HEDEFI OLMAYAN BIRINE 
	        HICBIR PROGRAM YARDIM EDEMEZ.
	        """)
	        time.sleep(5)
                continue
            hdf=float(hdf)
            if not 100>=hdf>=0:
                continue
        except:
            if hdf=="q" or hdf=="Q":
                quit()
            del hdf
            continue
        break
    if not 100>=float((float(hdf*10 - ilkd*4)*10/6 - quiz_t*3/14 - float(vize_t*7)/3) / (float(kalan_v*7)/3 + float(kalan_q*3)/14))>=0:
        print(kmavi+"""

                 ###########################################
   		#				            #
		#   """+G+"""  UZGUNUM ÇARLİ AMA BU NOTLARLA   """+kmavi+"""      #
                #    """+G+"""   HEDEFİNE ULASMAN İMKANSİZ   """+kmavi+"""        #
                #	      ________________  	    #
         	#             \\  """+G+"""NOTUN: {} """.format(str(ort_net)[:4])+kmavi+"""/	          #
    		###############\\____________/###############
               		        
				
"""+G)
        raw_input("[ent]")
        exit()
    else:
        print(kmavi+"""
 
                 ##############################################
   		#				               #
		#"""+G+"""    FAZLA KASMANA GEREK YOK ONUMUZDEKİ """+kmavi+"""       #
                #  """+G+"""    SİNAVLARDAN MİNİMUM {} ALSAN HEDEFİNE """.format(str((float(hdf*10 - ilkd*4)*10/6 - quiz_t*3/14 - float(vize_t*7)/3) / (float(kalan_v*7)/3 + float(kalan_q*3)/14))[:4])+kmavi+"""#
		#    """+G+"""         RAHAT ULASABİLİRSİN    """+kmavi+"""          #
		#                       		       #
		#   """+G+"""             NOTUN: {}	  """.format(float(str(ort_net)[:4]))+kmavi+"""             #
		#_____________________________________________ #
		 ##############################################
		 

		 
""")
        raw_input(G+"[ent]")
        exit()
exit()
