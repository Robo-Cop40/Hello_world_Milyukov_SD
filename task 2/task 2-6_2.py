donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()


recipient = input("Введите группу крови пациента (I, II, III, IV): ").strip().upper()


valid_groups = ["I", "II", "III", "IV"]

if donor not in valid_groups or recipient not in valid_groups:
    print("Ошибка: Введена некорректная группа крови")
else:
    
    if donor == recipient or donor == "I":
        print(f"Переливание крови группы {donor} пациенту с группой {recipient} ВОЗМОЖНО")
    else:
        print(f"Переливание крови группы {donor} пациенту с группой {recipient} НЕВОЗМОЖНО")