def coneccionBBDD():

	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	try:
		miCursor.execute('''
    		CREATE TABLE DATOSUSUARIOS(
	    	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	    	NOMBRE_USUARIO VARCHAR(50),
	    	PASSWORD VARCHAR(50),
	    	APELLIDO VARCHAR(15),
	    	DIRECCION VARCHAR(50),
	    	COMENTARIOS VARCHAR(200))
	    	''')

		messagebox.showinfo("BBDD","La BBDD ya ha sido creada anteriormente")
	
	except:
		messagebox.showwarning("!atencion","BBDD creada con exito")


def salirAplicacion():
	valor=messagebox.askquestion("Salir","Salir de la aplicacion?")
	
	if valor=="yes":
	    root.destroy() # ayuda a salir de la aplicaicon


def borrarCampos():
   
   cuadroID.delete(0,"end")
   cuadroNombre.delete(0,"end")
   cuadroPass.delete(0,"end")
   cuadroApellido.delete(0,"end")
   cuadroDireccion.delete(0,"end")
   textoComentario.delete(1.0,END)


def crearUsuario():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	datos=minombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentario.get()
	#miCursor.executemany("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",datos)

	miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'" + miNombre.get() + "','" + miPass.get() + "','" + miApellido.get() + "','" + miDireccion.get() + "','" + textoComentario.get("1.0",END) + "')")
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro insertado con Exito")


def leer():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	valor=miID.get()
	miCursor.execute("SELECT* FROM DATOSUSUARIOS WHERE ID =" + valor)
	elUsuario=miCursor.fetchall() # devuelve un array con los registros de mi sentencia sql 
	for i in elUsuario:
		miID.set(i[0])
		miNombre.set(i[1])
		miPass.set(i[2])
		miApellido.set(i[3])
		miDireccion.set(i[4])
		textoComentario.insert(1.0,i[5])
	miConexion.commit()	


def actualizar():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	valor=miID.get()
	miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
		"', PASSWORD='" + miPass.get() +
		"', APELLIDO='" + miApellido.get() +
		"', DIRECCION='" + miDireccion.get() +
		"', COMENTARIOS='" + textoComentario.get("1.0", END) +
		"' WHERE ID=" + valor)

	miConexion.commit()
	messagebox.showinfo("BBDD","Registro Actualizado con Exito")



def eliminar():

	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()
	valor=miID.get()
	miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + valor)
	miConexion.commit()
	messagebox.showinfo("BBDD","Registro Eliminado con Exito")
	borrarCampos()