# Simple DSA challenge: find the median to get the flag
arr = [12, 3, 5, 7, 4, 19, 26]
arr.sort()
median = arr[len(arr)//2]
if median == 7:
    print("Your flag is: 3CS{CTF-Vers.2_dsaarray}")
else:
    print("Try again!")
