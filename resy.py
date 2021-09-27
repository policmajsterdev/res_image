from PIL import Image
import os.path

filepath = os.path.dirname(__file__)  # Bierząca ścieżka
lista_plikow = list(os.listdir())
os.mkdir("Skompresowane")  # Nowy folder na skompresowane zdjęcia
nowa_sciezka = filepath + "\\" + "Skompresowane"  # Ustanowienie nowej ścieżki do Nowego folderu


for i in lista_plikow:
    if i != "resy.py":
        try:
            im = Image.open(i)
            print(i, "-", im.size)
            text = i.split('.')[0]
            roz = i.split('.')[1]
            if roz == "png":
                im = im.quantize(method=2) # Kompresja ok 70%
                new_text = text + "." + roz
                im.save(os.path.join(nowa_sciezka, new_text), optimize=True, quality=90)
            else:
                new_text = text + "." + roz
                im.save(os.path.join(nowa_sciezka, new_text), optimize=True, quality=30)  # Kompresja 70%
        except PermissionError:
            pass


print("Zakończenie programu.")
input()

