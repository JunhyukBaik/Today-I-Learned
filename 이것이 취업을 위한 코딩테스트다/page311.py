#page311 Q01
group_num = 0
N = int(input())
fears = list(map(int, input().split()))
#print(fears)
fears.sort(reverse=True)
#print(fears)
for i in range(N):
    group = list()
    mx = fears[i]
    group.append(fears[i:i+mx])
    if i+mx < N:
        group.append(fears[i+mx:])
    gr_len = len(group)
    if gr_len > group_num:
        group_num = gr_len
print(group_num)

#input ex)
#5
#2 3 1 2 2

#output ex)
#2
