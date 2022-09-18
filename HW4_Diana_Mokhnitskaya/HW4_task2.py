a = 2
c = a * 2
print("first variant of multiplication:" + str(c))
c_bin = bin(a << 1)
print("second variant of multiplication:", int(c_bin, 2))

d = c//2
print("first variant of division:" + str(d))
d_bin = bin(c >> 1)
print("second variant of division:", int(d_bin, 2))
