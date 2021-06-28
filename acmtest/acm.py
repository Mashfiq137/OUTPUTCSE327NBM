import pandas as pd
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import glob

ex_file=pd.read_excel('MidNightHackathon212.1.xlsx',sheet_name=0)   #image file path
images=glob.glob("*.jpg")                                       # image format (case sensitive: 'JPG' & 'jpg')
i=0
for row in ex_file.itertuples(index=False):                     # Iteration through the xlsx
    try:
        print (row)                                             # printing each row of the xlsx
        image_files = Image.open(images[i])                     # open Image file
        i=i+1
        font_type = ImageFont.truetype('Doland-Regular.otf',18) # Font Style
        draw = ImageDraw.Draw(image_files)                      # Draw object
        str1= "Name: " + str(row[0])                            # Name on variable
        str2= "Id: " + str(row[1])                              # Id on variable
        draw.text(xy=(300,20),text= str2,fill=(100,100,100),font=font_type)     #Writing on image file: ID
        draw.text(xy=(100,60),text= str1,fill=(123,233,157),font=font_type)     # Writing on image file: Name
        filename = row[1]
        image_files.save(filename+'.jpg', quality=90)           #save file
    except:
        print("Not enough Image files")                         #exception if not enough image files.