if __name__ == '__main__':
    birthdays = {
        'Peter Ginsberg': '04/15/1981',
        'Daylon Kinsinger': '01/17/1969',
        'Griffin Matherly': '09/21/2000',
        'Adam Gontier': '07/14/1979',
        'Dustin Bates': '02/23/1972'}

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)
    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))