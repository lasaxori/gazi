# -*- coding: utf-8 -*-
import os, time
vizeuyari="\033[93m"+"\n SIMDI VIZE NOTLARINIZI YAZINIZ\n"+"\nIPUCU= VIZE NOTUNUZU  "+"\033[101m"+"14+13+19+10.5"+"\033[0m"+"\033[1;37;40m"+"\033[33m"+"  seklinde de yazbilirsiniz\n"+"\033[32m"
tasak="Tassak mi geciosun aq ya bu nedir ya:{}\n"
vizetoplam="0123456789.q+"
hedef="""
         1.donem sonu puan
         hedefin kac     = """
nott_l={}
donem=1
vize_liste=[]
quiz_liste=[]
geri=0
key=0
keyy=0
v_3=True
q_14=True
kmavi="\033[94m"
G = '\033[32;1m'
menu=kmavi+"""
  ||===============================||
  ||"""+G+"""  for turn menu >> "q" or "Q"  """+kmavi+"""||
  ||"""+G+"""  for turn back >> "g" or "G" """+kmavi+""" ||
  ||===============================||
    """+G
donem1m="""
            Ilk olarak 1.Donem NOTLARINDAN BASLAYALIM
            
            """
donem2m="""
            SIMDI 2. DONEM NOTLARINIZI GIRINIZ
            
            """
for ana in str(menu+donem1m).split("\n"):
    print(ana)
    time.sleep(0.07)
for sira in range(1,50):
    sira-=geri
    if sira==15:
        quiz_liste=nott_l.values()
        keyy=1
        key=1
        sira=1
        geri+=14
        kalan_q=14-len(nott_l)
        nott_l.clear()
    if keyy==1 and sira==4:
        kalan_v=3-len(nott_l)
        print(kalan_v)
        vize_liste=nott_l.values()
        break
    while True:
        if key==1:
            print(vizeuyari)
            key+=1
        if keyy==1:
            nott=raw_input("{}. VİZE NOTU: ".format(sira)).replace(",",".").replace(" ","")
        if keyy==0:
            nott=raw_input("{}. QUIZ NOTU: ".format(sira)).replace(",",".").replace(" ","")
        if nott.split()==["g"] or nott.split()==["G"]:
            if sira==1:
                geri+=1
                break
            print(kmavi+"\n islem geri alindi!\n"+G)
            geri+=2
            try:
                nott_l.pop(str(sira-1))
            except:
                pass
            break
        if nott.split()==["q"] or nott.split()==["Q"]:
            quit()
        if bool(nott)==False:
            if sira==14 and keyy==0:
                q_14=False
            if sira==3 and keyy==1:
                v_3=False
            break
        if bool(nott)==True:
            try:
                if 0<=eval(nott)<=100:
                    
                    nott=str(eval(nott))
                if not 0<=eval(nott)<=100:
                    print("\n hatali giris\n tekrar deneyin\n")
                    continue
                nott_l[str(sira)]=float(eval(nott)) 
            except:
                print("\n hatali giris\n tekrar deneyin\n")
                continue
            break
        break
    
 
vize_t=0
for i in vize_liste:
    vize_t+=float(i)
quiz_t=0
for i in quiz_liste:
    quiz_t+=float(i)

if len(vize_liste)==0 and len(quiz_liste)==0:
    os.system("clear")
    sikayet="""
    
    
    
          BU SAYFAYI SENIN ICIN ACTIM
          
          NEDEN DIYE MI SORUYORSUN
          
          KENDINE SOR BI
          
          
          ULAN APTAL HIC BI NOT GIRMEMISSIN
          
          NASIL HESAPLAMAMI BEKLIYORSUN
          """
    for i in sikayet.split("\n"):
        print i
        time.sleep(0.04)
    time.sleep(5)
    quit()
elif len(vize_liste)==0:
    ort_1=float(quiz_t)/len(quiz_liste)
elif len(quiz_liste)==0:
    ort_1=float(vize_t)/len(vize_liste)
else: 
    ort_1=float(float(vize_t)/len(vize_liste)*7)/10 + float(float(quiz_t)/len(quiz_liste)*3)/10
    
del kalan_q
del kalan_v
vize_liste=[]
quiz_liste=[]
geri=0
key=0
keyy=0
for ana in str(menu+donem2m).split("\n"):
    print(ana)
    time.sleep(0.07)
for sira in range(1,50):
    sira-=geri
    if sira==15:
        quiz_liste=nott_l.values()
        keyy=1
        key=1
        sira=1
        geri+=14
        kalan_q=14-len(nott_l)
        print(kalan_q)
        nott_l.clear()
    if keyy==1 and sira==4:
        kalan_v=3-len(nott_l)
        print(kalan_v)
        vize_liste=nott_l.values()
        break
    while True:
        if key==1:
            print(vizeuyari)
            key+=1
        if keyy==1:
            nott=raw_input("{}. VİZE NOTU: ".format(sira)).replace(",",".").replace(" ","")
        if keyy==0:
            nott=raw_input("{}. QUIZ NOTU: ".format(sira)).replace(",",".").replace(" ","")
        if nott.split()==["g"] or nott.split()==["G"]:
            if sira==1:
                geri+=1
                break
            print(kmavi+"\n islem geri alindi!\n"+G)
            geri+=2
            try:
                nott_l.pop(str(sira-1))
            except:
                pass
            break
        if nott.split()==["q"] or nott.split()==["Q"]:
            quit()
        if bool(nott)==False:
            if sira==14 and keyy==0:
                q_14=False
            if sira==3 and keyy==1:
                v_3=False
            break
        if bool(nott)==True:
            try:
                if 0<=eval(nott)<=100:
                    
                    nott=str(eval(nott))
                if not 0<=eval(nott)<=100:
                    print("\n hatali giris\n tekrar deneyin\n")
                    continue
                nott_l[str(sira)]=float(eval(nott)) 
            except:
                print("\n hatali giris\n tekrar deneyin\n")
                continue
            break
        break
