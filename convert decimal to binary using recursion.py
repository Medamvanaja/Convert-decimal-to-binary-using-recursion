def convertToBin(a):

   if a > 1:

       convertToBin(a//2)

   print(a % 2,end = '')



d = 34
convertToBin(d)

print()

