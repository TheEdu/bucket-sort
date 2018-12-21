import math
import csv

GIFTBAG_SIZE = 5

def insertionSort(houses):
   for index in range(1,len(houses)):

     currentvalue = houses[index]
     position = index

     while position>0 and int(houses[position-1][1])>int(currentvalue[1]):
         houses[position] = houses[position-1]
         position = position-1

     houses[position] = currentvalue

def giftBagSort(houses, giftBagSize=GIFTBAG_SIZE):
    # Calculando los Maximos y Minimos
    minGiftNumber = int(houses[0][1])
    maxGiftNumber = int(houses[0][1])
    for i in range(0, len(houses)):
        if int(houses[i][1]) < minGiftNumber:
            minGiftNumber = int(houses[i][1])
        elif int(houses[i][1]) > maxGiftNumber:
            maxGiftNumber = int(houses[i][1])

    # Inicializacion de las giftBags (buckets)
    giftBagCount = math.floor((maxGiftNumber - minGiftNumber) / giftBagSize) + 1
    giftBags = []
    for i in range(0, giftBagCount):
        giftBags.append([])

    # Agregando valores a las giftBags (buckets)
    for i in range(0, len(houses)):
        giftBags[math.floor((int(houses[i][1]) - minGiftNumber) / giftBagSize)].append(houses[i])

    # Ordenando las GiftsBags
    sortedHouses = []
    for i in range(0, len(giftBags)):
        insertionSort(giftBags[i])
        for j in range(0, len(giftBags[i])):
            sortedHouses.append(giftBags[i][j])

    return sortedHouses

if __name__ == '__main__':
    houses = []
    header=[]

    # Leer .cvs
    with open("casas.csv", "r") as csvfile:
        reader  = csv.reader(csvfile)
        header = next(reader)
        for row in reader:
            houses.append(row)

    # Ordenar Houses
    sortedHouses = giftBagSort(houses)

    # Escribir .cvs
    with open("casasOrdenadas.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)
        for row in range(0, len(sortedHouses)):
            writer.writerow(sortedHouses[row])

