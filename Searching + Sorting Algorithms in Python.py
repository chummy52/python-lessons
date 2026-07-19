# Algorithms 
# examples of sorting algorithms:
# insert sort, bubble sort, selection sort, merge sort, gnome sort

# an algorithm is just step by step instructions for solving some problem to sort information as in the real world just means to order it 
# ex: from smallest to largest or alphabetically or some other heuristic
# its among the algorithms that we're going to focus on today in addition to 'searching', which of course is looking for information

# the goal of this lesson is to give u different mental models for and methodologies
# for actually solving problems by giving you a sense of how these real world algorithms can be translated to actual computers that we can control

#example of algorithm: taking attendance, we can use scanners, or do the old school where you count with ur hands 
# another example:
# theres a lot of people in a place (probably an odd number of people)
# the first tep is to stand up and think of the number 1
# the second step is for them to pair off with someone standing, add their number to the other person and remember the sum ( 1 + 1 = 2)
# at this point, everyone except maybe an odd number  of  people in the room are thinking of 2
# the third step is, there are pairs now, so one person in a pair should sit down
# to those people who are still standing, the algorithm's still going
# so the fourth step for those taht are still standing, go back to the second step
# so as you can see at this part, it is encouraging a loop or a repeat
# so after doing the second step, the number of people that are standing should've drop 
# at this part, almost everyone has sat down, but there are probably some that are still standing
# so what will you do? hmm lets do some arithmetic and add all of the people that we're left standing
# now if you think about the algorithm, that we just executed
# each of the people started with the number 1 and then half of them handed off their number
# and then half of the people handed off their number, and then half of the them handed off their number
# so theoretically, all of these ones which we started should be aggregated into the final count
# now if the execution of the algorithm is correct we should know now the number of the people inside of a room
# after knowing the number of the people in a room, then we can end the algorithm
# final algorithm = log2 n


# arrays = one of the simplest of data structures inside of a computer where you just take 
# where you just take the memory in your computer and you break it up into chunnks
# and you can store a bunch of integers, a bunch of strings, whatever, back to back to back to back 
# and that's the key characterstic for an array.
# it is a chunk of memory wherein all of the values they're in are back to back to back 
# so right next to each other in memory 
# so basically an array in a memory is like a grid, starting with the first chunk or box of a grid, meaning byte 0 and then the last box of the grid, probably byte 1 million or something
# example: let's assume that we want 1234567 chunks of memory for the moment,
# and inside of them we might put something like these numbers here |[1][5][10][20][50][100][500]|
# the interesting thing about computers is that even though if i were to ask someone to find the number 50 in this array,
# our eyes would quickly see where it is because we sort of have this bird's eye view
# but the catch with computers and with code that we write , is that really these arrays,
# are equivalent to a whole bunch of "closed doors" and the computer can't just have this bird's eye view of everything
# if the computer wants to see what value is at a certain location 
# it has to do the metaphorical equivalent of going to that location 
# opening the door, and looking, then closing it and moving on to the next,
# that is to say that a computer can only look at or access one value at a time
# Now thats in the simplest form
# you can build fancier computers that theoretically can do more than that
# but all of the code we write generally is going to assume that model.
# you can't just see everythign at once 
# you have to go to each location in these "closed doors"
# when we talk about the locations in memory , we're gonna start counting from 0 instead of 1 
# so it will be like | door[0], door[1], door[2], door[3], door[4], door[5], door[6]
# so just ingrained in your mind that if you hear something like location 6,
# that's actually implying that there's at least 7 total location because we started counting at 0

# now here's an example, 7 box or lockers filled with money in each
# the goal is to search for some specific denomination of interest and use the lockers as a metaphor
# for what your computer is going to do and what your code ultimately is going to do if we're searching for a problem
#               _______    
#               |     |
# like input -> |a box| -> output | input which is the lockers that are closed, the output which we
#               |     |             need to be a boolean, True or False, inside the box will be the algorithm
#               -------
# we will have two searching methods, going from left to right opening one by one which is an example of linear search and then binary search where we will imply 2 because we're having that problem in 2 again and again and again
# so for instance, linear search - left to right, right to left, we could document our pseudo code as follows:

# For each door from left to right
#   if 50 is behind the door
#       Return true
# Return false # if you get all the way through the lcokers and you have never once declared true by finding the 50,
# you might as well default at the very end to saying False - "i did not find it"
#example of Big O notations:
#O(n^2)
# O(n log n)
# O(n) - linear search
# O(log n) - binary search
#O(1)



