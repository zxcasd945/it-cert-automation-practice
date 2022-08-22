
from PIL import Image
from glob import glob
import os
home=os.path.expanduser('~')
path=home+'/image/*'


for file in glob('/home/student-04-62df7b1db086/images/*'):
    image = Image.open(file).convert('RGB')


    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0]
    image.rotate(270).resize((128,128)).save('/opt/icons/{}.jpeg'.format(filename))
