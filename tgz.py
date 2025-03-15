import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import tarfile
import os

def extract_tgz(file_path, extract_to, progress_bar):
    try:
        with tarfile.open(file_path, 'r:gz') as tar:
            members = tar.getmembers()
            total_files = len(members)
            
            for i, member in enumerate(members):
                tar.extract(member, path=extract_to)
                progress_bar['value'] = (i + 1) / total_files * 100
                root.update_idletasks()
        messagebox.showinfo("Success", "Extraction complete!")
    except Exception as e:
        messagebox.showerror("Error", f"Extraction failed: {e}")

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("TGZ Files", "*.tgz")])
    if file_path:
        extract_to = filedialog.askdirectory(title="Select Extraction Directory")
        if extract_to:
            progress_bar['value'] = 0
            extract_tgz(file_path, extract_to, progress_bar)

root = tk.Tk()
root.title("TGZ Extractor")
root.geometry("500x250")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=20)

drop_label = tk.Label(frame, text="Click below to select a .tgz file and extract", pady=10)
drop_label.pack()

select_button = tk.Button(frame, text="Select TGZ File", command=open_file_dialog)
select_button.pack()

progress_bar = ttk.Progressbar(frame, length=400, mode='determinate')
progress_bar.pack(pady=10)

root.mainloop()
