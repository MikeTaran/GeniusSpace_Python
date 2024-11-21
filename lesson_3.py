password = "password123"
# new_pass = input("Input password: ")
new_pass = "1234"
if new_pass == password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

days_of_week = {
    "1": 'Monday',
    "2": 'Tuesday',
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday",
    "7": "Sunday"
}
# new_day = input("Input day number of week: ")
new_day = "5"
if new_day in days_of_week.keys():
    print(days_of_week[new_day])
else:
    print("Error days number")
#
# new_num = int(input("Input number: "))
new_num = 5
for i in range(1, 11):
    print(f"{new_num} x {i} = {new_num*i}")
#
sum_num = 0
num_list = [1, 2, 3, 4]
for i in num_list:
    sum_num += i
print(sum_num)
#
sum_num = 0
num_1 = 6
for i in range(1, num_1 + 1):
    sum_num += i
print(sum_num)
#
num_2 = 50
for i in range(1, num_2 + 1):
    if i // 10 == i % 10:
        print(i)
#
num_lst = [1, 50]
primes = []
for num in range(num_lst[0], num_lst[1] + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
print(primes)
