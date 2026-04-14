# # rotate list
# def rotate_list(xs:list, k:int) -> list:
#     n=len(xs)
#     if n==0:
#         return []
#     k=k%n
#     if k<0:
#         k+=n
#     res=[None]*n
#     for i in range(n):
#         res[(i+k)%n]=xs[i]
#     return res

# # matrix borader sum
# total=0
# def matrix_border_sum(m: int, n: int, matrix: list[list[int]]) ->int:
#     for i in range(m):
#         for j in range(n):
#             if i==0 or i==m-1 or j==0 or j==n-1:
#                 total+=matrix[i][j]
#     return total

# # two sum
# def count_pairs(nums: list[int], target: int) -> int:
#     count=0
#     n=len(nums)
#     for i in range (n):
#         for j in range (i+1, n):
#             if nums[i]+nums[j]==target:
#                 count+=1
#     return count

# # encoding (RLE)
# def rle_encode(s: str) -> str:
#     res=""
#     count=1
#     for i in range (len(s)):
#         if i < len(s)-1 and s[i]==s[i+1]:
#             count+=1
#         else:
#             res+=s[i]+str(count)
#             count=1
#     return res

# # decoding 
# def rle_decode(t: str) -> str:          # aaabbcc --> a3b2c1
#     res=""
#     for i in range (0, len(t), 2):
#         char=t[i]
#         count=int(t[i+1])
#         res+=char*count
#     return res

# # roman to integers
# def roman_to_int(s: str) -> int:
#     total=0
#     values={
#         'I' :1, 'V' :5, 'X' :10, 'L' :50, 'C' :100, 'D' :500, 'M' :1000
#     }
#     for i in range(len(s)):
#         if i<len(s)-1 and values[s[i]]<values[s[i+1]]:
#             total-=values[s[i]]
#         else:
#             total+=values[s[i]]
#                                     # roman_to_int("MCMXCIV")  # 1994

# # greedy word wrap
# # two-sum
# # grade histogram

# # greedy word wrap


# import textwrap

# # Your wrap function
# def wrap(text: str, width: int) -> list[str]:
#     wrap_text = textwrap.wrap(text, width)
#     return wrap_text



# # password validator
# def is_valid_password(pw: str) -> bool:
#     if len(pw) < 8 or ' ' in pw:
#         return False 
    
#     has_lower=False
#     has_upper=False
#     has_digit=False
#     has_special=False

#     special_char = "!@#$%^&*?_"

#     for char in pw:
#         if char.isLower(): has_lower=True
#         eplif char.isupper(): has_upper = True
#         elif char.isdigit(): has_digit = True
#         elif char in special_char: has_special = True

# # read a file
# try:
#     with open("/Users/sabyasachi/Documents/programming_for_ai/input.txt")  as file:
#         lines=file.readlines()
#         # read line by line

#     num_lines=len(lines) # how many lines in list
#     num_words=sum(len(line.split()) for line in lines) # count words
#     num_chars=sum(len(line.rstrip("\n") for line in lines)) # count chars without newlines

#     with open("/Users/sabyasachi/Documents/programming_for_ai/summary.txt") as file:
#         file.write(f"lines:{num_lines}\n")
#         file.write(f"words:{num_words}\n")
#         file.write(f"chars:{num_chars}\n")
#         # creates summary file with 3 lines

# except FileNotFoundError:
#     print("missing file")





# # week 2 practicals



# # Password Validator

# class PasswordValidator:
#     def __init__(self, pw):
#         self.pw = pw

#     def checks(self):
#         special = "!@#$%^&*?_"
#         result = {
#             "min_length": len(self.pw) >= 8,
#             "has_lower": any(c.islower() for c in self.pw),
#             "has_upper": any(c.isupper() for c in self.pw),
#             "has_digit": any(c.isdigit() for c in self.pw),
#             "has_special": any(c in special for c in self.pw),
#             "no_spaces": " " not in self.pw
#         }
#         return result

#     def is_valid(self):
#         checks = self.checks()
#         return all(checks.values())

#     def report(self):
#         failed = []
#         checks = self.checks()

#         for rule, passed in checks.items():
#             if not passed:
#                 failed.append(rule)

#         return failed





# import math

# class Fraction:
#     def __init__(self, n, d):
#         if d == 0:
#             raise ValueError("denominator cannot be zero")

#         if d < 0:
#             n = -n
#             d = -d

#         g = math.gcd(n, d)
#         self._n = n // g
#         self._d = d // g

# @property
# def n(self):
#     return self._n

# @property
# def d(self):
#     return self._d

# def __add__(self, other):
#     n = self.n * other.d + other.n * self.d
#     d = self.d * other.d
#     return Fraction(n, d)

# def __sub__(self, other):
#         n = self.n * other.d - other.n * self.d
#         d = self.d * other.d
#         return Fraction(n, d)

# def __mul__(self, other):
#         n = self.n * other.n
#         d = self.d * other.d
#         return Fraction(n, d)

# def __truediv__(self, other):
#         n = self.n * other.d
#         d = self.d * other.n
#         return Fraction(n, d)

# def __eq__(self, other):
#         return self.n == other.n and self.d == other.d

# def __str__(self):
#         return f"{self.n}/{self.d}"


# # grade histogram

# class GradeHistogram:

#     def __init__(self, scores):
#         self.scores = scores

#     def compute(self):
#         grades = {"F":0, "P":0, "C":0, "D":0, "HD":0}

#         for s in self.scores:
#             if s < 50:
#                 grades["F"] += 1
#             elif s < 65:
#                 grades["P"] += 1
#             elif s < 75:
#                 grades["C"] += 1
#             elif s < 85:
#                 grades["D"] += 1
#             else:
#                 grades["HD"] += 1

#         return grades
    
#     def __str__(self):
#         grades = self.compute()

#         result = ""
#         for g in ["F","P","C","D","HD"]:
#             result += g + ": " + "#" * grades[g] + "\n"

#         return result





