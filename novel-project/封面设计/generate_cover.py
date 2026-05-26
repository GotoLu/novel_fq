"""
《歪打正着》封面生成器
使用Pillow生成小说封面图像
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import math
import random
import os

# 创建输出目录
os.makedirs("output", exist_ok=True)

# 画布尺寸 (1563x2500px, 300dpi)
WIDTH = 1563
HEIGHT = 2500
DPI = 300

# 色彩定义
COLORS = {
    "wisdom_blue": (43, 95, 138),      # #2B5F8A
    "energy_orange": (245, 166, 35),   # #F5A623
    "mystery_purple": (107, 91, 149),  # #6B5B95
    "dark_gray": (51, 51, 51),         # #333333
    "cream": (245, 240, 232),          # #F5F0E8
    "bright_yellow": (255, 215, 0),    # #FFD700
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "light_blue": (100, 150, 200),
    "soft_purple": (150, 130, 180),
}

def create_gradient_background(width, height, color1, color2, direction="vertical"):
    """创建渐变背景"""
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)
    
    for i in range(height if direction == "vertical" else width):
        ratio = i / (height if direction == "vertical" else width)
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        
        if direction == "vertical":
            draw.line([(0, i), (width, i)], fill=(r, g, b))
        else:
            draw.line([(i, 0), (i, height)], fill=(r, g, b))
    
    return img

def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    """绘制圆角矩形"""
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def draw_detective_character(draw, cx, cy, scale=1.0):
    """绘制李大嘴卡通形象"""
    s = scale
    
    # 身体（瘦高）
    body_w, body_h = int(180*s), int(400*s)
    body_x = cx - body_w//2
    body_y = cy - body_h//2 + 100
    
    # 西装（大两号，皱巴巴效果）
    suit_color = (80, 80, 100)
    draw.polygon([
        (body_x, body_y),
        (body_x + body_w, body_y),
        (body_x + body_w + 30, body_y + body_h),
        (body_x - 30, body_y + body_h),
    ], fill=suit_color, outline=(50, 50, 70), width=2)
    
    # 西装褶皱线
    for i in range(3):
        fx = body_x + 40 + i * 50
        draw.line([(fx, body_y + 50), (fx + 10, body_y + body_h - 50)], 
                  fill=(60, 60, 80), width=2)
    
    # 领带（歪的）
    tie_points = [
        (cx - 15, body_y + 20),
        (cx + 15, body_y + 20),
        (cx + 25, body_y + 120),
        (cx - 5, body_y + 120),
    ]
    draw.polygon(tie_points, fill=COLORS["energy_orange"], outline=(200, 130, 20), width=1)
    
    # 白衬衫
    shirt_w, shirt_h = int(100*s), int(80*s)
    draw.rounded_rectangle(
        [cx - shirt_w//2, body_y, cx + shirt_w//2, body_y + shirt_h],
        radius=10, fill=COLORS["white"], outline=(200, 200, 200), width=1
    )
    
    # 脖子
    neck_w, neck_h = int(40*s), int(50*s)
    draw.rounded_rectangle(
        [cx - neck_w//2, body_y - neck_h, cx + neck_w//2, body_y],
        radius=5, fill=(255, 220, 180), outline=(230, 190, 150), width=1
    )
    
    # 头部
    head_w, head_h = int(140*s), int(160*s)
    head_x = cx - head_w//2
    head_y = body_y - neck_h - head_h + 20
    
    # 脸型（瘦长）
    draw.ellipse([head_x, head_y, head_x + head_w, head_y + head_h], 
                 fill=(255, 220, 180), outline=(230, 190, 150), width=2)
    
    # 头发（乱糟糟中分）
    hair_color = (60, 50, 40)
    # 顶部头发
    draw.arc([head_x - 10, head_y - 30, head_x + head_w + 10, head_y + 60], 
             start=0, end=180, fill=hair_color, width=25)
    # 翘起的发丝
    for i in range(5):
        hx = head_x + 20 + i * 25
        hy = head_y - 10 - random.randint(5, 20)
        draw.line([(hx, head_y), (hx + random.randint(-10, 10), hy)], 
                  fill=hair_color, width=3)
    
    # 中分线
    draw.line([(cx, head_y), (cx, head_y + 40)], fill=hair_color, width=2)
    
    # 眉毛（不对称）
    draw.arc([cx - 45, head_y + 50, cx - 15, head_y + 70], 
             start=0, end=180, fill=hair_color, width=3)
    draw.arc([cx + 15, head_y + 48, cx + 45, head_y + 68], 
             start=0, end=180, fill=hair_color, width=3)
    
    # 眼睛（被放大镜片效果）
    eye_y = head_y + 75
    # 左眼
    draw.ellipse([cx - 40, eye_y - 15, cx - 10, eye_y + 15], 
                 fill=COLORS["white"], outline=(100, 100, 100), width=2)
    draw.ellipse([cx - 30, eye_y - 5, cx - 20, eye_y + 5], fill=COLORS["dark_gray"])
    # 右眼
    draw.ellipse([cx + 10, eye_y - 15, cx + 40, eye_y + 15], 
                 fill=COLORS["white"], outline=(100, 100, 100), width=2)
    draw.ellipse([cx + 20, eye_y - 5, cx + 30, eye_y + 5], fill=COLORS["dark_gray"])
    
    # 眼镜（厚圆镜片，滑到鼻尖）
    glass_y = eye_y + 10
    # 左镜片
    draw.ellipse([cx - 55, glass_y - 25, cx - 5, glass_y + 25], 
                 outline=(80, 80, 80), width=4)
    # 右镜片
    draw.ellipse([cx + 5, glass_y - 25, cx + 55, glass_y + 25], 
                 outline=(80, 80, 80), width=4)
    # 鼻梁架
    draw.line([(cx - 5, glass_y), (cx + 5, glass_y)], fill=(80, 80, 80), width=3)
    # 镜腿
    draw.line([(cx - 55, glass_y), (cx - 65, glass_y - 20)], fill=(80, 80, 80), width=3)
    draw.line([(cx + 55, glass_y), (cx + 65, glass_y - 20)], fill=(80, 80, 80), width=3)
    
    # 鼻子
    draw.polygon([
        (cx, glass_y + 25),
        (cx - 8, glass_y + 45),
        (cx + 8, glass_y + 45),
    ], fill=(255, 200, 160), outline=(230, 180, 140), width=1)
    
    # 嘴巴（歪嘴笑）
    mouth_y = glass_y + 55
    draw.arc([cx - 25, mouth_y - 10, cx + 25, mouth_y + 10], 
             start=200, end=340, fill=(200, 80, 80), width=3)
    
    # 手（手指抵下巴 - 福尔摩斯姿势）
    hand_x = cx + 80
    hand_y = body_y + 30
    # 手臂
    draw.line([(cx + 90, body_y + 20), (hand_x, hand_y)], 
              fill=(255, 220, 180), width=15)
    # 手指
    for i in range(3):
        fx = hand_x + i * 8
        draw.line([(hand_x, hand_y), (fx, hand_y - 20)], 
                  fill=(255, 220, 180), width=6)
    
    # 腿（细长腿）
    leg_w = int(30*s)
    leg_h = int(200*s)
    # 左腿
    draw.rounded_rectangle(
        [cx - 50, body_y + body_h, cx - 50 + leg_w, body_y + body_h + leg_h],
        radius=5, fill=(60, 60, 80), outline=(40, 40, 60), width=1
    )
    # 右腿
    draw.rounded_rectangle(
        [cx + 20, body_y + body_h, cx + 20 + leg_w, body_y + body_h + leg_h],
        radius=5, fill=(60, 60, 80), outline=(40, 40, 60), width=1
    )
    
    # 鞋子（大码）
    shoe_w, shoe_h = int(50*s), int(25*s)
    draw.ellipse([cx - 65, body_y + body_h + leg_h - 5, cx - 5, body_y + body_h + leg_h + shoe_h], 
                 fill=(40, 40, 40), outline=(20, 20, 20), width=2)
    draw.ellipse([cx + 5, body_y + body_h + leg_h - 5, cx + 65, body_y + body_h + leg_h + shoe_h], 
                 fill=(40, 40, 40), outline=(20, 20, 20), width=2)

def draw_flying_papers(draw, count=8):
    """绘制飞舞的纸张"""
    for i in range(count):
        x = random.randint(50, WIDTH - 150)
        y = random.randint(100, HEIGHT - 400)
        w = random.randint(60, 120)
        h = random.randint(80, 150)
        angle = random.randint(-30, 30)
        
        # 纸张颜色
        paper_color = (250, 248, 240)
        
        # 绘制旋转的矩形（简化）
        draw.rectangle([x, y, x + w, y + h], fill=paper_color, 
                      outline=(200, 200, 200), width=1)
        
        # 纸张上的文字线
        for j in range(3):
            ly = y + 20 + j * 20
            draw.line([(x + 10, ly), (x + w - 10, ly)], fill=(180, 180, 180), width=1)

def draw_arrows(draw, count=6):
    """绘制错乱箭头"""
    for i in range(count):
        x = random.randint(100, WIDTH - 100)
        y = random.randint(200, HEIGHT - 600)
        length = random.randint(50, 150)
        angle = random.randint(0, 360)
        
        color = random.choice([
            COLORS["energy_orange"],
            COLORS["bright_yellow"],
            COLORS["light_blue"],
        ])
        
        # 箭头线
        end_x = x + int(length * math.cos(math.radians(angle)))
        end_y = y + int(length * math.sin(math.radians(angle)))
        draw.line([(x, y), (end_x, end_y)], fill=color, width=4)
        
        # 箭头头部
        arrow_size = 15
        draw.polygon([
            (end_x, end_y),
            (end_x - arrow_size, end_y - arrow_size//2),
            (end_x - arrow_size, end_y + arrow_size//2),
        ], fill=color)

def draw_question_marks(draw, count=5):
    """绘制问号"""
    try:
        font = ImageFont.truetype("msyh.ttc", 60)
    except:
        font = ImageFont.load_default()
    
    for i in range(count):
        x = random.randint(100, WIDTH - 100)
        y = random.randint(150, HEIGHT - 500)
        color = random.choice([
            COLORS["mystery_purple"],
            COLORS["energy_orange"],
            COLORS["bright_yellow"],
        ])
        draw.text((x, y), "?", fill=color, font=font)

def draw_inverted_magnifier(draw, cx, cy, size=100):
    """绘制倒置放大镜"""
    # 镜片（倒置）
    draw.ellipse([cx - size, cy - size, cx + size, cy + size], 
                 outline=COLORS["energy_orange"], width=5)
    draw.ellipse([cx - size + 10, cy - size + 10, cx + size - 10, cy + size - 10], 
                 outline=COLORS["bright_yellow"], width=2)
    
    # 手柄（向上）
    handle_points = [
        (cx - 15, cy - size),
        (cx + 15, cy - size),
        (cx + 10, cy - size - 80),
        (cx - 10, cy - size - 80),
    ]
    draw.polygon(handle_points, fill=(100, 80, 60), outline=(80, 60, 40), width=2)
    
    # 镜片里的问号
    try:
        font = ImageFont.truetype("msyh.ttc", 80)
    except:
        font = ImageFont.load_default()
    draw.text((cx - 25, cy - 35), "?", fill=COLORS["mystery_purple"], font=font)

def draw_title(draw):
    """绘制标题文字"""
    # 尝试加载中文字体
    fonts_to_try = [
        "msyh.ttc",
        "simhei.ttf",
        "simsun.ttc",
        "C:/Windows/Fonts/msyh.ttc",
        "C:/Windows/Fonts/simhei.ttf",
    ]
    
    title_font = None
    subtitle_font = None
    author_font = None
    
    for font_path in fonts_to_try:
        try:
            title_font = ImageFont.truetype(font_path, 120)
            subtitle_font = ImageFont.truetype(font_path, 50)
            author_font = ImageFont.truetype(font_path, 40)
            break
        except:
            continue
    
    if not title_font:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        author_font = ImageFont.load_default()
    
    # 主标题
    title = "歪理侦探正着破案"
    title_y = HEIGHT - 480
    
    # 标题阴影
    draw.text((WIDTH//2 + 4, title_y + 4), title, 
              fill=(0, 0, 0), font=title_font, anchor="mm")
    # 标题主体 - 白色
    draw.text((WIDTH//2, title_y), title, 
              fill=COLORS["white"], font=title_font, anchor="mm")
    # 标题描边 - 橙色
    draw.text((WIDTH//2, title_y), title, 
              fill=COLORS["white"], font=title_font, anchor="mm", 
              stroke_width=3, stroke_fill=COLORS["energy_orange"])
    
    # 副标题
    subtitle = "推理全错，破案全对"
    subtitle_y = HEIGHT - 350
    draw.text((WIDTH//2, subtitle_y), subtitle, 
              fill=COLORS["bright_yellow"], font=subtitle_font, anchor="mm",
              stroke_width=2, stroke_fill=COLORS["dark_gray"])
    
    # 标签语
    tagline = "【番茄小说 · 幽默推理】"
    tagline_y = HEIGHT - 280
    draw.text((WIDTH//2, tagline_y), tagline, 
              fill=COLORS["light_blue"], font=author_font, anchor="mm")
    
    # 作者名
    author = "作者：XXX"
    author_y = HEIGHT - 180
    draw.text((WIDTH//2, author_y), author, 
              fill=COLORS["cream"], font=author_font, anchor="mm")

def draw_crack_effect(draw):
    """绘制裂缝错位效果"""
    crack_x = WIDTH // 2
    
    # 锯齿状裂缝
    points = []
    y = 100
    while y < HEIGHT - 500:
        offset = random.randint(-15, 15)
        points.append((crack_x + offset, y))
        y += random.randint(20, 40)
    
    if len(points) > 1:
        draw.line(points, fill=COLORS["bright_yellow"], width=3)
        # 裂缝发光效果
        draw.line(points, fill=(255, 255, 200), width=1)

def draw_case_silhouette(draw):
    """绘制案件现场剪影"""
    # 左侧：悬疑元素剪影
    # 建筑物剪影
    building_color = (30, 40, 60)
    
    # 建筑1
    draw.rectangle([50, HEIGHT - 800, 200, HEIGHT - 400], 
                   fill=building_color, outline=(20, 30, 50), width=2)
    # 窗户
    for row in range(4):
        for col in range(2):
            wx = 70 + col * 60
            wy = HEIGHT - 780 + row * 80
            is_lit = random.choice([True, False])
            color = COLORS["bright_yellow"] if is_lit else (40, 50, 70)
            draw.rectangle([wx, wy, wx + 30, wy + 50], fill=color, outline=(30, 40, 60), width=1)
    
    # 建筑2
    draw.rectangle([200, HEIGHT - 700, 350, HEIGHT - 400], 
                   fill=(35, 45, 65), outline=(25, 35, 55), width=2)
    
    # 右侧：喜剧元素
    # 夸张的放大镜剪影
    draw.ellipse([WIDTH - 250, HEIGHT - 750, WIDTH - 100, HEIGHT - 600], 
                 outline=COLORS["energy_orange"], width=3)
    draw.line([(WIDTH - 175, HEIGHT - 600), (WIDTH - 175, HEIGHT - 500)], 
              fill=COLORS["energy_orange"], width=8)
    
    # 侦探帽剪影
    hat_points = [
        (WIDTH - 300, HEIGHT - 650),
        (WIDTH - 200, HEIGHT - 680),
        (WIDTH - 180, HEIGHT - 650),
        (WIDTH - 220, HEIGHT - 620),
        (WIDTH - 280, HEIGHT - 620),
    ]
    draw.polygon(hat_points, fill=(50, 60, 80), outline=(40, 50, 70), width=2)

def generate_cover():
    """生成封面图像"""
    print("开始生成封面...")
    
    # 创建渐变背景
    print("1. 创建渐变背景...")
    img = create_gradient_background(WIDTH, HEIGHT, 
                                      COLORS["wisdom_blue"], 
                                      COLORS["mystery_purple"])
    draw = ImageDraw.Draw(img)
    
    # 添加纹理效果
    print("2. 添加背景纹理...")
    for i in range(500):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.randint(1, 3)
        opacity = random.randint(20, 60)
        color = (255, 255, 255)
        draw.ellipse([x, y, x + size, y + size], fill=color)
    
    # 绘制案件剪影
    print("3. 绘制案件现场剪影...")
    draw_case_silhouette(draw)
    
    # 绘制裂缝效果
    print("4. 绘制裂缝错位效果...")
    draw_crack_effect(draw)
    
    # 绘制错乱箭头
    print("5. 绘制错乱箭头...")
    random.seed(42)  # 固定随机种子
    draw_arrows(draw, count=8)
    
    # 绘制飞舞的纸
    print("6. 绘制飞舞的纸张...")
    random.seed(123)
    draw_flying_papers(draw, count=10)
    
    # 绘制问号
    print("7. 绘制问号...")
    random.seed(456)
    draw_question_marks(draw, count=6)
    
    # 绘制倒置放大镜
    print("8. 绘制倒置放大镜...")
    draw_inverted_magnifier(draw, 200, 400, size=80)
    draw_inverted_magnifier(draw, WIDTH - 200, 350, size=60)
    
    # 绘制主角形象
    print("9. 绘制主角形象...")
    draw_detective_character(draw, WIDTH // 2, HEIGHT // 2 - 100, scale=1.2)
    
    # 绘制标题
    print("10. 绘制标题文字...")
    draw_title(draw)
    
    # 添加边框装饰
    print("11. 添加边框装饰...")
    border_width = 8
    draw.rectangle([20, 20, WIDTH - 20, HEIGHT - 20], 
                   outline=COLORS["energy_orange"], width=border_width)
    draw.rectangle([30, 30, WIDTH - 30, HEIGHT - 30], 
                   outline=COLORS["bright_yellow"], width=2)
    
    # 角落装饰
    corner_size = 60
    for x, y in [(40, 40), (WIDTH - 40, 40), (40, HEIGHT - 40), (WIDTH - 40, HEIGHT - 40)]:
        draw.ellipse([x - corner_size//2, y - corner_size//2, 
                     x + corner_size//2, y + corner_size//2], 
                     outline=COLORS["energy_orange"], width=3)
    
    print("封面绘制完成！")
    return img

def save_cover(img, base_name="cover"):
    """保存封面为多种格式"""
    # 保存为PNG（无损，支持透明）
    png_path = f"output/{base_name}.png"
    img.save(png_path, "PNG", dpi=(DPI, DPI))
    print(f"✅ PNG格式已保存: {png_path}")
    
    # 保存为JPG（压缩，适合网络）
    jpg_path = f"output/{base_name}.jpg"
    img_rgb = img.convert("RGB")
    img_rgb.save(jpg_path, "JPEG", quality=95, dpi=(DPI, DPI))
    print(f"✅ JPG格式已保存: {jpg_path}")
    
    # 保存缩略图
    thumb = img.copy()
    thumb.thumbnail((400, 640))
    thumb_path = f"output/{base_name}_thumb.jpg"
    thumb.save(thumb_path, "JPEG", quality=90)
    print(f"✅ 缩略图已保存: {thumb_path}")
    
    return png_path, jpg_path

def main():
    """主函数"""
    print("=" * 60)
    print("《歪打正着》封面生成器")
    print("=" * 60)
    print()
    
    # 生成封面
    img = generate_cover()
    
    # 保存
    print()
    print("保存文件...")
    png_path, jpg_path = save_cover(img, "歪打正着_封面")
    
    # 输出信息
    print()
    print("=" * 60)
    print("生成完成！")
    print("=" * 60)
    print(f"尺寸: {WIDTH}x{HEIGHT}px")
    print(f"分辨率: {DPI}dpi")
    print(f"PNG: {png_path}")
    print(f"JPG: {jpg_path}")
    print()
    print("提示：")
    print("- PNG格式适合印刷（无损质量）")
    print("- JPG格式适合网络发布（压缩体积）")
    print("- 如需更高质量，建议使用专业设计软件（Photoshop/Illustrator）")
    print("  根据此方案进行精修")

if __name__ == "__main__":
    main()
