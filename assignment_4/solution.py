# create dictionary with key as the name of person and age as value

birthday_dict = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
}

print('Welcome to the birthday dictionary. We know the birthdays of:\nAlbert Einstein\nBenjamin Franklin\nAda Lovelace ')

name = input('Who\'s birthday do you want to look up?: ')

for key in birthday_dict:
    if name in key:
        print(key + '\'s birthday is ' + birthday_dict[key])
