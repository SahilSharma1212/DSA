word  = "abcdefd"
ch = "d"

idx = word.find(ch)

if idx >= 0:
    print(word[:idx+1][::-1] + word[idx+1:])
else:
    print(word)