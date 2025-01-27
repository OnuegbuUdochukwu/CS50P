fileName = input("File Name: ")

if fileName.endswith(".jpg") or fileName.endswith(".jpeg"):
    print("image/jpeg")
elif fileName.endswith(".pdf"):
    print("application/pdf")

    ...
    
else:
    print("application/octet-stream")


# Another method
def main():
    extension = input("Enter a file name with the extension: ").lower().strip()
    print(f"{name_extension(extension)}")

def name_extension(name):
    if name.endswith(".zip"):
        return "application/zip"

    elif name.endswith(".jpg") or name.endswith(".jpeg"):
        return "image/jpeg"

    elif name.endswith(".gif"):
        return "image/gif"

    elif name.endswith(".png"):
        return "image/png"

    elif name.endswith(".pdf"):
        return "application/pdf"

    elif name.endswith(".txt"):
        return "text/plain"

    # Return default MIME type if file type is not recognized
    else:
        return "application/octet-stream"


main()
