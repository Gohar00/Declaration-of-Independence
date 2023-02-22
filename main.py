import PyPDF2

# Open PDF file in read_binary mode
pdf_file = open("US_Declaration.pdf", 'rb')

# Create a PdfReader object to read the file
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF
num_pages = len(pdf_reader.pages)

# Create an empty dictionary to store the state data
signers_dict = {}

# Loop through the pages of the PDF
for i in range(3, num_pages):

    # Get the current page object
    pdf_page = pdf_reader.pages[i]
    # Extract the text from the page
    text = pdf_page.extract_text()
    # Split the text into lines
    lines = text.split('\n')
    j = 0

    # Loop through the lines of the page
    while j < len(lines):
        # Check if the line contains a colon and does not start with a square bracket
        if ':' in lines[j] and not lines[j].startswith('['):
            # Get the state name from the line
            state = lines[j].strip(':')
            # Strip any whitespace from the state name and use it as the dictionary key
            key = state.strip()
            # Create an empty list to store the values(signers) for this state
            values = []
            j += 1
            # Loop through the lines until the next colon, square bracket, or blank space is encountered
            while j < len(lines) and (':' not in lines[j]) and not lines[j].startswith('[') and lines[j] not in ' ':
                values.append(lines[j].strip(" "))
                j += 1
            # If the state already exists in the dictionary, add the new values to the existing list
            if key in signers_dict:
                signers_dict[key].extend(values)
            # If the state is not already in the dictionary, create a new entry with the key and values
            else:
                signers_dict[key] = values
        # If the line does not contain a colon or starts with a square bracket, move to the next line
        else:
            j += 1

# Close the PDF file
pdf_file.close()

# Loop through the dictionary and print the state names and their signers associated
for i in signers_dict:
    print(i, signers_dict[i])







