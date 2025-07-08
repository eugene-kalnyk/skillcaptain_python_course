file = open('numbers.txt', "w")

for num in range (1,11):
    file.write(str(num) + '\n')

file.close()