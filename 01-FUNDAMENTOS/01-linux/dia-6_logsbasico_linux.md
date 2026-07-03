# Día 6 — Logs básicos en Linux

## ¿Qué es un log?

Un log es un registro de eventos importantes del sistema.

Los logs pueden guardar información sobre:

* inicios de sesión;
* cierres de sesión;
* errores;
* advertencias;
* actividad de servicios;
* uso de `sudo`;
* instalaciones y actualizaciones;
* intentos de acceso;
* mensajes del sistema;
* actividad de aplicaciones.

Un log no guarda absolutamente todo lo que hago, pero sí registra muchos eventos importantes para administración, soporte técnico y ciberseguridad.

## ¿Para qué sirven los logs?

Los logs sirven para investigar qué ocurrió en una máquina.

Ayudan a responder preguntas como:

* ¿Qué pasó?
* ¿Cuándo pasó?
* ¿Qué usuario estaba involucrado?
* ¿Qué servicio generó el error?
* ¿Hubo intentos fallidos de acceso?
* ¿Se instaló o eliminó algún paquete?
* ¿Un servicio se inició, falló o se detuvo?

En ciberseguridad, los logs son importantes porque funcionan como evidencia técnica.

## /var/log

En Linux, muchos archivos de log se encuentran en:

```bash
/var/log
```

Para ver esa carpeta:

```bash
ls /var/log
```

Algunos logs comunes son:

```text
auth.log   = autenticación, sudo e inicios de sesión
syslog     = mensajes generales del sistema
kern.log   = mensajes del kernel
apt/       = historial de paquetes y actualizaciones
```

## journalctl

`journalctl` sirve para ver los logs administrados por `systemd`.

Ver logs generales:

```bash
journalctl
```

Ver los últimos eventos:

```bash
journalctl -n 20
```

Ver logs del arranque actual:

```bash
journalctl -b
```

Ver errores del arranque actual:

```bash
journalctl -p err -b
```

Ver logs en tiempo real:

```bash
journalctl -f
```

La opción `-f` significa `follow`, es decir, seguir los logs mientras ocurren.

## Ver logs de un servicio

Para ver los logs de un servicio específico:

```bash
journalctl -u nombre-servicio
```

Ejemplo con Apache:

```bash
journalctl -u apache2
```

Para ver los logs de Apache en tiempo real:

```bash
journalctl -f -u apache2
```

Esto permite observar lo que va ocurriendo con ese servicio.

## Filtrar logs por fecha

Con `--since` puedo ver logs desde un momento específico.

Ejemplos:

```bash
journalctl --since "1 hour ago"
journalctl --since "10 minutes ago"
journalctl --since "yesterday"
journalctl -u apache2 --since "1 hour ago"
```

Esto es útil cuando quiero investigar un problema que ocurrió recientemente.

## Ver logs por usuario

Cada usuario tiene un número llamado UID.

Para ver mi UID:

```bash
id
```

Para ver logs relacionados con un usuario específico:

```bash
journalctl _UID=1000
```

Normalmente, el primer usuario creado en Ubuntu tiene UID `1000`.

## tail

`tail` sirve para ver las últimas líneas de un archivo.

```bash
tail archivo.log
```

Por defecto muestra las últimas 10 líneas.

Para ver solo 5 líneas:

```bash
tail -n 5 archivo.log
```

Para seguir un archivo en tiempo real:

```bash
tail -f archivo.log
```

Ejemplo:

```bash
tail -f /var/log/syslog
```

## grep

`grep` sirve para buscar texto dentro de un archivo.

Ejemplo:

```bash
grep "error" /var/log/syslog
```

Para ignorar mayúsculas y minúsculas:

```bash
grep -i "error" /var/log/syslog
```

Esto encuentra palabras como:

```text
error
Error
ERROR
```

Buscar intentos fallidos de autenticación:

```bash
sudo grep -i "failed" /var/log/auth.log
```

## Logs de APT

APT también tiene logs.

Para ver el historial de instalaciones, actualizaciones y eliminaciones:

```bash
less /var/log/apt/history.log
```

Este archivo ayuda a saber qué paquetes fueron instalados, actualizados o eliminados.

## Limpiar logs antiguos del journal

Existe un comando para reducir el tamaño de los logs antiguos:

```bash
sudo journalctl --vacuum-size=500M
```

Este comando elimina logs antiguos hasta que el journal quede cerca de 500 MB.

No es un comando para investigar. Es un comando para limpiar espacio.

## Comparación con Windows

`journalctl` en Linux se parece un poco a `Event Viewer` en Windows.

Ambos permiten revisar:

* eventos del sistema;
* errores;
* servicios;
* actividad de usuarios;
* eventos de seguridad;
* actividad de aplicaciones.

No son exactamente iguales, pero la idea es parecida.

## Resumen

```text
Log        = registro de eventos importantes
/var/log   = carpeta donde se guardan muchos logs
journalctl = herramienta para ver logs de systemd
-u         = filtrar por servicio
-f         = seguir logs en tiempo real
--since    = filtrar por fecha
tail       = ver últimas líneas de un archivo
tail -f    = seguir un archivo en tiempo real
grep       = buscar palabras dentro de logs
```

## Idea principal

Los logs son evidencia técnica. Sirven para investigar eventos del sistema, errores, actividad de servicios, usuarios, accesos y cambios importantes.

En ciberseguridad, los logs ayudan a reconstruir qué ocurrió en una máquina.
