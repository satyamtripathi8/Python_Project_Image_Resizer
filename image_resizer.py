from PIL import Image
img = Image.open('ram.jpg')
print(img.size)
Ri = img.resize((512,512))
Ri.save('Ram.jpg')
print(Ri.size)