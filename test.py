# q\dr\d
# eq2r35q24q6r1gq8r3

# qw\drt\d
# qw2rt3qw4ert5qw6rt7gqw8rt9

# \d\d/\d\d
# qw26/2358e389/25e


def test():
    regex = '\d\d/\d\d'
    text = 'qw26/2358e389/25e'

    if not regex:
        print("Ошибка: Введите регулярное выражение")
        return

    if not text:
        print("Ошибка: Введите текст для поиска")
        return

    nums_index = []
    start = 0

    while True:
        index = regex.find(r"\d", start)
        if index == -1:
            break
        nums_index.append(index)
        start = index + 1

    new_regex = regex.replace(r"\d", "#")

    new_text = ''
    for i in range(len(text)):
        if text[i] not in "0123456789":
            new_text += text[i]
        else:
            new_text += "#"

    found_indices = []
    start = 0

    while True:
        index = new_text.find(new_regex, start)
        if index == -1:
            break
        found_indices.append((index, index + len(new_regex)))
        start = index + 1


test()