## Linus W. and River P.
## Exercise 10.3

file_name = input("Enter file: ")
if len(file_name) < 1 :
    file_name = "mbox-short.txt"
handle = open(file_name)

alphabet = 'abcdefghijklmnopqrstuvxwyz'

words = {}
for line in handle :
    line = line.rstrip()
    line = line.lower()
    for char in line :
        if char in alphabet :
            words[char] = words.get(char, 0) + 1

lst = []
for key, value in words.items() :
    temp = (value, key)
    lst.append(temp)

lst.sort(reverse = True)
for letter, freq in lst :
    print(letter, freq)