import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import zipfile
import os
import time

def animate_progress_bar():
    for i in range(101):
        progress_bar["value"] = i
        root.update_idletasks()
        time.sleep(0.02)

def unzip_file():
    file_path = filedialog.askopenfilename(filetypes=[("ZIP Files", "*.zip")])
    if not file_path:
        return
    # Show the selected file name in the label
    file_label.config(text=f"Selected ZIP File: {os.path.basename(file_path)}")
    
    extract_to = filedialog.askdirectory(title="Select Extraction Directory")
    if not extract_to:
        return
    try:
        progress_bar["value"] = 0
        animate_progress_bar()
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        messagebox.showinfo("Success", "ZIP extraction complete!")
    except Exception as e:
        messagebox.showerror("Error", f"ZIP extraction failed: {e}")

def zip_files():
    files = filedialog.askopenfilenames(title="Select Files to Zip")
    if not files:
        return
    # Show the selected files in the label
    file_label.config(text=f"Selected Files: {', '.join([os.path.basename(file) for file in files])}")
    
    save_path = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP Files", "*.zip")])
    if not save_path:
        return
    try:
        progress_bar["value"] = 0
        animate_progress_bar()
        with zipfile.ZipFile(save_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                zipf.write(file, os.path.basename(file))
        messagebox.showinfo("Success", "Files zipped successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Zipping failed: {e}")

root = tk.Tk()
root.title("ZIP Utility")
root.geometry("600x400")
root.resizable(True, True)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=20)

drop_label = tk.Label(frame, text="Choose an option below", pady=10)
drop_label.pack()

unzip_button = tk.Button(frame, text="Unzip File", command=unzip_file)
unzip_button.pack(pady=10)

zip_button = tk.Button(frame, text="Zip Files", command=zip_files)
zip_button.pack(pady=10)

progress_bar = ttk.Progressbar(frame, length=500, mode='determinate')
progress_bar.pack(pady=10)

# Label to display selected file(s)
file_label = tk.Label(frame, text="No file selected", pady=10)
file_label.pack()

root.mainloop()
