# Dia 4 - Procesos y servicios en Linux

## Objetivo

Entender que programas estan corriendo, como verlos y como revisar servicios del sistema.

## Procesos

Un proceso es un programa en ejecucion. Cada proceso tiene un numero llamado PID.

Comandos principales:

```bash
ps aux
top
pgrep NOMBRE
```

Ejemplos:

```bash
ps aux | less
pgrep bash
top
```

## Servicios

Un servicio es un proceso administrado por el sistema, normalmente con `systemd`.

Comandos seguros para mirar:

```bash
systemctl status
systemctl list-units --type=service
systemctl status ssh
```

Si un servicio no existe, Linux mostrara un error. Eso tambien es aprendizaje.

## Logs de servicios

Para ver mensajes del sistema:

```bash
journalctl -n 50
journalctl -xe
```

Para ver logs de un servicio:

```bash
journalctl -u NOMBRE_SERVICIO
```

## Practica

1. Ejecuta:

```bash
ps aux | head
```

2. Escribe que columnas ves.
3. Ejecuta:

```bash
systemctl list-units --type=service | head
```

4. Elige un servicio y revisa su estado:

```bash
systemctl status NOMBRE_SERVICIO
```

5. Guarda tus notas en:

```text
laboratorio/notas/dia-04.txt
```

## Preguntas finales

- Que es un PID?
- Que diferencia hay entre un proceso y un servicio?
- Para que sirve `top`?
- Para que sirve `systemctl status`?
- Para que sirve `journalctl`?
