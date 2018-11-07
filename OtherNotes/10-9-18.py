'''         wordplay.py         '''

fin = open("words.txt")

'''
line = fin.readline()
print(line)
'''

'''
for _ in range(10):
    line = fin.readline()
    line = line.strip()
    print(line)
'''


'''
for line in fin:
    if 'e' not in line:
        print(line.strip())
'''

'''
def avoid(string, undesirables):
    for letter in undesirables:
        if letter in string:
            return True
    return False

b = avoid("yellow", "abcdef")
print(b)
'''

'''
def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

c = is_abecedarian("abcdea")
print(c)
'''

for line in fin:
    print(line.strip()[::-1])
