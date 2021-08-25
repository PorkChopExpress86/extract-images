# Extract Images from Documents
This will extract all images from the following documents:
1. *.doc
2. *.docx
3. *.pdf
4. *.xls
5. *.xlsx

This will require a folder path for an input and a folder path to store the extracted image copies.

```
./extract-images.py --source "/home/username/Documents/files/" --destination "/home/username/Documents/images/"
```
The output images will be placed in folders with the files name-extentions, ex. someFilename-pdf
