# -*- coding: utf-8 -*-
import os, time
os.system("clear")
W = "\033[0m"
G = '\033[32;1m'
R = '\033[31;1m'
k="\033[91m"
kmavi="\033[94m"
y="\033[92m"
kizil="\033[101m"
norm="\033[1;37;40m"+"\033[92m"
sari="\033[43m"
s="\033[33m"
menu=['   '  ,         
'           ############          ##       ############      '+kizil+R+'...'+norm,
'         ## '+G+'                   #   #                 #      '+R+kizil+'...'+norm,
'        # '+G+'                    #     #               #       '+s+sari+'...'+norm,
'       # '+G+'                    #       #             #        '+sari+s+'...'+norm,
'       #     ########## '+G+'    #         #          #          '+sari+s+"""..."""+norm,
'       #  	       #  '+G+'  ############      #####         '+sari+s+"""..."""+norm,
'        #	       # '+G+'  #           #      #	            '+sari+s+"""..."""+norm,
'         #	      #   #             #    # 	            '+sari+s+"""..."""+norm,
'           #         #   #              #   #		    '+sari+s+"""..."""+norm,
'    	    #########   #               #  ############     '+sari+s+"""..."""+norm,
' ',    	     
kmavi+'     _____________________________________________________________',
r'   //                                                             \\',
'  ||'+G+' GAZI HAZIRLIK DONEM SONU NOT HESAPLAMA PROGRAMINA HOSGELDINIZ '+kmavi+'||',
r'   \\_____________________________________________________________//',
'                    ||                           ||          ',    
'                    ||'+G+'       VERSION= 0.32 '+kmavi+'      ||',
kmavi+'             ||========================================||  ',
'             ||                                        ||',
'             ||'+G+' YALNIZCA BIR DONEM ORTALAMASI ICIN "'+s+'1'+G+'" '+kmavi+'||',
'             ||'+G+'   HER IKI DONEM ORTALAMASI ICIN    "'+s+'2'+G+'" '+kmavi+'||',
'             ||'+G+'   HER IKI DONEM  HIZLI HESAP ICIN  "'+s+'3'+G+'" '+kmavi+'||',
'             ||'+G+'  GAZI HOCALARI HAKKINDA BILGI ICIN "'+s+'4'+G+'" '+kmavi+'||',
'             ||'+G+'            CIKMAK ICIN ISE         "'+s+'q'+G+'" '+kmavi+'||',
'             ||========================================||']

menu2=["""\033[91m""" +"""                            ............""",
"""                           || """+"""\033[101m""" +"""\033[93m"""+"""!DIKKAT!"""+    """\033[1;37;40m"""+     """\033[91m""" +""" ||""",
"""  #••••••••••••••••••••••••••          ••••••••••••••••••••••••••••#""",
"""  #   """+"""\033[33m"""+"""EGER NOTUNUZ GIRILMEMIS ISE BOS BIRAKINIZ, 0 ise 0 yaziniz!"""+"""\033[91m"""+"""  #""",
"""  #########------------------------------------------------#########"""]
sablon=["ADI","SOYADI","ANNE ADI","BABA ADI","DOGUM TARIHI","ADRESI","DOGUM YERI","TC KIMLIK NO","Tel No"]

sablon_k=["ADI","SOYADI","KIZLIK SOYADI","ANNE ADI","BABA ADI","DOGUM TARIHI","ADRESI","DOGUM YERI","TC KIMLIK NO","Tel No"]

vizeuyari="\033[93m"+"\n SIMDI VIZE NOTLARINIZI YAZINIZ\n"+"\nIPUCU= VIZE NOTUNUZU  "+"\033[101m"+"14+13+19+10.5"+"\033[0m"+"\033[1;37;40m"+"\033[33m"+"  seklinde de yazbilirsiniz\n"+"\033[92m"
tasak="Tassak mi geciosun aq ya bu nedir ya:{}\n"
vizetoplam="0123456789.q+"

