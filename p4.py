def isPalindrome(number):
    return str(number) == str(number)[::-1]

def largestPalidrome(min,max):
    results = []
    for i in range(min,max):
        for j in range(min,max):
            product = i * j
            if isPalindrome(product):
                results.append(product)
    return sorted(results)[-1]

print(largestPalidrome(100,1000))