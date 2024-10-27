import cv2


carregaAlgoritmo = cv2.CascadeClassifier ('mydogdetector.xml')
imagem = cv2.imread('tosa.jpg')
font=cv2.FONT_HERSHEY_SIMPLEX
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

Dog = carregaAlgoritmo.detectMultiScale(imagemCinza, scaleFactor=1.2, minNeighbors=20, flags = 75, minSize=(50, 50))
print(Dog)

for (x,y,w,h) in Dog:
    cv2.rectangle(imagem, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.putText(imagem, 'Cachorro', (x, y), font, 0.9, (0, 255, 0), 3)

cv2.imshow('Imagem', imagem)
cv2.waitKey(0)

