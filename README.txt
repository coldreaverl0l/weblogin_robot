El programa presente es un robot que permite iniciar sesión de forma automática en una página web, hay que tener en cuenta
 algunas consideraciones:

 1) Se cuenta con dos archivos.py, el primero es solo para agregar credenciales como usuario y contraseña; mientras que el
 otro es para iniciar sesión en la página web deseada, lo que ocurre cuando se ejecuta el script. 

 2) En las líneas 15, 21 y 31 del código, está la clave para que el robot funcione, ya que se debe ingresa ID o nombre respectivo 
 del recurso web para ingresar usuario, contraseña y boton de submit, lo cuál puede variar de una página a otra, para poder saber
 el nombre exacto del recurso, hay que hacer click derecho sobre él y poner "inspeccionar elemento". 

 3) Esto es una técnica de web scrapping básica, donde la librería que hace el trabajo se llama "selenium". 

 