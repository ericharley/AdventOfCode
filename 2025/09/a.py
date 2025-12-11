from itertools import combinations
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle

corners = []

lines = open('input.txt').read().split()
for line in lines:
  a,b = map(int,line.split(','))
  corners.append((a,b))

def area(a,b):
  return (1+abs(a[0]-b[0]))*(1+abs(a[1]-b[1]))

v = 0
for a,b in combinations(corners,2):
  if area(a,b) > v:
    v = area(a,b)
    max_a = a
    max_b = b

print(v)

def polygon_area(points):
    """
    points: list of (x, y) vertices in order around the polygon.
            Last point need NOT equal the first; we'll wrap automatically.
    Returns: area (non-negative float)
    """
    n = len(points)
    area2 = 0  # this will hold 2 * signed_area

    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]  # wrap to 0 at the end
        area2 += x1 * y2 - x2 * y1

    return abs(area2) / 2.0


def intersect_segment_with_vertical(p1, p2, x_const):
    (x1, y1), (x2, y2) = p1, p2
    if x1 == x2:  # parallel, no unique intersection
        return None
    t = (x_const - x1) / (x2 - x1)
    y = y1 + t * (y2 - y1)
    return (x_const, y)

def intersect_segment_with_horizontal(p1, p2, y_const):
    (x1, y1), (x2, y2) = p1, p2
    if y1 == y2:  # parallel
        return None
    t = (y_const - y1) / (y2 - y1)
    x = x1 + t * (x2 - x1)
    return (x, y_const)

def clip_polygon(poly, xmin, ymin, xmax, ymax):
    """Clip polygon poly (list of (x,y)) to axis-aligned rect [xmin,xmax]x[ymin,ymax]."""
    def clip_halfspace(poly, inside, intersect):
        if not poly:
            return []
        out = []
        n = len(poly)
        for i in range(n):
            S = poly[i]
            E = poly[(i + 1) % n]
            S_in = inside(S)
            E_in = inside(E)

            if S_in and E_in:
                # in -> in
                out.append(E)
            elif S_in and not E_in:
                # in -> out
                I = intersect(S, E)
                if I is not None:
                    out.append(I)
            elif not S_in and E_in:
                # out -> in
                I = intersect(S, E)
                if I is not None:
                    out.append(I)
                out.append(E)
            else:
                # out -> out: add nothing
                pass
        return out

    # 1. x >= xmin (left)
    poly = clip_halfspace(
        poly,
        inside=lambda p: p[0] >= xmin,
        intersect=lambda a, b: intersect_segment_with_vertical(a, b, xmin),
    )

    # 2. x <= xmax (right)
    poly = clip_halfspace(
        poly,
        inside=lambda p: p[0] <= xmax,
        intersect=lambda a, b: intersect_segment_with_vertical(a, b, xmax),
    )

    # 3. y >= ymin (bottom)
    poly = clip_halfspace(
        poly,
        inside=lambda p: p[1] >= ymin,
        intersect=lambda a, b: intersect_segment_with_horizontal(a, b, ymin),
    )

    # 4. y <= ymax (top)
    poly = clip_halfspace(
        poly,
        inside=lambda p: p[1] <= ymax,
        intersect=lambda a, b: intersect_segment_with_horizontal(a, b, ymax),
    )

    return poly

v = 0
h0 = 0
h = 0
for a,b in combinations(corners,2):
  if area(a,b) > v:
    h0 += 1
    xmin, xmax = sorted([a[0],b[0]])
    ymin, ymax = sorted([a[1],b[1]])
    if polygon_area(clip_polygon(corners, xmin, ymin, xmax, ymax)) == (xmax-xmin)*(ymax-ymin):
      h += 1
      v = area(a,b)
      max_a = a
      max_b = b

print(v)


poly_points = corners

# --- 2. Rectangle you want to overlay ---
# rectangle given by (xmin, ymin, xmax, ymax)
rx_min, ry_min = max_a
rx_max, ry_max = max_b

# --- 4. Plot ---
fig, ax = plt.subplots(figsize=(8, 8))

# blue background
ax.set_facecolor('#7399ff')   # pick any blue

# polygon (white fill, black outline)
poly_patch = Polygon(poly_points,
                     closed=True,
                     facecolor='white',
                     edgecolor='black',
                     linewidth=1.0)
ax.add_patch(poly_patch)

# rectangle (yellow outline, no fill)
rect_width  = rx_max - rx_min
rect_height = ry_max - ry_min
rect_patch = Rectangle((rx_min, ry_min),
                       rect_width, rect_height,
                       fill=False,
                       edgecolor='#ffd94d',   # light yellow
                       linewidth=1.5)
ax.add_patch(rect_patch)

# make it look nice
ax.set_aspect('equal', 'box')
ax.autoscale_view()

# optional: add a little padding around the shape
xmin = min(x for x, y in poly_points) - 1000
xmax = max(x for x, y in poly_points) + 1000
ymin = min(y for x, y in poly_points) - 1000
ymax = max(y for x, y in poly_points) + 1000
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

plt.show()
