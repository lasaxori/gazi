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
                      ||       VERSION= 0.3        ||
               ||========================================||  
               ||                                        ||
               || YALNIZCA BIR DONEM ORTALAMASI ICIN "1" ||
               ||   HER IKI DONEM ORTALAMASI ICIN    "2" ||
               ||        GAZININ YILDIZLARI ICIN     "3" ||
               ||  GAZI HOCALARI HAKKINDA BILGI ICIN "4" ||
               ||            CIKMAK ICIN ISE         "q" ||
               ||=========================================="""
            

menu2="""                               ............
                              || !DIKKAT! ||
   #••••••••••••••••••••••••••••          ••••••••••••••••••••••••••#
   #   EGER NOTUNUZ GIRILMEMIS ISE BOS BIRAKINIZ, 0 ise 0 yaziniz!  #
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



tasak="Tassak mi geciosun aq ya bu nedir ya:{}\n"









while True:
    print("\033[1;37;40m")
    print("\033[32m")
    print(menu)
    print("\033[91m")
    print(menu2)
    print("\033[32m")
    oc=1
    oc2=1

    
    
    islem=input("islem no:")
    if islem=="3":
        print("bu bolum daha yapim asamasind\n")
        continue
    
    
    
    
    
    
    
    
    if islem=="4":
        if islem=="4":
            h=open("hocalar.txt","r")
            b=open("hoca_b.txt","r")
            print("""
            
        HAKKINDA BILGI SAHIBI OLMAK ISTEDIGINIZ
          HOCAYI SECINIZ
          
        menuye donmek icin="q"
          
          """)
            for sira, i in enumerate(h,1):
                print("("+str(sira).zfill(2)+") "+i, end="")
            print("""
            
        HAKKINDA BILGI SAHIBI OLMAK ISTEDIGINIZ
          HOCAYI SECINIZ
          
        menuye donmek icin= "q"
          """)
            while True:
                ist=input("\n\n NUMARAYI GIRINIZ: ")
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
        print("\n Cikiliyor..\n")
        quit()
    if not (islem=="1" or islem=="2" or islem=="3" or islem==4):
        continue
    elif islem=="1":
        quiz_l=[]
        vize_l=[]
        while True:
            q_1=input("1. QUIZ NOTU:")
            if "," in q_1:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_1)==False:
                break
            elif q_1.split()==["q"]:
                print("\n CIKILIYOR..\n")
                quit()
            elif bool(q_1)==True:
                try:
                    float(q_1)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(q_1)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(q_1))
                continue
            quiz_l+=[q_1]
            break
        while True:
            q_2=input("2. QUIZ NOTU:")
            if "," in q_2:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_2)==False:
                break
            elif q_2.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_2]
            break
        while True:
            q_3=input("3. QUIZ NOTU:")
            if "," in q_2:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_3)==False:
                break
            elif q_3.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_3]
            break
        while True:
            q_4=input("4. QUIZ NOTU:")
            if "," in q_4:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_4)==False:
                break
            elif q_4.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_4]
            break
        while True:
            q_5=input("5. QUIZ NOTU:")
            if "," in q_5:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_5)==False:
                break
            elif q_5.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_5]
            break
        while True:
            q_6=input("6. QUIZ NOTU:")
            if "," in q_1:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_6)==False:
                break
            elif q_6.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_6]
            break
        while True:
            q_7=input("7. QUIZ NOTU:")
            if "," in q_7:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_7)==False:
                break
            elif q_7.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_7]
            break
        while True:
            q_8=input("8. QUIZ NOTU:")
            if "," in q_8:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_8)==False:
                break
            elif q_8.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_8]
            break
        while True:
            q_9=input("9. QUIZ NOTU:")
            if "," in q_9:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_9)==False:
                break
            elif q_9.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_9]
            break
        while True:
            q_10=input("10. QUIZ NOTU:")
            if "," in q_10:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_10)==False:
                break
            elif q_10.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_10]
            break
        while True:
            q_11=input("11. QUIZ NOTU:")
            if "," in q_11:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_11)==False:
                break
            elif q_11.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_11]
            break
        while True:
            q_12=input("12. QUIZ NOTU:")
            if "," in q_12:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_12)==False:
                break
            elif q_12.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_12]
            break
        while True:
            q_13=input("13. QUIZ NOTU:")
            if "," in q_13:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_13)==False:
                break
            elif q_13.split()==["q"]:
               print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_13]
            break
        while True:
            q_14=input("14. QUIZ NOTU:")
            if "," in q_14:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_14)==False:
                break
            elif q_14.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_14]
            break
    
        print("\n\nSIMDI VIZE NOTLARINIZO YAZINIZ\n")

        while True:
            v_1=input("1. VIZE NOTU:")
            if "," in v_1:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(v_1)==False:
                break
            elif v_1=="q":
                print("\n CIKILIYOR..\n")
                quit()
            elif bool(v_1)==True:
                try:
                   float(v_1)
                except:
                   print("moruq yalnizca sayi yaz\n")
                   continue
            if not 100>=float(v_1)>=0:
                print(tasak.format(v_1))
                continue
            vize_l+=[v_1]
            anahtar=1
            break
        while True:
            v_2=input("2. VIZE NOTU:")
            if "," in v_2:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(v_2)==False:
                break
            elif v_2.split()==["q"]:
                print("\n CIKILIYOR..\n")
                quit()
            elif bool(v_2)==True:
                try:
                    float(v_2)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(v_2)>=0:
                print(tasak.format(v_2))
                continue
            vize_l+=[v_2]
            break
        while True:
            v_3=input("3. VIZE NOTU:")
            if "," in v_3:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(v_3)==False:
                break
            elif v_3=="q":
                print("\n CIKILIYOR..\n")
                quit()
            elif bool(v_3)==True:
                try:
                    float(v_3)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(v_3)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(v_3))
                continue
            vize_l+=[v_3]
            break
        vize_t=0
        for i in vize_l:
            vize_t+=float(i)
        quiz_t=0
        for i in quiz_l:
            quiz_t+=float(i)
        if len(vize_l)==0 and len(quiz_l)==0:
            print("""\n aq cocu oyun mu oynuosun
    HIC BI NOT GIRMEMISSIN
        NE SIKIME CALISTIRIYORSUN BENI
    
            """)
            input("[ent]")
            quit()
        if len(quiz_l)==0 and len(vize_l)!=0:
            ort=vize_t/len(vize_l)
        elif len(quiz_l)!=0 and len(vize_l)==0:
            ort=quiz_t/len(quiz_l)
            if ort<45:
                print("""
     

                 ###############################################
                #                                               #
                #      HIC VIZE GIRMEMISSIN O YUZDEN GOTUN      #
                #       KALKMASIN NOTUN HER AN DUSEBILIR!       #
                #         derdim ama daha fazla dusemezki       #
                #                                               #
                #          MUTIS  NOTUN: {}                    #
                #                                               #
                #                                               #
                 ###############################################


 
""".format(str(ort)[:4]))
                input("[ent]")
                continue
            else:
                print("""


                 ###############################################
                #                                               #
                #      HIC VIZE GIRMEMISSIN O YUZDEN GOTUN      #
                #       KALKMASIN NOTUN HER AN DUSEBILIR!       #
                #                  BE CAREFUL!                  #
                #                                               #
                #                  NOTUN: {}                   #
                #                                               #
                #                                               #
                 ###############################################


 
""".format(str(ort)[:4]))
                input("[ent]")
                continue
        else:
            ort=(vize_t/len(vize_l))*7/10 + (quiz_t/len(quiz_l))*3/10
        
        if ort<45:
            print("""
     

                 ###############################################
                #                                               #
                #             NIYE YASIOSUN LA SEN              #
                #        BOS, SENIN YANINDA DOLU KALIR          #
                #          OLSENE ARTIK NE BEKLIOSUN            #
                #     AMA SAKIN REKOR NOTUNU OGRENMEDEN OLME    #
                #                                               #
                #             MUTIS  NOTUN: {}                #
                #                                               #
                #                                               #
                 ###############################################


 
""".format(str(ort)[:4]))
            input("[ent]")
            continue
        elif 60>ort>=45:
            print(r"""
     

               /############################################\
              ||                                            ||
              ||  KANKA 2. DONEM DERSLER DAHA DA ZORLASCK   ||
              ||    UZGUNUM AMA BENCE SEN KESIN KALDIN      ||
              ||     AMA BU DUNYANIN SONU DEGIL DEMI        ||
              ||                                            ||
              ||                NOTUN: {}                 ||
             /_______________________________________________\
            /finale girebilmek icin 2.donem en az {} almalisin\
           /---------------------------------------------------\


 
""".format(str(ort)[:4],str((300-2*ort)/3)[:2]))
            input("[ent]")
            continue
        if 60<=ort<75:
            print("""
     

                 ##############################################
                ||                                            ||
                ||    EGER FINALSIZ GECMEK ISTIYORSAN         ||
                ||       DAHA COK CALISMAN GEREK.             ||
                ||             SONRA DEMEDI DEME              ||
                ||                                            ||
                ||                NOTUN: {}                   ||
                 ##############################################


 
""".format(str(ort)[:4]))
            input("[ent]")
            continue
        if ort>=75:
            print("""


                 ###########################################
                #                                           #
                #      LAN QOPEK, NE BICIM CALISTIN         #
                #              			            #
                #             ORTALAMAN: {}                #
                #                                           #
                #              CONGRATULATIONS              #
                #                                           #
                #                                           #
                 ###########################################


 
""".format(str(ort)[:4]))
            input("[ent]")
            continue
    a=0 
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
            q_1=input("1. QUIZ NOTU:")
            if "," in q_1:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_1)==False:
                break
            elif q_1.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_1]
            break
        while True:
            q_2=input("2. QUIZ NOTU:")
            if "," in q_2:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_2)==False:
                break
            elif q_2.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_2]
            break
        while True:
            q_3=input("3. QUIZ NOTU:")
            if "," in q_3:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_3)==False:
                break
            elif q_3.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_3]
            break
        while True:
            q_4=input("4. QUIZ NOTU:")
            if "," in q_4:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_4)==False:
                break
            elif q_4.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_4]
            break
        while True:
            q_5=input("5. QUIZ NOTU:")
            if "," in q_5:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_5)==False:
                break
            elif q_5.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_5]
            break
        while True:
            q_6=input("6. QUIZ NOTU:")
            if "," in q_6:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_6)==False:
                break
            elif q_6.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_6]
            break
        while True:
            q_7=input("7. QUIZ NOTU:")
            if "," in q_7:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_7)==False:
                break
            elif q_7.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_7]
            break
        while True:
            q_8=input("8. QUIZ NOTU:")
            if "," in q_8:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_8)==False:
                break
            elif q_8.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_8]
            break
        while True:
            q_9=input("9. QUIZ NOTU:")
            if "," in q_9:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_9)==False:
                break
            elif q_9.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_9]
            break
        while True:
            q_10=input("10. QUIZ NOTU:")
            if "," in q_10:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_10)==False:
                break
            elif q_10.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_10]
            break
        while True:
            q_11=input("11. QUIZ NOTU:")
            if "," in q_11:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_11)==False:
                break
            elif q_11.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_11]
            break
        while True:
            q_12=input("12. QUIZ NOTU:")
            if "," in q_12:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_12)==False:
                break
            elif q_12.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_12]
            break
        while True:
            q_13=input("13. QUIZ NOTU:")
            if "," in q_13:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_13)==False:
                break
            elif q_13.split()==["q"]:
               print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_13]
            break
        while True:
            q_14=input("14. QUIZ NOTU:")
            if "," in q_14:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(q_14)==False:
                break
            elif q_14.split()==["q"]:
                print("\n CIKILIYOR..\n")
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
            quiz_l+=[q_14]
            break
    
        print("\n\nSIMDI VIZE NOTLARINIZO YAZINIZ\n")

        while True:
            v_1=input("1. VIZE NOTU:")
            if "," in v_1:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(v_1)==False:
                break
            elif v_1=="q":
                print("\n CIKILIYOR..\n")
                quit()
            elif bool(v_1)==True:
                try:
                   float(v_1)
                except:
                   print("moruq yalnizca sayi yaz\n")
                   continue
            if not 100>=float(v_1)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(v_1))
                continue
            vize_l+=[v_1]
            break
        while True:
            v_2=input("2. VIZE NOTU:")
            if "," in v_2:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(v_2)==False:
                break
            elif v_2.split()==["q"]:
                print("\n CIKILIYOR..\n")
                quit()
            elif bool(v_2)==True:
                try:
                    float(v_2)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(v_2)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(v_2))
                continue
            vize_l+=[v_2]
            break
        
        while True:
            v_3=input("3. VIZE NOTU:")
            if "," in v_3:
                print("\033[91m")
                print("""
                VIRGUL YERINE NOKTA KULLANINIZ
                """)
                print("\033[32m")
                continue
            if bool(v_3)==False:
                break
            elif v_3.split()==["q"]:
                print("\n CIKILIYOR..\n")
                quit()
            elif bool(v_3)==True:
                try:
                    float(v_3)
                except:
                    print("moruq yalnizca sayi yaz\n")
                    continue
            if not 100>=float(v_3)>=0:
                print("Tassak mi geciosun aq ya bu nedir ya:{}\n".format(v_3))
                continue
            vize_l+=[v_3]
            break

        vize_t=0
        for i in vize_l:
            vize_t+=float(i)
        quiz_t=0
        for i in quiz_l:
            quiz_t+=float(i)
        
            
        if a==1:
            if len(vize_l)==0 and len(quiz_l)==0:
                print("\n aq madem hic not girmicen 1. Secenegi secseydin\n")
                input("[ent]")
                quit()
            elif len(vize_l)==0:
                ort_2=quiz_t/len(quiz_l)
    
            elif len(quiz_l)==0:
                ort_2=vize_t/len(vize_l)
            else: 
                ort_2=(vize_t/len(vize_l))*7/10 + (quiz_t/len(quiz_l))*3/10
            islem=0
            break
        if a==0:
            if len(vize_l)==0 and len(quiz_l)==0:
                print("\n aq madem hic not girmicen 1. Secenegi secseydin\n")
                input("[ent]")
                quit()
            elif len(vize_l)==0:
                ort_1=quiz_t/len(quiz_l)
    
            elif len(quiz_l)==0:
                ort_1=vize_t/len(vize_l)
            else: 
                ort_1=(vize_t/len(vize_l))*7/10 + (quiz_t/len(quiz_l))*3/10
            a=1
            
    ort_net=ort_1*4/10 + ort_2*6/10

    if ort_net>=75:
        print("""

                 ##############################################
   		#				               #
		#       HELAL OLSUN LAN FINALSIZ GECTIN!       #
                #          QOPEK GIBI CALISTIN DIMI LAN        #
		#                SENI HAYVAN HERIF             #
		#                       		       #
		#               CONGRATULATIONS		       #
		#	                  	NOTUN: {}     #
		#					       #
		 ##############################################

""".format(ort_net))
        input("[ent]")
        continue
    elif ort_net>=50:
        print("""

                 ##############################################
   		#				               #
		#    KANKA IPIN UCUNDASIN HEMEN AC KITABINI    #
                #      BASLA DERS CALISMAYA KAYBEDECEK         #
		#           1 SANIYEN YOK ARTIK.               #
		#                       		       #
		#                NOTUN: {}	              #
		#___________________________    	       #
		√finalden en az {} almalisin|    	      #
		 ~~~~~~~~~~~~~~~~~~~~~~~~~~~###################

""".format(str(ort_net)[:4],str((300-2*ort_net)/3)[:4]))
        input("[ent]")
        continue
    else:
        print("""

                 ###############################################
   		#						#
		#    aptal herif bosa yasiyosun keske olsen     #
                #      finale kaldin derdim ama sen direk       #
		#          hazirlikta kaldin agla               #
		#                       			#
		#                NOTUN: {}	               #
		#___________________________  			#
		√finalden en az {} almalisin|	               #
		 ~~~~~~~~~~~~~~~~~~~~~~~~~~~####################

""".format(str(ort_net)[:4],str((300-2*ort_net)/3)[:4]))
        input("[ent]")
        continue
