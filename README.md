# Background Remover with GUI 🖼️

A Python-based desktop application to remove backgrounds from images using AI-powered background removal. The tool provides a simple and user-friendly interface built with `Tkinter`, allowing users to choose between transparent and solid background options, preview results, and save the output.

---

## ✨ Features

- 📤 Upload `.jpg`, `.png`, or other image files.
- 🎯 Automatically detects and isolates the main subject using AI (powered by `rembg`).
- 🎨 Choose between:
  - Transparent background (PNG)
  - Solid color background (user-selected)
- 🖼️ View original and processed images side by side.
- 💾 Save the output image in desired format.
- ⚠️ Error message if no subject is detected.

---

## 🔧 Requirements

- Python 3.8+
- Libraries:
  - `rembg`
  - `pillow`
  - `opencv-python`
  - `tkinter` (usually comes with Python)
  - `numpy`
  - `numba==0.56.4` *(for compatibility)*

---

## 🛠️ Installation

```bash
# Clone this repo
git clone https://github.com/your-username/background-remover-gui.git
cd background-remover-gui

# Create and activate virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install --upgrade pip
pip install rembg==2.0.50 pillow opencv-python numpy==1.23.5 numba==0.56.4
