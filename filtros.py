import cv2, numpy

def gaussiano(img, n = 5):
    gausiana = cv2.GaussianBlur(img,(n,n),5)
    return gausiana

def mediana(img, n=5):
    mediana = cv2.medianBlur(img,n)
    return mediana

def nitidez(img, n = 5):
    frame = cv2.GaussianBlur(img,(n,n),5)
    nitida = cv2.addWeighted(img,1.5,frame,-0.5,0)
    return nitida

def mostrar(texto, imagen):
    """
    Muestra una imagen en pantalla hasta que el usuario presione una tecla
    Cuando el usuario presiona cualquier tecla, se cierra la ventana
    """
    cv2.imshow(texto,imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    img = cv2.imread('img/imagen1.jpg')
    mostrar('Original', img)
    mostrar('Gausiano', mediana(img,7))



