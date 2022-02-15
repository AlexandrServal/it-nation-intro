def make_abbr(words: str) -> str:

    abbr = ''
    for word in words.split():
        abbr += word[0]
    new_abbr = abbr.upper()
    return new_abbr
    pass
