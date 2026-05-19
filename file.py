# ===========================================
# Task 1: Longest Harmonic Subsequence (5 pt)
# ===========================================
from typing import List

def longest_harmonic_subsequence(nums: List[int]) -> int:
    """
    Find the length of the longest harmonic subsequence (meaning elements do not have to be contiguous).
    A subsequence is harmonic if its max and min values differ by exactly 1.
    
    Requirements:
    1) Must run in O(n) time.
    2) Do not sort the original list.
    3) Return 0 if no harmonic subsequence exists.
    """

    result=0
    for n in nums:
        count = nums.count(n) + nums.count(n+1)
        result = max(result, count)
    return result



    '''
    Example input nums = [1, 3, 2, 2, 5, 2, 3, 7]
        Output:5 because (2,3) or [3, 2, 2, 2, 3]
    '''

    # TODO: implement
    raise NotImplementedError

# ====================================
# Task 2: Smart Text Truncation (5 pt)
# ====================================
import textwrap
def truncate_text(text: str, max_length: int) -> str:
    """
    Truncate text to fit a maximum length without breaking words.

    Requirements:
      1) The total length of the returned string must be <= max_length.
      2) If truncation occurs, append "..." to the end (dots count toward max_length).
      3) Do not split a word; truncate at the last space that allows the ellipsis to fit.
      4) If the entire text fits within max_length, return it as-is without dots.

    Returns:
        str: The truncated string with an ellipsis if necessary.
    """
    wordwrap=textwrap.wrap(text, max_length)
    return wordwrap
    '''
    Example:
    Input: text="The marathon continues today", max_length=20
    Output: "The marathon..." (Length 15 is ≤ 20; adding "continues" would exceed the limit).
    '''

    # TODO: implement
    raise NotImplementedError



# =======================================
# Task 3: Inventory Stock Checker (10 pt)
# =======================================
class StockTracker:
    """
    Accepts a list of integer stock levels for different items.
    
    Categories:
      - Out     : level == 0
      - Low     : 1 <= level <= 5
      - Healthy : 6 <= level <= 20
      - Over    : level > 20
    """
    def __init__(self, levels: list[int]):
        self.levels=levels

    
    def compute(self) -> dict[str, int]:
        categories={
            'Out' : 0, 'Low' : 0, 'Healthy' : 0, 'Over' : 0
        }
        n=len(self.levels)
        for i in range(n):
            if i in self.levels == 0:
                categories["Out"] +=1
            elif i in self.levels >=1 and i in self.levels <= 5:
                categories["Low"] +=1
            elif i in self.levels >=6 and i in self.levels <= 20:
                categories["Healthy"] +=1
            else:
                categories["Over"] +=1
        return categories


    def __str__(self) -> str:
        """Format: 'Status: |' per count (Out, Low, Healthy, Over)"""
        checks=self.compute()
        
    
    '''
    Example Input: [15, 0, 2, 45, 10, 0, 4]
    Output:
    Out: ||
    Low: ||
    Healthy: ||
    Over: |
    '''


print(longest_harmonic_subsequence([1, 3, 2, 2, 5, 2, 3, 7]))
