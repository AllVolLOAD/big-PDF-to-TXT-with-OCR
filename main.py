import random
import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from PIL import Image



PDF_file = Path(r"d_big_100p.pdf")
page_start = int(input('Input START page number :   '))
page_end = int(input('Input END page number   :   '))
language = str(input('Input LANGUAGE in PDF (rus/eng/fra)  :   '))
image_file_list = []


if platform.system() == "Windows":
    print('[1/5] win system was find')

    pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
    print('[2/5] tesseract was find')

    path_to_poppler_exe = Path(r"C:\poppler-23.01.0\Library\bin")
    print('[3/5] poppler was find')

    out_directory = Path(r"~\Desktop").expanduser()
else:
    out_directory = Path("~").expanduser()


text_file = out_directory / Path("out_text_" + str(random.randint(1, 10)) + ".txt")  # defense rewriting


def main(here_start, here_end, language_in_pdf):

    count = here_start

    with TemporaryDirectory() as tempdir:

        if platform.system() == "Windows":
            pdf_pages = convert_from_path(
                PDF_file,
                500,
                poppler_path=path_to_poppler_exe,
                first_page=here_start,
                last_page=here_end
            )
        else:
            pdf_pages = convert_from_path(PDF_file, 500)
        print('[4/5] cycle convertating to poppler was start')

        for page_enumeration, page in enumerate(pdf_pages, start=1):

                filename = f"{tempdir}\page {page_enumeration:03}.jpg"

                page.save(filename, "JPEG")

                image_file_list.append(filename)

        print('[5/5] cycle convertating img-txt was start')
        with open(text_file, "w", encoding='utf-8') as output_file:

            for image_file in image_file_list:

                print(f"Page {count} is ready")

                text = str(pytesseract.image_to_string(Image.open(image_file), lang=language_in_pdf))

                text = text.replace("-\n", "")

                output_file.write(text)

                count += 1


if __name__ == "__main__":

    main(page_start, page_end, language)
