# Vehicle Routing Problem Project

Ovaj repozitorijum sadrži projekat za rešavanje problema rutiranja vozila (*Vehicle Routing Problem - VRP*), optimizacionog problema koji se koristi za planiranje optimalnih ruta vozila u logistici i transportu.

## Opis projekta

Problem rutiranja vozila uključuje pronalaženje najefikasnijih ruta za jedno ili više vozila kako bi se dostavile robe ili usluge različitim klijentima, uz minimizaciju troškova kao što su vreme, udaljenost ili gorivo, i poštovanje ograničenja kao što su kapacitet vozila ili vremenski prozori.

## Kako koristiti

1. Klonirajte repozitorijum: git clone https://github.com/Andrija4/Vehicle-Routing-Problem-Project.git cd Vehicle-Routing-Problem-Project

2. Proverite da li imate instaliran Python i potrebne biblioteke. Ukoliko je potreban dodatni softver, instalirajte ga pomoću: pip install -r requirements.txt
(Ako fajl `requirements.txt` ne postoji, pogledajte zavisnosti u kodu i ručno instalirajte potrebne biblioteke.)

3. Pokrenite program:python main.py
Zamenite `main.py` sa imenom glavnog fajla ukoliko je drugačije.

## Organizacija fajlova

- `main.py`  
Glavni fajl za pokretanje programa.
- Ostali fajlovi uključuju implementaciju različitih funkcionalnosti, ulazne podatke i testove.

## Primer ulaznih podataka

Ulazni podaci se obično definišu u tekstualnim fajlovima ili Python skriptama. Format ulaza može uključivati:
- Koordinate klijenata
- Broj i kapacitet vozila
- Matricu udaljenosti između tačaka

Primer ulaznog fajla:
5 # Broj klijenata 3 # Broj vozila 10 20 # Koordinate klijenta 1 15 25 # Koordinate klijenta 2 ...

## Plan unapređenja

- [ ] Dodavanje podrške za različite heuristike i optimizacione algoritme
- [ ] Vizualizacija ruta korišćenjem biblioteka kao što su Matplotlib ili Folium
- [ ] Detaljna dokumentacija i korisnički interfejs

## Autor

Projekat je razvijen od strane [Andrija4](https://github.com/Andrija4). Slobodno otvorite *issue* ili pošaljite *pull request* ako želite da doprinesete.

## Licence

Ovaj projekat nema specifičnu licencu, pa se koristi **"as-is"**. Ukoliko imate pitanja ili predloge, slobodno ih podelite putem sekcije *issues*.
