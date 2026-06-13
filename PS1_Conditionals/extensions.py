# strip() removes accidental spaces, .lower() lowercases everything before any comparisons run
extensions= (input("File Name: ")).strip().lower()


# .endswith() checks only the tail of the string — the file extension
# .jpg and .jpeg are different extensions but the same image format, so they share one branch
if extensions.endswith(".jpg") or extensions.endswith(".jpeg"):
    print ("image/jpeg")        # MIME (Multipurpose Internet Mail Extensions) type — label telling the computer what kind of file this is and how to handle it
elif extensions.endswith(".pdf"): 
    print ("application/pdf") # MIME type for PDF documents
elif extensions.endswith(".gif"):
    print ("image/gif")       # MIME type for PDF documents
elif extensions.endswith(".png"):
    print ("image/png")         # MIME type for PNG image files
elif extensions.endswith(".txt"):
    print ("text/plain")        # MIME type for plain text files
elif extensions.endswith(".zip"):
    print ("application/zip")   # MIME type for ZIP archive files
    
#else is the catch-all — runs only if every condition above was False
# application/octet-stream means "unknown file type, treat as raw binary data"
else:
    print ("application/octet-stream") 

