# importing Image class from PIL package 
from PIL import Image 

def main():
  blockLength = blockWidth = 50

  coorSys = {"Johnson Center": [(blockLength * 16.5) + 80, (blockWidth * 6.5) + 35],
            "AFC": [(blockLength * 19.5) + 80, (blockWidth * 10.3) + 35],
            "RAC": [(blockLength * 13) + 80, (blockWidth * 5.8) + 35],
            "Skyline": [(blockLength * 19.2) + 80, (blockWidth * 4.7) + 35], 
            "SUB 1": [(blockLength * 15.5) + 80, (blockWidth * 5.9) + 35], 
            "Ike's": [(blockLength * 20.8) + 80, (blockWidth * 7.8) + 35],
            "Southside": [(blockLength * 19.5) + 80, (blockWidth * 5.1) + 35],
            "The Globe": [(blockLength * 11) + 80, (blockWidth * 7) + 35],
            "The Spot": [(blockLength * 20) + 80, (blockWidth * 2.4) + 35],
            "Parking": [(blockLength * 18.7) + 80, (blockWidth * 7.6) + 35]}

  im = Image.open(r"chat/map.jpg") 
  pin = Image.open(r"chat/Pin.png")
  pinWidth = 290


  for key, value in coorSys.items():
    if key == "Johnson Center":
      xCoord = int(tuple(value)[0])
      yCoord = int(tuple(value)[1])
      im.paste(pin, (xCoord - int(pinWidth/2.63), yCoord - int(pinWidth-10))) # 290x290px
    elif key == "AFC":
      xCoord = int(tuple(value)[0])
      yCoord = int(tuple(value)[1])
      im.paste(pin, (xCoord - int(pinWidth/2.63), yCoord - int(pinWidth-10))) # 290x290px
    elif key == "RAC":
      xCoord = int(tuple(value)[0])
      yCoord = int(tuple(value)[1])
      im.paste(pin, (xCoord - int(pinWidth/2.63), yCoord - int(pinWidth-10))) # 290x290px
    elif key == "Skyline":
      xCoord = int(tuple(value)[0])
      yCoord = int(tuple(value)[1])
      im.paste(pin, (xCoord - int(pinWidth/2.63), yCoord - int(pinWidth-10))) # 290x290px
    elif key == "SUB 1":
      xCoord = int(tuple(value)[0])
      yCoord = int(tuple(value)[1])
      im.paste(pin, (xCoord - int(pinWidth/2.63), yCoord - int(pinWidth-10))) # 290x290px
    elif key == "Ike's":
      xCoord = int(tuple(value)[0])
      yCoord = int(tuple(value)[1])
      im.paste(pin, (xCoord - int(pinWidth/2.63), yCoord - int(pinWidth-10))) # 290x290px
    elif key == "Southside":
      xCoord = int(tuple(value)[0])
      yCoord = int(tuple(value)[1])
      im.paste(pin, (xCoord - int(pinWidth/2.63), yCoord - int(pinWidth-10))) # 290x290px
    elif key == "The Globe":
      xCoord = int(tuple(value)[0])
      yCoord = int(tuple(value)[1])
      im.paste(pin, (xCoord - int(pinWidth/2.63), yCoord - int(pinWidth-10))) # 290x290px
    elif key == "The Spot":
      xCoord = int(tuple(value)[0])
      yCoord = int(tuple(value)[1])
      im.paste(pin, (xCoord - int(pinWidth/2.63), yCoord - int(pinWidth-10))) # 290x290px
    elif key == "Parking":
      xCoord = int(tuple(value)[0])
      yCoord = int(tuple(value)[1])
      im.paste(pin, (xCoord - int(pinWidth/2.63), yCoord - int(pinWidth-10))) # 290x290px
    

  im.show()
