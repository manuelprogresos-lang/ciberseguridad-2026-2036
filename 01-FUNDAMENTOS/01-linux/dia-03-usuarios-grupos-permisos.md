# Día 3 — Usuarios, grupos y permisos en Linux

## Objetivo

Aprender cómo Linux identifica a los usuarios y grupos, y cómo decide quién puede leer, modificar o ejecutar un archivo o carpeta.

## Usuarios

Cada usuario tiene un identificador numérico llamado UID.

Ejemplo:

```text
uid=1000(manuel)
```

Esto significa:

* `1000` es el UID.
* `manuel` es el nombre del usuario.

Linux utiliza internamente el UID para identificar al usuario.

El usuario `root` normalmente tiene:

```text
UID 0
```

## Grupos

Un grupo permite reunir varios usuarios y compartir permisos entre ellos.

Cada grupo tiene un identificador llamado GID.

Ejemplo:

```text
gid=1000(manuel)
```

Un usuario puede tener:

* un grupo principal;
* varios grupos secundarios.

Comandos utilizados:

```bash
whoami
id
groups
```

## Propietario, grupo y otros

Cada archivo o carpeta tiene permisos para tres categorías:

```text
usuario propietario | grupo propietario | otros
```

Ejemplo:

```text
-rwxr-x---
```

Se divide así:

```text
rwx   r-x   ---
user  group others
```

Significa:

* El propietario puede leer, escribir y ejecutar.
* El grupo puede leer y ejecutar.
* Los demás usuarios no tienen permisos.

## Permisos

Los permisos principales son:

```text
r = read    = leer
w = write   = escribir
x = execute = ejecutar
```

En archivos:

* `r`: leer el contenido.
* `w`: modificar el contenido.
* `x`: ejecutar el archivo.

En carpetas:

* `r`: ver los nombres de los archivos.
* `w`: crear, borrar o renombrar archivos.
* `x`: entrar en la carpeta y acceder a su contenido.

## Método simbólico de chmod

`chmod` significa `change mode` y sirve para cambiar permisos.

Las letras utilizadas son:

```text
u = user
g = group
o = others
a = all
```

Ejemplos:

```bash
chmod u+x script.sh
chmod g+r archivo.txt
chmod o-r archivo.txt
chmod a-rwx archivo.txt
```

Los símbolos significan:

```text
+ = añadir permiso
- = quitar permiso
```

## Método numérico

Cada permiso tiene un valor:

```text
r = 4
w = 2
x = 1
```

Combinaciones:

```text
0 = ---
1 = --x
2 = -w-
3 = -wx
4 = r--
5 = r-x
6 = rw-
7 = rwx
```

Ejemplos:

```bash
chmod 644 documento.txt
```

Resultado:

```text
rw-r--r--
```

```bash
chmod 700 carpeta/
```

Resultado:

```text
rwx------
```

```bash
chmod 755 script.sh
```

Resultado:

```text
rwxr-xr-x
```

## Permisos recomendados

```text
600 = archivo privado
644 = documento normal
700 = carpeta o script privado
755 = script o carpeta accesible para lectura y ejecución
```

No se recomienda utilizar `777` sin una razón clara, porque entrega todos los permisos al propietario, al grupo y a los demás usuarios.

## Comandos aprendidos

```bash
whoami
id
groups
ls -l
ls -ld
chmod
```

## Lo que aprendí

Aprendí que:

1. Linux identifica a los usuarios mediante UID.
2. Linux identifica a los grupos mediante GID.
3. Un grupo puede contener varios usuarios.
4. Cada archivo tiene un propietario y un grupo.
5. Los permisos se dividen entre propietario, grupo y otros.
6. `chmod` permite añadir o quitar permisos.
7. Los permisos pueden representarse con letras o números.
8. Los permisos sirven para proteger archivos y limitar acciones.


