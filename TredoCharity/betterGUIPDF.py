#pyinstaller --noconfirm --onedir --windowed --add-data "c:\users\conno\appdata\local\programs\python\python310\lib\site-packages/customtkinter;customtkinter/"  betterGUIPDF.py
import PyPDF2
from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")
# Create a tkinter window
root = ctk.CTk()
root.title("PDF Parser")

# Define a function to open the file dialog
def choose_file():
    filepath = ctk.filedialog.askopenfilename(filetypes=[('PDF files', '*.pdf')])
    file_path_entry.delete(0, ctk.END)
    file_path_entry.insert(0, filepath)

# Define a function to search for the keywords
def search_keywords():
    # Get the file path and keywords from the text boxes
    file_path = file_path_entry.get()
    keywords = [keyword.strip() for keyword in keyword_entry.get().upper().split(',')]

    # Create a PDF reader object
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Initialize the counter dictionary
    keyword_count = {}

    # Loop through each page in the PDF file
    for page_num in range(len(pdf_reader.pages)):
        # Get the text from this page
        page_obj = pdf_reader.pages[page_num]
        page_text = page_obj.extract_text().upper()


        # Loop through each keyword
        for keyword in keywords:
            # Search for the keyword in this page's text
            if keyword in page_text:
                # If the keyword is found, increment the counter
                if keyword not in keyword_count:
                    keyword_count[keyword] = 1
                else:
                    keyword_count[keyword] += page_text.count(keyword)

    # Output the number of times each keyword was found
    output_text.delete('1.0', ctk.END)
    for keyword, count in keyword_count.items():
        output_text.insert(ctk.END, f"The keyword '{keyword}' was found {count} times in the PDF file.\n")


    #vaporwave
    output_text.insert(ctk.END, "Of the " + str(len(keywords)) +" words searched, " + str(len(keyword_count)) + " found. " + str(100 * (len(keyword_count) / len(keywords))) + "%")
    






# Create the file path label and text box
file_path_label = ctk.CTkLabel(root, text="PDF file path:",font=("Arial", 20))
file_path_label.grid(row=0, column=0, padx=5, pady=5)
file_path_entry = ctk.CTkEntry(root, width=800,font=("Arial", 20))
file_path_entry.grid(row=0, column=1, padx=5, pady=5)
file_path_button = ctk.CTkButton(root, text="Choose file", command=choose_file,font=("Arial", 20))
file_path_button.grid(row=0, column=2, padx=5, pady=5)

# Create the keyword label and text box
keyword_label = ctk.CTkLabel(root,font=("Arial", 20), text="Keywords (comma-separated):")
keyword_label.grid(row=1, column=0, padx=5, pady=5)
keyword_entry = ctk.CTkEntry(root, width=800,font=("Arial", 20))
keyword_entry.grid(row=1, column=1, padx=5, pady=5)

# Create the search button
search_button = ctk.CTkButton(root, text="Search keywords", command=search_keywords,font=("Arial", 20))
search_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Create the output text box
output_text = ctk.CTkTextbox(root, height=800, width=800, font=("Arial", 20))
output_text.grid(row=3, column=0, columnspan=3, padx=5, pady=10, sticky="ew")

# Start the tkinter event loop
root.mainloop()
