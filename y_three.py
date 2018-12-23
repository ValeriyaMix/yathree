from collections import Counter


chisl = input('Vvedite chislo: ')
mas = list(map(int,input('Введите massiv ').split()))
if len(mas) == int(chisl):
    count_objects = Counter(mas)
    list_values = count_objects.values()
    counter_equal = 0
    for i in list_values:
        if i == 1:
            counter_equal += 1
    print(counter_equal)
else:
    raise ValueError(chisl, "elementa massiva nygno vvesti")

