# 1
num_list = [1, 2, 3]
num_list.append(10)
num_list.append(20)
print(num_list)
num_list.remove(10)
print(num_list)
# 2
list_1 = list(range(1, 6))
print(list_1)
print(sum(list_1))
# 3
list_2 = list(range(1, 6))
dbl_lst = [num ** 2 for num in list_2]
print(list_2)
print(dbl_lst)
# 1
tpl = ("яблуко", "банан", "апельсин")
print(*tpl, sep="\n")
# 2
tpl_1 = tuple(range(1, 5))
tpl_2 = (10, 20)
tpl_3 = tpl_1 + tpl_2
print(tpl_3)
# 1
dict_1 = {
    "name": "Tom",
    "age": 25,
    "sport": "tennis"
}
print(dict_1)
# 2
dict_2 = {
    "Kolobok": 1959,
    "Neznayka": 1961,
}
dict_2["Ognivo"] = 1975
print(dict_2)
# 3
countrys = {
    "Ukraine": "Kyiv",
    "Spain": "Madrid",
    "Italy": "Rome",
    "Poland": "Warsaw"
}
new_country = input("Input country: ")
if new_country in countrys:
    print(countrys[new_country])
else:
    print("This country is not count")
