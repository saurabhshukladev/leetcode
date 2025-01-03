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

### reorder-data-in-log-files <br/> https://leetcode.com/problems/reorder-data-in-log-files
- Method 1: seprate Digit log lines and letter log lines
    - then split the letter log lines from " " and join them again leaving the first word and use these as keys and keep logs safe in values of dictionary
    - there will be a lot of edge cases in letter logs sorting,
        - for duplicates append the first word at end to create difference and sort it based on first word only if all other words are same, do this to the duplicate found in the letterLogMap after poping it and the new log that you were going to insert and insert them 
- Method 2: TODO

### majority-element <br/> https://leetcode.com/problems/majority-element
- Method 1: make a map for counting the elements, in second loop find max element
- Method 2: TODO