''' Ovo je bin packing problem koji je rijesen pomocu jednostavnog heuristickog algoritma,
 First Fit Decreasing (FFD) algoritma.
 Napomena: ovo je heuristicki algoritam, te samim tim rezultat ne mora biti optimalno rjesenje.
 Prvo sortiramo stavke u opadajucem redoslijedu po velicinima, a potom svaku
 stavku postavljamo u prvu korpu u listi koja raspolaze sa dovoljno praznog prostora za tu stavku.
 time complexity: O(n^2) '''

import sys
sys.path.append('../')

# funkcija koja ucitava instance problema iz zadate putanje
def readInInstances(path):
    dict = {}
    f = open(path, "r")
    bin_size = int(f.readline())
    number_of_instances = int(f.readline())
    n = 1
    for line in f:
        dict["item" + str(n) + ""] = int(line)
        n += 1
    f.close()
    return bin_size, number_of_instances, dict

''' funkcija koja za argument uzima dictionary (stavki i velicina) i velicinu kanti
a kao rezultat vraca listu skupova objekata, gdje je suma velicina objekata
svakog skupa manja ili jednaka od max_summed_size_per_bin.'''

def first_fit_decreasing_algorithm(dictionary, max_summed_size_per_bin, return_sizes=None):
    # definiramo listu skupova (korpi), u kojoj cemo cuvati stavke svake korpe
    list_of_bins = []

    # stavke sortiramo u opadajucem redoslijedu po njihovim velicinama

    items = list(dictionary.keys())
    sorted_items = sorted(items, key=lambda x: dictionary[x], reverse=True)  # sortiranje u opadajucem redoslijedu

    # stavljamo svaku stavku u prvu korpu sa dovoljno praznog prostora:
    for my_item in sorted_items:
        found_a_bin = False
        item_size = dictionary[my_item]

        # provjeravamo da li postoji korpa sa dovoljno praznog prostora za ovu stavku
        for index, my_bin in enumerate(list_of_bins):  # "my_bin" je skup stavki u korpi
            # trazimo sumu velicina stavki u korpi
            summed_items_in_bin = sum([dictionary[x] for x in my_bin])

            # ako postoji dovoljno prostora za ovu stavku u korpi, stavljamo je u korpu
            if item_size <= (max_summed_size_per_bin - summed_items_in_bin):
                list_of_bins[index].add(my_item)
                found_a_bin = True
                break  # iskacemo iz "for index, my bin" petlje

        # ukoliko nismo stavili my_item u neku korpu, tada tu stavku stavljamo u novu korpu
        if found_a_bin == False:
            list_of_bins.append({my_item})

    # return sizes koristimo kao uslov pri ispisu da li indeksa stavki ili njihovih vrijednosti u korpama
    if return_sizes is None:
        return list_of_bins  # vracamo nazive stavki
    else:
        print(len(list_of_bins))
        # pravimo listu podlisti, gdje svaka podslita sadrzi velicine stavki u korpi:
        list_of_item_sizes = [sorted([dictionary[x] for x in sublist]) for sublist in list_of_bins]
        return list_of_item_sizes



