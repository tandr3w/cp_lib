# Note: i hate this problem

n = int(input())
pieces = list(map(int, input().split()))

board_frequencies = [0] * 2002
for i in pieces:
    board_frequencies[i] += 1

board_lengths = [0] * 4004
lengths = list(set(pieces))

if len(lengths) == 1:
    print(*[int(len(pieces)/2), 1])
else:
    for i in range(len(lengths)):
        for k in range(i, len(lengths)):
            if k != i:
                board_lengths[lengths[i] + lengths[k]] += min(board_frequencies[lengths[i]], board_frequencies[lengths[k]])
            if k == i and board_frequencies[i+1] >= 2:
                board_lengths[lengths[i] + lengths[k]] += board_frequencies[lengths[i]]//2
    print(*[max(board_lengths), board_lengths.count(max(board_lengths))])