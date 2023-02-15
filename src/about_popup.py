# Functions to create "About CIEPaperFinder" popup window.

import tkinter as tk  # to create about popup
from tkinter import ttk  # to create button

import os  # for icon path manipulation
import sys  # for executable file compatibility

import webbrowser  # to open repository link


# Function to open link to GitHub
def open_repo():
    webbrowser.open_new_tab("https://github.com/Ali246801232/CIEPaperFinder")


# Function to show information about program
def show_about(root):
    # Create 'About' popup
    about = tk.Toplevel(root)
    about.title("About CIEPaperFinder")
    about.config(bg="#262626")

    # Make sure new window is focused.
    about.grab_set()
    about.focus_set()

    # Create file path for popup icon
    if getattr(sys, 'frozen', False):
        icon_path = os.path.join(os.path.dirname(sys.executable), "paperfindericon.ico")
    else:
        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "paperfindericon.ico")

    # Set window icon
    about.iconbitmap(icon_path)

    # Display 'About' text
    tk.Label(
        about,
        text="CIEPaperFinder v1.0.0\n\nCIEPaperFinder is a Python-based graphical user interface (GUI) program that enables users to access and download Cambridge International Examinations (CIE) past papers and resources from a range of 101 IGCSE subjects, 51 O Level subjects, and 81 AS & A Level subjects.\n\nTo download a paper, simply input the required details and press the 'Download File' button and select a download location.\n\nFor more information about the program, please visit the GitHub repository by clicking the button below.",
        background="#262626",
        foreground="white",
        font=("Helvetica", 10),
        wraplength=256
    ).pack()

    # Button to redirect to GitHub repository
    github_button = ttk.Button(about, text="Open GitHub", command=lambda: open_repo())
    github_button.pack(pady=10)

    about.mainloop()
