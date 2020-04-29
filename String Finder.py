word = "Pranav" #word you want to search for the target phrase

word = word.lower()

target = "pranav" #target phrase you want to find within the word

target = target.lower()

new_target = target[::-1]

found = True

in_loop = 0

for index,char in enumerate(word):
    if char == new_target[0]:
        in_loop += 1
        for x in range(0, len(new_target)):
            if new_target[x] == word[index-x]:
                if found == False:
                    found = False
                else:
                    found = True
            else:
                found = False
    


if found == True and in_loop > 0:
    print("Target was found within string")
else:
    print("Target wasn't found within string")
            
            
            
