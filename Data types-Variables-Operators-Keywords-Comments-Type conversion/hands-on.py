import datetime
b = input("enter your age here:")
c = int(b) or float(b)
if c >= 30 and c <= 60:
    print("you are getting old: age is  {}, type is: {}, and your name is {}".format(
        c, type(c), "agodin"))
else:
    print("maybe you are too young or over old, age is : {}, type is: {}".format(b, type(b)))

print("the time now for this is: {}, name is {}".format(
    datetime.datetime.now(), "agodin"))
