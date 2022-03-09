from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import cv2
import os


img=None
 
def cargar_imagen():
    archivo_abierto=filedialog.askopenfilename(initialdir = "C:/",
                title = "Seleccione archivo",filetypes =[
                ("Imagen jpg","*.jpg"),
                ("Imagen png","*.png"),
                ("Todos los formatos","*.*")])
    if len(archivo_abierto) > 0:
    
        #leer la imagen
        img=cv2.imread(archivo_abierto,cv2.IMREAD_UNCHANGED)
        # img=imutils.resize(img,height=380)
        return img 


def mostrar_imagen():
    global img
    img=cargar_imagen()
    # img_cesar=img 
    escala=30
    anchura=int(img.shape[1]*escala/100)
    altura=int(img.shape[0]*escala/100)
    # (alto,ancho,canales)=img.shape
    # r=200/ancho
    # dim=(200,int(alto*r))
    # img=cv2.resize(img,dim)
    img=cv2.resize(img,dsize=(anchura,altura))
    #para vizualizar imagen
    imag=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #imagen traida con TKinter
    im=Image.fromarray(imag)
    imagenfinal=ImageTk.PhotoImage(image=im)
    # imagen que se modifica y se guarda 
    imagen.configure(image=imagenfinal)
    imagen.image=imagenfinal
    #texto de la imagen de entrada
    info=Label(frame2,text='imagen seleccionada')
    info.grid(column=0,row=6,padx=5,pady=5)
   

def guardar_archivo():
    archivo_guardado=filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como ",defaultextension=".jpg",
                                 filetypes = (("jpg ","*.jpg"),
                                              ("png","*.png"),
                                              ("todos los formatos","*.*")))
    
    global img
    cv2.imwrite(archivo_guardado,img)

def elimar_imagen():
    # imagen.image=img
    # imagen.grid_remove()
    imagen.configure(image=None)
    imagen.image=None


    
#ventana 
ventana=Tk()
ventana.geometry('800x600')
ventana.title('Proyecto Imagen')
frame1=Frame(ventana,bg='sky blue')
# frame1.pack(expand=True,fill='both')
frame1.pack(expand=True,fill='both')
frame1.config(width=300,height=300)
frame2=Frame(ventana,bg='white')
frame2.config(bd=24)
frame2.config(relief='sunken')
frame2.pack(expand=True,fill='both')
#La imagen de entrada 
imagen=Label(frame2)
imagen.grid(column=0,row=3)




#creamos el boton
boton=Button(frame1,text='Abrir Imagen',width=25,command=mostrar_imagen)
boton.grid(column=0,row=0,padx=5,pady=5)
boton2=Button(frame1,text="Guardar archivo",bg="light green",width=25,command=guardar_archivo)
boton2.grid(column=0,row=1,padx=5,pady=5)
boton3=Button(frame1,text="Borrar Imagen",bg="red",width=25,command=elimar_imagen)
boton3.grid(column=0,row=2,padx=5,pady=5)

ventana.mainloop()