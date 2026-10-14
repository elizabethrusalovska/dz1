try:
    with open("text55.txt", "r", encoding="utf-8") as file:
        text = file.read()

    print("Вміст файлу:")
    print(text)

    print("Кількість символів:", len(text))
    print("Кількість слів:", len(text.split()))
    print("Кількість рядків:", len(text.splitlines()))

except FileNotFoundError:
    print("Помилка: файл не знайдено!")

except PermissionError:
    print("Помилка: немає дозволу на читання файлу!")

except UnicodeDecodeError:
    print("Помилка: не вдалося прочитати текст у кодуванні UTF-8!")