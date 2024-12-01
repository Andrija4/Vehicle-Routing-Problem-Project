# Vehicle Routing Problem Project

Ovaj repozitorijum sadrži projekat vezan za rešavanje problema rutiranja vozila (*Vehicle Routing Problem - VRP*). Problem rutiranja vozila je optimizacioni problem koji ima široku primenu u logistici, transportu i distribuciji.

## Opis projekta

Cilj ovog projekta je razviti rešenje za optimizaciju ruta vozila kako bi se minimizirali troškovi, pređena udaljenost ili vreme, uz poštovanje ograničenja kao što su kapacitet vozila, vremenski prozori ili specifični zahtevi klijenata.

## Sadržaj

- **Kod**  
  Implementacija algoritama za rešavanje VRP-a, uključujući heuristike i optimizacione tehnike.
- **Podaci**  
  Ulazni skupovi podataka koji definišu mrežu klijenata, vozila i ograničenja.
- **Rezultati**  
  Primeri rezultata optimizovanih ruta i analiza njihovih performansi.

## Tehnologije

Projekat je razvijen koristeći:
- Programski jezik **C**
- Standardne biblioteke i algoritme za optimizaciju

## Kako koristiti

1. Klonirajte repozitorijum: git clone https://github.com/Andrija4/Vehicle-Routing-Problem-Project.git cd Vehicle-Routing-Problem-Project
2. Pogledajte ulazne fajlove u direktorijumu `data` za primer ulaznih skupova podataka.
3. Kompajlirajte i pokrenite projekat: gcc -o vrp_solver main.c ./vrp_solver data/input_file.txt
Zamenite `data/input_file.txt` odgovarajućim fajlom sa podacima.

## Organizacija

- `src/`  
Glavni izvorni kod projekta.
- `data/`  
Skupovi podataka za testiranje.
- `results/`  
Generisani rezultati i analize.

## Plan razvoja

- [x] Implementacija osnovnog heurističkog algoritma
- [ ] Dodavanje naprednih algoritama (npr. genetski algoritam, simulirano kaljenje)
- [ ] Vizualizacija ruta
- [ ] Dokumentacija i korisnički interfejs

## Autor

Projekat je razvijen od strane [Andrija4](https://github.com/Andrija4). Slobodno otvorite *issue* ili pošaljite *pull request* ako želite da doprinesete.

## Licence

Ovaj projekat nema specifičnu licencu, pa se koristi **"as-is"**. Ukoliko imate pitanja ili predloge, slobodno ih podelite putem sekcije *issues*.


