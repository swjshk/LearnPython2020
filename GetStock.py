f = open("stock1.txt", 'r')

#combine the line to a record
record_list = ['']
i = 0
for line in f:
    if line == '\n':
        record_list.append('')
        i += 1
    else:
        record_list[i] += line

for record in record_list:
    print(record)

print(i)
