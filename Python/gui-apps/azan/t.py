from json import load

with open('/mnt/TOSHIBA/Islam-projects/Python/gui_apps/azan/countries+cities.json') as all :

    dicti2 = load(all)

all1 = []

for i in range(len(dicti2 ) ) :


    all1.append(dicti2[i]["name"])

# print(all)


# all2 = []

# for i in range(len(dicti2 ) + 1):

#     # i[i]['name'].append(l)

#     all2.append([i]["name"])

# cites.keys()

# print(cites)
# print(l)
# print(len(l))