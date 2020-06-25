from urllib.request import urlopen

story = urlopen("hhtp://sixty-north.com/c/t.txt")
words = []
for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        words.append(word)

story.close()