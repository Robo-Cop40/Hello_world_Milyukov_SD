print("=== Анализ последовательности ДНК ===\n")


dna = input("Введите последовательность ДНК: ").upper()

print(f"\nПоследовательность в верхнем регистре: {dna}\n")


count_A = dna.count("A")
count_T = dna.count("T")
count_G = dna.count("G")
count_C = dna.count("C")


total_length = len(dna)


print("Подсчёт нуклеотидов:")
print(f"A: {count_A}")
print(f"T: {count_T}")
print(f"G: {count_G}")
print(f"C: {count_C}")


print(f"\nОбщая длина: {total_length} нуклеотидов")


if total_length > 0:
    print(f"\nПроцентное содержание нуклеотидов:")
    print(f"A: {(count_A / total_length * 100):.1f}%")
    print(f"T: {(count_T / total_length * 100):.1f}%")
    print(f"G: {(count_G / total_length * 100):.1f}%")
    print(f"C: {(count_C / total_length * 100):.1f}%")
else:
    print("\nПоследовательность пуста, невозможно рассчитать процентное содержание")