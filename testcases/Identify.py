import pytesseract
import testcases
from PIL import Image


if __name__ == '__main__':
    text = pytesseract.image_to_string(Image.open("test.png"),lang="eng")
    print(text)