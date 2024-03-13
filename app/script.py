with open("output.txt", "w") as file:
    file.write("nevin beni konteynırdan üretti\n")

import os

# Eğer output.txt dosyası varsa, onu oku
if os.path.exists("output.txt"):
    with open("output.txt", "r") as file:
        file_content = file.read()
        print("output.txt dosyası bulundu ve içeriği okundu:")
        print(file_content)
else:
    # Eğer output.txt dosyası yoksa, yeni bir input.txt dosyası oluştur ve içine "Aranan dosya bulunamadı" yaz
    with open("input.txt", "w") as file:
        file.write("Aranan dosya bulunamadı\n")
    print("output.txt dosyası bulunamadı, yeni bir input.txt dosyası oluşturuldu ve içine 'Aranan dosya bulunamadı' yazıldı.")
