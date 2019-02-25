"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
def isPalindrome(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        a = n
        rev = 0
        while n > 0:
            rev = rev*10 + n%10 # building reverse then compare with original
            n = n//10
        if rev == a:
            return True
        else:
            return False

def LargestPalindrome():
    lis = [0]
    i = 0
    for n1 in range(100,1000):
        for n2 in range(100,1000):
            if isPalindrome(n1*n2):
                if n1 * n2 > lis[i]:
                    lis.append(n1 * n2)
                    i += 1
    return lis

def LargestPalindrome2():
    palindrome_values = {}
    for x in range(100, 1000):
        for y in range(100, 1000):
            value = x * y
            if str(value) == str(value)[::-1]:
                if value not in palindrome_values:
                    palindrome_values[value] = str(x) + "*" + str(y)


    return sorted(palindrome_values.keys(), reverse=True)[:1], palindrome_values[906609]

print(LargestPalindrome())
print("This program took: " + str(time.process_time() * 1000) + "ms.")

