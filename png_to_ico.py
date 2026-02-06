from PIL import Image

# 開啟 PNG
img = Image.open("abc.png")

# 轉成 RGBA（避免某些 PNG 沒透明通道）
img = img.convert("RGBA")

# 多尺寸 ICO
sizes = [
    (16, 16),
    (32, 32),
    (48, 48),
    (256, 256)
]

img.save("abc.ico", format="ICO", sizes=sizes)

print("轉換完成：icon.ico（含多尺寸）")
