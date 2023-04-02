# CIEPaperFinder
# Author: Ali Irfan
# Date: Saturday, 01/04/2023
# This program allows you to access and download CIE past papers from https://papers.gceguide.com.
# Simply enter the required details to quickly find and download your desired paper."

# Current version of the program
VERSION = "v0.1.0"

from tkinter import ttk  # to create button start GUI mainloop

from gui import root, paper_qual, paper_code, paper_session, paper_year, paper_type, paper_num  # to get gui and inputs

from file_handler import create_link, open_link  # for download button
from popups import show_about, show_error  # for about button and error popup


# Function to call relevant functions from file_handler.py
def button_press(f_qual, f_code, f_session, f_year, f_type, f_num):
    final_url = create_link(f_qual.get(), f_code.get(), f_session.get(), f_year.get(), f_type.get(), f_num.get())
    if final_url[0] == 1:
        show_error(final_url[1])
    elif final_url[0] == 0:
        link_opened = open_link(final_url[1])
        if link_opened[0] == 1:
            show_error(link_opened[1])
    else:
        show_error("Something went wrong.")


# Create download button and pass input values to file_handler.py
input_list = [paper_qual, paper_code, paper_session, paper_year, paper_type, paper_num]
download_button = ttk.Button(root, text="Download File", command=lambda: button_press(*input_list))
download_button.pack(pady=10)

# Create about button
about_button = ttk.Button(root, text="About CIEPaperFinder", command=lambda: show_about(VERSION))
about_button.pack()

# Version checking is below the rest of the code to make sure buttons are created first.
from version_checker import compare_version  # for version checking

# Call function from version_checker.py to compare versions
version_compared = compare_version(VERSION)
if version_compared[0] == 1:
    show_error(version_compared[1])

# Start GUI event loop
root.mainloop()
