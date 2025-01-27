## tags
- TODO
- FIX
- BUG
- TRY

###  roman-to-integer <br/> https://leetcode.com/problems/roman-to-integer/
- if the roman before the another roman has smaller value then reduce it by 1 point  
- example I = 1 before X = 10 is 9

### merge-sorted-array <br/> https://leetcode.com/problems/merge-sorted-array
- use existing_list[:] = new_list to copy new list over the old one

### remove-element <br/> https://leetcode.com/problems/remove-element
- since max value for numbers in the list is 50 we can change the removable numbers to 51 and sort it
- alternate: move a pointer and index if pointer is not equal to val then assign it to index
    - index only moves it i is not equal to val, index stops on val to replace it

### remove-duplicates-from-sorted-array <br/> https://leetcode.com/problems/remove-duplicates-from-sorted-array
- Method 1: make the duplicate element 101 as it is the max value possible and sort (this is slow and complexity is worst case O(n2) most of the time O(nlogn))
- Method 2: take 2 pointer, i moves with each iteration but j only moves when a[j-1] != a[i]
    - Explanation: j keeps looking back such that a[j] == a[j-1] (this is not needed in code, this is vibe), when i finds a[i] that
    that is diffrent that a[j-1] i tell j to assign a[i] to a[j] and move one step forward
    - j lags behind and only move when i has found a different number, j doesn't like moving on duplicates it stops after taking 1 step
    - j waits on number to be replaced

### remove-duplicates-from-sorted-array-ii <br/> https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
- Method 1: same as remove-duplicates-from-sorted-array-ii but instead of comparing nums[i] and nums[j-1], compare nums[i] with nums[j-1]. and adjust starting vlaues of i and j so that they start with index of 2 instead of 1

### reorder-data-in-log-files <br/> https://leetcode.com/problems/reorder-data-in-log-files
- Method 1: seprate Digit log lines and letter log lines
    - then split the letter log lines from " " and join them again leaving the first word and use these as keys and keep logs safe in values of dictionary
    - there will be a lot of edge cases in letter logs sorting,
        - for duplicates append the first word at end to create difference and sort it based on first word only if all other words are same, do this to the duplicate found in the letterLogMap after poping it and the new log that you were going to insert and insert them 
- Method 2: fix isDigit code to exit in O(1) no need to loop over all the items
    - make tuples by making the identifier (1st word) the 2nd element in tuple
    - using this we can use tuple to sort, when the first element is same then and only then second element is considered for sorting but if we concat the elements and sort it considers it as different elements and sorting is not as expected
- Method 3: building on top sorting using tuples to sort
    - instead of using tuple (log, identifier), we can use (isDigit, log, identifier) and sort all in one go
    - Note: tuples can have any number of elements are order and immutable



### majority-element <br/> https://leetcode.com/problems/majority-element
- Method 1: make a map for counting the elements, in second loop find max element
- Method 2: remove the second loop and keep track of res and maxCount in same loop
    - use the following to simplify the code
        -       dict.get(key, defualt value if no key is found)
- Method 3: Boyer-Moore Majority Voting Algorithm
    - imagine each number's count can reduce each other count
    - we assume that the first element is majority
    - every time we see that number again we increase count by one
    - every time we see some other number we decreace count by one
    - if the count becomes 0 we assign the current number as max
    - in this the max number will always come on top as it has more than n/2 occurrences and will cancel every other numbers count combined

### rotate <br/> https://leetcode.com/problems/rotate
- Method 1: split the List in 2 parts based on k (front and back)
    - then clear List and extend it with back + front, as after rotating this will be the sequence
- Method 2