vize_t=0
for i in vize_liste:
    vize_t+=float(i)
quiz_t=0
for i in quiz_liste:
    quiz_t+=float(i)

if len(vize_liste)==0 and len(quiz_liste)==0:
    os.system("clear")
    sikayet="""
    
    
    
          BU SAYFAYI SENIN ICIN ACTIM
          
          NEDEN DIYE MI SORUYORSUN
          
          KENDINE SOR BI
          
          
          ULAN APTAL MADEM 1 DONEMIN NOTLARINI HESAPLICAN
          
          NIYE 1. SECENEGI SECMIOSUN O ZAMAN
         
          """
    for i in sikayet.split("\n"):
        print i
        time.sleep(0.04)
    time.sleep(5)
    quit()
elif len(vize_liste)==0:
    ort_2=quiz_t/len(quiz_liste)
    ort_net=ort_1*4/10 + ort_2*6/10
elif len(quiz_liste)==0:
    ort_2=vize_t/len(vize_liste)
    ort_net=ort_1*4/10 + ort_2*6/10
else: 
    ort_2=(vize_t/len(vize_liste))*7/10 + (quiz_t/len(quiz_liste))*3/10
    ort_net=ort_1*4/10 + ort_2*6/10    
    
if bool(q_14) and bool(v_3):
    if  ort_2>=75:
        print("""

                 ##############################################
   		#				               #
		#       HELAL OLSUN LAN FINALSIZ GECTIN!       #
                #          QOPEK GIBI CALISTIN DIMI LAN        #
		#                SENI HAYVAN HERIF             #
		#                       		       #
		#               CONGRATULATIONS		       #
		#	                  	NOTUN: {}    #
		#					       #
		 ##############################################

""".format(str(ort_net)[:4]))
        raw_input("[ent]")
        exit()
    elif ort_net>=45 :
        print("""

                 ##############################################
   		#				               #
		#    KANKA IPIN UCUNDASIN HEMEN AC KITABINI    #
                #      BASLA DERS CALISMAYA KAYBEDECEK         #
		#           1 SANIYEN YOK ARTIK.               #
		#                       		       #
		#                NOTUN: {}	             #
		#_____________________________    	       #
		√finalden en az {} almalisin|                #
		 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#################

""".format(str(ort_net)[:4],str((300-2*ort_net)/3)[:4]))
        raw_input("[ent]")
        exit()
    else:
        print("""

                 ###############################################
   		#						#
		#    aptal herif bosa yasiyosun keske olsen     #
                #      finale kaldin derdim ama sen direk       #
		#          hazirlikta kaldin agla               #
		#                       			#
		#                NOTUN: {}	              #
		#____________________________  			#
		√ finalden en az {} almalisin|			#
                √ tabi boyle bisi mumkunse   |			#
		 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~|##################

""".format(str(ort_net)[:4],str((300-2*ort_net)/3)[:2]))
        raw_input("[ent]")
        exit()
    
    
#Sinavlar Bitmemis İse
if 71<ort_2:
    print("""

                 ###############################################
   		#						#
		#      2.DONEME SUPER BASLAMİSSİN AFERİM        #
                #  EGER BU DONEM ORTALAMANİ 75 USTUNDE TUTMAYİ  #
		#           BASARİRSAN FİNALSİZ GECERSİN        #
		#                       			#
		#                NOTUN: {}	              #
		#    			  			#
		|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
                | BU DONEMKİ SİNAVLARDAN MİNİMUM {} alman lazim |
		|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

""".format(str(ort_net)[:4],str((750 - float(vize_t*7)/3 - float(quiz_t*3)/14) / (float(kalan_v*7)/3 + float(kalan_q)/14*3))[:4]))
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
    if not 100>=float((float(hdf*10 - ort_1*4)*10/6 - quiz_t*3/14 - float(vize_t*7)/3) / (float(kalan_v*7)/3 + float(kalan_q*3)/14))>=0:
        print(kmavi+"""

                 ###########################################
   		#				            #
		# """+G+"""    UZGUNUM ÇARLİ AMA BU NOTLARLA   """+kmavi+"""      #
                #   """+G+"""    HEDEFİNE ULASMAN İMKANSİZ """+kmavi+"""          #
                #	      ________________  	    #
         	#             \\"""+G+"""  NOTUN: {} """.format(str(ort_net)[:4])+kmavi+"""/	          #
    		###############\\____________/###############
               		        
				
"""+G)
        raw_input("[ent]")
        exit()
    else:
        print(kmavi+"""
 
                 ##############################################
   		#				               #
		# """+G+"""   FAZLA KASMANA GEREK YOK ONUMUZDEKİ   """+kmavi+"""     #
                #  """+G+"""    SİNAVLARDAN MİNİMUM {} ALSAN HEDEFİNE """.format(str((float(hdf*10 - ort_1*4)*10/6 - quiz_t*3/14 - float(vize_t*7)/3) / (float(kalan_v*7)/3 + float(kalan_q*3)/14))[:4])+kmavi+"""#
		#       """+G+"""      RAHAT ULASABİLİRSİN   """+kmavi+"""           #
		#                       		       #
		#    """+G+"""            NOTUN: {}	  """.format(float(str(ort_net)[:4]))+kmavi+"""             #
		#_____________________________________________ #
		 ##############################################
		 

		 
"""+G)
        raw_input("[ent]")
        exit()
exit()

