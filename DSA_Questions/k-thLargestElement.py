import heapq

def find_kth_largest(nums: list, k: int) -> int:
    if not nums:
        raise ValueError("The list is empty. Please enter at least one number.")
    if k <= 0 or k > len(nums):
        raise ValueError("Invalid k. It must be between 1 and the length of the list.")

    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  
    
    return heap[0]  

try:
    user_input = input("Enter a list of integers separated by spaces: ").strip()
    
    if not user_input:
        print("Invalid input. The list cannot be empty.")
    else:
        nums = list(map(int, user_input.split()))
        k = int(input("Enter the value of k: "))

        result = find_kth_largest(nums, k)
        print(f"The {k}-th largest element is: {result}")

except ValueError as e:
    print(f"Error: {e}")
