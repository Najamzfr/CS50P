camel = input('Camelcase : ')
snake = []
for c in camel:
    if c.isupper():
        snake = snake + ['_',c.lower()]
    else:
        snake = snake + [c]
snake = ''.join(snake)
print('snake_case : ',snake)

