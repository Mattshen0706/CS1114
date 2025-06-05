# def longestPalindrome(string1,string1copy,formattedstring,indexpoint):
#     if len(string1)<=1 and len(string1copy)<=1:
#         return formattedstring
#     elif len(string1)<=1:
#         if string1[0]==string1[len(string1)-1]:
#             formattedstring[indexpoint].append(string1[0])
#             return longestPalindrome(string1[1:len(string1)-1],string1copy,formattedstring,indexpoint)
#         else:
#             indexpoint+=1
#             return longestPalindrome(string1[1:len(string1)],string1copy,formattedstring,indexpoint)
#     else:
#         if string1copy[0]==string1copy[len(string1copy)-1]:
#             formattedstring[indexpoint].append(string1copy[0])
#             return longestPalindrome(string1,string1copy[1:len(string1)-1],formattedstring,indexpoint)
#         else:
#             indexpoint+=1
#             return longestPalindrome(string1,string1copy[0:len(string1)-1],formattedstring,indexpoint)
            

# word="wwoww"
# formattedstring=[]
# print(longestPalindrome(word,word,formattedstring,0))


# CORRECT ANSWER:

def longestPalindrome(s):
    if not s or len(s) == 1:
        return s

    start = 0
    end = 0

    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)       # Odd-length palindromes
        len2 = expandAroundCenter(s, i, i + 1)   # Even-length palindromes
        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end+1]

def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

word = "whwoooooow2323woww"
print(longestPalindrome(word))
