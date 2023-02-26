# big-PDF-to-TXT-with-OCR

## for WINDOWS, read full/part of ur pdf, with tesseract ocr and write in txt

### INSTALL tesseract engine :

1. download 
 >https://github.com/UB-Mannheim/tesseract/wiki/Downloading-Tesseract-OCR-Engine
2. edit path in code
```
  pytesseract.pytesseract.tesseract_cmd = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
```
  
### INSTALL poppler :
  
  1. download
> https://github.com/oschwartz10612/poppler-windows/releases/download/v23.01.0-0/Release-23.01.0-0.zip
  2. unarhivate and move to separate directory
  3. ADD folder "bin" to PATH variable 
  4. edit path in the code to that directrory
 ```
 path_to_poppler_exe = Path(r"C:\poppler-23.01.0\Library\bin")
 ```
 
    
import libralies and adapt to yourself
    
    
    
