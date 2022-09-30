q = input("Введите свое имя: ")
print("Привет, " + q)
lst = [99, 28, 29, 1, 10]
print("Изначальный список: ", lst)
for i in range(len(lst) - 1):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j+1]:
            x = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = x
print("Упорядоченный список: ", lst)


