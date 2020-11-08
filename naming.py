# this program is for renaming the files in descending order
# of "CONTENT CREATED" attribute

from PIL import Image
from PIL.ExifTags import TAGS
import os


TRICOfiles = os.listdir("TRICO")
i = 0

for f in TRICOfiles:
	if (f == ".DS_Store"):
		continue

	image = Image.open("TRICO/" + f)
	exifdata = image.getexif()

	# get attributes
	flg = False
	for tag_id in exifdata:
		tag = TAGS.get(tag_id, tag_id)
		data = exifdata.get(tag_id)

		if (tag == "DateTime"):
			break

	data = data.replace(":", "-")

	os.rename("TRICO/" + f, "TRICO/" + data +".jpg")
	i = i + 1

	

print(i)




"""
imagename = "TRICO/1.jpg"

image = Image.open(imagename)

exifdata = image.getexif()

for tag_id in exifdata:
	tag = TAGS.get(tag_id, tag_id)
	data = exifdata.get(tag_id)

	if isinstance(data, bytes):
		data = data.decode()

	#print(f"{tag:25}: {data}")
	print(tag)
	print(data)
"""