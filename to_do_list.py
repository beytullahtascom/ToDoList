
to_do_list = []


# Kullanıcıdan bir görev girmesini isteyelim ve bunu listeye ekleyelim
def add_task():
    task = input("Lütfen görev giriniz:\n")
    to_do_list.append(task)
    print("Görev başarıyla eklendi.")

# Kullanıcı listeyi görmek isterse ne yapacağız
def see_task():
    for task in to_do_list:
        print("- " + task)

# Kullanıcıdan silmesini istediği görev için fonksiyon yazalım
def del_task():
    deltask = input("Silmek istediğiniz görevi yazınız:\n")
    if deltask in to_do_list:
        to_do_list.remove(deltask)
        print("Görev başarıyla silindi.")
    else:
        print("Görev bulunamadı")


# Döngü yazalım
while True:
    print("To-Do List Uygulaması")
    print("1- Görev Gir")
    print("2- Listeyi Gör")
    print("3- Görev Sil")
    print("4- Çıkış Yap")

    choice = input("Lütfen bir seçenek girin: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        see_task()
    elif choice == "3":
        del_task()
    elif choice == "4":
        print("Sistemden çıkış yapılıyor")
        break
    else:
        print("Lütfen geçerli bir seçenek giriniz")
