import cv2, numpy
import matplotlib.pyplot as plt
import urllib.request

from cv2 import ROTATE_90_CLOCKWISE

def redim_borde(img, new_dim:list):
    dimension = img.shape[0:2]
    lista_escala = [dimension[0]/new_dim[0] , dimension[1]/new_dim[1]]
    escala = max(lista_escala)
    img_redim = cv2.resize(img,(0,0), fx = 1/escala, fy = 1/escala)
    final = cv2.copyMakeBorder(img_redim,
        0,
        new_dim[0]-img_redim.shape[0],
        0,
        new_dim[1]-img_redim.shape[1],
        cv2.BORDER_CONSTANT, value = [255,255,255])
    return final

def redim_recorte(img, new_dim:list):
    dimension = img.shape[0:2]
    lista_escala = [dimension[0]/new_dim[0] , dimension[1]/new_dim[1]]
    escala = max(lista_escala)
    img_redim = cv2.resize(img,(0,0), fx = 1/escala, fy = 1/escala)
    final = img[0:new_dim[0],0:new_dim[1]]
    return final

def redim_escala(img, new_dim:list):
    dimension = img.shape[0:2]
    lista_escala = [dimension[0]/new_dim[0] , dimension[1]/new_dim[1]]
    escala = max(lista_escala)
    img_redim = cv2.resize(img,(0,0), fx = 1/escala, fy = 1/escala)
    return img_redim


def mostrar(texto, imagen):
    """
    Muestra una imagen en pantalla hasta que el usuario presione una tecla
    Cuando el usuario presiona cualquier tecla, se cierra la ventana
    """
    cv2.imshow(texto,imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    #url = input('Ingrese la url: ')
    url = 'https://img.freepik.com/foto-gratis/primer-disparo-flor-morada_181624-25863.jpg?size=626&ext=jpg'
    urllib.request.urlretrieve(url, 'img/imagen1.jpg')
    
    img = cv2.imread('img/imagen1.jpg')
    mostrar('Original', img)
    mostrar('Recorte', redim_recorte(img, [300,300]))
    mostrar('Escalado', redim_escala(img, [300,300]))
    mostrar('Borde', redim_borde(img, [300,300]))

    


    
    

