current_char = 'A'
current_num = 2

for i in range(5):
    if i % 2 == 0:
        for j in range(i + 1):
            print(current_char, end=" ")
            current_char = chr(ord(current_char) + 1)
    else:
        for j in range(i + 1):
            print(current_num, end=" ")
            current_num += 1
    print()
