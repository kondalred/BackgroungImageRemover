import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk
from rembg import remove
import io
import cv2
import numpy as np

class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Remover")
        self.original_img = None
        self.processed_img = None
        self.bg_color = None
        self.use_transparent = tk.BooleanVar(value=True)
        self.setup_ui()

    def setup_ui(self):
        tk.Button(self.root, text="Upload Image", command=self.load_image, font=("Arial", 12), width=25, height=2).pack(pady=10)
        tk.Radiobutton(self.root, text="Transparent Background", variable=self.use_transparent, value=True, font=("Arial", 11)).pack()
        tk.Radiobutton(self.root, text="Solid Background", variable=self.use_transparent, value=False, font=("Arial", 11)).pack()
        tk.Button(self.root, text="Pick Background Color", command=self.pick_color, font=("Arial", 12), width=25, height=2).pack(pady=5)
        tk.Button(self.root, text="Remove Background", command=self.remove_background, font=("Arial", 12), width=25, height=2).pack(pady=10)
        tk.Button(self.root, text="Save Image", command=self.save_image, font=("Arial", 12), width=25, height=2).pack(pady=10)

        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack()
        self.original_label = tk.Label(self.canvas_frame)
        self.original_label.grid(row=0, column=0, padx=10)
        self.processed_label = tk.Label(self.canvas_frame)
        self.processed_label.grid(row=0, column=1, padx=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if not file_path:
            return
        self.original_img = Image.open(file_path).convert("RGBA")
        self.display_image(self.original_img, self.original_label)

    def pick_color(self):
        color_code = colorchooser.askcolor(title="Choose background color")[0]
        if color_code:
            self.bg_color = tuple(map(int, color_code))

    def remove_background(self):
        if self.original_img is None:
            messagebox.showerror("Error", "Please upload an image first.")
            return

        try:
            with io.BytesIO() as output_bytes:
                self.original_img.save(output_bytes, format="PNG")
                result = remove(output_bytes.getvalue())
                result_img = Image.open(io.BytesIO(result)).convert("RGBA")
            
            if not self.use_transparent.get():
                bg = Image.new("RGBA", result_img.size, self.bg_color if self.bg_color else (255, 255, 255, 255))
                bg.paste(result_img, mask=result_img)
                result_img = bg

            self.processed_img = result_img
            self.display_image(self.processed_img, self.processed_label)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image.\n{str(e)}")

    def save_image(self):
        if self.processed_img is None:
            messagebox.showerror("Error", "upload the image to save")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png")])
        if file_path:
            self.processed_img.save(file_path)
            messagebox.showinfo("Saved", "image saved successfully!")

    def display_image(self, img, widget):
        resized = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(resized)
        widget.image = img_tk
        widget.config(image=img_tk)

if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()
