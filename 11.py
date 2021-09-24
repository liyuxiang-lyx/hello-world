a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
j = 0
v = 0
n = 0
m = 0
z = 0
x = 0
print("a b c")
print("d e f")
print("g h j")
a = int(input("a=?"))
c = int(input("c=?"))
h = int(input("h=?"))
print(a)
print(c)
print(h)
if a > c & a > h:
    if a != c & a != h:
        z = a+c
        x = a+h
        v = z+x
        print("总数等于:", v)
        if v % 2 == 0:
            n = int(v/2)
            print("加起来的总数应该是:", n)
            if v % 3 != 0:
                m = float(v/3)
                print("中间的大小应该是:", m)
            if v % 3 == 0:
                m = int(v/3)
                print("中间的大小应该是:", m)
        if v % 2 == 1:
            print("错误:无法整除")
if c > a & c > h:
    if c != a & c != h:
        z = c+a
        x = c+h
        v = z+x
        print("总数等于:", v)
        if v % 2 == 0:
            n = int(v/2)
            print("加起来的总数应该是:", n)
            if v % 3 != 0:
                m = float(v/3)
                print("中间的大小应该是:", m)
            if v % 3 == 0:
                m = int(v/3)
                print("中间的大小应该是:", m)
        if v % 2 == 1:
            print("错误:无法整除")
if h > c & h > a:
    if h != c & h != a:
        z = h+c
        x = h+a
        v = z+x
        print("总数等于:", v)
        if v % 2 == 0:
            n = int(v/2)
            print("加起来的总数应该是:", n)
            if v % 3 != 0:
                m = float(v/3)
                print("中间的大小应该是:", m)
            if v % 3 == 0:
                m = int(v/3)
                print("中间的大小应该是:", m)
        if v % 2 == 1:
            print("错误:无法整除")
