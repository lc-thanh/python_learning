INP = open("./DATA.txt")
OUT = open("./OUTPUT_DATA.txt", "w")

# string = INP.read()
# strings = string.split(' ')
# for str in strings:
#     OUT.writelines([str, "\n"])

# dict1 = dict()
# dict1['a'] = 2003
# print('b' in dict1)
# print(dict1.get('a', 0))


words = dict()
line = input('Enter a line of text: ')
words = line.split()
count = dict()

print('Counting...')
for word in words:
    count[word] = count.get(word, 0) + 1

print('Count: ', count)

INP.close()
OUT.close()


def Test():
    pass


if __name__ == "__main__":
    Test()
    print('Done!')
