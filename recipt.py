from pprint import pprint
cook_book = {}
with open('recipes.txt', 'rt', encoding="utf8") as file:
    for l in file:
        d_name = l.strip()
        cook_book[d_name] = []

        ingridient_count = file.readline()
        for i in range(int(ingridient_count)):
            menu = {}
            dish = file.readline()
            name, quantity, measure = dish. strip().split(' | ')
            menu['ingredient_name'] = name
            menu['quantity'] = quantity
            menu['measure'] = measure
            cook_book[d_name].append(menu)
        blank_line = file.readline()

pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingridiens = {}
    for dish in dishes:
        for ingridient in  cook_book[dish]:
            ingridiens[ingridient['ingredient_name']] = {'measure': ingridient['measure'],
                                                         'quantity': int(ingridient['quantity'])*person_count}
    return ingridiens


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

def read_file (file):
    with open(file,'r', encoding= 'utf8') as f:
        lines = f.readlines()
        count = len(lines)
        lines = ''.join(lines)
        return f.name,count,lines
files = ['1.txt', '2.txt','3.txt']
read_files = []
for i in files:
    info = read_file(i)
    read_files.append(info)
read_files.sort(key=lambda x : x[1])
pprint(read_files)
with open('result.txt', 'w', encoding='utf8') as f:
    for file in read_files:
        f.write("\n".join(map(str, file))+'\n')