reader = open('input.txt', 'r')


def remove_new_line(s):
    return s.rstrip()


data = list(map(remove_new_line, reader.readlines()))
reader.close()

max_number = int(data[0])
possible = set()
for i in range(1, max_number + 1):
    possible.add(i)

current_try = list()
for i in range(1, len(data)):
    if data[i] != 'YES' and data[i] != 'NO' and data[i] != 'HELP':
        current_try = data[i].split(' ')
        continue

    if data[i] == 'YES':
        joined_possible = set()
        for k in range(len(current_try)):
            if int(current_try[k]) in possible:
                joined_possible.add(int(current_try[k]))
        possible = joined_possible
    elif data[i] == 'NO':
        for m in range(len(current_try)):
            possible.discard(int(current_try[m]))
    else:
        result = list(possible)
        result.sort()
        writer = open('output.txt', 'w')
        writer.write(' '.join([str(item) for item in result]))
        writer.close()
