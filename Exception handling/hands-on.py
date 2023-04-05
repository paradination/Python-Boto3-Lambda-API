def add(a,b):
    try:
        c = a + b
        return c
    except Exception as e:
        print("error:{}, the value:{}, and type is:{}, the value:{} and type is:{}".format(e,a,type(a),b,type(b)))

d = add(1,"3")
print(d)
print("this is to check this training")

