# -*- coding: utf-8 -*-
import os
menu="""              
             ############          ##       ############      ###
           ##                    #   #                 #      ###
          #                     #     #               #         
         #                     #       #             #         # 
         #     ##########     #         #          #           #
         #  	      	 #    ############      #####          #
          #		##   #           #       #	       #
           #	        #   #            #     # 	       #
             #       ##   #              #   #		       #
    	      #######    #               #  #############      #
       
     ____________________________________________________________________
    /                                                                   /
   /   GAZI HAZIRLIK DONEM SONU NOT HESAPLAMA PRORAMINA HOSGELDINIZ    /
  /___________________________________________________________________/
                      ||                           ||
                      ||       VERSION= 0.31       ||
               ||========================================||  
               ||                                        ||
               || YALNIZCA BIR DONEM ORTALAMASI ICIN "1" ||
               ||   HER IKI DONEM ORTALAMASI ICIN    "2" ||
               ||   2. DONEM HIZLI HESAPLAMA ICIN    "3" ||
               ||  GAZI HOCALARI HAKKINDA BILGI ICIN "4" ||
               ||            CIKMAK ICIN ISE         "q" ||
               ||========================================||"""
            

menu2="""\033[91m""" +"""                               ............
                              || """+"""\033[101m""" +"""\033[93m"""+"""!DIKKAT!"""+    """\033[1;37;40m"""+     """\033[91m""" +""" ||
   #••••••••••••••••••••••••••••          ••••••••••••••••••••••••••#
   #   """+"""\033[33m"""+"""EGER NOTUNUZ GIRILMEMIS ISE BOS BIRAKINIZ, 0 ise 0 yaziniz!"""+"""\033[91m"""+"""  #
   #########---------------------------------------------############

"""

sablon="""

ADI   =   {}
SOYADI =  {}
ANNE ADI =  {}
BABA ADI =  {}
DOGUM TARIHI= {}
ADRESI =   {}
DOGUM YERI=   {}
TC KIMLIK NO= {}
Tel No=  {}
"""

