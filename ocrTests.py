try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

tessdata_dir_config = '--tessdata-dir "<C:\\Users\\Luis\\AppData\\Local\\Programs\\Python\\Python35\\Lib\\site' \
                      '-packages\\pytesseract>" '

print(pytesseract.image_to_string(Image.open('blurred numbers.png'), lang='dig2'))
