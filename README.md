# PNG / ICO 檔案格式轉換 (Python)

這是一個練習用專案。

一個使用 **Python** 撰寫的工具，可將 **PNG 圖片** 轉換成 WINDOWS 系統使用的 **ICO 圖示文件格式**。

也可將 WINDOWS 系統使用的 **ICO 圖示文件格式** 轉換成 **PNG 圖片**。

支援在本機執行，並可透過 **PyInstaller** 打包成 Windows 可執行檔（`.exe`），方便一般使用者使用。

詳細請見: **/dist**

---

## 📌 專案功能

- 透過 `pillow` Python 圖片處理標準套件
- 可打包成單一 `.exe` 檔（不需安裝 Python）

---

## 🧰 使用技術

- Python 3
- pillow
- PyInstaller

---

## 🖥️ 環境需求

- Windows 作業系統
- Python 已安裝（僅開發與打包時需要）

---

## 🚀 使用方式

### STEP 01:
```bash
    py --version
    pip3 --version
```

### STEP 02
```bash
    pip3 install pillow
```

### STEP 03:
```bash
    pip install pyinstaller
    # 打包成exe檔
    pyinstaller --clean --onefile --windowed --icon="./png_to_ico/icon.ico" --name "PNG轉ICO" ./png_to_ico/png_to_ico_GUI.py
    pyinstaller --clean --onefile --windowed --icon="./ico_to_png/icon.ico" --name "ICO轉PNG" ./ico_to_png/ico_to_png_GUI.py
```