print('Kalkukator Purata Nilai Gred MRSM 🎓')
print("\nSila tulis mengikut ejaan yang betul dan tepat")
while True:
 ujian= str(input("\nAdakah ini Ujian Formatif (Ya/Tidak):"))
 if ujian == "Ya":
    #input
    str(input("\nSila tekan '⤶' di keyboard untuk meneruskan»»⟩"))
    nama =  str(input("\nSila masukkan nama pendek anda:"))
    print ("\nNama yang bagus!")
    str(input("\nSila tekan '⤶' di keyboard untuk teruskan»»⟩"))
    melayu = float(input("\nSila Masukkan Markah BM :"))
    inggeris =float(input("\nSila Masukkan Markah BI:"))
    math = float(input("\nSila Masukkan Markah MT:"))
    sci = float(input("\nSila Masukkan Markah SN:"))
    reka= float(input("\nSila Masukkan Markah RBT :"))
    islam = float(input("\nSila Masukkan Markah PAI :"))
    sj = float(input("\nSila Masukkan Markah Sejarah: "))                                           
    geog= float(input("\nSila Masukkan Markah Geografi:"))
    #Bahasa Inggeris
    if (inggeris >= 80):
        bi= 4.00
    elif (inggeris >= 75):
        bi=3.75
    elif (inggeris >= 70):
         bi=3.50
    elif (inggeris >= 65):
         bi=3.25
    elif (inggeris >= 60):
        bi=3.00
    elif (inggeris >= 55):
        bi=2.75
    elif (inggeris >= 50):
        bi =2.50
    elif (inggeris >= 45):
        bi=2.25
    elif (inggeris >= 40):
        bi=2.00
    elif (inggeris >= 35):
        bi=1.00
    else:
        bi=0.00
    #Bahasa Melayu
    if (melayu >= 80):
        bm= 4.00
    elif (melayu >= 75):
        bm=3.75
    elif (melayu >= 70):
        bm=3.50
    elif (melayu >= 65):
        bm=3.25
    elif (melayu >= 60):
        bm=3.00
    elif (melayu >= 55):
        bm=2.75
    elif (melayu >= 50):
        bm=2.50
    elif (melayu >= 45):
        bm=2.25
    elif (melayu >= 40):
        bm=2.00
    elif (melayu >= 35):
        bm=1.00
    else:
        bm=0.00
    #Matenatik
    if (math >= 80):
        mt= 4.00
    elif (math >= 75):
        mt=3.75
    elif (math >= 70):
        mt=3.50
    elif (math >= 65):
        mt=3.25
    elif (math >= 60):
        mt=3.00
    elif (math >= 55):
        mt=2.75
    elif (math >= 50):
        mt=2.50
    elif (math >= 45):
        mt=2.25
    elif (math >= 40):
        mt=2.00
    elif (math >= 35):
        mt=1.00
    else:
        mt=0.00
    #Sains
    if (sci >= 80):
        sn= 4.00
    elif (sci >= 75):
        sn=3.75
    elif (sci >= 70):
        sn=3.50
    elif (sci >= 65):
        sn=3.25
    elif (sci >= 60):
        sn=3.00
    elif (sci >= 55):
        sn=2.75
    elif (sci >= 50):
        sn=2.50
    elif (sci >= 45):
        sn=2.25
    elif (sci >= 40):
        sn=2.00
    elif (sci >= 35):
        sn=1.00
    else:
        sn=0.00
    #RBT
    if (reka >= 80):
        rbt= 4.00
    elif (reka >= 75):
        rbt=3.75
    elif (reka >= 70):
        rbt=3.50
    elif (reka >= 65):
        rbt=3.25
    elif (reka >= 60):
        rbt=3.00
    elif (reka >= 55):
        rbt=2.75
    elif (reka >= 50):
        rbt=2.50
    elif (reka >= 45):
        rbt=2.25
    elif (reka >= 40):
        rbt=2.00
    elif (reka >= 35):
        rbt=1.00
    else:
        rbt=0.00
    #PAI
    if (islam >=80):
        pai=4.00
    elif (islam >= 75):
        pai=3.75
    elif (islam >= 70):
        pai=3.50
    elif (islam >= 65):
        pai=3.25
    elif (islam >= 60):
        pai=3.00
    elif (islam >= 55):
        pai=2.75
    elif (islam >= 50):
        pai=2.50
    elif (islam >= 45):
        pai=2.25
    elif (islam >= 40):
        pai=2.00
    elif (islam >= 35):
        pai=1.00
    else:
        pai=0.00
    #Sejarah
    if (sj >= 80):
        sej= 4.00
    elif (sj >= 75):
        sej=3.75
    elif (sj >= 70):
        sej=3.50
    elif (sj >= 65):
        sej=3.25
    elif (sj >= 60):
        sej=3.00
    elif (sj >= 55):
        sej=2.75
    elif (sj >= 50):
        sej=2.50
    elif (sj >= 45):
        sej=2.25
    elif (sj >= 40):
        sej=2.00
    elif (sj >= 35):
        sej=1.00
    else:
        sej=0.00
    #Geografi
    if (geog >= 80):
        geo= 4.00
    elif (geog >= 75):
        geo=3.75
    elif (geog >= 70):
        geo=3.50
    elif (geog >= 65):
        geo=3.25
    elif (geog >= 60):
        geo=3.00
    elif (geog >= 55):
        geo=2.75
    elif (geog >= 50):
        geo=2.50
    elif (geog >= 45):
        geo=2.25
    elif (geog >= 40):
        geo=2.00
    elif (geog >= 35):
        geo=1.00
    else:
        geo=0.00
    #Pengiraan
    Bm = bm*5.00
    Bi = bi*5.00
    Mt = mt*5.00
    Sn = sn*5.00
    Rbt = rbt*4.00
    Pai = pai*4.00
    Sej = sej*3.00
    Geo = geo*3.00    
    #Pengiraan2
    jumlah = Bm + Bi + Mt + Sn + Rbt + Pai + Sej + Geo
    purata = jumlah/34
    #Hasil
    print("\nPNG anda untuk Ujian Setara Semester ini ialah",round(purata,2))
    if purata ==4.00:
        print("\nTahniah",nama, "!, Anda mendapat pointer 4.00. Kekalkan prestasi anda. ")
    elif purata >= 3.50:
        print("\nTahniah",nama,"!, Teruskan usaha anda.")
    elif purata >= 3.00:
        print("\nAnda sudah lakukan yang terbaik,",nama,"! Cuba Lagi dalam ujian seterusnya.")
    else:
        print("\n Jangan putus asa,",nama,". Teruskan berusaha dengan lebih gigih.")
 elif ujian == "Tidak":
    #Input
    str(input("\nSila tekan '⤶' untuk meneruskan»»⟩"))
    nama =  str(input("\nSila masukkan nama pendek anda:"))
    print ("\nNama yang bagus!")
    str(input("\nSila tekan '⤶' untuk teruskan»»⟩"))
    melayu = float(input("\nSila Masukkan Markah BM :"))
    inggeris =float(input("\nSila Masukkan Markah BI:"))
    math = float(input("\nSila Masukkan Markah MT:"))
    sci = float(input("\nSila Masukkan Markah SN:"))
    reka= float(input("\nSila Masukkan Markah RBT :"))
    islam = float(input("\nSila Masukkan Markah PAI :"))
    sj = float(input("\nSila Masukkan Markah Sejarah: "))                                           
    geog= float(input("\nSila Masukkan Markah Geografi:"))
    psv= float(input("\nSila Masukkan Markah Seni:"))
    ask= float(input("\nSila Masukkan Markah PJ:"))
    #Bahasa Inggeris
    if (inggeris >= 80):
        bi= 4.00
    elif (inggeris >= 75):
        bi=3.75
    elif (inggeris >= 70):
        bi=3.50
    elif (inggeris >= 65):
        bi=3.25
    elif (inggeris >= 60):
        bi=3.00
    elif (inggeris >= 55):
        bi=2.75
    elif (inggeris >= 50):
        bi =2.50
    elif (inggeris >= 45):
        bi=2.25
    elif (inggeris >= 40):
        bi=2.00
    elif (inggeris >= 35):
        bi=1.00
    else:
        bi=0.00
    #Bahasa Melayu
    if (melayu >= 80):
        bm= 4.00
    elif (melayu >= 75):
        bm=3.75
    elif (melayu >= 70):
        bm=3.50
    elif (melayu >= 65):
        bm=3.25
    elif (melayu >= 60):
        bm=3.00
    elif (melayu >= 55):
        bm=2.75
    elif (melayu >= 50):
        bm=2.50
    elif (melayu >= 45):
        bm=2.25
    elif (melayu >= 40):
        bm=2.00
    elif (melayu >= 35):
        bm=1.00
    else:
        bm=0.00
    #Matenatik
    if (math >= 80):
        mt= 4.00
    elif (math >= 75):
        mt=3.75
    elif (math >= 70):
        mt=3.50
    elif (math >= 65):
        mt=3.25
    elif (math >= 60):
        mt=3.00
    elif (math >= 55):
        mt=2.75
    elif (math >= 50):
        mt=2.50
    elif (math >= 45):
        mt=2.25
    elif (math >= 40):
        mt=2.00
    elif (math >= 35):
        mt=1.00
    else:
        mt=0.00
    #Sains
    if (sci >= 80):
        sn= 4.00
    elif (sci >= 75):
        sn=3.75
    elif (sci >= 70):
        sn=3.50
    elif (sci >= 65):
        sn=3.25
    elif (sci >= 60):
        sn=3.00
    elif (sci >= 55):
        sn=2.75
    elif (sci >= 50):
        sn=2.50
    elif (sci >= 45):
        sn=2.25
    elif (sci >= 40):
        sn=2.00
    elif (sci >= 35):
        sn=1.00
    else:
        sn=0.00
    #RBT
    if (reka >= 80):
        rbt= 4.00
    elif (reka >= 75):
        rbt=3.75
    elif (reka >= 70):
        rbt=3.50
    elif (reka >= 65):
        rbt=3.25
    elif (reka >= 60):
        rbt=3.00
    elif (reka >= 55):
        rbt=2.75
    elif (reka >= 50):
        rbt=2.50
    elif (reka >= 45):
        rbt=2.25
    elif (reka >= 40):
        rbt=2.00
    elif (reka >= 35):
        rbt=1.00
    else:
        rbt=0.00
    #PAI
    if (islam >=80):
        pai=4.00
    elif (islam >= 75):
        pai=3.75
    elif (islam >= 70):
        pai=3.50
    elif (islam >= 65):
        pai=3.25
    elif (islam >= 60):
        pai=3.00
    elif (islam >= 55):
        pai=2.75
    elif (islam >= 50):
        pai=2.50
    elif (islam >= 45):
        pai=2.25
    elif (islam >= 40):
        pai=2.00
    elif (islam >= 35):
        pai=1.00
    else:
        pai=0.00
    #Sejarah
    if (sj >= 80):
        sej= 4.00
    elif (sj >= 75):
        sej=3.75
    elif (sj >= 70):
        sej=3.50
    elif (sj >= 65):
        sej=3.25
    elif (sj >= 60):
        sej=3.00
    elif (sj >= 55):
        sej=2.75
    elif (sj >= 50):
        sej=2.50
    elif (sj >= 45):
        sej=2.25
    elif (sj >= 40):
        sej=2.00
    elif (sj >= 35):
        sej=1.00
    else:
        sej=0.00
    #Geografi
    if (geog >= 80):
        geo= 4.00
    elif (geog >= 75):
        geo=3.75
    elif (geog >= 70):
        geo=3.50
    elif (geog >= 65):
        geo=3.25
    elif (geog >= 60):
        geo=3.00
    elif (geog >= 55):
        geo=2.75
    elif (geog >= 50):
        geo=2.50
    elif (geog >= 45):
        geo=2.25
    elif (geog >= 40):
        geo=2.00
    elif (geog >= 35):
        geo=1.00
    else:
        geo=0.00
    #ASK
    if (ask >= 80):
        Ask= 4.00
    elif (ask >= 75):
        Ask=3.75
    elif (ask >= 70):
        Ask=3.50
    elif (ask >= 65):
        Ask=3.25
    elif (ask >= 60):
        Ask=3.00
    elif (ask >= 55):
        Ask=2.75
    elif (ask >= 50):
        Ask=2.50
    elif (ask >= 45):
        Ask=2.25
    elif (ask >= 40):
        Ask=2.00
    elif (ask >= 35):
        Ask=1.00
    else:
        Ask=0.00
    #SENI
    if (psv >= 80):
        Psv= 4.00
    elif (psv >= 75):
        Psv=3.75
    elif (psv >= 70):
        Psv=3.50
    elif (psv >= 65):
        Psv=3.25
    elif (psv >= 60):
        Psv=3.00
    elif (psv >= 55):
        Psv=2.75
    elif (psv >= 50):
        Psv=2.50
    elif (psv >= 45):
        Psv=2.25
    elif (psv >= 40):
        Psv=2.00
    elif (psv >= 35):
        Psv=1.00
    else:
        Psv=0.00        
    #Pengiraan
    Bm = bm*5.00
    Bi = bi*5.00
    Mt = mt*5.00
    Sn = sn*5.00
    Rbt = rbt*4.00
    Pai = pai*4.00
    Sej = sej*3.00
    Geo = geo*3.00    
    Komputer = Ask*2.00    
    Seni = Psv*2.00    
    #Pengiraan2
    jumlah = Bm + Bi + Mt + Sn + Rbt + Pai + Sej + Geo + Komputer + Seni
    purata = jumlah/38
    #Hasil
    print("\nPNG anda untuk Ujian Semester ini ialah",round(purata,2))
    #Motivasi
    if purata ==4.00:
        print("\nTahniah",nama, "!, Anda mendapat pointer 4.00. Kekalkan prestasi anda.")
    elif purata >= 3.50:
        print("\nTahniah",nama,"!, Teruskan usaha anda.")
    elif purata >= 3.00:
        print("\nAnda sudah lakukan yang terbaik,",nama,"! Cuba Lagi dalam ujian seterusnya.")
    else:
        print("\n Jangan putus asa,",nama,". Teruskan berusaha dengan lebih gigih.")
 else:
    print("\nData tidak sah❗ Sila masukkan mengikut ejaan yang diberikan.")        
 repeat = str( input("\nAdakah anda ingin mengira lagi❓(Ya/Tidak)"))
 if repeat != "Ya":
    break
 #Output    
print("\nTerima Kasih kerana telah menggunakan Kalkulator ini")
print("\nOleh: Waldan")