from knock05 import Ngram


if __name__ == '__main__':
    word1 = "paraparaparadise"
    word2 = "paragraph"
    gram1 = Ngram(word1)
    gram2 = Ngram(word2)
    X = gram1.make_char_ngram(2)
    Y = gram2.make_char_ngram(2)

    union_XY = X.union(Y)
    intersection_XY = X.intersection(Y)
    difference_XY = X.difference(Y)

    print("X: {0}".format(X))
    print("Y: {0}\n".format(Y))
    print("union of X,Y: {0}".format(union_XY))
    print("intersection of X, Y: {0}".format(intersection_XY))
    print("difference of X, Y: {0}\n".format(difference_XY))

    if 'se' in X:
        print("'se' is in X.")
    else:
        print("'se' is not in X.")
        
    if 'se' in Y:
        print("'se' is in Y.")
    else:
        print("'se' is not in Y.")