import os
import funcionesPrato as fun

fun.bienvenida()
nombre = fun.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

if fun.existe_archivo(nombre+".user"):
  nombre, edad, sexo, lugar, amigos, muro = fun.leer_usuario(nombre)
else:
  edad, sexo, lugar, amigos, muro= fun.obtener_datos(nombre)
  print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
  fun.datos(nombre,edad,sexo,lugar,amigos)
  print("""
    --------------------------------------------------
    Ya podemos preguntar, recordar y calcular datos. Esperamos que disfrutes con tuerca
    --------------------------------------------------""")

opcion = 1
while opcion != 0:
  opcion = fun.opcion_menu()
  if opcion == 1:
    fun.msg(nombre,amigos,muro)
  elif opcion == 2:
    fun.mostrar_muro(muro)
  elif opcion == 3:
    fun.datos(nombre, edad, sexo, lugar, amigos)
  elif opcion == 4:
    fun.cambio_datos(nombre,edad,sexo,lugar,amigos,muro)
  elif opcion == 5:
    print("Esta es la lista de amigos", amigos)
    nuevo_amigo = input("Agrega un amigo: ")
    amigos = fun.agregar_amigo(nombre,amigos, nuevo_amigo)
  elif opcion == 6:
    fun.cambiar_usuario(nombre, edad,sexo,lugar,amigos,muro)
  elif opcion == 0:
    print("Has decidido salir. Guardando perfil en ",nombre+".user")
    fun.escribir_usuario(nombre,edad,sexo,lugar,amigos, muro)
  else:
    print("No conozco la opcion que has ingresado. Intentalo otra vez.")