def is_palindrome(string: str) -> bool:
    new_string = string
    new_string = new_string[::-1] # переворот строки
    if new_string == string:
        return True
    else:
        return False