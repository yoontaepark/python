han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    # print('Line:', line) : 에러찾을때 해당 앞라인들에다 print 걸어보기
    wds = line.split()
    # print('Words') : 마찬가지로 print 걸어보기

    #Guardian statement: 선 필터를 걸만한 수식을 건다. 이 경우 문자열 길이로 제어
    #if len(wds) < 3:
    #    continue
    #if wds[0] != 'From':
    #    continue

    #Guardian in a compount statement: 이렇게 병렬로 걸수도 있는데, gurdian이 먼저가야 에러가 안남
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
