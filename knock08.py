def cipher(sample):
    ans = ''
    for ch in sample:
        if ch.islower():
            ans += chr(219-ord(ch))
        else:
            ans += ch
    print(ans)
    return ans


if __name__ == '__main__':
    cipher(cipher("This iS A pEn."))
