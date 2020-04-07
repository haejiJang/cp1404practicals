out_file = open("name.txt", 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", 'r')
name = in_file.read().strip()
in_file.close()
print("Your name is ", name)

number_file = open("numbers.txt", 'r')
line1 = int(number_file.readline())
line2 = int(number_file.readline())
number_file.close()
print(line1+line2)

number_file = open("numbers.txt", 'r')
total = 0
for line in number_file:
    number = int(line)
    total += number
in_file.close()
print(total)