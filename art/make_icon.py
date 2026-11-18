"""Generates the Instant Respawn icon (original artwork): a heart with a respawn arrow and a lightning bolt."""
from PIL import Image, ImageDraw, ImageFilter
import math, os, sys

S = 1024
mask = Image.new("L", (S, S), 0)
ImageDraw.Draw(mask).rounded_rectangle([24, 24, S - 24, S - 24], radius=200, fill=255)

bg = Image.new("RGBA", (S, S))
top, bot = (58, 16, 28), (18, 6, 12)
d = ImageDraw.Draw(bg)
for y in range(S):
    t = y / (S - 1)
    d.line([(0, y), (S, y)], fill=tuple(int(top[i] * (1 - t) + bot[i] * t) for i in range(3)) + (255,))

art = Image.new("RGBA", (S, S), (0, 0, 0, 0))
a = ImageDraw.Draw(art)
cx, cy = S // 2, S // 2

# Circular respawn arrow (open ring with an arrowhead).
R, W = 360, 46
green = (110, 240, 140, 255)
a.arc([cx - R, cy - R, cx + R, cy + R], start=-60, end=250, fill=green, width=W)
ang = math.radians(-60)
tip_x, tip_y = cx + R * math.cos(ang), cy + R * math.sin(ang)
# Arrowhead pointing along the clockwise direction at the arc's start.
dirx, diry = -math.sin(ang), math.cos(ang)
nx, ny = math.cos(ang), math.sin(ang)
L, H = 110, 95
a.polygon([
    (tip_x - dirx * L * 0.2 + nx * H, tip_y - diry * L * 0.2 + ny * H),
    (tip_x - dirx * L * 0.2 - nx * H, tip_y - diry * L * 0.2 - ny * H),
    (tip_x - dirx * -L, tip_y - diry * -L),
], fill=green)

# Pixel-style heart in the middle.
heart = [
    "..XX...XX..",
    ".XXXX.XXXX.",
    "XXXXXXXXXXX",
    "XXXXXXXXXXX",
    "XXXXXXXXXXX",
    ".XXXXXXXXX.",
    "..XXXXXXX..",
    "...XXXXX...",
    "....XXX....",
    ".....X.....",
]
px = 44
hx0 = cx - len(heart[0]) * px // 2
hy0 = cy - len(heart) * px // 2 + 10
red, shine = (232, 40, 56, 255), (255, 140, 150, 255)
for r, row in enumerate(heart):
    for c, ch in enumerate(row):
        if ch == "X":
            col = shine if (r, c) in [(1, 1), (1, 2), (2, 1)] else red
            a.rectangle([hx0 + c * px, hy0 + r * px, hx0 + (c + 1) * px - 1, hy0 + (r + 1) * px - 1], fill=col)

# Lightning bolt over the heart = "instant".
bolt = [(560, 300), (420, 540), (510, 540), (450, 740), (620, 470), (525, 470), (600, 300)]
a.polygon([(x + 6, y + 8) for x, y in bolt], fill=(0, 0, 0, 120))
a.polygon(bolt, fill=(255, 214, 64, 255), outline=(255, 250, 210, 255), width=8)

glow = art.filter(ImageFilter.GaussianBlur(22))
out = Image.alpha_composite(bg, glow)
out = Image.alpha_composite(out, art)
out = Image.composite(out, Image.new("RGBA", (S, S), (0, 0, 0, 0)), mask)

dest = sys.argv[1]
out.resize((512, 512), Image.LANCZOS).save(os.path.join(dest, "logo-512.png"))
out.resize((128, 128), Image.LANCZOS).save(os.path.join(dest, "icon.png"))
