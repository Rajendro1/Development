from typing import Counter


def sol(arr, target, n_stape):
	for i in range(len(arr)):
		if arr[i] == target:
    		# continue
			return(arr[i + n_stape])
		
def sol1(arr, target, n_stape):
	# arr = 0
	while(True):
		arr += 1
		if arr == target:
			continue
			
		return (arr + n_stape )

# Python3 program to demonstrate use of
# circular array using extra memory space

def prints(a, n, ind):

	# Create an auxiliary array of twice size.
	b = [None]*2*n
	i = 0
	
	# Copy a[] to b[] two times
	while i < n:
		b[i] = b[n + i] = a[i]
		i = i + 1
	
	i = ind

	# print from ind-th index to (n+i)th index.
	while i < n + ind :
		print(b[i], end = " ");
		i = i + 1

# Driver Code
a = ['A', 'B', 'C', 'D', 'E', 'F']
n = len(a);
prints(a, n, 3);

#This code is contributed by rishabh_jain


if __name__ == '__main__':
	nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "Queen", "King", "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "Queen", "King", "Ace"]
	# print(sol(nums, 3, 4))
	print(nums, len(a), 3)

