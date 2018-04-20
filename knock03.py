import re

if __name__ == '__main__':
    sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    words = re.findall(r'\w+', sentence)
    for w in words:
        print('{0}: {1}'.format(w, len(w)))