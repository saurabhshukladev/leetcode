###  roman-to-integer <br/> https://leetcode.com/problems/roman-to-integer/
- if the roman before the another roman has smaller value then reduce it by 1 point  
- example I = 1 before X = 10 is 9

### merge-sorted-array <br/> https://leetcode.com/problems/merge-sorted-array
- use existing_list[:] = new_list to copy new list over the old one

### remove-element <br/> https://leetcode.com/problems/remove-element
- since max value for numbers in the list is 50 we can change the removable numbers to 51 and sort it
- alternate: move a pointer and index if pointer is not equal to val then assign it to index
    - index only moves it i is not equal to val, index stops on val to replace it