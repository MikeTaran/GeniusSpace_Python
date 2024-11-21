str_1 = "hello"
num_1 = 25
num_2 = 15.23
bln_1 = True
lst_1 = [1, 2, 3]
tpl = (5,"ok", 7)
var_1 = None
dct_1 = {"name": "Tom", "age": 25}
#
num_str = 125
num_str = str(num_str)
print(type(num_str))
#
message = 'Hi, my name is Python!'
new_message = message.replace("y", "0").replace("i", "1")
print(new_message)
#
split_test = 'This is a split test'.split()
print(split_test)
string_join = " ".join(split_test)
print(string_join)
#
print(len(string_join))
#
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)
#
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)
#
print(list_extend.index(6))
print(len(list_append))
#
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test.keys())
print(dict_test.values())
print(dict_test.items())