sablon_k="""

ADI   =   {}
SOYADI =  {}
KIZLIK SOYADI= {}
ANNE ADI = {}
BABA ADI = {}
DOGUM TARIHI= {}
ADRESI =  {}
DOGUM YERI=   {}
TC KIMLIK NO= {}
Tel No=  {}
"""
vizeuyari="\033[93m"+"\n SIMDI VIZE NOTLARINIZI YAZINIZ\n"+"\nIPUCU= VIZE NOTUNUZU  "+"\033[101m"+"14+13+19+10.5"+"\033[0m"+"\033[1;37;40m"+"\033[33m"+"  seklinde de yazbilirsiniz\n"+"\033[32m"
tasak="Tassak mi geciosun aq ya bu nedir ya:{}\n"
vizetoplam="0123456789.q+"
a=0
while True:
    print("\033[1;37;40m")
    print("\033[32m")
    print(menu)
    print("\033[91m")
    print(menu2)
    print("\033[32m")
    oc=1
    oc2=1

    
    
    islem=raw_input("islem no:")
    if islem=="3":
        os.system("python2 3.py")
        continue
    if islem=="4":
        if islem=="4":
            import time
            
            h=open("hocalar.txt","r")
            b=open("hoca_b.txt","r")
            print("")
            for sira, i in enumerate(h,1):
                time.sleep(0.05)
                print("("+str(sira).zfill(2)+") "+i.replace("\n","") )
            print("""
            
        HAKKINDA BILGI SAHIBI OLMAK ISTEDIGINIZ
          HOCAYI SECINIZ
          
        menuye donmek icin= "q"
          """)
            while True:
                ist=raw_input("\n\n NUMARAYI GIRINIZ: ")
                if ist=="q":
                    oc=0
                    break
                try:
                    int(ist)
                except:
                    print("\n liste sira numarasini gir")
                    continue
                if not 0<int(ist)<55:
                    print("\n liste sira numarasini gir")
                    continue
                for sira , i in enumerate(b,1):
                    if sira==int(ist):
                        i=i.split("|")
                        if i[0]=="E":
                            print(sablon.format(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]))
                
                    
                        if i[0]=="K":
                            print(sablon_k.format(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))
                            
                
                h=open("hocalar.txt","r")
                b=open("hoca_b.txt","r")
                continue
            if oc==0:
                print("\nmenuye donuluyor..\n")
                oc=1
                continue
            
    if islem=="q":
        quit()
        quit()
        exit()
    if not (islem=="1" or islem=="2" or islem=="3" or islem==4):
        continue
    elif islem=="1":
        os.system("python2 1.py")
 
 
 
       
    while islem=="2":
        if a==0:
            print("""
            Ilk olarak 1.Donem NOTLARINDAN BASLAYALIM
            
            """)
        if a==1:
            print("""
            SIMDI 2. DONEM NOTLARINIZI GIRINIZ
            
            """)
        while True:
            quiz_l=[]
            vize_l=[]
            q_1=raw_input("1. QUIZ NOTU:").replace(",",".")
            if bool(q_1)==False:
                kalan_q=14
                break
            elif q_1.split()==["q"]:
                
                quit()
            elif bool(q_1)==True:
                try:
                    float(q_1)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_1)>=0:
                print(tasak.format(q_1))
                continue
            kalan_q=14-1
            quiz_l+=[q_1]
            break
        while True:
            q_2=raw_input("2. QUIZ NOTU:").replace(",",".")
            if bool(q_2)==False:
                break
            elif q_2.split()==["q"]:
                
                quit()
            elif bool(q_2)==True:
                try:
                    float(q_2)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_2)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_2))
                continue
            kalan_q=14-2
            quiz_l+=[q_2]
            break
        while True:
            q_3=raw_input("3. QUIZ NOTU:").replace(",",".")
            if bool(q_3)==False:
                break
            elif q_3.split()==["q"]:
                
                quit()
            elif bool(q_3)==True:
                try:
                    float(q_3)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_3)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_3))
                continue
            kalan_q=14-3
            quiz_l+=[q_3]
            break
        while True:
            q_4=raw_input("4. QUIZ NOTU:").replace(",",".")
            if bool(q_4)==False:
                break
            elif q_4.split()==["q"]:
                
                quit()
            elif bool(q_4)==True:
                try:
                    float(q_4)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_4)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_4))
                continue
            kalan_q=14-4
            quiz_l+=[q_4]
            break
        while True:
            q_5=raw_input("5. QUIZ NOTU:").replace(",",".")
            if bool(q_5)==False:
                break
            elif q_5.split()==["q"]:
                
                quit()
            elif bool(q_5)==True:
                try:
                    float(q_5)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_5)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_5))
                continue
            kalan_q=14-5
            quiz_l+=[q_5]
            break
        while True:
            q_6=raw_input("6. QUIZ NOTU:").replace(",",".")
            if bool(q_6)==False:
                break
            elif q_6.split()==["q"]:
                
                quit()
            elif bool(q_6)==True:
                try:
                    float(q_6)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_6)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_6))
                continue
            kalan_q=14-6
            quiz_l+=[q_6]
            break
        while True:
            q_7=raw_input("7. QUIZ NOTU:").replace(",",".")
            if bool(q_7)==False:
                break
            elif q_7.split()==["q"]:
                
                quit()
            elif bool(q_7)==True:
                try:
                    float(q_7)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_7)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_7))
                continue
            kalan_q=14-7
            quiz_l+=[q_7]
            break
        while True:
            q_8=raw_input("8. QUIZ NOTU:").replace(",",".")
            if bool(q_8)==False:
                break
            elif q_8.split()==["q"]:
                
                quit()
            elif bool(q_8)==True:
                try:
                    float(q_8)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_8)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_8))
                continue
            kalan_q=14-8
            quiz_l+=[q_8]
            break
        while True:
            q_9=raw_input("9. QUIZ NOTU:").replace(",",".")
            if bool(q_9)==False:
                break
            elif q_9.split()==["q"]:
                
                quit()
            elif bool(q_9)==True:
                try:
                    float(q_9)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_9)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_9))
                continue
            kalan_q=14-9
            quiz_l+=[q_9]
            break
        while True:
            q_10=raw_input("10. QUIZ NOTU:").replace(",",".")
            if bool(q_10)==False:
                break
            elif q_10.split()==["q"]:
                
                quit()
            elif bool(q_10)==True:
                try:
                    float(q_10)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_10)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_10))
                continue
            kalan_q=14-10
            quiz_l+=[q_10]
            break
        while True:
            q_11=raw_input("11. QUIZ NOTU:").replace(",",".")
            if bool(q_11)==False:
                break
            elif q_11.split()==["q"]:
                
                quit()
            elif bool(q_1)==True:
                try:
                    float(q_11)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_11)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_11))
                continue
            kalan_q=14-11
            quiz_l+=[q_11]
            break
        while True:
            q_12=raw_input("12. QUIZ NOTU:").replace(",",".")
            if bool(q_12)==False:
                break
            elif q_12.split()==["q"]:
                
                quit()
            elif bool(q_12)==True:
                try:
                    float(q_12)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_12)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_12))
                continue
            kalan_q=14-12
            quiz_l+=[q_12]
            break
        while True:
            q_13=raw_input("13. QUIZ NOTU:").replace(",",".")
            if bool(q_13)==False:
                break
            elif q_13.split()==["q"]:
               
               quit()
            elif bool(q_13)==True:
                try:
                    float(q_13)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_13)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_13))
                continue
            kalan_q=14-13
            quiz_l+=[q_13]
            break
        while True:
            q_14=raw_input("14. QUIZ NOTU:").replace(",",".")
            if bool(q_14)==False:
                break
            elif q_14.split()==["q"]:
                
                quit()
            elif bool(q_14)==True:
                try:
                    float(q_14)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_14)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_14))
                continue
            kalan_q=14-14
            
            quiz_l+=[q_14]
            break
    
        print(vizeuyari)

        while True:
            v_1=raw_input("1. VIZE NOTU:").replace(",","")
            if v_1=="q":
                quit()
            if bool(v_1)==False:
                kalan_v=3
                break
            try:
                if 0<=float(v_1)<=100:
                    vize_l+=[v_1]
                    kalan_v=2
                    break
            except:
                pass
            try:
                if 0<=eval(v_1)<=100:
                    vize_l+=[eval(v_1)]
                    kalan_v=2
                    break
            except:
                print("\n hatali giris\n")
                continue
        while True:
            v_2=raw_input("2. VIZE NOTU:").replace(",","")
            if v_2=="q":
                
                quit()
            if bool(v_2)==False:
                break
            try:
                if 0<=float(v_2)<=100:
                    vize_l+=[v_2]
                    kalan_v=1
                    break
            except:
                pass
            try:
                if 0<=eval(v_2)<=100:
                    vize_l+=[eval(v_2)]
                    kalan_v=1
                    break
            except:
                print("\n hatali giris\n")
                continue
        while True:
            v_3=raw_input("3. VIZE NOTU:").replace(",","")
            if v_3=="q":
                
                quit()
            if bool(v_3)==False:
                break
            try:
                if 0<=float(v_3)<=100:
                    vize_l+=[v_3]
                    kalan_v=0
                    
                    break
            except:
                pass
            try:
                if 0<=eval(v_3)<=100:
                    vize_l+=[eval(v_3)]
                    kalan_v=0
                    
                    break
            except:
                print("\n hatali giris\n")
                continue
            if not 100>=float(v_3)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(v_3))
                continue
            
        vize_t=0
        for i in vize_l:
            vize_t+=float(i)
        quiz_t=0
        for i in quiz_l:
            quiz_t+=float(i)
        
            
        if a==1:
            if len(vize_l)==0 and len(quiz_l)==0:
                print("\n aq madem hic not girmicen 1. Secenegi secseydin\n")
                raw_input("[ent]")
                quit()
            elif len(vize_l)==0:
                ort_2=quiz_t/len(quiz_l)
                ort_net=ort_1*4/10 + ort_2*6/10

    
            elif len(quiz_l)==0:
                ort_2=vize_t/len(vize_l)
                ort_net=ort_1*4/10 + ort_2*6/10

            else: 
                ort_2=(vize_t/len(vize_l))*7/10 + (quiz_t/len(quiz_l))*3/10
                ort_net=ort_1*4/10 + ort_2*6/10

            islem=0
            break
        if a==0:
            if len(vize_l)==0 and len(quiz_l)==0:
                print("\n aq madem hic not girmicen 1. Secenegi secseydin\n")
                raw_input("[ent]")
                quit()
            elif len(vize_l)==0:
                ort_1=quiz_t/len(quiz_l)
    
            elif len(quiz_l)==0:
                ort_1=vize_t/len(vize_l)
            else: 
                ort_1=(vize_t/len(vize_l))*7/10 + (quiz_t/len(quiz_l))*3/10
            a=1
            


    if bool(q_14) and bool(v_3):
        if ort_2>=75 :
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
            continue
        elif ort_net>=48 and ort_2<75:
            print("""

                 ##############################################
   		#				               #
		#    KANKA IPIN UCUNDASIN HEMEN AC KITABINI    #
                #      BASLA DERS CALISMAYA KAYBEDECEK         #
		#           1 SANIYEN YOK ARTIK.               #
		#                       		       #
		#                NOTUN: {}	             #
		#___________________________    	       #
		√finalden en az {} almalisin|                #
		 ~~~~~~~~~~~~~~~~~~~~~~~~~~~###################

""".format(str(ort_net)[:4],str((300-2*ort_net)/3)[:4]))
            raw_input("[ent]")
            continue
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
            continue
    
    
