import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def convert_to_ico():
    # 開啟檔案選擇視窗
    file_path = filedialog.askopenfilename(
        title="選擇 PNG 檔案",
        filetypes=[("PNG Files", "*.png")]
    )
    
    if not file_path:
        return  # 使用者取消

    try:
        img = Image.open(file_path)
        img = img.convert("RGBA")  # 確保有透明通道
        
        # ICO 多尺寸
        sizes = [
            (16, 16),
            (32, 32),
            (48, 48),
            (256, 256)
        ]
        
        # 生成 ICO 路徑
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        save_path = os.path.join(os.path.dirname(file_path), f"{base_name}.ico")
        
        img.save(save_path, format="ICO", sizes=sizes)
        
        messagebox.showinfo("完成", f"轉換完成：\n{save_path}")
    except Exception as e:
        messagebox.showerror("錯誤", f"轉換失敗：{e}")

# 建立 GUI
root = tk.Tk()
root.title("PNG → ICO 小工具")
root.geometry("300x150")

label = tk.Label(root, text="建議選擇 256 * 256 像素的 PNG 圖片", pady=20)
label.pack()

btn = tk.Button(root, text="選擇圖片", command=convert_to_ico, width=25, height=2)
btn.pack()

root.mainloop()
