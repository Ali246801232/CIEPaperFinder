# Code for creating the GUI interface and setting up user inputs.

import os  # for icon path manipulation
import sys  # for executable file compatibility

import tkinter as tk  # to create GUI
from tkinter import ttk  # to use enhanced widgets

import dictionaries  # for subject count

# Create root widget
root = tk.Tk()
root.title("CIEPaperFinder")
root.geometry("440x440")

# Create file path for window icon
if getattr(sys, 'frozen', False):
    icon_path = os.path.join(os.path.dirname(sys.executable), "paperfindericon.ico")
else:
    icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "paperfindericon.ico")

# Set window icon
root.iconbitmap(icon_path)

# Set background colour
root.config(bg="#262626")

# Create base style
style = ttk.Style()
style.configure("TLabel", background="#262626", foreground="white")

# Display title and number of supported subjects
ttk.Label(root, text="Welcome to CIEPaperFinder!", style="TLabel", font=("Helvetica", 20)).pack()
ttk.Label(root, text=str(len(dictionaries.IGCSE)) + " IGCSE subjects", style="TLabel", font=("Helvetica", 14)).pack()
ttk.Label(root, text=str(len(dictionaries.OLevel)) + " O Level subjects", style="TLabel", font=("Helvetica", 14)).pack()
ttk.Label(root, text=str(len(dictionaries.ALevel)) + " AS & A Level subjects", style="TLabel", font=("Helvetica", 14)).pack()

# Create qualification input box
ttk.Label(root, text="Qualification:", style="TLabel").pack()
paper_qual = ttk.Combobox(root, values=[
    "IGCSE",
    "O Level",
    "AS & A Level"
], width=35)
paper_qual.set("IGCSE")
paper_qual.pack()

# Create subject code input box
ttk.Label(root, text="Subject Code:", style="TLabel").pack()
paper_code = ttk.Entry(root, width=35)
paper_code.pack()

# Create paper season input box
ttk.Label(root, text="Exam Session:", style="TLabel").pack()
paper_session = ttk.Combobox(root, values=[
    "Feb/Mar",
    "May/Jun",
    "Oct/Nov"
], width=35)
paper_session.set("Feb/Mar")
paper_session.pack()

# Create paper year input box
ttk.Label(root, text="Paper Year:", style="TLabel").pack()
paper_year = ttk.Combobox(root, values=list(range(2000, 2023)), width=35)
paper_year.set(2000)
paper_year.pack()

# Create resource type input box
ttk.Label(root, text="Resource Type:", style="TLabel").pack()
paper_type = ttk.Combobox(root, values=[
    "Question Paper",
    "Marking Scheme",
    "Insert",
    "Transcript (Languages)",
    "Sound File (Languages)",
    "Candidate Cards (Languages)",
    "Confidential Instructions (Sciences)",
    "Pre-Release Material (Computer Science)",
    "Source Files (Computer Science / IT)",
    "Survey Map (Geography)"
], width=35)
paper_type.set("Question Paper")
paper_type.pack()

# Create paper number/variant input box
ttk.Label(root, text="Paper Number/Variant:", style="TLabel").pack()
paper_num = ttk.Entry(root, width=35)
paper_num.pack()
