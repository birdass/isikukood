while True:
    try:
        isikukood = int(input("Твой исикукод -> "))
        isikukood= str(isikukood)
        if len(isikukood)==11:
            kod=int(str(isikukood[7])+str(isikukood[8])+str(isikukood[9]))
            if isikukood[0] == '1' or isikukood[0] == '3' or isikukood[0] == '5':
                pol="Мужчина"
            elif isikukood[0] == '2' or isikukood[0]== '4' or isikukood[0] == '6':
                pol="Женщина"
            a= int(isikukood[1])
            b= int(isikukood[2])
            c= int(isikukood[3])
            d= int(isikukood[4])
            e= int(isikukood[5])
            f= int(isikukood[6])
            if isikukood[1] <= "2" and isikukood[2] <="2":
                data=f"{e}{f}.{c}{d}.20{a}{b}"
            else:
                data=f"{e}{f}.{c}{d}.19{a}{b}"
            if 1<=kod<=10:
                reg="Kuressaare Haigla"
            elif 11<=kod<=19:
                reg="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
            elif 21<=kod<=220:
                reg="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
            elif 221<=kod<=270:
                reg="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
            elif 271<=kod<=370:
                reg="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
            elif 371<=kod<=420:
                reg="Narva Haigla"
            elif 421<=kod<=470:
                reg="Pärnu Haigla"
            elif 471<=kod<=490:
                reg="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
            elif 491<=kod<=520:
                reg="Järvamaa Haigla (Paide)"
            elif 521<=kod<=570:
                reg="Rakvere, Tapa haigla"
            elif 571<=kod<=600:
                reg="Valga Haigla"
            elif 601<=kod<=650:
                reg="Viljandi Haigla"
            elif 651<=kod<=700:
                reg="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
            print(pol, data, reg)
        else:
            print("Ошибка")
    except:
        print("Ошибка")



