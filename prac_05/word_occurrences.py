word = input("Enter: ")
turn_to_list = word.split(" ")
get_dict = {}
for key in turn_to_list:
    if get_dict.get(key) is None:
        get_dict[key] = 1
    else:
        get_dict[key] += 1
for keys in get_dict.keys():
    print("{:{}} : {}".format(keys, 10, get_dict[keys]))