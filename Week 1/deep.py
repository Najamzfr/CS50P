x = input('What is the Answer to the Great Question of life, Universe and Everything? ').lower().strip()

def deep(x):
    if x == '42':
        print('Yes')
    elif x == 'forty two':
        print('Yes')
    elif x == 'forty-two':
        print('Yes')
    elif x == 'Forty-two':
        print('Yes')
    else:
        print('No')

deep(x)
