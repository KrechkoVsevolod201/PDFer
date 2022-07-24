from fpdf import FPDF
from PIL import Image
import glob
import os
import img2pdf
from os import listdir


def pdf_conv():

    path = "D:/PycharmProjects/PDFer/image/"  # get the path of images
    imagelist = listdir(path)  # get list of all images
    pdf = FPDF('P', 'mm', 'A4')  # create an A4-size pdf document
    x, y, w, h = 0, 0, 200, 250
    for image in imagelist:
        pdf.add_page()
        pdf.image(path + image, x, y, w, h)

    pdf.output("images.pdf", "F")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pdf_conv()
