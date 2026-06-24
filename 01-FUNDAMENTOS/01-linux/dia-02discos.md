# Día 2 — Discos, particiones y sistemas de archivos

## Problema encontrado

Ubuntu detectó un disco de 1 TB, pero no pudo montarlo y mostró el siguiente error:

```text
Unable to access “1.0 TB Volume”
Error mounting /dev/sdb1
wrong fs type, bad option, bad superblock or other error
```

## Dispositivo identificado

El disco completo fue identificado como:

```text
/dev/sdb
```

La primera partición del disco fue identificada como:

```text
/dev/sdb1
```

Aprendí que `/dev/sdb` representa el disco físico completo y `/dev/sdb1` representa una partición dentro de ese disco.

## Comandos utilizados

### Ver discos y sistemas de archivos

```bash
lsblk -f
```

Este comando permite ver los discos, las particiones, los sistemas de archivos y los puntos de montaje.

### Identificar el sistema de archivos

```bash
sudo blkid /dev/sdb1
```

El resultado fue:

```text
/dev/sdb1: BLOCK_SIZE="512" UUID="C6704B8D704B82E3" TYPE="ntfs" PARTUUID="ba62a93c-01"
```

## Resultado del diagnóstico

La partición utiliza el sistema de archivos:

```text
NTFS
```

NTFS es un sistema de archivos utilizado principalmente por Windows.

Linux detectó correctamente:

* El disco físico.
* Su capacidad de aproximadamente 1 TB.
* La partición `/dev/sdb1`.
* El sistema de archivos NTFS.
* Que el disco no tiene protección contra escritura.

Sin embargo, detectar el disco no significa que Linux pueda montarlo correctamente.

## Información mostrada por el kernel

El kernel mostró que el disco tiene:

```text
1953525167 bloques lógicos de 512 bytes
Capacidad aproximada: 1.00 TB / 932 GiB
Write Protect: off
Caché de lectura y escritura activada
```

## Conceptos aprendidos

### Disco

Un disco es el dispositivo físico completo.

Ejemplo:

```text
/dev/sdb
```

### Partición

Una partición es una división lógica dentro del disco.

Ejemplo:

```text
/dev/sdb1
```

### Sistema de archivos

El sistema de archivos organiza cómo se guardan los archivos dentro de una partición.

En este caso:

```text
NTFS
```

### Montar

Montar significa conectar un sistema de archivos a una carpeta de Linux para poder acceder a su contenido.

### Formatear

Formatear significa crear un sistema de archivos nuevo. Puede eliminar o hacer inaccesibles los datos existentes.

Montar y formatear no son lo mismo.

### Solo lectura

Montar un disco como solo lectura permite consultar sus archivos sin modificar el contenido.

La opción utilizada es:

```text
ro
```

## Posibles causas del error

El problema podría deberse a:

* El disco no se expulsó correctamente.
* Windows dejó el sistema NTFS en estado de hibernación.
* El Inicio rápido de Windows dejó el volumen bloqueado.
* El sistema de archivos contiene errores.
* Falta algún componente para montar NTFS.
* Existe un problema físico, aunque todavía no hay suficiente evidencia para afirmarlo.

## Precauciones tomadas

No ejecuté comandos de formateo o reparación automática.

No utilicé:

```bash
mkfs
fsck -y
ntfsfix
```

Primero realicé un diagnóstico para evitar perder información.

## Lo que aprendí

Aprendí que antes de intentar reparar un disco hay que identificar:

1. El dispositivo correcto.
2. La partición correcta.
3. El sistema de archivos.
4. Los mensajes del kernel.
5. Si el disco contiene información importante.
6. Si es posible acceder primero en modo de solo lectura.

También aprendí que no se debe ejecutar un comando únicamente porque aparece en Internet. Primero debo comprender qué modifica y qué riesgo tiene.

## Próximo paso

Intentar montar `/dev/sdb1` en modo de solo lectura y revisar el mensaje de error exacto sin modificar los datos.

