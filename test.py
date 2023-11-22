# q\dr\d
# eq2r35q24q6r1gq8r3

# qw\drt\d
# qw2rt3qw4ert5qw6rt7gqw8rt9

# \d\d/\d\d
# qw26/2358e389/25e

# \D2\d
# r2342tge22


def test():
    regex = '\D2\d\D'
    text = 'r2342tge22R'

    nums_index = []
    start = 0

    regex_d = regex.replace(r"\D", "@")
    while True:
        index = regex_d.find(r"\d", start)
        if index == -1:
            break
        nums_index.append(index)
        start = index + 1

    not_nums_index = []
    start = 0

    regex_D = regex.replace(r"\d", "#")
    while True:
        index = regex_D.find(r"\D", start)
        if index == -1:
            break
        not_nums_index.append(index)
        start = index + 1

    new_regex = regex.replace(r"\d", "#")
    new_regex = new_regex.replace(r"\D", "@")

    not_regex = []

    for i in range(len(new_regex)):
        if new_regex[i] != "@" and new_regex[i] != "#":
            not_regex.append((i, new_regex[i]))
            if new_regex[i] in "0123456789":
                new_regex = new_regex.replace(new_regex[i], "#")
            else:
                new_regex = new_regex.replace(new_regex[i], "@")

    new_text = ''
    for i in range(len(text)):
        if text[i] not in "0123456789":
            new_text += '@'
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

    if found_indices:
        for start, end in found_indices:
            flag = True
            for i in range(len(nums_index)):
                if text[start + nums_index[i] - i] not in "0123456789":
                    flag = False
            for i in range(len(not_nums_index)):
                if text[start + not_nums_index[i] - i] in "0123456789":
                    flag = False
            for i in range(len(not_regex)):
                if text[start + not_regex[i][0]] != not_regex[i][1]:
                    flag = False
            if flag:
                print(text[start:end])
    else:
        print("Совпадений не найдено")


test()