"""
================================================================================
🔍 COMPLETE SEARCHING & SORTING ALGORITHMS IN PYTHON
================================================================================
BroCode Style - Easy to Understand! 🚀

TABLE OF CONTENTS:
================================================================================
SEARCHING ALGORITHMS:
    1. linear_search(lst, target)      - Check one by one
    2. binary_search(sorted_lst, target) - Cut in half

SORTING ALGORITHMS:
    3. bubble_sort(lst)               - Compare & swap adjacent
    4. selection_sort(lst)            - Find minimum, put at start
    5. insertion_sort(lst)           - Build sorted one by one
    6. merge_sort(lst)                - Divide & conquer
    7. quick_sort(lst)                 - Partition around pivot

Test data: [64, 25, 12, 22, 11]

Let's learn by doing! 💪
================================================================================
"""

# ================================================================================
# 1. LINEAR SEARCH
# ================================================================================
"""
What is Linear Search?
    Linear Search checks each element one by one until it finds the target.

When to use:
    ✅ When the data is NOT sorted
    ✅ When the data is small
    ✅ When you only need to find ONE match

Time Complexity: O(n) - If the list is twice as big, it takes twice as long!
"""
def linear_search(lst, target):
    """
    Linear Search - Loop through and check each element
    
    How it works:
        1. Loop through each index (0, 1, 2, ...)
        2. Check if lst[i] equals target
        3. If equal, return i (the index)
        4. If we finish the loop, return -1 (not found)
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i  # Found it! Return the index
    return -1  # Not found


# ================================================================================
# 2. BINARY SEARCH
# ================================================================================
"""
What is Binary Search?
    Binary Search divides the search area in HALF each time until found.

CRITICAL: The list MUST be sorted first! Otherwise it won't work!

When to use:
    ✅ When data is SORTED
    ✅ When data is large
    ✅ When you need BLIZZARD speed! ⚡

Time Complexity: O(log n) - Even with 1 million items, only ~20 checks!
"""
def binary_search(sorted_lst, target):
    """
    Binary Search - Keep dividing in half until you find it!
    
    IMPORTANT: The list MUST be sorted first!
    
    How it works:
        1. Look at the middle element
        2. If middle == target: Found it!
        3. If middle < target: Search in RIGHT half
        4. If middle > target: Search in LEFT half
        5. Repeat until found or no elements left
    """
    left = 0
    right = len(sorted_lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if sorted_lst[mid] == target:
            return mid  # Found it!
        elif sorted_lst[mid] < target:
            left = mid + 1  # Target is in right half
        else:
            right = mid - 1  # Target is in left half
    
    return -1  # Not found


# ================================================================================
# 3. BUBBLE SORT
# ================================================================================
"""
What is Bubble Sort?
    Compare adjacent elements and swap if they're in wrong order.
    The largest elements "bubble up" to the end!

When to use:
    ✅ For teaching (easy to understand)
    ✅ For small datasets
    ✅ When data is ALREADY nearly sorted

How it works:
    1. Compare element at index 0 with index 1
    2. If first > second, SWAP them!
    3. Move to next pair
    4. Repeat until end
    5. Largest element is now at the end!
    6. Repeat until no swaps needed

Time Complexity: O(n²)
"""
def bubble_sort(lst):
    """
    Bubble Sort - Compare adjacent elements and swap if wrong order
    
    How it works:
        1. Compare lst[j] with lst[j+1]
        2. If lst[j] > lst[j+1], SWAP them!
        3. After each pass, largest element "bubbles" to end
        4. If no swaps, array is sorted! Stop early!
    """
    n = len(lst)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                # Swap!
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        
        if not swapped:
            break  # Already sorted! Stop early!
    
    return lst


# ================================================================================
# 4. SELECTION SORT
# ================================================================================
"""
What is Selection Sort?
    Find the MINIMUM element, put it at position 0.
    Find the NEXT minimum, put it at position 1.
    Repeat until done!

When to use:
    ✅ When memory writes are expensive
    ✅ For small datasets
    ✅ When you want predictable performance

How it works:
    1. Find the smallest element in entire array
    2. Swap it with the first element
    3. Find the smallest in remaining array
    4. Swap it with the second element
    5. Repeat

