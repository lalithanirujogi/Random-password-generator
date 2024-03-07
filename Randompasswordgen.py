import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
characters = '!@#$^_()[]{}/'
number = '1234567890'
all = lower + upper + characters + number
length = int(input('enter a number : '))
password= "".join(random.sample(all,length))
print('The Generated Password is',password)
