# -*- coding: utf-8 -*-
"""Detección_Placas4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iNAkpFW37cHNoDHq78l9AKqzEw_E35TG
"""


import matplotlib.pyplot as plt

from PIL import Image
import cv2 as cv2
import numpy as np

import os


ruta1 = "E:/CARLOS/"
file2 = ruta1+'Training/'    #Seleccionar Training or Test
files_names1 = os.listdir(file2)  # hace una lista de las clases
print(files_names1)

#file1 = cv2.imread(ruta1+ "/Placas/carro38.jpg")
# 38 y 52

"""ENTRENAR MODELO OCR:"""


def resize_scale(img, scale_percent):
    # scale_percent contiene el porcentaje en el que se debe escalar la imagen
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized


def resize_fix(img, dim):
    dsize = (dim, dim)
    # resize image
    resized = cv2.resize(img, dsize)
    return resized


# Falta estandarizar tamaño de imagen:

# Leer imágenes y conformar vectores

files_names1 = os.listdir(file2)  # List all directories in file2
vectr1 = []
target1 = []
etiquetas = []
etiquetasD = {}  # Diccionario
num_clase1 = 0
contador = 0
cnt = 0
for clase in files_names1:
    ruta2 = os.listdir(file2+clase)
    contador = contador+1
    etiquetas.append([contador, clase])
    etiquetasD[contador] = [clase]
    # contador=0
    #print('ruta2', ruta2)
    cnt = 0
    for imagen in ruta2:
        cnt = cnt+1
        # if contador<20:
        #print('size', np.shape(imagen))
        aux = file2 + clase + '/' + imagen
        #image = plt.imread(aux)
        image = cv2.imread(aux)
        image_ = resize_fix(image, 128)  # redimensiona a 64x64
        if cnt == 1:
            cv2.imshow('',image_)
            # cv2.imshow('winname',image_)
            print('Ruta: ', aux)
        if image_ is None:
            continue
        vectr1.append(image_)  # vector de vectores
        # print(vectr)
        # clasifica las imagenes de acuerdo a la clase a la que pertenecen
        target1.append(contador)

# np.save(file2+'vectr1',vectr1)
print('vectr1', vectr1)
print('target1', target1)
print('etiquetas', etiquetas)

np.save(ruta1+'/Vectors/vectr1', vectr1)
np.save(ruta1+'/Vectors/target1', target1)
np.save(ruta1+'/Vectors/etiquetasD', etiquetasD)