Time Complexity: O(n²) - Always, no best case!
"""
def selection_sort(lst):
    """
    Selection Sort - Find minimum, put at start
    
    How it works:
        1. Find smallest element in positions 0 to n-1
        2. Swap with position 0
        3. Find smallest in positions 1 to n-1
        4. Swap with position 1
        5. Repeat until sorted
    """
    n = len(lst)
    
    for i in range(n):
        # Assume position i has the minimum
        min_idx = i
        
        # Find the minimum in the remaining array
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        
        # Swap minimum with position i
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    
    return lst


# ================================================================================
# 5. INSERTION SORT
# ================================================================================
"""
What is Insertion Sort?
    Build sorted array ONE ELEMENT AT A TIME.
    Take each element and insert it in correct position in sorted portion.

When to use:
    ✅ When data is ALMOST sorted already
    ✅ For small datasets
    ✅ When new elements keep coming in

How it works:
    1. First element is sorted (by itself)
    2. Take next element
    3. Find correct position in sorted portion
    4. Shift larger elements to the right
    5. Insert current element
    6. Repeat

Time Complexity: O(n²) but O(n) if already nearly sorted!
"""
def insertion_sort(lst):
    """
    Insertion Sort - Build sorted array one element at a time
    
    How it works:
        1. Start from second element (index 1)
        2. Store current element in key
        3. Compare with elements to the left
        4. Shift larger elements to the right
        5. Insert key in correct position
        6. Repeat for all elements
    """
    n = len(lst)
    
    for i in range(1, n):
        # Store current element to insert
        key = lst[i]
        
        # Move elements that are greater than key to the right
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        
        # Insert key in correct position
        lst[j + 1] = key
    
    return lst


# ================================================================================
# 6. MERGE SORT
# ================================================================================
"""
What is Merge Sort?
    DIVIDE AND CONQUER!
    1. Split array in half
    2. Sort each half (recursively)
    3. Merge them back together

When to use:
    ✅ For LARGE datasets
    ✅ When you need GUARANTEED O(n log n)
    ✅ When stability matters (preserves order of equal elements)

How it works:
    1. If 0 or 1 elements, already sorted!
    2. Split array in half
    3. Recursively sort each half
    4. Merge sorted halves together

Time Complexity: Always O(n log n) - Guaranteed! ✅
Space: O(n) - Needs extra space
"""
def merge_sort(lst):
    """
    Merge Sort - Divide, Conquer, Merge!
    
    How it works:
        1. If array has 0 or 1 elements, it's sorted!
        2. Split array in half
        3. Recursively sort each half
        4. Merge sorted halves together
    """
    # Base case: 0 or 1 element is already sorted!
    if len(lst) <= 1:
        return lst
    
    # Split in half
    mid = len(lst) // 2
    
    # Left half and right half
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    
    # Merge sorted halves
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted arrays into one sorted array
    
    How it works:
        1. Compare first elements of both arrays
        2. Add the smaller one to result
        3. Repeat until one array is empty
        4. Add remaining elements
    """
    result = []
    i = j = 0
    
    # Compare and add smaller elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# ================================================================================
# 7. QUICK SORT
# ================================================================================
"""
What is Quick Sort?
    1. Pick a PIVOT element
    2. PARTITION: elements smaller than pivot go LEFT, larger go RIGHT
    3. Recursively sort both partitions

When to use:
    ✅ For GENERAL PURPOSE sorting
    ✅ When you need FASTEST average case
    ✅ When memory is limited (in-place version)

How it works:
    1. Pick a pivot (usually last element)
    2. Partition: smaller elements go left, larger go right
    3. Recursively sort left and right partitions
    4. Combine: left + pivot + right

Time Complexity:
    - Best/Average: O(n log n) - Super fast!
    - Worst: O(n²) - when already sorted!
"""
def quick_sort(lst):
    """
    Quick Sort - Pick pivot, partition, recursively sort
    
    How it works:
        1. If 0 or 1 elements, already sorted!
        2. Pick pivot (last element)
        3. Partition into left (<= pivot) and right (> pivot)
        4. Recursively sort left and right
        5. Combine: left + pivot + right
    """
    # Base case
    if len(lst) <= 1:
        return lst
    
    # Pick pivot (last element)
    pivot = lst[-1]
    
    # Partition: left has elements <= pivot, right has elements > pivot
    left = [x for x in lst[:-1] if x <= pivot]
    right = [x for x in lst[:-1] if x > pivot]
    
    # Recursively sort and combine
    return quick_sort(left) + [pivot] + quick_sort(right)


