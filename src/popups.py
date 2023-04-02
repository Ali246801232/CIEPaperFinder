import tkinter as tk  # to create about popup
from tkinter import ttk  # to create button

import os  # for icon path manipulation
import sys  # for executable file compatibility

import webbrowser  # to open button links

from gui import root  # to create popup


# Function to show popup with latest version
def show_version(latest_version):
    # Create new version popup
    version = tk.Toplevel(root)
    version.title("New Version Available")
    version.config(bg="#262626")

    # Make sure new window is focused.
    version.grab_set()
    version.focus_set()

    # Create file path for window icon
    if getattr(sys, 'frozen', False):
        icon_path = os.path.join(os.path.dirname(sys.executable), "paperfindericon.ico")
    else:
        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "paperfindericon.ico")

    # Set window icon
    version.iconbitmap(icon_path)

    # Display version text
    tk.Label(
        version,
        text=f"A new version of CIEPaperFinder ({latest_version}) is available. If you would like to download it, please click the button below to visit the GitHub releases page.",
        background="#262626",
        foreground="white",
        font=("Helvetica", 10),
        wraplength=256
    ).pack()

    # Button to redirect to GitHub repository
    releases_button = ttk.Button(version, text="Open Releases Page", command=lambda: webbrowser.open_new_tab("https://github.com/Ali246801232/CIEPaperFinder/releases"))
    releases_button.pack(pady=10)

    # Button to cancel

    version.mainloop()

# Function to display popup with error message
def show_error(message):
    # Create error popup
    error = tk.Toplevel()
    error.title("Error")
    error.config(bg="#262626")

    # Make sure new window is focused.
    error.grab_set()
    error.focus_set()

    # Create file path for popup icon
    if getattr(sys, 'frozen', False):
        icon_path = os.path.join(os.path.dirname(sys.executable), "paperfindericon.ico")
    else:
        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "paperfindericon.ico")

    # Set window icon
    error.iconbitmap(icon_path)

    # Display error message
    tk.Label(
        error,
        text=message,
        background="#262626",
        foreground="white",
        font=("Helvetica", 10),
        wraplength=256
    ).pack()

    ok_button = ttk.Button(error, text="OK", command=lambda: error.destroy())
    ok_button.pack()

    error.mainloop()

# Function to show popup with information about program
def show_about(current_version):
    # Create about popup
    about = tk.Toplevel(root)
    about.title("About CIEPaperFinder")
    about.config(bg="#262626")

    # Make sure new window is focused.
    about.grab_set()
    about.focus_set()

    # Create file path for winidow icon
    if getattr(sys, 'frozen', False):
        icon_path = os.path.join(os.path.dirname(sys.executable), "paperfindericon.ico")
    else:
        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "paperfindericon.ico")

    # Set window icon
    about.iconbitmap(icon_path)

    # Display about text
    tk.Label(
        about,
        text=f"CIEPaperFinder {current_version}\n\nCIEPaperFinder is a Python-based graphical user interface (GUI) program that enables users to access and download Cambridge International Examinations (CIE) past papers and resources from a range of 101 IGCSE subjects, 51 O Level subjects, and 81 AS & A Level subjects.\n\nTo download a paper, simply input the required details and press the 'Download File' button and select a download location.\n\nFor more information about the program, please visit the GitHub repository by clicking the button below.",
        background="#262626",
        foreground="white",
        font=("Helvetica", 10),
        wraplength=256
    ).pack()

    # Button to redirect to GitHub repository
    github_button = ttk.Button(about, text="Open GitHub", command=lambda: webbrowser.open_new_tab("https://github.com/Ali246801232/CIEPaperFinder"))
    github_button.pack(pady=10)

    about.mainloop()
