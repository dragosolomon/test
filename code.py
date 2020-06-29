from urllib.request import urlopen

def fetch_words():
    story = urlopen("http://sixty-north.com/c/t.txt")

    words = []

    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            words.append(word)
    story.close()

    for word in words:
        print(word)

print(__name__)