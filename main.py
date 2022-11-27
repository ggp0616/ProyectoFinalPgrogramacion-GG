import qrcode
data = 'https://www.youtube.com/watch?v=vP1nhjPMyhc'   #"Proyecto Final para la presentación del 28/11"
img = qrcode.make(data)
img.save('QRcode.png')
img.show()