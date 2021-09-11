
from tkinter import *
from tkinter import messagebox
import sqlite3 

root=Tk()


#-------- ---------------comienzo de campos-----------------------------
miFrame=Frame(root)
miFrame.pack()

miID=StringVar()
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDireccion=StringVar()


cuadroID=Entry(miFrame,textvariable=miID)
cuadroID.grid(row=0,column=1,padx=10,pady=10 )

cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10 )
cuadroNombre.config(fg="red",justify="right")


cuadroPass=Entry(miFrame,textvariable=miPass)
cuadroPass.grid(row=2,column=1,padx=10,pady=10 )
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=3,column=1,padx=10,pady=10 )


cuadroDireccion=Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10 )

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=5,column=1,padx=10,pady=10 )
scrollVert=Scrollbar(miFrame,command=textoComentario.yview)# el yview permite determinar sobre que eje se va a desplazar el scroll ya sea eje x o y 
scrollVert.grid(row=5,column=2,sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)





#-------------------etiquetas---------------------

idLabel=Label(miFrame,text="Id:")
idLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

passLabel=Label(miFrame,text="Password:")
passLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

direccionLabel=Label(miFrame,text="Direccion:")
direccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

comentarioLabel=Label(miFrame,text="Comentarios:")
comentarioLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)



#-------------------BOTONES----------------------------

miFrame2=Frame(root)
miFrame2.pack()

crearBoton=Button(miFrame2,text="Crear",command=crearUsuario)
crearBoton.grid(row=1,column=0,sticky="e",padx=10,pady=10)

leerBoton=Button(miFrame2,text="Leer",command=leer)
leerBoton.grid(row=1,column=1,sticky="e",padx=10,pady=10)

actualizarBoton=Button(miFrame2,text="Actualizar",command=actualizar)
actualizarBoton.grid(row=1,column=2,sticky="e",padx=10,pady=10)


borrarBoton=Button(miFrame2,text="Borrar",command=eliminar)
borrarBoton.grid(row=1,column=3,sticky="e",padx=10,pady=10)



root.mainloop()
