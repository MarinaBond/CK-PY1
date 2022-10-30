def get_count_char(str_):
    dict_x = {}
    str_ = "".join(str_.split())
    str_ = str_.lower()
    for symbol in str_:
        if symbol.isalpha():
            if symbol in dict_x:
                dict_x[symbol] += 1
            else:
                dict_x[symbol] = 1
    return dict_x

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
