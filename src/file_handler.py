# Functions for opening URLs, downloading files from URLs, and displaying errors.
# Functions return 0 for success, 1 for error w/ error message.

import requests  # to check for 404 pages

import tkinter as tk  # to create error popup
from tkinter import ttk  # to create "OK" button

from tkinter import filedialog  # for download file dialog

import os  # for icon path manipulation
import sys  # for executable file compatibility

import dictionaries  # for dictionaries of subjects and resource types


# Function to check details and create url
def create_link(f_qual, f_code, f_session, f_year, f_type, f_num):
    # Initialize url with website link
    file_url = "https://papers.gceguide.com/"

    # Check given qualification and subject code
    if f_qual == "IGCSE":
        url_qual = "Cambridge%20IGCSE/"
        try:
            url_sub = dictionaries.IGCSE[f_code]
        except KeyError:
            return 1, "Invalid or unsupported subject code"
    elif f_qual == "O Level":
        url_qual = "O%20Levels/"
        try:
            url_sub = dictionaries.OLevel[f_code]
        except KeyError:
            return 1, "Invalid or unsupported subject code"
    elif f_qual == "AS & A Level":
        url_qual = "A%20Levels/"
        try:
            url_sub = dictionaries.ALevel[f_code]
        except KeyError:
            return 1, "Invalid or unsupported subject code"
    else:
        return 1, "Invalid or unsupported qualification"

    # Check given exam session
    if f_session == "Feb/Mar":
        url_session = "m"
    elif f_session == "May/Jun":
        url_session = "s"
    elif f_session == "Oct/Nov":
        url_session = "w"
    else:
        return 1, "Invalid exam session"

    # Check given paper year
    if int(f_year) < 2000 or int(f_year) > 2022:
        return 1, "Invalid paper year"

    # Check given resource type
    try:
        if f_type != "Pre-Release Material (Computer Science)":
            url_type = dictionaries.ResourceTypes[f_type][0]
            url_extension = dictionaries.ResourceTypes[f_type][1]
        else:
            # Handle special case
            url_type = "pm"
            url_extension = ".pdf"
    except KeyError:
        return 1, "Invalid or unsupported resource type."

    # Check given paper number
    if len(str(f_num)) != 2 or not str(f_num).isnumeric:
        return 1, "Invalid paper number and/or variant. If it has one digit, like '1', try variations like '01'."

    # Create file name and url using given information
    file_name = f"{f_code}_{url_session}{f_year[2: 4]}_{url_type}_{f_num}{url_extension}"
    file_url += f"{url_qual}/{url_sub}/{f_year}/{file_name}"

    # Return final url
    return 0, file_url


# Function to check and open link to file
def open_link(file_url):
    # Check for and handle special case
    if "pm" in file_url:
        return_val = open_link_special(file_url)
        return return_val

    # Check HTTP status code
    try:
        response = requests.get(file_url)
    except requests.exceptions.RequestException:
        return 1, "Something went wrong"

    # Download file if found
    if response.status_code != 404:
        download_path = browse_path(file_url.split('/')[-1], file_url[-4:])
        if download_path:
            download_file(file_url, download_path)
            return 0, "Success."
        else:
            return 1, "Download cancelled."
    else:
        return 1, "The file does not exist or could not be found. Try checking the details you entered."


# Function to check and open link to file - Special Case
def open_link_special(file_url):
    # Check HTTP status code
    try:
        response_a = requests.get(file_url)
        response_b = requests.get(file_url.replace(".pdf", ".zip"))
    except requests.exceptions.RequestException:
        return 1, "Something went wrong."

    # Open either link if file found
    if response_a.status_code != 404:
        download_path = browse_path(file_url.split('/')[-1], file_url[-4:])
        if download_path:
            download_file(file_url, download_path)
            return 0, "Success."
        else:
            return 1, "Download cancelled."
    elif response_b.status_code != 404:
        download_path = browse_path(file_url.replace(".pdf", ".zip").split('/')[-1], file_url.replace(".pdf", ".zip")[-4:])
        if download_path:
            download_file(file_url.replace(".pdf", ".zip"), download_path)
            return 0, "Success."
        else:
            return 1, "Download cancelled."
    else:
        return 1, "The file does not exist or could not be found. Try checking the details you entered."


# Function to allow user to browse for download path
def browse_path(file_name, file_extension):
    # Create Toplevel window for file dialog
    file_dialog = tk.Toplevel()
    file_dialog.withdraw()

    # Browse file path from save dialog
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    file_path = filedialog.asksaveasfilename(initialdir=downloads_folder, initialfile=file_name, defaultextension=file_extension, filetypes=[(
                                                                                                                                             dictionaries.ExtensionMap[file_extension], f"*{file_extension}"), ("All files", "*.*")])
    file_dialog.destroy()

    # Return file path
    return file_path


# Function to download file
def download_file(file_url, file_path):
    response = requests.get(file_url)
    with open(file_path, 'wb') as file:
        file.write(response.content)


# Function to display error
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

    ok_button = ttk.Button(error, text="OK", command=lambda: close_window(error))
    ok_button.pack()

    error.mainloop()


# Function to close window
def close_window(window):
    window.destroy()
