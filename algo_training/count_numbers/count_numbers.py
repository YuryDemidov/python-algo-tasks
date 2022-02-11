reader = open('input.txt', 'r')


def remove_new_line(s):
    return s.rstrip()


data = list(map(remove_new_line, reader.readlines()))
reader.close()

ans = list()
results = {}

for i in range(1, int(data[0]) + 1):
    num, count = data[i].split(' ')
    if num in results:
        results[num] = results[num] + int(count)
    else:
        results[num] = int(count)

sortedRes = sorted(map(int, sorted(results.keys())))

writer = open('output.txt', 'w')
for i in range(len(sortedRes)):
    writer.write(str(sortedRes[i]) + ' ' + str(results[str(sortedRes[i])]) + '\n')
writer.close()
