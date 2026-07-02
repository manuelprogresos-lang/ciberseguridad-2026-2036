# Día 5 — Paquetes y actualizaciones en Linux

## ¿Qué es un paquete?

Un paquete es un archivo preparado para instalar software en Linux.

Puede contener:

* programas ejecutables;
* bibliotecas;
* archivos de configuración;
* documentación;
* scripts de instalación;
* información sobre la versión;
* dependencias necesarias;
* instrucciones para instalar o eliminar el software.

En Ubuntu y otras distribuciones basadas en Debian, los paquetes suelen utilizar el formato `.deb`.

## ¿Qué es APT?

APT es el administrador de paquetes utilizado en Ubuntu.

APT se encarga de:

* buscar paquetes;
* descargar paquetes;
* instalar programas;
* resolver dependencias;
* actualizar programas;
* eliminar paquetes;
* consultar repositorios.

APT normalmente obtiene los paquetes desde repositorios configurados en el sistema.

## Repositorios

Un repositorio es un servidor que contiene paquetes de software y su información.

APT consulta esos repositorios para conocer:

* qué paquetes existen;
* qué versiones están disponibles;
* cuáles tienen actualizaciones;
* qué dependencias necesita cada paquete.

## apt update

El comando:

```bash
sudo apt update
```

actualiza la lista local de paquetes disponibles.

No instala las nuevas versiones de los programas.

APT descarga información sobre las versiones disponibles en los repositorios y la guarda en el sistema.

Durante este proceso pueden aparecer mensajes como:

```text
GET
HIT
IGN
```

Significados:

* `GET`: se descargó información nueva desde el repositorio.
* `HIT`: la información existente ya estaba actualizada.
* `IGN`: cierta información fue ignorada porque no era necesaria o no estaba disponible temporalmente.

## apt upgrade

El comando:

```bash
sudo apt upgrade
```

instala las nuevas versiones disponibles de los paquetes que ya están instalados.

La secuencia habitual es:

```bash
sudo apt update
sudo apt upgrade
```

Primero se actualiza el catálogo y después se instalan las actualizaciones.

## Instalar paquetes

Para instalar un paquete:

```bash
sudo apt install nombre-paquete
```

Ejemplo:

```bash
sudo apt install mc
```

`mc` es Midnight Commander, un administrador de archivos para la terminal.

También es posible instalar un paquete `.deb` descargado localmente:

```bash
sudo apt install ./archivo.deb
```

## Buscar información de un paquete

Buscar paquetes:

```bash
apt search nombre
```

Ver información detallada:

```bash
apt show nombre-paquete
```

Ver los archivos instalados por un paquete:

```bash
dpkg -L nombre-paquete
```

## Eliminar paquetes

Eliminar un programa:

```bash
sudo apt remove nombre-paquete
```

Eliminar el programa y sus archivos de configuración:

```bash
sudo apt purge nombre-paquete
```

Eliminar dependencias que ya no son necesarias:

```bash
sudo apt autoremove
```

## El comando tree

El comando `tree` muestra la estructura de carpetas y archivos de una ruta.

Ejemplo:

```bash
tree /etc
```

`tree` no muestra directamente la estructura interna de un paquete. Muestra la organización de archivos y directorios del sistema.

## Uso de sudo

`sudo` permite ejecutar un comando con privilegios administrativos.

Ejemplo:

```bash
sudo apt install mc
```

El comando:

```bash
sudo su
```

abre una sesión completa como usuario `root`.

Aunque evita escribir `sudo` repetidamente, es más seguro utilizar `sudo` solamente en los comandos que realmente necesitan permisos administrativos.

## Resumen

```text
Paquete     = conjunto de archivos preparados para instalar software
Repositorio = servidor donde se almacenan paquetes
APT         = herramienta que administra paquetes
apt update  = actualiza la lista de versiones disponibles
apt upgrade = instala las actualizaciones
apt install = instala paquetes
apt remove  = elimina paquetes
```

La idea principal del día es:

> APT consulta repositorios, administra paquetes y resuelve las dependencias necesarias para instalar y actualizar software.
