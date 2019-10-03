i = input('enter the combination: ')
# enter the combination: tommyhilfiger1977
ncount = sum(c.isdigit() for c in s)
wcount = sum(c.isalpha() for c in s)
print("number of letters in the string is" , wcount)
print ("number of digits in the string is ", ncount)
