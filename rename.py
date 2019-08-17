# Example python rename.py '/root/Bureaublad/data/boefjes/front' 
from PIL import Image
import os,sys,glob
directory=sys.argv[1]
i=int(0)
for infilename in glob.iglob(directory+'/*.png'):
	im = Image.open(infilename)
	rgb_im = im.convert('RGB')
	outfilename = "/boefje%d.jpg" % int(i + 1)
	outfile=os.path.join(directory, outfilename)
	print(directory+outfile)
	rgb_im.save(directory+outfile)
	i += 1