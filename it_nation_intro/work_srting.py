def get_string_length(string: str) -> int:
    print(len(string)) #длинна строки
    return len(string)
    pass


def remove_vowels(document: str) -> str:

    document = document.replace('a', '') # удаление символа
    document = document.replace('e', '')
    document = document.replace('i', '')
    document = document.replace('o', '')
    document = document.replace('u', '')
    document = document.replace('y', '')
    document = document.replace('A', '')
    document = document.replace('E', '')
    document = document.replace('I', '')
    document = document.replace('O', '')
    document = document.replace('U', '')
    document = document.replace('Y', '')
    return document
    pass
