# coding=utf-8

def bubble_sort(arr, ascending=True):
	"""Bubble Sorting"""

	n = len(arr)
	for i in range(n):
		for j in range(0, n - i - 1):
			if ascending:
				flag = arr[j] > arr[j + 1]
			else:
				flag = arr[j] < arr[j + 1]
			if flag:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

	return arr


def insertion_sort(arr, ascending=True):
	"""Insertion Sorting"""

	for i in range(1, len(arr)):
		selection = arr[i]
		j = i - 1
		while j >= 0:
			if ascending:
				flag = selection < arr[j]
			else:
				flag = selection > arr[j]
			if flag:
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = selection

	return arr


def merge_sort(arr, ascending=True):
	"""Merge Sorting"""

	n = len(arr)
	if n <= 1:
		return arr
	m = n // 2

	left = merge_sort(arr[:m], ascending=ascending)
	right = merge_sort(arr[m:], ascending=ascending)

	# merge
	left_i, right_i = 0, 0
	new_arr = []
	while left_i < len(left) and right_i < len(right):
		if ascending:
			flag = left[left_i] < right[right_i]
		else:
			flag = left[left_i] > right[right_i]
		if flag:
			new_arr.append(left[left_i])
			left_i += 1
		else:
			new_arr.append(right[right_i])
			right_i += 1
	new_arr.extend(left[left_i:])
	new_arr.extend(right[right_i:])

	return new_arr


# example
arr = [2, 1, 3, 5, 4, 7, 9, 8, 6, 12, 30, 15, 29, 28, 24, 20]

print("bubble_sort ascending: \n", bubble_sort(arr, ascending=True))
print("bubble_sort decending: \n", bubble_sort(arr, ascending=False))

print("insertion_sort ascending: \n", insertion_sort(arr, ascending=True))
print("insertion_sort decending: \n", insertion_sort(arr, ascending=False))

print("merge_sort ascending: \n", merge_sort(arr, ascending=True))
print("merge_sort decending: \n", merge_sort(arr, ascending=False))
