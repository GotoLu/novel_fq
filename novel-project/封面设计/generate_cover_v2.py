"""
《歪理神探》发布版封面生成器。

使用 Pillow 生成文字准确、可直接用于后台预览的竖版封面。
当前版本为程序化占位成品：适合条件发布阶段使用；若后续有专业画师图，
可沿用本脚本的文字层和字段规范。
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import random


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)

WIDTH = 900
HEIGHT = 1200
DPI = 300

TITLE = "歪理神探"
VOLUME = "证据不会笑"
TAGLINE = "全警局都笑我，直到真相站在我这边"
BADGE = "轻喜探案"
RULE = "歪理只能指路  证据才能判人"

COLORS = {
    "ink": (18, 22, 28),
    "midnight": (26, 38, 54),
    "steel": (56, 78, 98),
    "paper": (236, 230, 218),
    "white": (250, 248, 242),
    "amber": (246, 177, 63),
    "gold": (255, 212, 97),
    "red": (192, 54, 43),
    "cyan": (115, 196, 220),
    "shadow": (6, 8, 12),
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/STHeiti Medium.ttc" if bold else "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Supplemental/Songti.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def gradient() -> Image.Image:
    img = Image.new("RGB", (WIDTH, HEIGHT), COLORS["ink"])
    px = img.load()
    for y in range(HEIGHT):
        yr = y / HEIGHT
        for x in range(WIDTH):
            xr = x / WIDTH
            glow = max(0, 1 - math.hypot(xr - 0.34, yr - 0.72) * 1.6)
            r = int(18 + 26 * yr + 52 * glow)
            g = int(22 + 32 * yr + 28 * glow)
            b = int(30 + 40 * yr + 8 * glow)
            px[x, y] = (r, g, b)
    return img


def add_noise(img: Image.Image) -> None:
    draw = ImageDraw.Draw(img, "RGBA")
    random.seed(20260604)
    for _ in range(2400):
        x = random.randint(0, WIDTH - 1)
        y = random.randint(0, HEIGHT - 1)
        alpha = random.randint(8, 24)
        draw.point((x, y), fill=(255, 255, 255, alpha))


def draw_evidence_board(draw: ImageDraw.ImageDraw) -> None:
    board = (70, 88, 830, 430)
    draw.rounded_rectangle(board, radius=18, fill=(232, 225, 212, 42), outline=(255, 255, 255, 70), width=2)
    draw.line((110, 168, 760, 168), fill=(255, 255, 255, 56), width=2)
    draw.line((110, 250, 725, 250), fill=(255, 255, 255, 40), width=2)
    draw.line((110, 330, 790, 330), fill=(255, 255, 255, 35), width=2)

    nodes = [(165, 155), (330, 105), (560, 158), (710, 108), (238, 310), (500, 285), (695, 330)]
    for i, p in enumerate(nodes):
        for q in nodes[i + 1 :]:
            if random.random() < 0.38:
                draw.line((p[0], p[1], q[0], q[1]), fill=(246, 177, 63, 62), width=2)
    for x, y in nodes:
        draw.ellipse((x - 8, y - 8, x + 8, y + 8), fill=COLORS["amber"] + (150,))
        draw.rounded_rectangle((x + 15, y - 18, x + 95, y + 32), radius=5, fill=(245, 240, 228, 95))
        draw.line((x + 25, y - 2, x + 82, y - 2), fill=(45, 55, 65, 75), width=2)
        draw.line((x + 25, y + 12, x + 68, y + 12), fill=(45, 55, 65, 52), width=2)


def draw_stairs(draw: ImageDraw.ImageDraw) -> None:
    for i in range(9):
        y = 760 + i * 36
        x1 = 0 + i * 28
        draw.polygon(
            [(x1, y), (WIDTH, y - 95), (WIDTH, y - 55), (x1, y + 40)],
            fill=(13 + i * 3, 18 + i * 3, 24 + i * 3, 180),
        )
        draw.line((x1, y, WIDTH, y - 95), fill=(255, 255, 255, 22), width=2)


def draw_speaker(draw: ImageDraw.ImageDraw) -> None:
    x, y = 120, 705
    draw.ellipse((x + 35, y + 255, x + 430, y + 315), fill=(0, 0, 0, 95))
    draw.rounded_rectangle((x, y, x + 390, y + 265), radius=34, fill=(24, 27, 31), outline=(105, 122, 130), width=4)
    draw.rounded_rectangle((x + 24, y + 26, x + 365, y + 235), radius=24, fill=(15, 17, 20), outline=(56, 66, 72), width=2)
    draw.ellipse((x + 55, y + 60, x + 190, y + 195), fill=(7, 9, 12), outline=(83, 96, 104), width=5)
    draw.ellipse((x + 220, y + 60, x + 345, y + 185), fill=(7, 9, 12), outline=(83, 96, 104), width=4)
    draw.rounded_rectangle((x + 260, y + 118, x + 374, y + 224), radius=12, fill=(44, 34, 22), outline=COLORS["gold"], width=3)

    for i in range(5):
        gx = x + 278 + i * 18
        gy = y + 142 + (i % 2) * 20
        draw.ellipse((gx, gy, gx + 34, gy + 18), fill=COLORS["gold"], outline=(255, 236, 172), width=2)
    draw.arc((x + 305, y + 122, x + 360, y + 190), 195, 350, fill=(255, 238, 175), width=4)

    ribbon = [(x + 55, y - 4), (x + 100, y + 16), (x + 80, y + 84), (x + 116, y + 160), (x + 72, y + 154), (x + 48, y + 78)]
    draw.line(ribbon, fill=COLORS["red"], width=12, joint="curve")
    draw.line(ribbon, fill=(255, 126, 96), width=3, joint="curve")


def draw_detective(draw: ImageDraw.ImageDraw) -> None:
    cx, cy = 585, 650
    draw.ellipse((cx - 110, cy + 300, cx + 165, cy + 350), fill=(0, 0, 0, 105))
    draw.polygon([(cx - 68, cy - 15), (cx + 72, cy - 30), (cx + 118, cy + 290), (cx - 100, cy + 290)], fill=(34, 42, 50), outline=(87, 101, 108), width=3)
    draw.polygon([(cx - 40, cy + 5), (cx + 40, cy - 8), (cx + 20, cy + 118), (cx - 24, cy + 112)], fill=(231, 227, 217))
    draw.polygon([(cx - 7, cy + 18), (cx + 20, cy + 16), (cx + 34, cy + 135), (cx + 6, cy + 158)], fill=COLORS["amber"])
    draw.ellipse((cx - 52, cy - 130, cx + 58, cy - 5), fill=(229, 191, 150), outline=(105, 76, 55), width=2)
    draw.pieslice((cx - 68, cy - 148, cx + 64, cy - 45), 185, 360, fill=(38, 31, 25))
    draw.arc((cx - 34, cy - 72, cx - 2, cy - 48), 185, 345, fill=(45, 40, 36), width=2)
    draw.arc((cx + 14, cy - 74, cx + 46, cy - 50), 185, 345, fill=(45, 40, 36), width=2)
    draw.ellipse((cx - 37, cy - 58, cx - 7, cy - 30), outline=(38, 42, 46), width=4)
    draw.ellipse((cx + 9, cy - 60, cx + 39, cy - 32), outline=(38, 42, 46), width=4)
    draw.line((cx - 7, cy - 44, cx + 9, cy - 46), fill=(38, 42, 46), width=3)
    draw.arc((cx - 21, cy - 24, cx + 28, cy + 8), 15, 145, fill=(116, 47, 41), width=3)

    draw.rounded_rectangle((cx + 74, cy + 20, cx + 178, cy + 168), radius=10, fill=(48, 58, 64), outline=(164, 180, 174), width=3)
    for i in range(4):
        draw.line((cx + 92, cy + 48 + i * 24, cx + 158, cy + 43 + i * 24), fill=(229, 223, 204), width=3)

    draw.polygon([(cx - 185, cy - 5), (cx - 102, cy + 42), (cx - 115, cy + 78), (cx - 210, cy + 22)], fill=(34, 42, 50))
    draw.ellipse((cx - 225, cy + 10, cx - 186, cy + 48), fill=(229, 191, 150))

    draw.polygon([(cx - 70, cy + 286), (cx - 28, cy + 286), (cx - 38, cy + 430), (cx - 92, cy + 430)], fill=(28, 33, 40))
    draw.polygon([(cx + 24, cy + 286), (cx + 70, cy + 286), (cx + 100, cy + 430), (cx + 46, cy + 430)], fill=(28, 33, 40))
    draw.ellipse((cx - 104, cy + 420, cx - 25, cy + 452), fill=(13, 15, 18))
    draw.ellipse((cx + 42, cy + 420, cx + 125, cy + 452), fill=(13, 15, 18))

    draw.polygon([(705, 466), (770, 518), (744, 840), (650, 818)], fill=(12, 18, 26, 150))
    draw.polygon([(458, 500), (394, 565), (415, 842), (503, 822)], fill=(12, 18, 26, 120))


def draw_text_center(draw, xy, text, fnt, fill, stroke=0, stroke_fill=(0, 0, 0), spacing=0):
    draw.text(xy, text, font=fnt, fill=fill, anchor="mm", stroke_width=stroke, stroke_fill=stroke_fill, spacing=spacing)


def draw_title(draw: ImageDraw.ImageDraw) -> None:
    title_font = font(155, bold=True)
    volume_font = font(54, bold=True)
    tag_font = font(32, bold=True)
    rule_font = font(28)
    badge_font = font(30, bold=True)

    draw.rounded_rectangle((54, 46, 224, 93), radius=18, fill=(246, 177, 63, 230))
    draw.text((139, 69), BADGE, font=badge_font, fill=(31, 27, 22), anchor="mm")

    draw.rounded_rectangle((84, 112, 816, 246), radius=28, fill=(8, 11, 15, 122), outline=(255, 255, 255, 55), width=2)
    draw_text_center(draw, (450, 176), TAGLINE, tag_font, COLORS["white"], stroke=2, stroke_fill=(0, 0, 0))

    title_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    td = ImageDraw.Draw(title_layer)
    draw_text_center(td, (464, 500), TITLE, title_font, COLORS["white"], stroke=8, stroke_fill=(4, 6, 10))
    draw_text_center(td, (464, 500), TITLE, title_font, (255, 245, 214), stroke=2, stroke_fill=COLORS["amber"])
    title_layer = title_layer.filter(ImageFilter.UnsharpMask(radius=1.5, percent=150))
    draw.bitmap((0, 0), title_layer, fill=None)

    draw.rounded_rectangle((248, 594, 652, 666), radius=24, fill=(12, 15, 20, 210), outline=(255, 212, 97, 180), width=3)
    draw_text_center(draw, (450, 630), VOLUME, volume_font, COLORS["gold"], stroke=2, stroke_fill=(20, 14, 4))

    draw.rounded_rectangle((152, 1075, 748, 1132), radius=20, fill=(6, 9, 13, 190), outline=(255, 255, 255, 38), width=2)
    draw_text_center(draw, (450, 1104), RULE, rule_font, (235, 238, 228), stroke=1, stroke_fill=(0, 0, 0))


def generate_cover() -> Image.Image:
    img = gradient().convert("RGBA")
    add_noise(img)
    draw = ImageDraw.Draw(img, "RGBA")
    draw_evidence_board(draw)
    draw_stairs(draw)
    draw_speaker(draw)
    draw_detective(draw)
    draw_title(draw)
    draw.rectangle((18, 18, WIDTH - 18, HEIGHT - 18), outline=(246, 177, 63, 175), width=5)
    draw.rectangle((31, 31, WIDTH - 31, HEIGHT - 31), outline=(255, 255, 255, 45), width=2)
    return img.convert("RGB")


def save(img: Image.Image) -> None:
    png = OUT / "歪理神探_封面_v1.png"
    jpg = OUT / "歪理神探_封面_v1.jpg"
    thumb = OUT / "歪理神探_封面_v1_thumb.jpg"
    img.save(png, "PNG", dpi=(DPI, DPI))
    img.save(jpg, "JPEG", quality=94, optimize=True, dpi=(DPI, DPI))
    small = img.copy()
    small.thumbnail((300, 400))
    small.save(thumb, "JPEG", quality=90, optimize=True)
    print(f"PNG: {png}")
    print(f"JPG: {jpg}")
    print(f"Thumb: {thumb}")


def main() -> None:
    random.seed(9042)
    img = generate_cover()
    save(img)


if __name__ == "__main__":
    main()
