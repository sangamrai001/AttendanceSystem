import tkinter as tk
from tkinter import filedialog
import subprocess
import shutil
import os
from datetime import datetime
from tkinter import font


def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        destination_folder = create_destination_folder()
        shutil.copy(file_path, destination_folder)
        status_label.config(text=f"Image {os.path.basename(file_path)} uploaded to {destination_folder}")
        run_button.config(state=tk.NORMAL)


def run_python_file():
    python_file_path = "main.py"  # Provide the path to your Python file here
    if os.path.exists(python_file_path):
        try:
            result = subprocess.run(["python", python_file_path], capture_output=True, text=True)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, result.stdout)
            output_text.insert(tk.END, result.stderr)
        except Exception as e:
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, f"Error: {str(e)}")
    else:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Error: Python file not found")


def create_destination_folder():
    today_date = datetime.now().strftime("%d-%m-%Y")
    folder_name = f"test_{today_date}"
    folder_path = os.path.join(os.getcwd(), folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


# Create the main window
window = tk.Tk()
window.title("Image Uploader and Python Runner")
window.geometry("1200x1200")  # Increase the dialog box size

# Create a custom font with an increased size
custom_font = font.Font(family="Helvetica", size=16, weight="bold")

# Increase the size and font of the label
status_label = tk.Label(window, text="", font=("Arial", 16))
status_label.pack(pady=10)

# Create and configure the "Browse Image" button
browse_button = tk.Button(window, text="Browse Image", command=browse_image, font=custom_font, width=15, height=3)
browse_button.pack(pady=10)

# Create a text widget to display the output
output_text = tk.Text(window, height=30, width=60)
output_text.pack(pady=10)

# Initially disable the "Run Python File" button
run_button = tk.Button(window, text="Run Python File", state=tk.DISABLED, command=run_python_file, font=custom_font, width=15, height=3)
run_button.pack(pady=10)

window.mainloop()