# ================================================================================
# IN-PLACE QUICK SORT (uses less memory)
# ================================================================================
def quick_sort_inplace(lst, low=0, high=None):
    """
    In-place Quick Sort - Saves memory!
    
    This version doesn't create new lists,
    so it uses less memory.
    """
    if high is None:
        high = len(lst) - 1
    
    if low < high:
        # Partition and get pivot index
        pi = partition_inplace(lst, low, high)
        
        # Sort left and right partitions
        quick_sort_inplace(lst, low, pi - 1)
        quick_sort_inplace(lst, pi + 1, high)


def partition_inplace(lst, low, high):
    """
    Partition for in-place quick sort
    
    How it works:
        1. Choose last element as pivot
        2. Track elements smaller than pivot with index i
        3. Swap elements into correct positions
        4. Place pivot in correct position
    """
    pivot = lst[high]
    i = low - 1
    
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


# ================================================================================
# MAIN PROGRAM - TEST ALL ALGORITHMS
# ================================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("🚀 COMPLETE SEARCHING & SORTING ALGORITHMS")
    print("=" * 70)
    
    # Test data
    test_list = [64, 25, 12, 22, 11]
    
    print(f"\n📋 Test data: {test_list}")
    print("-" * 70)
    
    # ==========================================================================
    # TEST SEARCHING ALGORITHMS
    # ==========================================================================
    print("\n📍 SEARCHING ALGORITHMS")
    print("=" * 70)
    
    # TEST LINEAR SEARCH
    print("\n1️⃣  LINEAR SEARCH")
    print(f"    Searching in {test_list}")
    result = linear_search(test_list, 22)
    print(f"    linear_search({test_list}, 22) = {result}")
    
    # TEST BINARY SEARCH (must use sorted list!)
    print("\n2️⃣  BINARY SEARCH")
    sorted_list = bubble_sort(test_list.copy())
    print(f"    First sort: {sorted_list}")
    result = binary_search(sorted_list, 22)
    print(f"    binary_search({sorted_list}, 22) = {result}")
    
    # ==========================================================================
    # TEST SORTING ALGORITHMS
    # ==========================================================================
    print("\n🔀 SORTING ALGORITHMS")
    print("=" * 70)
    
    # TEST BUBBLE SORT
    print("\n3️⃣  BUBBLE SORT")
    arr = test_list.copy()
    result = bubble_sort(arr.copy())
    print(f"    Before: {test_list}")
    print(f"    After:  {result}")
    
    # TEST SELECTION SORT
    print("\n4️⃣  SELECTION SORT")
    arr = test_list.copy()
    result = selection_sort(arr.copy())
    print(f"    Before: {test_list}")
    print(f"    After:  {result}")
    
    # TEST INSERTION SORT
    print("\n5️⃣  INSERTION SORT")
    arr = test_list.copy()
    result = insertion_sort(arr.copy())
    print(f"    Before: {test_list}")
    print(f"    After:  {result}")
    
    # TEST MERGE SORT
    print("\n6️⃣  MERGE SORT")
    arr = test_list.copy()
    result = merge_sort(arr.copy())
    print(f"    Before: {test_list}")
    print(f"    After:  {result}")
    
    # TEST QUICK SORT
    print("\n7️⃣  QUICK SORT")
    arr = test_list.copy()
    result = quick_sort(arr.copy())
    print(f"    Before: {test_list}")
    print(f"    After:  {result}")
    
    # ==========================================================================
    # COMPLETE FLOW
    # ==========================================================================
    print("\n" + "=" * 70)
    print("📋 COMPLETE FLOW: SORT THEN SEARCH")
    print("=" * 70)
    
    data = [64, 25, 12, 22, 11]
    print(f"\n    Step 1: Original: {data}")
    
    # Sort first
    data = quick_sort(data)
    print(f"    Step 2: Sorted:   {data}")
    
    # Search
    result = binary_search(data, 22)
    print(f"    Step 3: Found 22 at index: {result}")
    
    print("\n" + "=" * 70)
    print("✅ ALL TESTS COMPLETE!")
    print("=" * 70)


