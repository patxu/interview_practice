# 10/16/2015
def helper(words, string):
    print string
    if len(words) == 0:
        return string
    else:
        word = words.pop(0)
        if len(word) < 4:
            return helper(words, string + word)
        else:
            return helper(words, string + word[0] + str(len(word)-2) + word[len(word)-1])
def abbreviate(s):
    words = []
    newWord = ""
    for char in s:
        if char.isalpha():
            newWord += char
        else:
            if len(newWord) == 0:
                words.append(char)
            else:
                words.append(newWord)
                words.append(char)
            newWord = ""
    if len(newWord) != 0:
        words.append(newWord)
    print words
    return helper(words, "")

if __name__ == '__main__':
    abbreviate("internationalization")
    # Test.assert_equals(abbreviate("accessibility"), "a11y")
    # Test.assert_equals(abbreviate("Accessibility"), "A11y")
