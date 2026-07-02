# Día 4.2 — Servicios en Linux

## Lo que aprendí hoy

Hoy aprendí la diferencia entre un proceso y un servicio en Linux.

- Un proceso es un programa que está ejecutándose.
- Un servicio es un proceso que normalmente trabaja en segundo plano realizando una tarea continua.

## Ejemplos de servicios

- NetworkManager administra la red.
- systemd-journald guarda registros del sistema.
- ssh permite conexiones remotas.
- cron ejecuta tareas programadas.

## systemd y systemctl

- systemd es el administrador de servicios de Linux.
- systemctl es el comando que utilizo para comunicarme con systemd.

La relación básica es:

Usuario → systemctl → systemd → servicio → proceso → PID

## Comandos básicos

```bash
systemctl status nombre-servicio
systemctl is-active nombre-servicio
systemctl is-enabled nombre-servicio
systemctl start nombre-servicio
systemctl stop nombre-servicio
systemctl restart nombre-servicio
