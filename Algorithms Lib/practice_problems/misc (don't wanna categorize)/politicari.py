n, k = map(int, input().split())
poli_list = [[0, 0, 0]]
for i in range(n):
    poli_list.append([0] + list(map(int, input().split())))



# n = 2
# k = 1000
# poli_list = [[0, 0, 0], [0]+[0, 2], [0]+[1, 0]]


states = {}

day_num = 2
curr_state = (2, 1) # curr politician, politician that blamed them
if k == 1:
    print(1)
elif k == 2:
    print(2)
else:
    while True:
        # Check for cycles
        if curr_state in states:
            k = (k-(states[curr_state])) % (day_num - states[curr_state])
            print(list(states.keys())[k + (states[curr_state]-2)][0])
            break

        states[curr_state] = day_num

        # Next day
        day_num += 1
        curr_state = poli_list[curr_state[0]][curr_state[1]], curr_state[0] 
        if day_num == k:
            print(curr_state[0])
            break


