user_input = ''
output = ''
available_commands = ['plain',
                      'bold',
                      'italic',
                      'inline-code',
                      'link',
                      'header',
                      'unordered-list',
                      'ordered-list',
                      'new-line',
                      '!done',
                      '!help']

# list of functions to define markdown formats applied to user input

def _help():
    print('Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line')
    print('Special commands: !help !done')


def plain():
    plain_text = input('Text: ')
    return plain_text


def bold():
    bold_text = input('Text: ')
    return '**' + bold_text + '**'


def italic():
    italic_text = input('Text: ')
    return('*' + italic_text + '*')


def inline_code():
    inline_code = input('Text: ')
    return '`' + inline_code + '`'


def link():
    label = input('Label: ')
    url = input('URL: ')
    return '[' + label + ']' + '(' + url + ')'


def header():
    header = int(input('Level: '))
    while header not in range(1, 6):        # as there are only 6 levels of headers we enforce user to be in this range
        print('The level should be within the range of 1 to 6')
        header = int(input('Level: '))
    header_text = input('Text: ')
    return '#' * header + ' ' + header_text + '\n'


def new_line():
    return '\n'

def _list(list_type):       # both types of lists are handled in single function
    rows = ''
    number_of_rows = int(input('Number of rows: '))
    while number_of_rows <= 0:
        print('The number of rows should be greater than zero')
        number_of_rows = int(input('Number of rows: '))
    for i in range(1, number_of_rows + 1):
        row_prompt = 'Row #' + str(i) + ': '
        row = input(row_prompt)
        if list_type == 'ordered-list':
            rows += str(i) + '. ' + str(row) + '\n'
        elif list_type == 'unordered-list':
            rows += '* ' + str(row) + '\n'
    return rows

# main program

while user_input != '!done':
    user_input = input('Choose a formatter: ')
    if user_input in available_commands:
        if user_input == '!help':
            _help()
        elif user_input == 'plain':
            output += plain()
            print(output)
        elif user_input == 'bold':
            output = output + bold()
            print(output)
        elif user_input == 'italic':
            output += italic()
            print(output)
        elif user_input == 'inline-code':
            output += inline_code()
            print(output)
        elif user_input == 'link':
            output += link()
            print(output)
        elif user_input == 'header':
            output += header()
            print(output)
        elif user_input == 'new-line':
            output += new_line()
            print(output)
        elif user_input == 'ordered-list' or user_input == 'unordered-list':
            output += _list(user_input)
            print(output)
    else:
        print('Unknown formatting type or command. Please try again.')

#save foratted text in a file upon calling !done command

file = open('output.md', 'w', encoding='utf-8')
file.write(output)
file.close()
