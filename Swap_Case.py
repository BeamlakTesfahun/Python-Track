def swap_case(s):
    empty = ""
    for chara in s:
        if chara.islower():
            chara = chara.upper()
        else:
            chara = chara.lower()
        empty += "".join(chara)
    return empty

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
