import os
import random
import linecache
from termcolor import colored



if os.name == 'nt':

    os.system('') 

print("Добро пожаловать в игру")


print("Введи своё имя")
player_name = input()

print(f"Приветствую тебя, {player_name}")

print(f"Теперь, {player_name}, выбери уровень сложности.")

print(f"Для этого введи одну из 3х цифр: 1, 2, 3. 1 - лёгкий уровень, 2 - средний, 3 - сложный")

level = int(input())


def first_level():
   with open('words_easy.txt', 'r', encoding="utf-8") as file:
      line_number = random.randint(1,5)
      desired_line = linecache.getline('words_easy.txt', line_number).strip().split(":")
      text = desired_line[1:]
      word_for_guessing1 = desired_line[0]
      lengt_of_word_for_guessing1 = len(list(word_for_guessing1))
   print(f"Отгадай загаданное слово. Что это может быть:{' '.join(text)}") 
   
   return word_for_guessing1,lengt_of_word_for_guessing1

def second_level():
   with open('words_medium.txt', 'r', encoding="utf-8") as file:
      line_number = random.randint(1,10)
      desired_line = linecache.getline('words_medium.txt', line_number).strip().split(":")
      text = desired_line[1:]
      word_for_guessing2 = desired_line[0]
      lengt_of_word_for_guessing2 = len(list(word_for_guessing2))
   print(f"Отгадай загаданное слово. Что это может быть:{' '.join(text)}") 
   
   return word_for_guessing2,lengt_of_word_for_guessing2


def trird_level():
   with open('words_hard.txt', 'r', encoding="utf-8") as file:
      line_number = random.randint(1,10)
      desired_line = linecache.getline('words_medium.txt', line_number).strip().split(":")
      text = desired_line[1:]
      word_for_guessing3 = desired_line[0]
      lengt_of_word_for_guessing3 = len(list(word_for_guessing3))
   print(f"Отгадай загаданное слово. Что это может быть:{' '.join(text)}") 
   
   return word_for_guessing3,lengt_of_word_for_guessing3

# Загружаем стадии из файла один раз
def load_hangman_stages(filename="hangman_stages.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    
    stages = content.strip().split("\n\n")  
    return stages

hangman_stages = load_hangman_stages()


def update_hangman_file(line_number, new_content, filename="hangman_stages.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()


    if line_number < len(lines):
        lines[line_number] = new_content
    else:
        while len(lines) <= line_number:
            lines.append("\n")
        lines[line_number] = new_content

    # Перезаписываем файл
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)


def human_answers(word_for_guessing, length_of_word_for_guessing):
    word_letters = list(word_for_guessing)
    guessed_letters = ["_"] * len(word_letters)
    max_attempts = length_of_word_for_guessing + 5
    attempt_count = 0
    used_letters = [] 

    print(f"\nСлово: {' '.join([colored('_', 'red')])}")

    while True:
        # --- Отображение состояния игры ---
        # Цветное отображение: угаданные буквы - зелёные, неугаданные - красные [[6]]
        colored_word = [
            colored(char, 'green') if char != '_' else colored('_', 'red') 
            for char in guessed_letters
        ]
        print(f"\nСлово: {' '.join(colored_word)}")
        print(f"Использованные буквы: {', '.join(used_letters)}")  # Отображение списка букв [[4]]

        # --- Обновление виселицы ---
        if attempt_count == 1:
            update_hangman_file(4, " O\n")
        elif attempt_count == 2:
            update_hangman_file(5, " |\n")
        elif attempt_count == 3:
            update_hangman_file(6, "/|\ \n")
        elif attempt_count == 4:
            update_hangman_file(7, " | \n")
        elif attempt_count == 5:
            update_hangman_file(8, "/ \ \n")
        elif attempt_count == 6:
            update_hangman_file(9, "  \n")
        elif attempt_count == 7:
            update_hangman_file(10, "   \n")

        # --- Вывод виселицы с цветом ---
        try:
            with open("hangman_stages.txt", "r", encoding="utf-8") as file:
                hangman_display = file.read()
                color = 'red' if attempt_count <= 2 else 'yellow' if attempt_count <= 4 else 'green'
                print(colored("\nТекущая стадия виселицы:\n" + hangman_display, color))
        except FileNotFoundError:
            print("Файл с виселицей не найден.")

        # --- Ввод буквы с валидацией ---
        print("\nВведи букву:")
        letter = input().strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue
        if letter in used_letters:
            print("Эта буква уже использовалась.")
            continue
        used_letters.append(letter)

        # --- Основная логика угадывания ---
        found = False
        for i in range(len(word_letters)):
            if word_letters[i] == letter and guessed_letters[i] == "_":
                guessed_letters[i] = letter
                found = True

        # --- Ответ на попытку ---
        if found:
            with open('responses.txt', 'r', encoding="utf-8") as file:
                desired_line2 = linecache.getline('responses.txt', 1).strip().split(":")
                text = desired_line2[1:]
                print(colored(f"{' '.join(text)}\n", 'green'))
        else:
            attempt_count += 1
            with open('responses.txt', 'r', encoding="utf-8") as file:
                desired_line2 = linecache.getline('responses.txt', 2).strip().split(":")
                text = desired_line2[1:]
                print(colored(f"{' '.join(text)}\n", 'red'))

        # --- Проверка окончания игры ---
        if attempt_count >= max_attempts:
            with open('responses.txt', 'r', encoding="utf-8") as file:
                desired_line2 = linecache.getline('responses.txt', 5).strip().split(":")
                text = desired_line2[1:]
                print(f"{' '.join(text)}")
                print(f"Загаданное слово: {word_for_guessing}")
            break
        if "_" not in guessed_letters:
            with open('responses.txt', 'r', encoding="utf-8") as file:
                desired_line2 = linecache.getline('responses.txt', 4).strip().split(":")
                text = desired_line2[1:]
                print(f"{' '.join(text)}")
            break

        os.system('cls' if os.name == 'nt' else 'clear')
        
       

if level == 1:
   word_for_guessing_level_1,lengt_of_word_for_guessing_level_1 = first_level()
   human_answers(word_for_guessing_level_1,lengt_of_word_for_guessing_level_1)
elif level == 2:
   word_for_guessing_level_2,lengt_of_word_for_guessing_level_2 = second_level()
   human_answers(word_for_guessing_level_2,lengt_of_word_for_guessing_level_2)
elif level == 3:
    word_for_guessing_level_3,lengt_of_word_for_guessing_level_3 = trird_level()
    human_answers(word_for_guessing_level_3,lengt_of_word_for_guessing_level_3)
else:
   print("Введите корректные данные")
   

   
