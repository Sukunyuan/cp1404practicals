input_file = open('name.txt', 'w')
input_file.write('Your name is Bob')
input_file.close()
output_file = open('name.txt', 'r')
print(output_file.read())
output_file.close()
open_file = open('numbers.txt', 'r')
total = 0
for number in open_file:
    total += float(number)
print("Total: {}".format(total))
open_file.close()
