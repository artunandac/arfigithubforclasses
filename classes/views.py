from django.shortcuts import render, redirect
from django.contrib import messages

from datetime import datetime, timezone

harflist = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ç','ğ','ı','ö','ş','ü',
    '0', '1', '2', '3','4', '5', '6', '7', '8', '9',
    ' ',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Ç','Ğ','I','Ö','Ş','Ü',
    '<','=','>','?','@','[',']','^','_','`','{','|','}','~',',','.','\\','\n'
]
encryptedlist = {}
decryptedlist = {}
kriptolist = []
encryptedkelime = ''
decryptedkelime = ''
siniflar = {'gXh{Kb':'9A',
            'gXh{Kc':'9B',
            'gXh{Ke':'9C',
            'gXh{Kg':'9D',
            'Xsb':'10A',
            'Xsc':'10B',
            'Xse':'10C',
            'Xsg':'10D',
            'Xsj':'10E',
            }

def writeerrorstotxt(sinif,isim, hatalianahtar, hatalimetin):
    date = datetime.now()
    with open("BULUNANHATALAR.txt","a", encoding="utf-8") as file:
        file.write(siniflar[sinif]+' '+isim+' '+ str(hatalianahtar)+' '+ hatalimetin+' '+ date.strftime("%A, %d. %B %Y %I:%M%p")+ '\n')        
        
def writelogstotxt(sinif,pagename):
    date = datetime.now()
    with open(siniflar[sinif]+".txt","a", encoding="utf-8") as file:
        file.write(siniflar[sinif]+' '+pagename+' '+ date.strftime("%A, %d. %B %Y %I:%M%p")+ '\n')        
# Create your views here.
def about(request, sinif):
    if sinif in list(siniflar.keys()):
        writelogstotxt(sinif,'ABOUT')
        return render(request, 'pages/about.html')
    else:
        date = datetime.now()
        with open("ERROR.txt","a", encoding="utf-8") as file:
            file.write('SOMEONE TRIED '+ date.strftime("%A, %d. %B %Y %I:%M%p")+ '\n')        
        return render(request, 'pages/youlittlebitch.html')
def index(request, sinif):
    if sinif in list(siniflar.keys()):
        writelogstotxt(sinif,'INDEX')
        if request.method == 'POST':
            encryptedkelime = ''
            decryptedkelime = ''
            anahtar = int(request.POST['anahtar'])
            sifrelenecekkelime  = str(request.POST['sifrele'])
            sifrelenmiskelime = str(request.POST['sifrecoz'])
            if (sifrelenecekkelime=='')!=(sifrelenmiskelime==''):

                birinci = anahtar
                ikinci = 2 * birinci - 1
                ucuncu = birinci + ikinci

                for i in range(int(len(harflist) / 3)):
                    kriptolist.append(birinci)
                    kriptolist.append(ikinci)
                    kriptolist.append(ucuncu)
                    birinci = ucuncu + ikinci
                    ikinci = birinci + ucuncu
                    ucuncu = birinci + ikinci

                kalan = len(harflist) - len(harflist) // 3 * 3
                if kalan == 1:
                    kriptolist.append(birinci)
                if kalan == 2:
                    kriptolist.append(birinci)
                    kriptolist.append(ikinci)
                else:
                    None
                eklenmiskarakterler = []
                atlamalistesi =[]

                for i in range(0,len(harflist)):
                    atlamamiktari = kriptolist[i]
                    atlamalistesi.append((i+atlamamiktari)%len(harflist))
                sonatlamalistesi = []
                for i in atlamalistesi:
                    if i not in sonatlamalistesi:
                        sonatlamalistesi.append(i)
                    else:
                        for z in sonatlamalistesi:
                            i+=1
                            i=i%len(harflist)
                            if i not in sonatlamalistesi:
                                sonatlamalistesi.append(i)
                                break
                            else:
                                None


                for i in range(0,len(harflist)):
                    decryptedlist[harflist[i]] = harflist[sonatlamalistesi[i]]
                    encryptedlist[harflist[i]] = harflist[sonatlamalistesi[i]]
                
                if sifrelenmiskelime!='':
                    print('sifrecözmebaslıyor')
                    for i in range(0, len(sifrelenmiskelime)):
                        decryptedkelime += list(decryptedlist.keys())[list(decryptedlist.values()).index(sifrelenmiskelime[i])]  
                    print(decryptedkelime)
                    context = {'text': decryptedkelime}
                    print(context)
                    return render(request, 'pages/detail.html', context)
                elif sifrelenecekkelime!='':
                    print('sifrelemebaslıyor')
                    for i in range(0, len(sifrelenecekkelime)):
                        print(type(encryptedkelime))
                        (encryptedkelime) += str(encryptedlist[sifrelenecekkelime[i]]) 

                    print(encryptedkelime)
                    context = {'text': encryptedkelime}
                    print(context)
                    return render(request, 'pages/detail.html', context)
            else:
                messages.add_message(request, messages.ERROR, 'Tek seferde yalnızca bir işlem yapın: Şifreleme veya Şifre Kırma')
                return redirect('')
        else:
            return render(request, 'pages/index.html')
    else:
        date = datetime.now()
        with open("ERROR.txt","a", encoding="utf-8") as file:
            file.write('SOMEONE TRIED '+ date.strftime("%A, %d. %B %Y %I:%M%p")+ '\n')        
        return render(request, 'pages/youlittlebitch.html')

# def hatayatesekkur(request,sinif):
#     messages.add_message(request, messages.ERROR, 'Hatayı Bildirdiğiniz İçin Teşekkürler')
#     return render(request, 'pages/classhata.html')
def hatabildir(request, sinif):
    if sinif in list(siniflar.keys()):
        writelogstotxt(sinif,'INDEX')
        if request.method == 'POST':
            hatalianahtar = int(request.POST['hatalianahtar'])
            isim  = str(request.POST['isim'])
            hatalimetin = str(request.POST['hatalimetin'])
            writeerrorstotxt(sinif,isim, hatalianahtar, hatalimetin)
            messages.add_message(request, messages.ERROR, 'Hatayı Bildirdiğiniz İçin Teşekkürler')
            context = {'text': sinif}
            return render(request, 'pages/classhata.html', context)
            # return render(request, 'pages/classhata.html')
        else:
            context = {'text': sinif}
            return render(request, 'pages/classhata.html', context)
            # return render(request, 'pages/classhata.html')
    else:
        date = datetime.now()
        with open("ERROR.txt","a", encoding="utf-8") as file:
            file.write('SOMEONE TRIED '+ date.strftime("%A, %d. %B %Y %I:%M%p")+ '\n')        
        return render(request, 'pages/youlittlebitch.html')
        
# def result(request, text):
#     context = {
#         'text': text
#     }
#     print(context)
#     return render(request, 'pages/detail.html', context)