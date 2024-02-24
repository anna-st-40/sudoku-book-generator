import os
import img2pdf
from pypdf import PdfMerger
from PIL import Image

from functions import filename_sorting_key

def generate_pdf(base_id):
  """
  Converts the images into one final pdf
  """

  os.mkdir(f"sudoku_{base_id}/pages/pdfs")

  imgs = [f for f in os.listdir(f"sudoku_{base_id}/pages") if os.path.isfile(os.path.join(f"sudoku_{base_id}/pages", f))] #iterate through all the files in the folder
  imgs.sort(key=filename_sorting_key)

  os.chdir(f"sudoku_{base_id}/pages")

  # Convert each image to a pdf file
  for i, img in enumerate(imgs):
    with Image.open(img) as image: 
      # convert the image to a PDF
      pdf = img2pdf.convert(image.filename)
      # write the PDF to its final destination
      with open(f"pdfs/{base_id}_page_{i+1}.pdf", "wb") as file:
        file.write(pdf)
        print(f"Converted {img} to page{i+1}.pdf")

  # Merge all the pdf files     
  os.chdir("pdfs")
  pdfs = os.listdir()
  pdfs.sort(key=filename_sorting_key)

  merger = PdfMerger()

  for pdf in pdfs:
      merger.append(pdf)

  os.chdir("../..")
  merger.write(f"sudoku_{base_id}.pdf")
  merger.close()