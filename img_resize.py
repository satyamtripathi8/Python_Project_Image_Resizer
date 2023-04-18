from PIL import Image
img = Image.open('ram.jpg')
height= int(input("Enter height"))
width= int(input("Enter width"))
Ri = img.resize((height,width))
Ri.save(f'day{width}{height}',width,height)