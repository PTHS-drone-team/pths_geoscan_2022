import math
from string import Template
import shutil

step = math.pi / 12
dist = 2 * math.pi / 3

now = 0

coords = {0: [], 1: [], 2: [], 3: []}
for i in range(20):
    coords[0].append((0, 0, 1))
    coords[1].append((math.sin(now), math.cos(now), 0.5))
    coords[2].append((math.sin(now + dist), math.cos(now + dist), 0.5))
    coords[3].append((math.sin(now + 2 * dist), math.cos(now + 2 * dist), 0.5))
    now += step

for drone_n, list_coords in coords.items():
    out_coords = ""
    for i in range(20):
        x, y, z = list_coords[i]
        out_coords += f"{{{x}, {y}, {z}}},\n"
    d = {"list_coords": out_coords}

    out_path = f"output/{drone_n}.lua"
    shutil.copyfile("template.lua", out_path)

    with open(out_path, 'r') as f:
        src = Template(f.read())
        out_text = src.substitute(d)

    with open(out_path, 'w') as f:
        f.write(out_text)
