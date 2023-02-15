# Dictionary for supported resource types and their extensions.
# This does not include special cases as they are handled separately.

ResourceTypes = {
    "Question Paper": ("qp", ".pdf"),
    "Marking Scheme": ("ms", ".pdf"),
    "Insert": ("in", ".pdf"),
    "Transcript (Languages)": ("qr", ".pdf"),
    "Sound File (Languages)": ("sf", ".mp3"),
    "Candidate Cards (Languages)": ("rp", ".pdf"),
    "Confidential Instructions (Sciences)": ("ci", ".pdf"),
    "Source Files (Computer Science / IT)": ("sf", ".zip"),
    "Survey Map (Geography)": ("i2", ".pdf")
}

ExtensionMap = {
    ".pdf": "Adobe Acrobat Document",
    ".mp3": "MP3 Format Sound",
    ".zip": "WinRAR ZIP archive"
}
