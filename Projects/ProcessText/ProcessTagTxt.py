reader = open("ORDER.1.txt")
# a=list(reader)
newlines = []
for line in reader:
    line1 = line[2:55] + "\n"
    # print(line1)
    newlines.append(line1)
print(newlines)

newfile = open("TAGINFO.txt", "w")


for nline in newlines:
    newfile.write(nline)
    print(nline, end="")

reader.close()
newfile.close()
