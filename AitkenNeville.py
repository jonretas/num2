# Aitkenneville
def AitkenNeville(x, y, x0):
    for k in range(1, len(y), 1):
        for j in range(len(y)-1, k-1, -1):
            y[j] = y[j]+(x0-x[j])/(x[j]-x[(j-k)])*(y[j]-y[j-1])
    return y[-1]