#Sinavlar Bitmemis İse
    elif ort_2>75:
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
                | BU DONEMKİ SİNAVLARDAN MİNİMUM {} alsan yeter
		|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|

""".format(str(ort_net)[:4],str((750 * (len(vize_l)+kalan_v) * (len(quiz_l)+kalan_q) -vize_t*7* (len(quiz_l)+kalan_q) - quiz_t*3* (len(vize_l)+kalan_v)) /(kalan_v*7* (len(quiz_l)+kalan_q) +  kalan_q*3* (len(vize_l)+kalan_v)))[:4]))
        raw_input("[ent]")
        continue

    elif 70<ort_2:
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

""".format(str(ort_net)[:4],str((750 * (len(vize_l)+kalan_v) * (len(quiz_l)+kalan_q) -vize_t*7* (len(quiz_l)+kalan_q) - quiz_t*3* (len(vize_l)+kalan_v)) /(kalan_v*7* (len(quiz_l)+kalan_q) +  kalan_q*3* (len(vize_l)+kalan_v)))[:4]))
        raw_input("[ent]")
        continue
    else:
        while True:
            try:
                hdf=raw_input("""
            yil sonu genel basari
            puani hedefin kac   = """).replace(",",".").replace(" ","").replace(" ","")
                if hdf=="q":
                    exit()
                if hdf=="":
                    continue
                hdf=float(hdf)
                if not 100>=hdf>=0:
                    continue
            except:
                continue
            break
        if not 100>=((len(vize_l)+kalan_v)*(len(quiz_l)+kalan_q)*10*((hdf*10-4*ort_1)/6) - 7*(len(quiz_l)+kalan_q)*vize_t - (len(vize_l)+kalan_v)*3*quiz_t)/(7*(len(quiz_l)+kalan_q)*kalan_v + (len(vize_l)+kalan_v)*3*kalan_q)>=0:
            print(r"""

                 ###########################################
   		#				            #
		#     UZGUNUM ÇARLİ AMA BU NOTLARLA         #
                #       HEDEFİNE ULASMAN İMKANSİZ           #
                #	      ________________  	    #
         	#             \  NOTUN: {} /	          #
    		###############\____________/###############
               		        
				
""".format(str(ort_net)[:4]))
            raw_input("[ent]")
            continue
        else:
            print("""
 
                 ##############################################
   		#				               #
		#    FAZLA KASMANA GEREK YOK ONUMUZDEKİ        #
                #      SİNAVLARDAN MİNİMUM {} ALSAN HEDEFİNE #
		#             RAHAT ULASABİLİRSİN              #
		#                       		       #
		#                NOTUN: {}	             #
		#_____________________________________________ #
		 ##############################################
		 

		 
""".format(str(((len(vize_l)+kalan_v)*(len(quiz_l)+kalan_q)*10*((hdf*10-4*ort_1)/6) - 7*(len(quiz_l)+kalan_q)*vize_t - (len(vize_l)+kalan_v)*3*quiz_t)/(7*(len(quiz_l)+kalan_q)*kalan_v + (len(vize_l)+kalan_v)*3*kalan_q))[:4],str(ort_net)[:4]))
            raw_input("[ent]")
            continue
    
