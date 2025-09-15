type_str = "Normal Fire Water Grass Electric Ice Fighting Poison Ground Flying Psychic Bug Rock Ghost Dragon Dark Steel Fairy"

type_list = type_str.split()

for type_1 in type_list:
    for type_2 in type_list:
        print("\"" +type_1 + type_2 + "\": 1,")