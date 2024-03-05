# create a dictionary
grocery = {}
# create a loop

while True :
    try:
        # take input from user
        item = input()
        #check if the item is in dict if yes add 1 to its value
        if item in grocery:
            grocery[item] += 1
        #else add the item to dict
        else:
            grocery[item] = 1

    except EOFError:
        #print all the item in grammatical oder
        for key in sorted(grocery.keys()):
            print(grocery[key],key.upper())

        # break the loop
        break
