def main():
    file_name = input("File name: ")
    if "." in file_name:
        file_name = file_name.split(".")
    else:
        return print("application/octet-stream")

    file_format = file_name[len(file_name) - 1]
    file_format = file_format.lower().strip()
    match file_format:
        case  "jpg" | "jpeg":
            print("image/jpeg")
        case "gif":
            print("image/gif")
        case "txt":
            print("text/plain")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")
main()