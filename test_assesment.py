# def rotate_right(xs: list, k: int) -> list:
#     n=len(xs)
#     if n==0:
#         return []
#     k=k%n
#     if k<0:
#         k+=n
#     res=[None]*n
#     for i in range(n):
#         res[(i+k)%n] = xs[i]
#     return res

# def matrix_border_sum(m: int, n: int, matrix: list[list[int]]) -> int:
#     total=0
#     for i in range(m):
#         for j in range(n):
#             if i==0 or i==m-1 or j==0 or j==n-1:
#                 total+=matrix[i][j]
#     return total


# def count_pairs(nums: list[int], target: int) -> int:
#     count=0
#     n=len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i]+nums[j]==target:
#                 count+=1
#     return count


# def rle_encode(s: str) -> str:
#     res=""
#     count=1
#     for i in range(len(s)):
#         if i<len(s)-1 and s[i]==s[i+1]:
#             count+=1
#         else:
#             res+=str(count)+s[i]
#             count=1
#     return res

# def rle_decode(t: str) -> str:
#     res=""
#     for i in range(len(t)):
#         char=t[i]
#         count=int(t[i+1])
#         res+=char*count
#     return res


# def roman_to_int(s: str) -> int:
#     total=0
#     values={
#         'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000
#     }

#     for i in range(len(s)):
#         if i<len(s)-1 and values[s[i]]<values[s[i+1]]:
#             total-=values[s[i]]
#         else:
#             total+=values[s[i]]

#     return total

# import textwrap
# def wrap(text: str, width: int) -> list[str]:
#     wordwrap=textwrap.wrap(text, width)
#     return wordwrap





# def is_valid_password(pw: str) -> bool:
#     if len(pw)<8 or ' ' in pw:
#         return False

#     special_char = '!@#$%^&*?_'

#     has_lower=False
#     has_upper=False
#     has_digit=False
#     has_special=False
    
#     for char in pw:
#         if char.islower():
#             has_lower=True
#         elif char.isupper():
#             has_upper=True
#         elif char.isdigit():
#             has_digit=True
#         elif char in special_char:
#             has_special=True

#     return has_lower and has_upper and has_digit and has_special



class PasswordValidator:
    def __init__(self, pw: str):
        self.pw = pw

    def checks(self) -> dict[str, bool]:
        special='!@#$%^&*?_'

        result={
            "min_length" : len(self.pw) >= 8,
            "has_lower" : any(c.islower() for c in self.pw),
            "has_upper" : any(c.isupper() for c in self.pw), 
            "has_digit" : any(c.isdigit() for c in self.pw),
            "has_special" : any(c in special for c in self.pw),
            "no_spaces" : " " not in self.pw
        }
        return result

    def is_valid(self) -> bool:
        checks=self.checks()
        return all(checks.values())
    
        
    def report(self) -> list[str]:
        failed=[]
        checks=self.checks()

        for rule,passed in checks.items():
            if not passed:
                failed.append(rule)
        return failed





class GradeHistogram:
    def __init__(self, scores: list[float]):
        self.scores=scores
    
    def compute(self) -> dict[str, int]:
        count=0
        grades={'F' : 0, 'P' : 0, 'C' : 0, 'D' : 0, 'HD' : 0}
        
        for s in self.scores:
            if s<50:
                grades["F"] += 1
            elif s<65:
                grades["P"] += 1
            elif s<75:
                grades["C"] += 1
            elif s<85:
                grades["D"] += 1
            else:
                grades["HD"] += 1
        return grades


    def __str__(self) -> str:
        grades=self.compute()
        res=""
        for g in ["F", "P", "C", "D", "HD"]:
            res += g + ": " + "#" * grades[g] + '\n'
        return res























