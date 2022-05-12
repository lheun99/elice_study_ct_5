n = int(input())
words = [input() for _ in range(n)]
set_words = set(words)
words = list(set_words)
# words = sorted(words)
# words = sorted(words, key=len)
words.sort(key=lambda x: (len(x), x))
for word in words:
    print(word)
