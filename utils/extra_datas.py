escape_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']


def make_title(title):
    name = ""
    for letter in title:
        if letter in escape_chars:
            name += f'\{letter}'
        else:
            name += letter
    return name