table=kmavi+"""
      
  ||==================================||
  ||"""+G+"""  for turn menu  >>   "q" or "Q"  """+kmavi+"""||
  ||"""+G+"""  for return list >>  "g" or "G"  """+kmavi+"""||
  ||==================================||
    """+G



a=0
v_3=00
q_14=545
ort_2=55555
ort_net=5558


while True:
    a=0
   # os.system("clear")
    time.sleep(0.04)
    print("\033[1;37;40m"+"\033[92m")
    time.sleep(0.04)
    for ana in menu:
        print(ana)
        time.sleep(0.04)
    print("\033[91m")
    time.sleep(0.04)
    for ana in menu2:
        print(ana)
        time.sleep(0.04)
    print("\033[92m")
    time.sleep(0.04)
    oc=1
    oc2=1
    islem=raw_input("islem no: ")
    if islem=="3":
        os.system("python2 3.py")
        continue
    if islem=="31":
        os.system("python2 5.py")
        continue
    if islem=="4":
        if islem=="4":
            h=open("hocalar.txt","r")
            b=open("hoca_b.txt","r")
            print("")
            for sira, i in enumerate(h,1):
                time.sleep(0.05)
                print("\033[101m"+"("+"\033[1;37;40m"+"\033[33m"+str(sira).zfill(2)+"\033[101m" +")"+"\033[92m"+"\033[1;37;40m"+" "+"\033[92m"+i.replace("\n","") )
            h.seek(0)
            b.seek(0)
            print('')
            time.sleep(0.1)
            print('')
            time.sleep(0.1)
            print("        HAKKINDA BILGI SAHIBI OLMAK ISTEDIGINIZ")
            time.sleep(0.1)
            print("          HOCAYI SECINIZ")
            for desk in table.split("\n"):
                time.sleep(0.1)
                print(desk)
            time.sleep(0.1)
            while True:
                
                ist=raw_input("\n\n NUMARAYI GIRINIZ: ")
                print("\n")
                if ist=="l" or ist=="L":
                    for sira, i in enumerate(h,1):
                        time.sleep(0.05)
                        print("\033[101m"+"("+"\033[1;37;40m"+"\033[33m"+str(sira).zfill(2)+"\033[101m" +")"+"\033[92m"+"\033[1;37;40m"+" "+"\033[92m"+i.replace("\n","") )
                    h.seek(0)
                    b.seek(0)
                    
                if ist=="q" or ist=="Q":
                    oc=0
                    break
                try:
                    int(ist)
                except:
                    time.sleep(0.1)
                    print("\n listedeki sira numarasini gir")
                    
                    continue
                if not 0<int(ist)<70:
                    print("\n liste sira numarasini gir")
                    continue
                for sira , i in enumerate(b,1):
                    if sira==int(ist):
                        i=i.split("|")
                        if i[0]=="E":
                            for sayi in range(9):
                                time.sleep(0.04)
                                print  W + '[' + G + sablon[sayi] + W + ']' + R + ' >> ' + W + i[sayi+1] 
                
                    
                        if i[0]=="K":
                            for sayi in range(10):
                                time.sleep(0.04)
                                print  W + '[' + G + sablon_k[sayi] + W + ']' + R + ' >> ' + W + i[sayi+1]
                time.sleep(0.02)
                print("\033[1;37;40m")
                time.sleep(0.02)
                print("\033[92m")
                time.sleep(0.02)
                h.seek(0)
                time.sleep(0.02)
                b.seek(0)
                time.sleep(0.02)
                continue
            if oc==0:
                print("\nmenuye donuluyor..\n")
                oc=1
                continue
    if islem=="q" or "Q"==islem:
        quit()
    if not (islem=="1" or islem=="2" or islem=="3" or islem=="4"):
        continue
    if islem=="1":
        os.system("python2 1.py")
        continue
    if islem=="2":
        os.system("python2 2.py")
        continue
