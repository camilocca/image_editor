from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import cv2
# import numpy as np
# # import imutils



def abrir_imagen():
    archivo_abierto=filedialog.askopenfilename(initialdir = "C:/",
                title = "Seleccione archivo",filetypes =[
                ("Imagen jpg","*.jpg"),
                ("Imagen png","*.png"),
                ("Todos los formatos","*.*")])
    if len(archivo_abierto) > 0:
        global img
        #leer la imagen
        img=cv2.imread(archivo_abierto)
        # img=imutils.resize(img,height=380)
        img=cv2.resize(img,dsize=(400,400),interpolation=cv2.INTER_CUBIC)
        #para vizualizar imagen
        # Imagetoshow=imutils.resize(img,width=380)
        # Imagetoshow=cv2.cvtColor(Imagetoshow,cv2.COLOR_BGR2RGB)
        Imagetoshow=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        im=Image.fromarray(Imagetoshow)
        imagenfinal=ImageTk.PhotoImage(image=im)

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
    # global img
    # img=None
    # imagen.configure(image=img)
    # imagen.image=img
    # imagen.grid_remove()
    imagen.configure(image=None)
    imagen.image=None
    

img=None
ventana=Tk()
ventana.geometry('800x600')
ventana.title('Proyecto Imagen')
frame1=Frame(ventana,bg='sky blue')
# frame1.pack(expand=True,fill='both')
frame1.pack(expand=True,fill='both')
frame1.config(width=300,height=300)
frame2=Frame(ventana,bg='gray')
frame2.config(bd=24)
frame2.config(relief='sunken')
frame2.pack(expand=True,fill='both')
#La imagen de entrada 
imagen=Label(frame2)
imagen.grid(column=0,row=3)

#creamos el boton 
boton=Button(frame1,text='Abrir Imagen',width=25,command=abrir_imagen)
boton.grid(column=0,row=0,padx=5,pady=5)
boton2=Button(frame1,text="Guardar archivo",bg="light green",width=25,command=guardar_archivo)
boton2.grid(column=0,row=1,padx=5,pady=5)
boton3=Button(frame1,text="Eliminar Imagen",bg="red",width=25,command=elimar_imagen)
boton3.grid(column=0,row=2,padx=5,pady=5)
    
ventana.mainloop()

# if __name__ == '__main__':
#     botones()
