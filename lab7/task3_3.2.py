data = open ("input.txt","r").readlines()
output = open("ouput.txt","w")

for line in data:
    output.write(line.upper())

print("Processing done")