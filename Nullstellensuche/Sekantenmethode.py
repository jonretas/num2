# Sekantenmethode
def Sekantenmethode(x0,x1,func,epsilon):
    fx0 = func(x0)
    fx1 = func(x1)
    while ((abs(fx1) > epsilon) and (abs(fx0-fx1) > epsilon)):
        tmp = x1
        x1 = x1 - fx1 * (x1-x0)/(fx1-fx0)
        x0 = tmp
        fx0 = fx1
        fx1 = func(x1)

    # Lösung
    return x1
