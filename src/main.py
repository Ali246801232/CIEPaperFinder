# CIEPaperFinder
# Author: Ali Irfan
# Date: Wednesday, 16/02/2023
# This program allows you to access and download CIE past papers from https://papers.gceguide.com.
# Simply enter the required details to quickly find and download your desired paper."

from tkinter import ttk  # to create button start GUI mainloop

from gui import root, paper_qual, paper_code, paper_session, paper_year, paper_type, paper_num  # for getting gui and inputs

from file_handler import create_link, open_link, show_error  # for download button
from about_popup import show_about  # for about button


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
about_button = ttk.Button(root, text="About CIEPaperFinder", command=lambda: show_about(root))
about_button.pack()

# Start GUI event loop
root.mainloop()
