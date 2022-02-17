import time
vocabulary_list = []
vocabulary2_list = []

with open("vocabulary.txt", "r") as tiedosto:
    for rivi in tiedosto:
        vocabulary_list.append(str(rivi.split()))

with open("vocabulary2.txt", "r") as tiedosto:
    for rivi in tiedosto:
        vocabulary2_list.append(str(rivi.split()))

alku = time.time()
merkkijono = ""
for alkio in vocabulary_list:
    if alkio not in vocabulary2_list:
        merkkijono = alkio
print(merkkijono)
loppu = time.time()
print("aikaa kului", loppu-alku, "s")


alku = time.time()
hajatustaulu = set()
merkkijono = ""
for alkio in vocabulary2_list:
    hajatustaulu.add(alkio)

for alkio in vocabulary_list:
    if alkio not in hajatustaulu:
        merkkijono = alkio
print(merkkijono)
loppu = time.time()
print("aikaa kului", loppu-alku, "s")


alku = time.time()
merkkijono = ""
sorted_list = sorted(vocabulary_list)
sorted_list2 = sorted(vocabulary2_list)
for i in range(0,len(sorted_list)):
    if sorted_list[i] != sorted_list2[i]:
        merkkijono = sorted_list[i]
        break
print(merkkijono)
loppu = time.time()
print("aikaa kului", loppu-alku, "s")