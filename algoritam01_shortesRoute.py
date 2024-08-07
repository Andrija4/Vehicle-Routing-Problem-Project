import random
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv

def napraviKlijente(n):
    listaKlijenta=[0]*n;
    for i in range(n):
        a = random.randint(0,100)
        b = random.randint(0,100)
        k = (a,b)
        listaKlijenta[i] = k
    return listaKlijenta

def napraviKlijente(n):
    listaKlijenta=[0]*n;
    for i in range(n):
        a = random.randint(0,100)
        b = random.randint(0,100)
        k = (a,b)
        listaKlijenta[i] = k
    return listaKlijenta

def napraviTabelu(liV1,liV2,liV3,updV1,updV2,updV3):

    lista1 = ["Vozilo 1:"]
    lista2 = ["Vozilo 2:"]
    lista3 = ["Vozilo 3:"]

    #Ubacujemo klijente vozila 1 u tabelu
    for i in range(0,len(liV1)):
        lista1.append(liV1[i])
        
    #Ubacujemo klijente vozila 2 u tabelu
    for i in range(0,len(liV2)):
        lista2.append(liV2[i])
        
    #Ubacujemo klijente vozila 3 u tabelu
    for i in range(0,len(liV3)):
        lista3.append(liV3[i])

    listaVozila = ["","Vozilo 1","Vozilo 2","Vozilo 3"]
    listaD = ["u.p.d.:",updV1,updV2,updV3]
        
    with open('algoritam1_tabela.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(lista1)
        writer.writerow(lista2)
        writer.writerow(lista3)
        writer.writerow(listaVozila)
        writer.writerow(listaD)

def napraviGrafik(liV1,liV2,liV3):

    G=nx.DiGraph()

    brojKlijenataV1=0
    brojKlijenataV2=0
    brojKlijenataV3=0

    putanjeV1=[]
    putanjeV2=[]
    putanjeV3=[]

    #Ubacujemo lokacije klijenata koje prolazi vozilo 1
    for i in range(0,len(liV1)):
        G.add_node(i+1,pos=(liV1[i][0],liV1[i][1]))
        brojKlijenataV1 = brojKlijenataV1 + 1

    #Pravimo putanje izmedju svih klijenata vozila 1
    for i in range(1,brojKlijenataV1):
        G.add_edge(i,i+1)
        putanjeV1.append((i,i+1))

    #Ubacujemo lokacije klijenata koje prolazi vozilo 2
    for i in range(0,len(liV2)):
        G.add_node(brojKlijenataV1+i+1,pos=(liV2[i][0],liV2[i][1]))
        brojKlijenataV2 = brojKlijenataV2 + 1

    #Pravimo putanje izmedju svih klijenata vozila 2
    for i in range(1,brojKlijenataV2):
        G.add_edge(brojKlijenataV1+i,brojKlijenataV1+i+1)
        putanjeV2.append((brojKlijenataV1+i,brojKlijenataV1+i+1))

    brojKlijenataV2=brojKlijenataV2+brojKlijenataV1

    #Ubacujemo lokacije klijenata koje prolazi vozilo 3
    for i in range(0,len(liV3)):
        G.add_node(brojKlijenataV2+i+1,pos=(liV3[i][0],liV3[i][1]))
        brojKlijenataV3 = brojKlijenataV3 + 1

    #Pravimo putanje izmedju svih klijenata vozila 3
    for i in range(1,brojKlijenataV3):
        G.add_edge(brojKlijenataV2+i,brojKlijenataV2+i+1)
        putanjeV3.append((brojKlijenataV2+i,brojKlijenataV2+i+1))

    pos=nx.get_node_attributes(G,'pos')

    nx.draw_networkx_nodes(G,pos,node_size=100)
    nx.draw_networkx_edges(G, pos, edge_color='b', arrows=True, edgelist=putanjeV1)
    nx.draw_networkx_edges(G, pos, edge_color='r', arrows=True, edgelist=putanjeV2)
    nx.draw_networkx_edges(G, pos, edge_color='green', arrows=True, edgelist=putanjeV3)

    #Legenda
    leg1 = mpatches.Patch(color='blue', label='Vozilo 1')
    leg2 = mpatches.Patch(color='red', label='Vozilo 2')
    leg3 = mpatches.Patch(color='green', label='Vozilo 3')
    
    plt.title('Algoritam 1 - najmanje predjena ruta')
    plt.legend(handles=[leg1,leg2,leg3],loc='lower right')

    plt.show()

#Baza
d = (50,50)

#Pravimo liste za predjene lokacije svakog vozila
liV1=[];
liV2=[];
liV3=[];

distance=[];

#Ukupna predjena distanca vozila
updV1=0
updV2=0
updV3=0

#Pocetne tacke vozila
liV1.append(d);
liV2.append(d);
liV3.append(d);

#Trenutne lokacije vozila
trV1 = d;
trV2 = d;
trV3 = d;

#lista najblizih klijenata sva 3 vozila
nbkV=[]

#Indexi najblizih klijenata sva 3 vozila
index1=0
index2=0
index3=0

#Distance klijenata od vozila
disKV1=0
disKV2=0
disKV3=0

n = int(input("Unesite broj klijenata: "))
listaKlijenta = napraviKlijente(n)
print("Lista klijenata: ",listaKlijenta)

while(len(listaKlijenta)>0):
    
    #Vozilo 1
    for i in range(0,len(listaKlijenta)):
        x = listaKlijenta[i][0]
        y = listaKlijenta[i][1]
        distanca = abs(x-trV1[0])+abs(y-trV1[1])

        distance.append(distanca)
    print("Distance vozila 1 od klijenta su:",distance)

    #Trazenje indexa za najblizeg klijenta
    disKV1 = distance[0]
    index1 = 0
    for i in range(1,len(distance)):
        if(disKV1>distance[i]):
            index1 = i
            disKV1 = distance[i]
    distance = []
    print("Index najblizeg klijenta od vozila 1 je:",index1)

    

    #Vozilo 2
    for i in range(0,len(listaKlijenta)):
        x = listaKlijenta[i][0]
        y = listaKlijenta[i][1]
        distanca = abs(x-trV2[0])+abs(y-trV2[1])

        distance.append(distanca)
    print("Distance vozila 2 od klijenta su:",distance)

    #Trazenje indexa za najblizeg klijenta
    disKV2 = distance[0]
    index2 = 0
    for i in range(1,len(distance)):
        if(disKV2>distance[i]):
            index2 = i
            min_broj = distance[i]
    distance = []
    print("Index najblizeg klijenta od vozila 2 je:",index2)

    

    #Vozilo 3
    for i in range(0,len(listaKlijenta)):
        x = listaKlijenta[i][0]
        y = listaKlijenta[i][1]
        distanca = abs(x-trV3[0])+abs(y-trV3[1])

        distance.append(distanca)
    print("Distance vozila 3 od klijenta su:",distance)

    #Trazenje indexa za najblizeg klijenta
    disKV3 = distance[0]
    index3 = 0
    for i in range(1,len(distance)):
        if(disKV3>distance[i]):
            index3 = i
            disKV3 = distance[i]
    distance = []
    print("Index najblizeg klijenta od vozila 3 je:",index3)

    #Ukoliko je vozilo 1 najblize nekom klijentu
    if(disKV1<=disKV2 and disKV1<=disKV3):

        liV1.append(listaKlijenta[index1])
        updV1 = updV1 + disKV1
        trV1 = listaKlijenta[index1]
        listaKlijenta.pop(index1)
        print("\nLista klijenata je:",listaKlijenta)
        print("Vozilo 1 je sada preslo:",liV1)
        print("Vozilo 1 je na lokaciji:",trV1)
        print("Distanca koju je vozilo 1 preslo:\n",updV1)

    #Ukoliko je vozilo 2 najblize nekom klijentu
    elif(disKV2<disKV1 and disKV2<=disKV3):

        liV2.append(listaKlijenta[index2])
        updV2 = updV2 + disKV2
        trV2 = listaKlijenta[index2]
        listaKlijenta.pop(index2)
        print("\nLista klijenata je:",listaKlijenta)
        print("Vozilo 2 je sada preslo:",liV2)
        print("Vozilo 2 je na lokaciji:",trV2)
        print("Distanca koju je vozilo 2 preslo:\n",updV2)

    #Ukoliko je vozilo 3 najblize nekom klijentu
    elif(disKV3<disKV1 and disKV3<disKV2):

        liV3.append(listaKlijenta[index3])
        updV3 = updV3 + disKV3
        trV3 = listaKlijenta[index3]
        listaKlijenta.pop(index3)
        print("\nLista klijenata je:",listaKlijenta)
        print("Vozilo 3 je sada preslo:",liV3)
        print("Vozilo 3 je na lokaciji:",trV3)
        print("Distanca koju je vozilo 3 preslo:\n",updV3)

#Vozila se vracaju u bazu
liV1.append(d);
liV2.append(d);
liV3.append(d);

print("\nVozila su obisla sledece lokacije:","\nVozilo 1:",liV1,"\nVozilo 2:",liV2,"\nVozilo 3:",liV3)
print("\nUkupno predjene distance su:","\nVozilo 1:",updV1,"\nVozilo 2:",updV2,"\nVozilo 3:",updV3)

napraviGrafik(liV1,liV2,liV3)
napraviTabelu(liV1,liV2,liV3,updV1,updV2,updV3)
