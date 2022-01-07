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
			else:
				break
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


def selection_sort(arr, ascending=True):
	"""Selection Sorting"""

	n = len(arr)
	k = 1
	for i in range(0, n):
		min = i
		for j in range(i + 1, n):
			if ascending:
				flag = arr[i] > arr[j]
			else:
				flag = arr[i] < arr[j]
			if flag:
				min = j
		arr[i], arr[min] = arr[min], arr[i]

	return arr


def counting_sort(arr, ascending=True):
	"""Counting Sorting"""

	max_len = max(arr)
	c = [0] * (max_len + 1)
	for i in arr:
		c[i] += 1
	arr = []
	if ascending:
		iters = range(max_len + 1)
	else:
		iters = range(max_len, -1, -1)
	for j in iters:
		if c[j] == 0:
			continue
		arr.extend([j] * c[j])

	return arr


def radix_sort_lsd(arr, ascending=True):
	"""Radix Sorting-LSD"""

	max_len = len(str(arr))
	for i in range(1, max_len + 1):
		bucket = {k:[] for k in range(10)}
		# append into bucket
		for x in arr:
			try:
				k = int(str(x)[-i])
			except:
				k = 0
			bucket[k].append(x)
		# pick out of bucket
		arr = []
		if ascending:
			iters = range(10)
		else:
			iters = range(9, -1, -1)
		for i in iters:
			arr.extend(bucket[i])

	return arr



if __name__ == '__main__':

	# example
	arr = [2, 1, 3, 5, 4, 7, 9, 9, 8, 6, 12, 30, 15, 29, 28, 24, 20, 25, 25]

	print("bubble_sort ascending: \n", bubble_sort(arr, ascending=True))
	print("bubble_sort decending: \n", bubble_sort(arr, ascending=False))

	print("insertion_sort ascending: \n", insertion_sort(arr, ascending=True))
	print("insertion_sort decending: \n", insertion_sort(arr, ascending=False))

	print("merge_sort ascending: \n", merge_sort(arr, ascending=True))
	print("merge_sort decending: \n", merge_sort(arr, ascending=False))

	print("selection_sort ascending: \n", selection_sort(arr, ascending=True))
	print("selection_sort decending: \n", selection_sort(arr, ascending=False))

	print("counting_sort ascending: \n", counting_sort(arr, ascending=True))
	print("counting_sort decending: \n", counting_sort(arr, ascending=False))

	print("radix_sort_lsd ascending: \n", radix_sort_lsd(arr, ascending=True))
	print("radix_sort_lsd decending: \n", radix_sort_lsd(arr, ascending=False))