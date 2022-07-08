from tkinter import *
from tkinter import filedialog
from PIL import Image
import pytesseract as pt
import os

global_directory = ''

def text_detection():
    global_keyword = keyword.get(1.0, "end-1c")
    # path for the folder for getting the raw images
    #path = "C:/Users/3115storeMRM/OneDrive - EPSA/Escritorio/SCANNED INVOICE/LIEBHERR/NOVEMBER 2021"
    path = global_directory

    # link to the file in which output needs to be kept
    fullTempPath = "C:/Users/3115storeMRM/OneDrive - EPSA/Escritorio/SCANNED INVOICE/outputFile.txt"

    # iterating the images inside the folder
    result.delete('1.0', END)
    for imageName in os.listdir(path):
        inputPath = os.path.join(path, imageName)
        img = Image.open(inputPath)

        # applying ocr using pytesseract for python
        text = pt.image_to_string(img, lang="eng")

        if global_keyword in text:
            result.insert(END, imageName + "- True\n")
            print(imageName + "- True")

            # saving the  text for appending it to the output.txt file
            # a + parameter used for creating the file if not present
            # and if present then append the text content
            """###BOUNDING BOX AROUND ALL TEXT
            img2 = cv2.imread(inputPath)
            d = pt.image_to_data(img2, output_type=Output.DICT)
            print(d.keys())
            n_boxes = len(d['text'])
            for i in range(n_boxes):
                if int(float(d['conf'][i])) > 60:
                    if (d['text'][i] == '3115-28012'):
                        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                        img2 = cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.namedWindow("output", cv2.WINDOW_KEEPRATIO)
            img2 = cv2.resize(img2, (2400, 3400))
            cv2.imshow('output', img2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            ###"""

            img2 = Image.open(inputPath)
            img2.show()

            file1 = open(fullTempPath, "w")

            # providing the name of the image
            file1.write(imageName + "\n")

            # providing the content in the image
            #file1.write(text + "\n")
            file1.close()
        else:
            print(imageName, "- False")
            result.insert(END, imageName + "- False\n")

    # for printing the output file
    file2 = open(fullTempPath, 'r')
    print(file2.read())
    file2.close()

def getFolderPath():
    folder_selected = filedialog.askdirectory()
    global global_directory
    global_directory = folder_selected
    directory.delete('1.0', END)
    directory.insert(END, folder_selected)

if __name__ == '__main__':
    pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    root = Tk()
    root.title('TEXT DETECTION IN IMAGE')
    root.geometry("800x600")

    # Create input
    directory = Text(root)
    directory.place(x=10, y=20, width=600, height=50)

    # Create button and assign function dirrectory to button
    button1 = Button(root, text="SET DIRECTORY", command=getFolderPath)
    button1.place(x=620, y=20, width=100, height=50)

    label1 = Label(root, text="KEYWORD", font=("Arial", 10))
    label1.place(x=180, y=80, width=70, height=20)
    keyword = Text(root)
    keyword.place(x=260, y=80, width=200, height=20)

    # Create input
    result = Text(root)
    result.place(x=10, y=120, width=600, height=460)

    # Create button and assign function dirrectory to button
    button2 = Button(root, text="SEARCH", command=text_detection)
    button2.place(x=620, y=119, width=100, height=50)

    root.mainloop()
    #text_detection()
