
protein = float(input("Введите массу белков (г): "))
fat = float(input("Введите массу жиров (г): "))
carb = float(input("Введите массу углеводов (г): "))
calories = (protein * 4) + (fat * 9) + (carb * 4)
print(f"Общая калорийность продукта: {calories} ккал")