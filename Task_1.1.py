# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input('Введите текст: ')   # Вводим текст
blocked_letters = ['а', 'б', 'в']   # Выделяем элементы, которые нельзя использовать
text = text.split()   # Разъединяем текс
text1 = []   # Создаем новый список

for word in text:
    add = True
    for letter in blocked_letters:
        if letter in word:
            add = False
    if add:
        text1.append(word)
        text1.append(' ')
result = ''.join(text1)
print(result)
