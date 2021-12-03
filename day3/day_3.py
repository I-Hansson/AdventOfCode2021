
### Part 1 ###
lines = open('input.txt').read().splitlines()
print(lines)
gamma = ""
epsilon = ""

for x in zip(*lines):
    if x.count('0') > x.count('1'):
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
print(gamma)
print(epsilon)
g = int(gamma, 2)
e = int(epsilon, 2)

print(e*g)


####Part 2 ####
data = lines[:]
print(data)
for i in range(len(data[0])):
    bits = list(zip(*data))[i]
    print(bits)
    if len(data) == 1:
        break
    if bits.count('0') > bits.count('1'):
        data = [line
                for line in data if line[i] == '0']
    else:
        data = [line
                for line in data if line[i] == '1']
oxygen = data[0]
oxygen = int(oxygen, 2)


data = lines[:]
for i in range(len(data[0])):

    bits = list(zip(*data))[i]
    if len(data) == 1:
        break
    if bits.count('0') <= bits.count('1'):
        data = [line
                for line in data if line[i] == '0'
                ]
    else:
        data = [line
                for line in data if line[i] == '1']
co2 = data[0]
co2 = int(co2, 2)
print(co2*oxygen)