#!/usr/bin/env python3
"""Render the two exact three-bit slices of the four-input OR profile."""
from math import cos, sin, tau
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 640, 440
BG, CARD, RULE = "#0b1523", "#132338", "#354c65"
INK, MUTED, ACTIVE = "#eff8fe", "#bdd2e4", "#ffd284"
COUNTS = {0: "#93adc2", 3: "#74c3ff", 4: "#65dec2"}
FONTS = (
    (Path("/System/Library/Fonts/Supplemental"), "Arial.ttf", "Arial Bold.ttf"),
    (Path("/usr/share/fonts/truetype/dejavu"), "DejaVuSans.ttf", "DejaVuSans-Bold.ttf"),
)


def font(size, bold=False):
    for directory, regular, semibold in FONTS:
        path = directory / (semibold if bold else regular)
        if path.is_file():
            return ImageFont.truetype(str(path), size)
    raise RuntimeError("Arial or DejaVu Sans is required")


TITLE, TEXT, LABEL, LARGE = font(32, True), font(20), font(21, True), font(26, True)


def vote_count(mask):
    return sum(bool(mask & ~(1 << i)) for i in range(4))


def project(mask, angle, center):
    x, y, z = [1 if mask & (1 << i) else -1 for i in range(3)]
    x, z = x * cos(angle) + z * sin(angle), -x * sin(angle) + z * cos(angle)
    y, z = y * cos(.38) - z * sin(.38), y * sin(.38) + z * cos(.38)
    scale = 50 / (1 + .11 * z)
    return center + scale * x, 218 - scale * y, z


def draw_cube(draw, hidden, angle, choice, center):
    draw.rounded_rectangle((center - 140, 88, center + 140, 338),
                           14, fill=CARD, outline=RULE, width=1)
    draw.text((center, 109), f"Hidden X1 = {hidden}", fill=INK, font=LABEL, anchor="mt")
    points = [project(mask, angle, center) for mask in range(8)]
    edges = [(a, a ^ (1 << i)) for a in range(8) for i in range(3) if not a & (1 << i)]
    for a, b in sorted(edges, key=lambda e: -(points[e[0]][2] + points[e[1]][2])):
        draw.line((*points[a][:2], *points[b][:2]), fill=RULE, width=3)
    for mask in sorted(range(8), key=lambda m: -points[m][2]):
        x, y, z = points[mask]
        radius = 6.5 - z
        draw.ellipse((x - radius, y - radius, x + radius, y + radius),
                     fill=COUNTS[vote_count(2 * mask + hidden)])
    x, y, _ = points[choice]
    draw.ellipse((x - 14, y - 14, x + 14, y + 14), outline=ACTIVE, width=3)
    bits = str(hidden) + "".join(str((choice >> i) & 1) for i in range(3))
    draw.text((center, 310), f"{bits}  ·  {vote_count(2 * choice + hidden)}/4 vote 1",
              fill=ACTIVE, font=LABEL, anchor="mt")


def frame(index, total):
    angle = tau * index / total + .35
    choice = 0 if index < total * 3 / 4 else 1
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)
    draw.text((28, 18), "One parent is hidden", font=TITLE, fill=INK)
    draw.text((29, 57), "Same visible bits pair the highlighted contexts.", font=TEXT, fill=MUTED)
    draw_cube(draw, 0, angle, choice, 164)
    draw_cube(draw, 1, angle, choice, 476)
    zeros_cost = vote_count(2 * choice) + vote_count(2 * choice + 1)
    ones_cost = 8 - zeros_cost
    draw.text((WIDTH // 2, 362),
              f"Output 0 costs {zeros_cost}   ·   Output 1 costs {ones_cost}",
              font=LARGE, fill=INK, anchor="mt")
    draw.text((WIDTH // 2, 403), "All contexts: restricted 6  /  unrestricted 4",
              font=TEXT, fill=MUTED, anchor="mt")
    return image


def main():
    frames = [frame(i, 40) for i in range(40)]
    sample = Image.new("RGB", (WIDTH * 2, HEIGHT * 2))
    for i, source in enumerate(frames[::10]):
        sample.paste(source, ((i % 2) * WIDTH, (i // 2) * HEIGHT))
    palette = sample.quantize(colors=48)
    indexed = [image.quantize(palette=palette, dither=Image.Dither.NONE) for image in frames]
    target = Path(__file__).with_name("parent-context-fibers.gif")
    indexed[0].save(target, save_all=True, append_images=indexed[1:], duration=115,
                    loop=0, optimize=True)
    print(f"{target.name}: {len(frames)} frames, {target.stat().st_size} bytes")


if __name__ == "__main__":
    main()
