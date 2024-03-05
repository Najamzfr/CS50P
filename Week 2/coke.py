#coin = int(input("Insert Coin: "))
due = 50

while due != 0:
    coin = int(input("Insert Coin: "))
    if coin in [25, 10, 5]:
        if due != 0:
            due = due-coin
            if due <= 0:
                print('Change Owed:', abs(due))
                break
            else:
                print('Amount Due:', due)
        else:
            print('Change Owed:', due)
            break
    elif coin not in [25, 10, 5]:
        print('Amount Due:', due)
        continue


