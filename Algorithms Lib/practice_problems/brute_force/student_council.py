# Super scuffed solution but it works LOL

pink_cost = int(input())
green_cost = int(input())
red_cost = int(input())
orange_cost = int(input())
target = int(input())
costs = {"green": green_cost, "pink": pink_cost, "red": red_cost, "orange": orange_cost}
counts_list = []
from math import inf
count = 0
best = inf

def recur(color, total_money, counts):
    global count
    global best
    global target
    total_money += costs[color]
    counts[color] += 1
    if total_money == target:
        if counts not in counts_list:
            count += 1
            print("# of PINK is " + str(counts["pink"]) + " # of GREEN is " + str(counts["green"]) + " # of RED is " + str(counts["red"]) + " # of ORANGE is " + str(counts["orange"]))
            if (counts["pink"] + counts["green"] + counts["red"] + counts["orange"]) < best:
                best = counts["pink"] + counts["green"] + counts["red"] + counts["orange"]
            counts_list.append(counts)
        return
    if total_money > target:
        return
    recur("pink", total_money, counts.copy())
    recur("green", total_money, counts.copy())
    recur("red", total_money, counts.copy())
    recur("orange", total_money, counts.copy())

recur("pink", 0, {"red": 0, "pink": 0, "green": 0, "orange": 0})
recur("green", 0, {"red": 0, "pink": 0, "green": 0, "orange": 0})
recur("red", 0, {"red": 0, "pink": 0, "green": 0, "orange": 0})
recur("orange", 0, {"red": 0, "pink": 0, "green": 0, "orange": 0})

print("Total combinations is " + str(count) + ".")
print("Minimum number of tickets to print is " + str(best) + ".")



