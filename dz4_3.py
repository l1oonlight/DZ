str = input()  # Строка
sll = str.lower()
for w in sll.split():  # пройтись по каждому слову
    if (w.startswith("а") or w.endswith("я")):  # Если слово начинается на букву а, или заканчивается на я
        print(w)  # ,то вывести его