import cv2
import os
from imutils import paths
import shutil

def listPosImagem():
    imagemPath = list(paths.list_images('GISLAINE/CACHORROS'))
    numero = 1
    if not os.path.exists('pos'):
        os.makedirs('pos')

    for i in imagemPath:
        i.replace(i, "pos/"+str(numero)+".jpg")
        shutil.copy(i, i.replace(i, "pos/"+str(numero)+".jpg"))
        img = cv2.imread("pos/" + str(numero) + ".jpg", cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img, (1000, 1000))
        cv2.imwrite("pos/" + str(numero) + ".jpg", resized_image)

        print(i.replace(i, "pos/"+str(numero)+".jpg"))

        numero += 1

listPosImagem()