import re

pattern = input("Введіть регулярний вираз: ")

try:
    regex = re.compile(pattern)
    print("Регулярний вираз правильний!")

    text = input("Введіть текст: ")
    result = regex.findall(text)

    print("Знайдені збіги:", result)

except re.error:
    print("Помилка: регулярний вираз має некоректний синтаксис.")