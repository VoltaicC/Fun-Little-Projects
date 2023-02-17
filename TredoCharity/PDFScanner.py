import PyPDF2

# Open the PDF file
pdf_file = open('CONTENDER_495.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Initialize the counter dictionary
keyword_count = {}

# Define the list of keywords
keywords = ['EMOJI', 'SEX', 'LOVE']

# Loop through each page in the PDF file
for page_num in range(len(pdf_reader.pages)):
    # Get the text from this page
    page_obj = pdf_reader.pages[page_num]
    page_text = page_obj.extract_text()
    page_text = page_text.upper()
    

    for keyword in keywords:
        # Search for the keyword in this page's text
        if keyword in page_text:
            # If the keyword is found, increment the counter
            if keyword not in keyword_count:
                keyword_count[keyword] = 1
            else:
                keyword_count[keyword] += page_text.count(keyword)


# Output the number of times the keyword was found
for keyword, count in keyword_count.items():
    print(f"The keyword '{keyword}' was found {count} times in the PDF file.")
