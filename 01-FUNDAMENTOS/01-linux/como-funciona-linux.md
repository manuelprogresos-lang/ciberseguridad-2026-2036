# Cómo funciona Linux por dentro

## Idea principal

Linux se puede entender mediante tres partes:

```text
1. Programas
2. Kernel
3. Hardware
```

La frase que debo recordar es:

> El usuario ejecuta, el programa pide, el kernel controla y el hardware trabaja.

---

## 1. El usuario y los programas

El usuario es la persona que utiliza el ordenador.

Cuando escribo:

```bash
cat archivo.txt
```

yo soy el usuario y `cat` es el programa que quiero utilizar.

Otros ejemplos de programas son:

```text
Firefox
Bash
Python
Git
Nano
```

Los programas no controlan directamente el disco, la memoria o la red. Primero deben pedirle ayuda al kernel.

---

## 2. El kernel

El kernel es la parte central de Linux.

Su trabajo es controlar y organizar el sistema.

El kernel se encarga de:

* comprobar permisos;
* controlar procesos;
* repartir memoria RAM;
* controlar discos;
* controlar la red;
* comunicarse con el hardware;
* decidir qué programa puede usar la CPU.

El kernel funciona como un intermediario entre los programas y el hardware.

---

## 3. El hardware

El hardware es la parte física del ordenador.

Ejemplos:

```text
CPU
Memoria RAM
Disco
Tarjeta de red
Teclado
Pantalla
USB
```

El hardware realiza el trabajo físico.

Por ejemplo:

* el disco lee archivos;
* la CPU ejecuta instrucciones;
* la RAM guarda datos temporalmente;
* la tarjeta de red envía información;
* la pantalla muestra resultados.

---

# Ejemplo con cat

Cuando escribo:

```bash
cat archivo.txt
```

ocurre lo siguiente:

1. El usuario escribe el comando.
2. Se ejecuta el programa `cat`.
3. `cat` le pide al kernel abrir el archivo.
4. El kernel comprueba si el archivo existe.
5. El kernel comprueba si el usuario tiene permiso de lectura.
6. El kernel le pide al disco que lea los datos.
7. El disco entrega los datos al kernel.
8. El kernel entrega los datos al programa `cat`.
9. `cat` muestra el contenido en la pantalla.

El recorrido es:

```text
Usuario
   ↓
Programa cat
   ↓
Kernel
   ↓
Disco y memoria
   ↓
Kernel
   ↓
Programa cat
   ↓
Pantalla
   ↓
Usuario
```

---

# Relación con los permisos

Cuando intento abrir un archivo, el kernel revisa:

```text
UID
GID
Grupos
Permisos r, w y x
```

Por ejemplo:

```text
-rw-r----- manuel estudiantes notas.txt
```

Significa:

```text
Manuel puede leer y escribir.
El grupo estudiantes puede leer.
Los demás usuarios no tienen acceso.
```

Si un usuario no tiene permiso, el kernel puede mostrar:

```text
Permission denied
```

---

# Analogía del restaurante

Puedo imaginar Linux como un restaurante:

```text
Usuario y programa = cliente
Kernel             = camarero
Hardware           = cocina
```

El cliente no entra directamente a la cocina.

Primero hace un pedido al camarero.

El camarero comprueba el pedido, lo lleva a la cocina y después devuelve el resultado al cliente.

En Linux ocurre algo parecido:

```text
Programa → Kernel → Hardware → Kernel → Programa
```

---

# Lo que aprendí

Aprendí que:

1. El usuario ejecuta programas.
2. Los programas le piden operaciones al kernel.
3. El kernel comprueba permisos.
4. El kernel controla el hardware.
5. El hardware realiza el trabajo físico.
6. El resultado vuelve al programa.
7. El programa muestra el resultado al usuario.

## Resumen

```text
El programa pide.
El kernel comprueba y controla.
El hardware trabaja.
```
