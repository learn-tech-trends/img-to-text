from PIL import Image
import pytesseract

def convert():
    im = Image.open(r'sample1.png')
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(im,lang = "eng")
    # text.replace("\n"," ")
    with open("message.txt","w") as file:
        file.write(text)
    print(text)
if __name__ == "__main__":
    convert()








