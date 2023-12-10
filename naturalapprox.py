def term(x, n):
    return (1/n)*((x/(1+x))**n)

def L(x, e = 10**(-6)):
    def heLper(n):
        if abs(term(x, n+1)) < e:
            return 0
        else:
            return term(x, n) + heLper(n+1)
    return heLper(x,e,1)


def print_mat(a11,a12,a13,a21,a22,a23,a31,a32,a33):
    mat, num0, num1 = [a11,a12,a13,a21,a22,a23,a31,a32,a33], 0, 0
    flot = False
    for i in range(2):
        if num1 != 1 and num0 != 2:
            flot = True
            break
        else:
            num0, num1 = 0,0
        for j in range(i, 9, 3):
            if j == 0:
                num0 += 1
            if j == 1:
                num1 += 1
    if flot:
        mat = [str(round(float(mat[i]), 1)) for i in range(len(mat))]
    else:
        mat = [str(int(mat[i])) for i in range(len(mat))]
    print("[", mat[0], mat[1], mat[2], "]")
    print("[", mat[3], mat[4], mat[5], "]")
    print("[", mat[6], mat[7], mat[8], "]")
