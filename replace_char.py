def replace_characters(lst = list, old = str, new = str):
    new_lst = []
    for word in lst:
        new_word = word.replace(old, new)
        new_lst.append(new_word)
    return new_lst
        

# Пример использования
test_list = ["hello", "world"]
old_char = "o"
new_char = "1"

result = replace_characters(test_list, old_char, new_char)
print("Результат:", result) 