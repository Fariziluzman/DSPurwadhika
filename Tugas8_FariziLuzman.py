x = {}

def cetakkamus(n):
    print('Key     Value')
    for key, value in x.items():
        print('{}      {}'.format(key, value))

def tambahkamus(kunci,nilai):
    x[kunci] = nilai 
    return x

def carikamus():
    cetakkamus(x)
    y = input ('Mau cari apa ? : ')
    hasil = list(filter(lambda z : y.lower() in str.lower(z), x ))
    print(hasil)

keluar = False
while (keluar == False) :
    menu = int(input('1.Show Dictionary\n2.Add Dictionary\n3.Search Dictionary\n4.Exit : '))
    if (menu == 1):
        cetakkamus(x)
    elif(menu == 2):
        ulang = int(input('Masukkin berapa kali ? :'))
        for i in range (ulang):
            cek = int(input('Mau nilai apa ? \n1.String\n2.Number : '))
            kunci = input('Masukkin kunci apa ? : ')
            nilai = input('Masukkin nilai apa ? : ' )
            if (cek == 1):
                nilai = nilai
            elif(cek == 2):
                nilai = int(nilai)
            tambahkamus(kunci,nilai)  
    elif(menu == 3):
        carikamus()
    elif(menu == 4):
        exit()
    else:
        print('Yang bener dong ngisinya !')
            
    print('Mau kembali ke menu utama? ')
    check = False
    while (check == False ) :
        menu = input('ya/tidak :  ').lower()
        if (menu == 'ya' or menu == 'tidak') :
            check = True
        else :
            print ('inputnya salah')
    if menu == 'tidak' :
        keluar = True


        


