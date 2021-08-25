import docx2txt
import os


def walk_folder(folder_path):
    for root, dir, files in os.walk(folder_path):
        for name in files:
            file_extension_check(os.path.join(root, name))


def file_extension_check(file_path):

    file_name_split = file_path.split(".")

    if file_name_split[-1] == "doc":
        extract_doc_image(file_path)

    elif file_name_split[-1] == "docx":
        extract_docx_image(file_path)

    elif file_name_split[-1] == "pdf":
        extract_pdf_image(file_path)

    elif file_name_split[-1] == "xls":
        extract_xls_image(file_path)

    elif file_name_split[-1] == "xlsx":
        extract_xlsx_image(file_path)

    else:
        pass


def extract_doc_image(file_path):
    pass


def extract_docx_image(file_path):
    pass


def extract_pdf_image(file_path):
    pass


def extract_xls_image(file_path):
    pass


def extract_xlsx_image(file_path):
    pass
