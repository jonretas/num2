# Bisektionsmethode
def Bisektionsmethode(a, b, func, epsilon):
    fa = func(a)
    fb = func(b)
    while abs(a-b) > epsilon:
        m = (a+b)/2
        fm = func(m)
        if fm == 0:
            # print("Nullstelle: m = " + str(m))
            return m
        elif fa*fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm

    # Loesung
    # print("Nullstelle: m = " + str(m))
    return m
