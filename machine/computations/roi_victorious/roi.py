n = [2212763594265, 16477842150, 141848091000]
fs = [1920130306020, 23837012100, 108714652200]

# g,m,c
g1,m1,c1 = fs
g,m,c = n

rfs = g1/c1/(1-m1/c1)
roi = g/c + 3*m/c*rfs

print(roi/25)
# 0.9393331434398695