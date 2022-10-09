def count_substring(string, sub_string):
    counter = 0 
    leng = len(sub_string)
    for i in range(len(string)):
        s = string[i:i+leng]
        if s == sub_string:
            counter +=1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
