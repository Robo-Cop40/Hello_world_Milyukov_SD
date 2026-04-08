n = int(input("Введите количество элементов: "))
A = []

for i in range(n):
    A.append(int(input(f"Введите элемент {i}: ")))

сумма = 0
i = 0
while i < n:
    if A[i] % 2 != 0:
        сумма = сумма + A[i]
    i = i + 1

print("Сумма нечётных элементов =", сумма)