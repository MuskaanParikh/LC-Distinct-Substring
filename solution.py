
def lengthOfLongestSubstring(s: str) -> int:
    findLongest = ''

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            unique = "".join(dict.fromkeys(substring))

            if unique == substring and len(findLongest) < len(substring):
                findLongest = substring
        
    return len(findLongest)

print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))
