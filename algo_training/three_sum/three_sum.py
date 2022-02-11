reader = open('threesum.in', 'r')
data = list(map(str.rstrip, reader.readlines()))
reader.close()

target, A1, A2, A3 = data
target = int(target)
A1 = list(map(int, A1.strip().split()[1:]))
A2 = list(map(int, A2.strip().split()[1:]))
A3 = list(map(int, A3.strip().split()[1:]))
A1.sort()
A2.sort()

reminders = {}
for k in range(len(A3)):
    reminders[A3[k]] = reminders.get(A3[k], k)
print(reminders)
hasAns = False
for i in range(len(A1)):
    for j in range(len(A2)):
        reminder = target - A1[i] - A2[j]
        if reminder in reminders:
            hasAns = True
            print(str(i) + ' ' + str(j) + ' ' + str(reminders[reminder]))
            break
    if hasAns:
        break
if not hasAns:
    print('-1')
