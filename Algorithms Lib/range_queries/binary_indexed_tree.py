# Lets you range sum query and update a value in O(log n)
# Worse time complexity than PSA but can update values in between sum queries, which PSA can only do in O(n)
# Each element k stores the sum of the element and the previous p(k)-1 elements, where p(k) is the largest power of two that divides k. Then, you can divide each range into log(n) ranges. 
# Sum can be calculated similarly to a PSA: sum(a, b) = sum(1, b) - sum(1, a-1) 
# When updating, you only need to update log(n) values, since each element only belongs to that many ranges.

# Code plagarised from https://gist.github.com/rajatdiptabiswas/79fc1ce5cf410df4139b291f75bf0794

def update(index, value, array, bi_tree):
	while index < len(array):
		bi_tree[index] += value
		index += index & -index

def get_sum(index, bi_tree):
	ans = 0
	while index > 0:
		ans += bi_tree[index]
		index -= index & -index
	return ans

def get_range_sum(left, right, bi_tree):
	ans = get_sum(right, bi_tree) - get_sum(left - 1, bi_tree)
	return ans

arr = [1, 5, 4, 7, 4, 6, 3]
n = len(arr)
arr.insert(0, 0)
tree = [0 for i in range(n+1)]

for index in range(1, n+1):
    update(index, arr[index], arr, tree)

# print(get_range_sum(leftIndex, rightIndex, tree))
# update(index, new_value - arr[index], arr, tree)	

