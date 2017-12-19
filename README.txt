Agregar algo al PATH
set PATH=%PATH%;C:\Program Files (x86)\Tesseract-OCR

imagemagick: para convertir de .pdf a .tif, no funcionó

ghostscript: convertir .pdf a .tif, no funcionó

jTessBoxEditor: crea archivo .tif a partir de un archivo .txt, y ademas crea archivo .box

Create trained data for Tesseract-OCR Windows

Option a) from .txt file (doesnt work for all)

Option 1: WORKS but the trained font doesnt work with noise

0. Install Tesseract-OCR. https://github.com/UB-Mannheim/tesseract/wiki
     Install pytesseract https://github.com/madmaze/pytesseract

1. Create text file with the "alphabeth to train". A file with a pair of lines with the digits from 0 to 9.

2. Download and install font file of digital-7 https://www.dafont.com/es/digital-7.font

3. Download jTessBoxEditor.

4. Open jTessBoxEditor, and go to TIFF/Box Genarator.

5. Set the input as the text file generated in step 1. Set output directory, the same as the input one. Choose a lang name, "dig" was used. Change the font used to the digital-7 one. Click generate to create TIFF/Box files.

6. Go to Box Editor to check if the characters were corectly classified, otherwise change them.

7. Go to Trainer. Select the Tesseract-OCR from the one installed in step 0. Write a lang, dig could be. Select the Training Data (the .box file generated in step 5). Training with existing box option. Run.

8. Select ShapeClustering in the same window, Run.

8. Copy the files generated (.normproto, .traineddata, .inttemp, pffmtable, .shapetable, .unicharset, .frequent_words_list, words_list) to the installation folder of Tesseract-OCR/tessdata

Option 2: ERROR
based on: http://michaeljaylissner.com/posts/2012/02/11/adding-new-fonts-to-tesseract-3-ocr-engine/

set PATH=%PATH%;C:\Program Files (x86)\Tesseract-OCR

1. Create word file with the training data, then convert to pdf

2. convert -density 300 -depth 4 dig3.seg.exp0.pdf dig3.seg.exp0.tif

3. tesseract dig3.seg.exp0.tif dig3.seg.exp0 batch.nochop makebox. ERROR in pixReadFromTiffStream: spp not in set {1,3,4}

Option 3: WORKS doesnt detect well
1. Create word file with the training data, then convert to pdf

For using ghostscript
set PATH=%PATH%;C:\Program Files\gs\gs9.22\bin
set PATH=%PATH%;C:\Program Files\gs\gs9.22\lib

2. Create tif file from pdf using ghostscript
gswin64 -o dig3.seg.exp0.tif -sDEVICE=tiffgray -r720x720 -g6120x7920 -sCompression=lzw dig3.seg.exp0.pdf

Create .jpg to validate results
convert -density 300 -depth 4 dig3.seg.exp0.pdf[0] dig3_validation.jpg

3. Create box file using tesseract-ocr
set PATH=%PATH%;C:\Program Files (x86)\Tesseract-OCR
tesseract dig3.seg.exp0.tif dig3.seg.exp0 batch.nochop makebox

4. Open jTessBoxEditor and see the box file, edit it and then train it.


Option 4: go from the box file generated in option 3.
1. tesseract dig4.seg.exp0.tif dig4.seg.box nobatch box.train .stderr