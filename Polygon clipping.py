import matplotlib.pyplot as plt
def inside(p, a, b):
    return (b[0]-a[0])*(p[1]-a[1]) - (b[1]-a[1])*(p[0]-a[0]) >= 0

def intersect(p1, p2, a, b):
    x1,y1 = p1; x2,y2 = p2
    x3,y3 = a; x4,y4 = b
    den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if den == 0: return None
    px = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / den
    py = ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / den
    return (px, py)

def suth_hodg(polygon, window):
    out = polygon
    for i in range(len(window)):
        new_out = []
        A, B = window[i], window[(i+1)%len(window)]
        for j in range(len(out)):
            P, Q = out[j], out[(j+1)%len(out)]
            if inside(Q, A, B):
                if not inside(P, A, B):
                    new_out.append(intersect(P, Q, A, B))
                new_out.append(Q)
            elif inside(P, A, B):
                new_out.append(intersect(P, Q, A, B))
        out = new_out
    return out

polygon = [(50,150),(200,50),(350,150),(350,300),
           (250,300),(200,250),(150,350),(100,250),(100,200)]
window  = [(100,100),(300,100),(300,300),(100,300)]

clipped = suth_hodg(polygon, window)

plt.fill(*zip(*polygon), fill=False, edgecolor="blue", label="Original Polygon")
plt.plot(*zip(*(window+[window[0]])), "r--", label="Clipping Window")
if clipped: plt.fill(*zip(*clipped), color="lightgreen", alpha=0.6, label="Clipped Polygon")

plt.legend(); plt.title("Sutherland-Hodgman Polygon Clipping (Simple)")
plt.show()
