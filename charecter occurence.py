string = input('enter a string to chek the occurence:').lower()
letter = input('enter a letter to find the count:').lower()

count = 0 

for i in string:
    if i == letter:
        count = count + 1

print('Total count found:' , count)