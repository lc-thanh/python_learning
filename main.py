# INP = open("./DATA.txt")
# OUT = open("./OUTPUT_DATA.txt", "w")

# string = INP.read()
# strings = string.split(' ')
# for str in strings:
#     OUT.writelines([str, "\n"])

# dict1 = dict()
# dict1['a'] = 2003
# print('b' in dict1)
# print(dict1.get('a', 0))


# words = dict()
# line = input('Enter a line of text: ')
# words = line.rstrip().split()
# count = dict()
#
# print('Counting...')
# for word in words:
#     count[word] = count.get(word, 0) + 1
#
# print('Count: ', count)


def maxWordCount(input_file: str, output_file: str):
    """
    Hàm đếm số lượng xuất hiện của mỗi từ trong file 'input_file' và
    đưa ra từ (hoặc các từ) có số lượng xuất hiện nhiều nhất vào file 'output_file'
    theo format "<Từ> <Số lượng>"
    :param input_file: File đầu vào
    :param output_file: File đầu ra
    :return: True, nếu thực thi thành công | False, nếu không thành công
    """

    INP = open(input_file)
    OUT = open(output_file, "w")

    # Đọc từng dòng dữ liệu trong file INP và tách ra từng chữ (words)
    # và đếm số lần xuất hiện của từng chữ đó
    counts = dict()
    for line in INP:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    # Tìm số lần xuất hiện lớn nhất
    maxCount = None
    for count in counts.values():
        if maxCount is None or count > maxCount:
            maxCount = count

    # Ghi kết quả vào file OUT theo format: "word maxCount"
    for word, count in counts.items():
        if count == maxCount:
            OUT.write(str(word))
            OUT.write(' ')
            OUT.write(str(count))
            OUT.write('\n')

    INP.close()
    OUT.close()


def Test():
    maxWordCount("DATA.txt", "OUTPUT_DATA.txt")


if __name__ == "__main__":
    Test()
    print('Done!')
