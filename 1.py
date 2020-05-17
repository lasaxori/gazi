# -*- coding: utf-8 -*-
import os, time
vizeuyari="\033[93m"+"\n SIMDI VIZE NOTLARINIZI YAZINIZ\n"+"\nIPUCU= VIZE NOTUNUZU  "+"\033[101m"+"14+13+19+10.5"+"\033[0m"+"\033[1;37;40m"+"\033[33m"+"  seklinde de yazbilirsiniz\n"+"\033[32m"
tasak="Tassak mi geciosun aq ya bu nedir ya:{}\n"
vizetoplam="0123456789.q+"
hedef="""
         1.donem sonu puan
         hedefin kac     = """

nott_l={}
W = "\033[0m"
vize_liste=[]
quiz_liste=[]
geri=0
key=0
keyy=0
cikis=0
duzen=0
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
for ana in menu.split("\n"):
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
                    nott_l[str(sira)]=float(eval(nott)) 
                    nott=str(eval(nott))
                if not 0<=eval(nott)<=100:
                    print("\n hatali giris\n tekrar deneyin\n")
                    continue
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
    print("""\n aq cocu oyun mu oynuosun
BI NOT GIRMEMISSIN
NE SIKIME CALISTIRIYORSUN BENI
    """)
    raw_input("[ent]")
    exit()
if len(quiz_liste)==0 and len(vize_liste)!=0:
    ort=float(vize_t)/len(vize_liste)
if len(quiz_liste)!=0 and len(vize_liste)!=0:
    ort=float(float(vize_t*7)/len(vize_liste) + float(quiz_t*3))/(len(quiz_liste)*10)

if len(quiz_liste)!=0 and len(vize_liste)==0:
    ort=float(quiz_t)/len(quiz_liste)
    if ort<45:
        print(kmavi+"""
     

            ###############################################
           #                                               #
           #"""+G+"""      HIC VIZE GIRMEMISSIN O YUZDEN GOTUN  """+kmavi+"""    #
           #  """+G+"""     KALKMASIN NOTUN HER AN DUSEBILIR!       """+kmavi+"""#
           #"""+G+"""         derdim ama daha fazla dusemezki"""+kmavi+"""       #
           #                                               #
           #          """+G+'MUTIS  NOTUN: {}                   '.format(str(ort)[:4])+kmavi+"""#
           #                                               #
           #                                               #
            ###############################################


 
""")
        raw_input(+G+"[ent]")
        exit()
    else:
        print(kmavi+"""


            ###############################################
           #                                               #
           #"""+G+"""      HIC VIZE GIRMEMISSIN O YUZDEN GOTUN"""+kmavi+"""      #
           #"""+G+"""       KALKMASIN NOTUN HER AN DUSEBILIR!"""+kmavi+"""       #
           #"""+G+"""                  BE CAREFUL! """+kmavi+"""                 #
           #                                               #
           #      """+G+"""            NOTUN: {}         """.format(str(ort)[:4])
+kmavi+"""         #
           #                                               #
           #                                               #
            ###############################################


 
""")
        raw_input("[ent]")
        exit()
if v_3==False or q_14==False:
    while True:
        try:
            hdf=raw_input("""
            1. donem sonu basari
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
    if kalan_q==0 and kalan_v!=0:
        x = float(hdf*30 - float(quiz_t*9)/14 - vize_t*7)/(kalan_v*7)
    if kalan_v==0 and kalan_q!=0:
        x = float(float(hdf*140)/3 - float(vize_t*7*14)/9 - quiz_t)/(kalan_q)
    if kalan_q!=0 and kalan_v!=0:
        x=str(float(hdf*10 - float(quiz_t*3)/14 - float(vize_t*7)/3) /( float(kalan_q*3)/14 + float(kalan_v*7)/3 ))
       
    if not 0<=float(x)<=100:
        print(kmavi+"""

                 ###########################################
   		#				            #
		# """+G+"""    UZGUNUM ÇARLİ AMA BU NOTLARLA      """+kmavi+"""   #
                #   """+G+"""    HEDEFİNE ULASMAN İMKANSİZ    """+kmavi+"""       #
                #	      ________________  	    #
         	#             \\ """+G+""" NOTUN: {} """.format(str(ort)[:4])+kmavi+"""/	            #
    		###############\\____________/###############
               		        
				
""")
        raw_input(G+"[ent]")
        exit()
    print(kmavi+"""
 
                 ##############################################
   		#				               #
		# """+G+"""   FAZLA KASMANA GEREK YOK ONUMUZDEKİ  """+kmavi+"""      #
                #   """+G+"""   SİNAVLARDAN MİNİMUM {} ALSAN HEDEFİNE""".format(str(x)[:4])+kmavi+""" #
		# """+G+"""            RAHAT ULASABİLİRSİN  """+kmavi+"""            #
		#                       		       #
		#  """+G+"""              NOTUN: {}	""".format(str(ort)[:4])+kmavi+"""               #
		#_____________________________________________ #
		 ##############################################
		 

		 
""")
    raw_input(G+"[ent]")
    exit()
if  ort<45:
    print(kmavi+"""
     

              ##################-----------################## 
             #						     #
             # """+G+"""            NIYE YASIOSUN LA SEN       """+kmavi+"""       # 
             #   """+G+"""     BOS, SENIN YANINDA DOLU KALIR      """+kmavi+"""    #
             #    """+G+"""      OLSENE ARTIK NE BEKLIOSUN         """+kmavi+"""   #
             # """+G+"""    AMA SAKIN REKOR NOTUNU OGRENMEDEN OLME  """+kmavi+"""  #
             #                                               #
             #   """+G+"""          MUTIS  NOTUN: {}""".format(str(ort)[:4])+kmavi+"""		   #
             #						     #
             #						     # 
	     #________________________________		     #
              -----------------------------------------------

                                                          
 
"""+G)
    raw_input("[ent]")
    exit()
if 45<=ort<70:
    print(kmavi+"""
     

           ##################-----------################## 
          #		     			      	 #
          #                                              #
          # """+G+"""            MUTIS  NOTUN: {}	"""+kmavi+"""         #    
          #   	  				         #
	   #_____________________________________________#
   

                                    

""".format(str(ort)[:4]))
    raw_input(G+"[ent]")
    exit()
if ort>=70:
    print(+kmavi+"""


               ###########################################
              #                                           #
              # """+G+"""     LAN QOPEK, NE BICIM CALISTIN """+kmavi+"""        #
              #              			          #
              #"""+G+"""             ORTALAMAN: {}    """.format(str(ort)[:4])+kmavi+"""           #
              #                                           #
              #  """+G+"""          CONGRATULATIONS   """+kmavi+"""             #
              #                                           #
              #                                           #
               ###########################################


 
"""+G)
    raw_input("[ent]")
    exit()
exit()