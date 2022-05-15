def reverse_string(string):
    # base  : len 0 , return string
    # recursive
    print(string)
    if len(string)==0: # base , return string
        return string
    else:
        return reverse_string(string[1:])+string[0]
        #recursive
# print(reverse_string("hello"))


def reverse_iter(string):
    reverse= ''
    for i in range(len(string)):
        reverse = reverse+string[len(string)-i-1]
    return reverse

print(reverse_iter("hello"))