import os
import random
import linecache

os.system('cls' if os.name == 'nt' else 'clear')

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
      word_for_guessing = desired_line[0]
   print(f"Отгадай загаданное слово. Что это может быть:{' '.join(text)}") 
   
   return word_for_guessing

def second_level():
   with open('words_medium.txt', 'r', encoding="utf-8") as file:
      line_number = random.randint(1,10)
      desired_line = linecache.getline('words_medium.txt', line_number).strip().split(":")
      text = desired_line[1:]
      word_for_guessing = desired_line[0]
   print(f"Отгадай загаданное слово. Что это может быть:{' '.join(text)}") 
   
   return word_for_guessing

def human_answers(word_for_guessing):
   letters_for_guessing = list(word_for_guessing)
   
   while word_for_guessing != str(letters_for_guessing):
      print("Введи букву загаданного слова") 
      letter = input()
      
   for i in range(0,len(letters_for_guessing)):
      if letter == letters_for_guessing[i]:
         with open('responses', 'r', encoding="utf-8") as file:
            desired_line2 = linecache.getline('responses.txt', 1).strip().split(":")
            text = desired_line2[1:]
            
   print(f"{' '.join(text)}")
      

if level == 1:
   first_level()
elif level == 2:
   second_level()
# if level == 3:
else:
   print("Введите крректные данные")