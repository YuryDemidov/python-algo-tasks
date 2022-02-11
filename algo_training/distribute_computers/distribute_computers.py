reader = open('input.txt', 'r')


def remove_new_line(s):
    return s.rstrip()


data = list(map(remove_new_line, reader.readlines()))
reader.close()

dis = 0
groupsData = data[1].split(' ')
compsData = data[2].split(' ')
groups = []
comps = []

for i in range(len(groupsData)):
    groups.append({
        'i': i,
        'v': int(groupsData[i])
    })
for i in range(len(compsData)):
    comps.append({
        'i': i,
        'v': int(compsData[i]) - 1
    })
groups = sorted(groups, key=lambda x: x['v'], reverse=True)
comps = sorted(comps, key=lambda x: x['v'], reverse=True)

ans = ['0'] * len(groups)
gP = 0
cP = 0

while gP < len(groups) and cP < len(comps):
    if groups[gP]['v'] <= comps[cP]['v']:
        dis += 1
        ans[groups[gP]['i']] = str(comps[cP]['i'] + 1)
        cP += 1
    gP += 1

writer = open('output.txt', 'w')
writer.write(str(dis) + '\n' + ' '.join(ans))
writer.close()
