import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

output_dir = "output_png"

def convert_to_ico():
    # 開啟檔案選擇視窗
    file_path = filedialog.askopenfilename(
        title="選擇 ICO 檔案",
        filetypes=[("ICO Files", "*.ico")]
    )
    
    if not file_path:
        return  # 使用者取消

    try:
        # 建立輸出資料夾
        os.makedirs(output_dir, exist_ok=True)

        img = Image.open(file_path)

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
        
        messagebox.showinfo("完成", f"轉換完成，圖片存放至：\\{output_dir} 資料夾")
        print(f"轉換完成，圖片存放至：\\{output_dir} 資料夾")
    except Exception as e:
        messagebox.showerror("錯誤", f"轉換失敗：{e}")
        print(f"轉換失敗：{e}")

# 建立 GUI
root = tk.Tk()
root.title("ICO → PNG 小工具")
root.geometry("300x150")

label = tk.Label(root, text="請選擇 ICO 檔案", pady=20)
label.pack()

btn = tk.Button(root, text="選擇檔案", command=convert_to_ico, width=25, height=2)
btn.pack()

root.mainloop()
