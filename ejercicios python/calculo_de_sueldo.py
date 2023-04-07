
"""
Realizar un algoritmo que permita calcular el sueldo de un determinado empleado de una empresa. Se debe permitir ingresar por teclado el DNI del empleado y la categoría a la que pertenece; el programa deberá mostrar el sueldo NETO (el bruto menos todos los descuentos) del empleado, su DNI y la categoría a la que pertenece (Debe imprimir el nombre de la categoría a la que pertenece). Tener en cuenta que las categorías tienen las siguientes cuestiones:

a. Categoría 0: Maestranza. Sueldo Bruto de $23600. Descuento de jubilación 11%.
	Descuento de Obra Social 3%.. Categoría 1: Administración. Sueldo Bruto de $35800. Descuento de Jubilación 11 %.
	Descuento de Obra social 5%.
c. Categoría 2: Gerencia. Sueldo Bruto de $60420. Descuento de Jubilación 11%. Descuento
	de Obra Social 5%. Descuento de club 4%."""

from time import sleep


print()
print("========Calculo del sueldo============")
print("Ingrese los datos del empleado")
print()
nombre = input("Nombre: ")	
print()
dni = input ("DNI: ")
print()



while True:
	print()
	print ( "Seleccione la categoria de " + nombre)
	print ( "0: Para Maestranza.")
	print ( "1: Para Administracion.")
	print ( "2: Para Gerencia.")
	print()
	categoria = input ("Ingrese la categoria: ")

	if categoria != "0":
		if categoria != "1":
			if categoria != "2":
				print ("valor incorrecto. Selecione 0, 1 o 2.")
				print()
				sleep(2)
				print()

	if (categoria == "0" or categoria == "1" or categoria == "2"):
		print ("hola")
		break
	



while categoria > "2":
	print()
	print ( "Seleccione la categoria de " + nombre)
	print ( "0: Para Maestranza.")
	print ( "1: Para Administracion.")
	print ( "2: Para Gerencia.")
	print()
	categoria = input ("Ingrese la categoria: ")

	if categoria != "0":
		if categoria != "1":
			if categoria != "2":
				print ("valor incorrecto. Selecione 0, 1 o 2.")
				print()
				sleep(2)
				print ("estoy en el if" +categoria)
				print()


if categoria == "0":
	bruto=23600;
	jubi= bruto*0.11;
	obra= bruto*0.03;
	desc=jubi+obra;
	neto= bruto-desc;
	categoria= "Maestranza"


	
if categoria == "1":
	bruto=35800;
	jubi= bruto*0.11;
	obra= bruto*0.05;
	desc=jubi+obra;
	neto= bruto-desc;
	categoria= "Administración"
	
if categoria == "2":
	bruto=60420;
	jubi= bruto*0.11;
	obra= bruto*0.05;
	club= bruto*0.04;
	desc=jubi+obra+club;
	neto= bruto-desc;
	categoria= "Gerencia"


print ("____________________________________________________________")
print ("                  RECIBO DE SUELDO")
print (" ")
print ("Empleado:  " + nombre)
print ("DNI:       " + dni)
print ("Categoria: " + categoria)
print ("                        HABERES       DESCUENTOS")
print (f"Sueldo bruto:          $  {bruto}")
print (f"Jubilacion:                            $   {jubi}")
print (f"Obra Social:                           $   {obra}")
if categoria == "2":
	print (f"Club:                                  $  {club}")
		
print ("                      __________________________")
print (f"             Total:     $  {bruto}      $  {desc}")
print ("       ")
print (f"Neto a pagar:  $  {neto}")
print ("____________________________________________________________")
print (" ")

