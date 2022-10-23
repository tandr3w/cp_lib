n = int(input())
pieces = list(map(int, input().split()))

board_frequencies = [0] * 2002
for i in pieces:
    board_frequencies[i] += 1

board_lengths = [0] * 10000
lengths = list(set(pieces))

if len(lengths) == 1:
    print(*[len(pieces)//2, 1])
else:
    for i in range(len(lengths)):
        for j in range(i, len(lengths)):
            if j != i:
                board_lengths[lengths[i] + lengths[n]] += min(board_frequencies[lengths[i]], board_frequencies[lengths[j]])
            if j == i and board_frequencies[i] >= 2:
                board_lengths[lengths[i] + lengths[n]] += board_frequencies[lengths[i]]//2
    print(*[max(board_lengths), board_lengths.count(max(board_lengths))])