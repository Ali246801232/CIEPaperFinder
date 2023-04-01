# Functions to check program version and create "Newer Version Available" popup window.

import tkinter as tk  # to create about popup
from tkinter import ttk  # to create button

import os  # for icon path manipulation
import sys  # for executable file compatibility

import webbrowser  # to open repository link

import requests  # to make HTTP requests to GitHub API

from gui import root  # to create version popup
from file_handler import show_error  # to create error popup

#  Function to compare the current version with the latest version
def compare_version(current_version):
    # Fetch latest version from GitHub API
    repo = "Ali246801232/CIEPaperFinder"
    url = f"https://api.github.com/repos/{repo}/releases"

    # Check for latest version
    response = requests.get(url)
    if response.status_code == 200:
        releases = response.json()
        if releases:
            latest_version = releases[0]["tag_name"]
            # Compare versions and display message accordingly
            if latest_version != current_version:
                show_version(latest_version)
            return 0, "Success"
        else:
            return 1, "No releases were found. How did you even get the program?"
    else:
        return 1, "Failed to fetch version. You can continue to use the program, but it is recommended to check GitHub for newer versions. You can find the link to the repository by clicking the 'About CIEPaperFinder' button."


# Function to open link to the releases
def open_releases():
    webbrowser.open_new_tab("https://github.com/Ali246801232/CIEPaperFinder/releases")

# Function to show information about program
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
    releases_button = ttk.Button(version, text="Open Releases Page", command=lambda: open_releases())
    releases_button.pack(pady=10)

    # Button to cancel

    version.mainloop()