from tkinter import*
from tkinter import messagebox  #para importar ventanas emergentes 

root=Tk()


def infoAdicional():
	messagebox.showinfo("Procesador de Jhinner","Procesador de texto 2da version 2021")


def avisoLicencia():
	messagebox.showwarning("Licencia","Producto bajo licencia GNU")

def salirAplicacion():
	#valor=messagebox.askquestion("Salir","Salir de la aplicacion?")
	valor=messagebox.askokcancel("Salir","Salir de la aplicacion?")
	if valor==True: # se pone "yes" si se utilizas askquiesion en lugar de askokcancel
	    root.destroy() # ayuda a salir de la aplicaicon


def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar","No es posible cerrar.Documento bloqueado")
	if valor== False:
		root.destroy()



barraMenu=Menu(root)
root.config(menu=barraMenu,width=300,height=300)

archivoMenu=Menu(barraMenu,tearoff=0) # esta funcion tearoff quita la lagrima o esa barra espaciadora del smenu
archivoMenu.add_command(label="Nuevo")# son submenus
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator() # serapara la lista en el submenu con una barra horizontal
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=salirAplicacion)



archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")


archivoHerramientas=Menu(barraMenu,tearoff=0)

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...",command=infoAdicional)


barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edicion",menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)

root.mainloop()
