import cmath

a = input()
jpos = a.find("j")
if(a[0] == "-"):
    startminus = a.find("-")
    sep = a.find('+', startminus)
    if (sep != -1):
        imaginary = float(a[sep:jpos])
    else:
        sep = a.find('-', startminus+1)
        imaginary = float(a[sep:jpos])
    real = float(a[:sep])
else:
    sep = a.find('+')
    if (sep != -1):
        imaginary = float(a[sep:jpos])
    else:
        sep = a.find('-')
        imaginary = float(a[sep:jpos])
    real = float(a[:sep])
res1 = cmath.phase(complex(real, imaginary))
res2 = abs(complex(real, imaginary))
print(res2)
print(res1)