# ================================================================================
# CHEAT SHEET
# ================================================================================

"""
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                          COMPLETE CHEAT SHEET                                    ║
╠══════════════════════════╦══════════════╦══════════════╦═══════════════════════════╣
║ Algorithm               ║ Time Best    ║ Time Worst   ║ Notes                      ║
╠══════════════════════════╬══════════════╬══════════════╬═══════════════════════════╣
║                         SEARCHING ALGORITHMS                                     ║
╠══════════════════════════╬══════════════╬══════════════╬═══════════════════════════╣
║ LINEAR SEARCH          ║ O(1)         ║ O(n)        ║ Works on unsorted data       ║
║ BINARY SEARCH          ║ O(1)         ║ O(log n)    ║ MUST be sorted first!         ║
╠══════════════════════════╬══════════════╬══════════════╬═══════════════════════════╣
║                          SORTING ALGORITHMS                                    ║
╠══════════════════════════╬══════════════╬══════════════╬═══════════════════════════╣
║ BUBBLE SORT            ║ O(n)         ║ O(n²)       ║ Easy, stops if sorted      ║
║ SELECTION SORT         ║ O(n²)        ║ O(n²)       ║ Few writes, predictable    ║
║ INSERTION SORT         ║ O(n)         ║ O(n²)       ║ Good for nearly sorted    ║
║ MERGE SORT              ║ O(n log n)   ║ O(n log n) ║ Guaranteed O(n log n)!   ║
║ QUICK SORT              ║ O(n log n)   ║ O(n²)       ║ Fastest in practice!     ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  📊 COMPLEXITY COMPARISON:                                                    ║
║                                                                                ║
║     n = 10        n = 100       n = 1,000       n = 1,000,000                   ║
║     ──────        ──────        ────────        ──────────────                 ║
║     O(1)          O(1)          O(1)             O(1)                         ║
║     O(log n)       O(log n)       O(log n)          O(~20)                        ║
║     O(n)           O(n)           O(n)              O(1,000,000)                   ║
║     O(n²)          O(n²)         O(n²)            O(10¹²)  (TOO SLOW!)         ║
║     O(n log n)     O(n log n)    O(n log n)        O(~20,000,000)               ║
║                                                                                ║
╠══════════════════════════════════════════════════════════════════════════════════════╣
║                                                                                ║
║  💡 PRO TIPS:                                                                  ║
║                                                                                ║
║  • Use sorted() or .sort() for real projects!                                ║
║  • Use binary search for fast searching (after sorting!)                     ║
║  • Quick Sort is fastest for general use                                        ║
║  • Merge Sort guarantees O(n log n) - no worst case!                         ║
║  • For nearly sorted data: Insertion Sort is best!                             ║
║                                                                                ║
║  🎯 WHEN TO USE WHICH:                                                        ║
║                                                                                ║
║  • Need to search once?           → Linear Search                                ║
║  • Need to search many times?    → Sort first, then Binary Search!            ║
║  • Tiny dataset (< 50 items)?    → Bubble/Selection/Insertion Sort                  ║
║  • Large dataset?               → Merge Sort or Quick Sort                    ║
║  • Almost sorted data?         → Insertion Sort (接近排序!)                    ║
║  • Need guaranteed speed?     → Merge Sort!                               ║
║                                                                                ║
║  🔑 KEY VOCABULARY:                                                           ║
║                                                                                ║
║  • O(1)         = Constant time (instant!)                                   ║
║  • O(log n)     = Logarithmic time (very fast!)                                 ║
║  • O(n)         = Linear time                                               ║
║  • O(n log n)   = Linearithmic time (fast!)                                    ║
║  • O(n²)        = Quadratic time (slow!)                                     ║
║                                                                                ║
║  📌 SPACE COMPLEXITY (Memory used):                                             ║
║                                                                                ║
║  • Bubble Sort:      O(1)  - In-place, no extra memory                       ║
║  • Selection Sort:   O(1)  - In-place, no extra memory                       ║
║  • Insertion Sort:   O(1)  - In-place, no extra memory                       ║
║  • Merge Sort:       O(n)  - Needs extra array for merging                  ║
║  • Quick Sort:       O(log n) - For recursive calls                          ║
║                                                                                ║
╚══════════════════════════════════════════════════════════════════════════════════════════════╝
"""

# yeah im gonna go back to this lesson next time fr