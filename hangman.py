import os

os.system('cls' if os.name == 'nt' else 'clear')

print("Добро пожаловать в игру")


print("Введи своё имя")
player_name = input()

print(f"Приветствую тебя, {player_name}")

print(f"Теперь, {player_name}, выбери уровень сложности.")

print(f" Для этого введи одну из 3х цифр: 1, 2, 3. 1 - лёгкий уровень, 2 - средний, 3 - сложный")

level = int(input())

# if level == 1:
    
