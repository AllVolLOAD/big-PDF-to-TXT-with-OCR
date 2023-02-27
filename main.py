import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from PIL import Image


ur_path_to_new_file = "name_file.txt"
PDF_file = Path(r"d_big_100p.pdf")
page_start = int(input('Input START page number :   '))
page_end = int(input('Input END page number   :   '))
language = str(input('Input LANGUAGE in PDF (rus/eng/fra)  :   '))


image_file_list = []


if platform.system() == "Windows":
    print('[1/4] win system was find')

    pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
    print('[2/4] tesseract was find')

    path_to_poppler_exe = Path(r"C:\poppler-23.01.0\Library\bin")
    print('[3/4] poppler was find')

    out_directory = Path(r"~\Desktop").expanduser()

if platform.system() == "Darwin":
    print('[1/4] mac system detected')

    pytesseract.pytesseract.tesseract_cmd = (r"/usr/local/bin/tesseract")
    print('[2/4] tesseract was find')

    path_to_poppler_exe = Path(r"/usr/local/bin/poppler-23.01.0/Library/bin")
    print('[3/4] poppler was find')

    out_directory = Path('~/Desktop').expanduser()

else:
    print('Your system not supported')
    exit()


text_file = out_directory / Path(ur_path_to_new_file)


def main(here_start, here_end, language_in_pdf):

    elem_num = 0
    count = here_start

    with TemporaryDirectory() as tempdir:

        print('[4/4] convertation cycle to poppler was start')
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

        for page_enumeration, page in enumerate(pdf_pages, start=1):

                filename = f"{tempdir}\page {page_enumeration:03}.jpg"

                page.save(filename, "JPEG")

                image_file_list.append(filename)

                with open(text_file, "a", encoding='utf-8') as output_file:

                    image_file = image_file_list[elem_num]

                    print(f"Page {count} is ready")

                    text = str(pytesseract.image_to_string(Image.open(image_file), lang=language_in_pdf))

                    text = text.replace("-\n", "")

                    output_file.write(text)

                    elem_num += 1

                    count += 1
        print('READY')


if __name__ == "__main__":

    main(page_start, page_end, language)

