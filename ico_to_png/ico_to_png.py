from PIL import Image
import os

ico_path = "abc.ico"
output_dir = "output_png"

# 建立輸出資料夾
os.makedirs(output_dir, exist_ok=True)

img = Image.open(ico_path)

# 取得 ICO 裡所有尺寸
sizes = img.info.get("sizes", [])

print("ICO 內包含的尺寸：", sizes)

for size in sizes:
    width, height = size

    # 指定要取哪個尺寸
    img_size = img.copy()
    img_size = img_size.resize(size, Image.LANCZOS)

    output_path = os.path.join(
        output_dir, f"input_{width}x{height}.png"
    )

    img_size.save(output_path, format="PNG")
    print(f"已輸出 {output_path}")
