Fecha: 6 abril 2023

Para ejecutar directamente (y no desde otra terminal) codigo Python  mientras codificamos recomiendo usar el editor de codigo:
Sublime Text 4

Para configurar Python en sublime Text seguimos los siguientes pasos desde la barra de tareas del programa:

1. Para habilitar el "Package Control" en "Preferences":
	Tools > Command Pallette > Package Control: install Package > SublimeREPEL   

2. Para instalar un plugins de Python:
	Preferences > Package Control > install Package > Python 3

3. Para abrir una terminal y ejecutar codigo Pytho:
	Tools > SublimeREPL > Python > Python  

4. Para ejecutar el codigo mientras lo trabajas de forma directa:
	Tools > Build System > New Build System > pegamos el codigo:
	
		{
  		 "target":"run_existing_window_command",
   		 "id":"repl_python_run",
    		"file":"config/python/Main.sublime-menu"
		} 

	Y lo guardamos (Ctrl+s) como: Run_python.sublime-build
	Se guarda en el mismo directorio donde se guardo el programa
	generalmente en C:archivos de programa > sublime Text > packages

	Para usarlo Hacemos :
	Tools > Build System > Run_python
	Luego en nuestro codigo ejecutamos con "Ctrl + B" 

5. Para configurar el internilieado automatico:
	Preferences > Setting > y al codigo le agrego el "word_wrap" asi:

		{
			"ignored_packages":
			[
				"Vintage",
			],
			"font_size": 13,
			"word_wrap": "true",
			"color_scheme": "Packages/Python 3/Gloom.tmTheme",
			"theme": "Brogrammer.sublime-theme",
		}

	luego guardo (Ctrl+s)

	
