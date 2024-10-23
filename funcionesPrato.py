import os

def bienvenida():
  print(""" 
    Bienvenido a ... 
              
      __                                      
    _/  |_ __ __   ___________   ____ _____   
    \   __\  |  \_/ __ \_  __ \_/ ___\\__  \  
    |  | |  |  /\  ___/|  | \/\  \___ / __ \_
    |__| |____/  \___  >__|    \___  >____  /
                      \/            \/     \/ 
  """)

def obtener_nombre():
  nombre = input("Para empezar, dime como te llamas: ")
  return nombre

def obtener_edad():
  anio = int(input("Para preparar tu perfil, dime en cual año naciste."))
  edad = 2024-anio-1
  return edad

def obtener_sexo():
  sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ").upper()
  while sexo != 'M' and sexo != 'F':
      sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ").upper()
  return sexo

def obtener_lugar():
  lugar = input("Cuentame mas de ti, para agregarlo a tu perfil. ¿De donde eres?")
  return lugar

def obtener_amigos(nombre):
  linea = input("Muy bien. Finalmente, escribe una lista con los nombres de tus amigos, separados por una ',': ")
  amigos = linea.split(",")
  if nombre in amigos:
    print("""
      --------------------------------------------------
      No puedes agregarte a ti mismo de amigo, sera eliminado.
      --------------------------------------------------
      """)
    amigos.remove(nombre)
  return amigos

def agregar_amigo(nombre,lista_amigos, nuevo_amigo):
  if nuevo_amigo == nombre:
    print("--------------------------------------------------")
    nuevo_amigo = input("No puedes agregarte como amigo a ti mismo. Agrega a otro: ")
  lista_amigos.append(nuevo_amigo)
  return lista_amigos


def obtener_datos(nombre):
    edad = obtener_edad()
    sexo = obtener_sexo()
    lugar = obtener_lugar()
    amigos = obtener_amigos(nombre)
    muro = []
    return (edad,sexo,lugar,amigos,muro)

def datos(nombre, edad, sexo, lugar, amigos):
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "años")
    print("Sexo:     ", sexo)
    print("Lugar:    ", lugar)
    print("Amigos:   ", len(amigos))
    print("--------------------------------------------------")


def msg(nombre, amigos, muro):
    mensaje = input("¿Que vas a escribir?")
    print("--------------------------------------------------")
    print(nombre, "dice:", mensaje)
    print("--------------------------------------------------")
    muro.append(mensaje)
    for amigo in amigos:
        if existe_archivo(amigo+".user"):
            archivo = open(amigo+".user","a")
            archivo.write(nombre+":"+mensaje+"\n")
            archivo.close()

def mostrar_muro(muro):
     print("------ MURO ("+str(len(muro))+" mensajes) ---------")
     for mensaje in muro:
         print(mensaje)
     print("--------------------------------------------------")

def opcion_menu():
    print("""\
      Acciones disponibles:
      1. Escribir un mensaje 
      2. Mostrar mi muro
      3. Mostrar los datos de perfil
      4. Actualizar datos
      5. Agregar un amigo
      6. Cambiar usuario
      0. Salir""")
    opcion = int(input("Ingresa una opcion: "))
    if opcion < 0 or opcion > 6:
        print("No conozco la opcion que has ingresado. IntÃ©ntalo otra vez.")
        return opcion_menu()
    return opcion


def cambio_datos(nombre,edad,sexo,lugar,amigos,muro):
  datos(nombre,edad,sexo,lugar,amigos)
  dato = input("¿Que dato cambiaras?").upper()
  print("--------------------------------------------------")
  if dato == "EDAD":
    edad = obtener_edad()
  elif dato == "SEXO":
    sexo = obtener_sexo()
  elif dato == "LUGAR":
    lugar = obtener_lugar()
  elif dato == "AMIGOS":
    amigos = obtener_amigos(nombre)
  elif dato == "NOMBRE":
    nombre = cambiar_nombre(nombre)
  escribir_usuario(nombre,edad,sexo,lugar,amigos,muro)

  return nombre,edad,sexo,lugar,amigos

def existe_archivo(ruta):
    return os.path.isfile(ruta)

def leer_usuario(nombre):
    archivo_usuario = open(nombre+".user","r")
    nombre = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    sexo = archivo_usuario.readline().rstrip()
    lugar = archivo_usuario.readline().rstrip()
    amigos = archivo_usuario.readline().rstrip().split(",")
    muro = []
    mensaje = archivo_usuario.readline().rstrip()
    while mensaje != "":
        muro.append(mensaje)
        mensaje = archivo_usuario.readline().rstrip()
    archivo_usuario.close()
    return(nombre, edad, sexo, lugar, amigos, muro)


def escribir_usuario(nombre,edad,sexo,lugar,amigos,muro):
    archivo_usuario = open(nombre+".user","w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(sexo+"\n")
    archivo_usuario.write(lugar+"\n")
    archivo_usuario.write(",".join(amigos)+"\n")
    for mensaje in muro:
      archivo_usuario.write(mensaje+"\n")
    print("Archivo",nombre+".user","guardado")
    archivo_usuario.close()

def cambiar_usuario(nombre, edad,sexo,lugar,amigos,muro):
  escribir_usuario(nombre, edad, sexo, lugar, amigos, muro)
  nombre_nuevo = input("¿A que usuario cambiara?")
  if existe_archivo(nombre_nuevo+".user"):
    nombre, edad, sexo, lugar, amigos, muro = leer_usuario(nombre)
    print("""
    --------------------------------------------------
    Has cambiado de usuario")
    --------------------------------------------------""") 
  else:
    print("No existe ese usuario")

def cambiar_nombre(nombre):
  nombre_nuevo = input("¿Como te llamaras ahora?")
  print("--------------------------------------------------")
  print("Ahora te llamaras", nombre_nuevo)
  print("--------------------------------------------------")
  os.remove(nombre+".user")
  escribir_usuario()
  nombre = nombre_nuevo
  return nombre