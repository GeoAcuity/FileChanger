import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime

# Function to find all .jpg and .jpeg files
def find_image_files(folder_directory):
    image_files = []
    for root, _, files in os.walk(folder_directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg')):
                image_files.append(os.path.join(root, file))
    return image_files

# Function to rename files and create a new folder
def rename_files_and_create_new_folder():
    folder_directory = folder_var.get()
    new_folder_directory = new_folder_var.get()
    location_of_collect = location_var.get()
    collection_platform = platform_var.get()
    date_of_collect = datetime.strptime(date_var.get(), '%m/%d/%y').strftime('%Y%m%d')

    # Set sequence number
    sequence_number = 1

    # Create a new folder
    folder_name = f"{location_of_collect}_{collection_platform}_{date_of_collect}"
    new_folder_path = os.path.join(new_folder_directory, folder_name)
    os.makedirs(new_folder_path, exist_ok=True)

    # Find all .jpg and .jpeg files
    image_files = find_image_files(folder_directory)

    # Move and rename files
    for file_path in image_files:
        file_ext = os.path.splitext(file_path)[1]
        new_filename = f"{folder_name}_{sequence_number}{file_ext}"
        new_file_path = os.path.join(new_folder_path, new_filename)
        shutil.copy(file_path, new_file_path)
        sequence_number += 1

    messagebox.showinfo("Success", "Images renamed and copied successfully.")

# Function to open folder browser
def browse_folder(var):
    folder_directory = filedialog.askdirectory()
    var.set(folder_directory)

# Create the main window
root = tk.Tk()
root.title("Rename Images")

# Create and set variables
folder_var = tk.StringVar()
new_folder_var = tk.StringVar()
location_var = tk.StringVar()
platform_var = tk.StringVar()
date_var = tk.StringVar()

# Create and place labels and entry widgets
tk.Label(root, text="Folder Directory:").grid(row=0, column=0, sticky="e")
tk.Entry(root, textvariable=folder_var, width=50).grid(row=0, column=1)
tk.Button(root, text="Browse", command=lambda: browse_folder(folder_var)).grid(row=0, column=2)

tk.Label(root, text="New Folder Directory:").grid(row=1, column=0, sticky="e")
tk.Entry(root, textvariable=new_folder_var, width=50).grid(row=1, column=1)
tk.Button(root, text="Browse", command=lambda: browse_folder(new_folder_var)).grid(row=1, column=2)

tk.Label(root, text="Location of Collect:").grid(row=2, column=0, sticky="e")
tk.Entry(root, textvariable=location_var).grid(row=2, column=1)

tk.Label(root, text="Collection Platform:").grid(row=3, column=0, sticky="e")
tk.Entry(root, textvariable=platform_var).grid(row=3, column=1)

tk.Label(root, text="Date of Collect:").grid(row=4, column=0, sticky="e")
date_entry = DateEntry(root, textvariable=date_var)
date_entry.grid(row=4, column=1)

# Create and place the button to run the function
tk.Button(root, text="Rename Images", command=rename_files_and_create_new_folder).grid(row=5, column=1)
root.mainloop()