def perm_no_dups(string):
    if string == None:
        return None
    perms = []
    if len(string) == 0:
        perms.append(" ")
        return perms

    first = string[0]
    remainder = string[1:]
    words = perm_no_dups(remainder)
    for word in words:
        for i in range(len(word)):
            s = word[:i] + first + word[i:]
            perms.append(s)

    return perms


print(perm_no_dups("".join([chr(c) for c in range(97, 97+5)])))