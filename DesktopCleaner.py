import os
import shutil

#----------------------------------------------------------------
# READ ME FIRST!
# Before running, you must specify the directories you want to use in the quotes below.
# For example: 
#   source_directory = r'C:/Users/johndoe/Desktop'
#   image_directory = r'C:/Users/johndoe/Documents/images'   
# Then simply uncomment the lines at the bottom of the script containing the cleaners you want to use.
#----------------------------------------------------------------

# Specify the directory where your files are located
source_directory = r''

# Specify the directory where you want your image files to be moved to.
image_directory = r''

# Specify the directory where you want your PDF files to be moved to.
pdf_directory = r''

# Specify the directory where you want your word documents to be moved to.
word_document_directory = r''

# Specify the directory where you want your text files to be moved to.
text_file_directory = r''


# Moves image files to a specified directory.
# Takes a source directory and a destination directory as arguments.
def cleanImages(source_directory, image_directory):

    files = os.listdir(source_directory)

    for file in files:
        if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg') or file.lower().endswith('.png'):
            # Construct the full path to the source file
            source_path = os.path.join(source_directory, file)
            # Move the file to the destination directory
            shutil.move(source_path, image_directory)

# Moves PDF files to a specified directory.
# Takes a source directory and a destination directory as arguments.
def cleanPDFs(source_directory, pdf_directory):

    files = os.listdir(source_directory)

    for file in files:
        if file.lower().endswith('.pdf'):
            # Construct the full path to the source file
            source_path = os.path.join(source_directory, file)
            # Move the file to the destination directory
            shutil.move(source_path, pdf_directory)

# Moves Word Documents to a specified directory.
# Takes a source directory and a destination directory as arguments.
def cleanWordDocs(source_directory, word_document_directory):

    files = os.listdir(source_directory)

    for file in files:
        if file.lower().endswith('.docx') or file.lower().endswith('.doc'):
            # Construct the full path to the source file
            source_path = os.path.join(source_directory, file)
            # Move the file to the destination directory
            shutil.move(source_path, word_document_directory)

# Moves Word Documents to a specified directory.
# Takes a source directory and a destination directory as arguments.
def cleanTextFiles(source_directory, text_document_directory):

    files = os.listdir(source_directory)

    for file in files:
        if file.lower().endswith('.txt'):
            # Construct the full path to the source file
            source_path = os.path.join(source_directory, file)
            # Move the file to the destination directory
            shutil.move(source_path, text_document_directory)

# UNCOMMENT THE CLEANERS YOU WANT TO USE AND RUN THE FILE.
#cleanImages(source_directory, image_directory)
#cleanPDFs(source_directory, pdf_directory)
#cleanWordDocs(source_directory, word_document_directory)
#cleanTextFiles(source_directory, text_file_directory)