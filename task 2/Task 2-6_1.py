 
try:
    
    pH = float(input("Введите значение pH (от 0 до 14): "))
    
    
    if pH < 0 or pH > 14:
        print("Ошибка: pH должно быть в диапазоне от 0 до 14")
    else:
        
        if pH < 7:
            print("Кислая среда")
        elif pH > 7:
            print("Щелочная среда")
        else:  # pH == 7
            print("Нейтральная среда")
            
except ValueError:
    print("Ошибка: Введите корректное число")