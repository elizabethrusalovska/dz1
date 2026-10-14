class EmptyTextError(Exception):
    pass


def analyze_text(text):
    if not isinstance(text, str):
        raise TypeError("Це не текст!")

    if text == "":
        raise EmptyTextError("Текст порожній!")

    return len(text)


text = input("Введіть текст: ")

try:
    result = analyze_text(text)
    print("Кількість символів:", result)
except EmptyTextError as e:
    print(e)
except TypeError as e:
    print(e)