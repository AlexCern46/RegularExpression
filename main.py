import tkinter as tk


def find_regex():
    result_text.delete("1.0", tk.END)
    regex = regex_entry.get()
    text = text_entry.get()

    if not regex:
        result_text.insert("1.0", "Ошибка: Введите регулярное выражение")
        return

    if not text:
        result_text.insert("1.0", "Ошибка: Введите текст для поиска")
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

    if found_indices:
        result_text.insert("1.0", text)
        for start, end in found_indices:
            flag = True
            for i in range(len(nums_index)):
                if text[start + nums_index[i] - i] not in "0123456789":
                    flag = False
            if flag:
                result_text.tag_add("found", f"1.{start}", f"1.{end}")
        result_text.tag_config("found", background="yellow")
    else:
        result_text.insert("1.0", "Совпадений не найдено")


root = tk.Tk()
root.title("Поиск регулярного выражения")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

regex_label = tk.Label(frame, text="Регулярное выражение:", font="Arial 12")
regex_label.grid(row=0, column=0, sticky="w")

regex_entry = tk.Entry(frame, font="Arial 12")
regex_entry.grid(row=0, column=1, padx=5)

text_label = tk.Label(frame, text="Текст для поиска:", font="Arial 12")
text_label.grid(row=1, column=0, sticky="w")

text_entry = tk.Entry(frame, font="Arial 12")
text_entry.grid(row=1, column=1, padx=5)

search_button = tk.Button(frame, text="Искать", font="Arial 12", command=find_regex)
search_button.grid(row=2, columnspan=2, pady=10)

result_text = tk.Text(root, height=5, width=30, font="Arial 12")
result_text.pack(padx=10, pady=10)

root.mainloop()
