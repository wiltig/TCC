import cv2
import os
from imutils import paths
import shutil

def listNegImagem():
    imagemPath = list(paths.list_images('GISLAINE/n'))
    numero = 1
    if not os.path.exists('neg'):
        os.makedirs('neg')

    for i in imagemPath:
        i.replace(i, "neg/"+str(numero)+".jpg")
        shutil.copy(i, i.replace(i, "neg/"+str(numero)+".jpg"))
        img = cv2.imread("neg/" + str(numero) + ".jpg", cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img, (1000, 1000))
        cv2.imwrite("neg/" + str(numero) + ".jpg", resized_image)

        print(i.replace(i, "neg/"+str(numero)+".jpg"))

        numero += 1

listNegImagem()



#
# def store_raw_images():
#     neg_images_link = '//image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
#     neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
#     pic_num = 1
#
#     if not os.path.exists('neg'):
#         os.makedirs('neg')
#
#     for i in neg_image_urls.split('\n'):
#         try:
#             print(i)
#             urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
#             img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
#             # should be larger than samples / pos pic (so we can place our image on it)
#             resized_image = cv2.resize(img, (100, 100))
#             cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
#             pic_num += 1
#
#         except Exception as e:
#             print(str(e))