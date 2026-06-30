# Día 4 — Procesos, PID y el comando top

## ¿Qué es un programa?

Un programa es un archivo que contiene instrucciones.

Ejemplos:

```text
Firefox
Nano
Python
cat
sleep
```

Cuando un programa está guardado en el disco, todavía no está ejecutándose.

---

## ¿Qué es un proceso?

Un proceso es un programa que está funcionando en ese momento.

Ejemplo:

```text
Firefox cerrado = programa guardado
Firefox abierto = proceso ejecutándose
```

Cuando ejecuto un programa, el kernel:

1. Crea el proceso.
2. Le asigna memoria.
3. Le permite utilizar la CPU.
4. Le asigna un número llamado PID.
5. Controla cuándo termina.

---

## ¿Qué es un PID?

PID significa:

```text
Process ID
```

Es un número que Linux utiliza para identificar cada proceso.

Ejemplo:

```text
4580 sleep 300
```

En este ejemplo:

```text
4580      = PID
sleep 300 = proceso ejecutándose
```

Cada proceso tiene su propio PID.

---

## ¿Qué hace top?

El comando:

```bash
top
```

muestra en tiempo real los procesos que Linux está ejecutando.

No muestra solamente los procesos de mi terminal. Puede mostrar procesos de todo el sistema.

Para salir de `top` debo pulsar:

```text
q
```

---

## Columnas importantes de top

### PID

Es el número que identifica al proceso.

### USER

Muestra qué usuario está ejecutando el proceso.

### %CPU

Muestra cuánto procesador está utilizando.

### %MEM

Muestra cuánta memoria RAM está utilizando.

### COMMAND

Muestra el nombre del programa o comando.

### S

Muestra el estado del proceso.

Algunos estados son:

```text
R = Running, ejecutándose
S = Sleeping, esperando
T = detenido o pausado
Z = zombie
```

---

## El proceso PID 1

El proceso con PID 1 normalmente es:

```text
systemd
```

`systemd` es un proceso muy importante porque ayuda a iniciar y administrar otros servicios del sistema.

No debo ejecutar:

```bash
kill 1
```

Intentar terminar el PID 1 puede causar problemas, cerrar servicios o dejar Linux inestable.

Antes de terminar cualquier proceso debo saber qué función cumple.

---

## Práctica con sleep

El comando:

```bash
sleep 300
```

crea un proceso que espera durante 300 segundos.

```text
300 segundos = 5 minutos
```

Mientras funciona en primer plano, la terminal queda ocupada.

Puedo detenerlo con:

```text
Ctrl + C
```

---

## Ejecutar un proceso en segundo plano

El comando:

```bash
sleep 300 &
```

crea el proceso `sleep` y lo deja funcionando en segundo plano.

El símbolo:

```text
&
```

significa que puedo seguir utilizando la terminal mientras el proceso continúa.

---

## Buscar el proceso

Puedo buscar procesos llamados `sleep` con:

```bash
pgrep -a sleep
```

Este comando muestra:

* el PID;
* el comando completo.

Ejemplo:

```text
4580 sleep 300
```

Si no muestra nada, significa que no hay ningún proceso `sleep` ejecutándose.

---

## Terminar el proceso

Para pedirle a un proceso que termine utilizo:

```bash
kill PID
```

Ejemplo:

```bash
kill 4580
```

Debo cambiar `4580` por el PID real que aparezca en mi terminal.

Después puedo comprobarlo:

```bash
pgrep -a sleep
```

Si no aparece nada, el proceso terminó.

El comando `kill` normalmente envía una petición para que el proceso cierre correctamente.

No debo usar `kill -9` sin entenderlo, porque fuerza la terminación del proceso.

---

## Diferencia entre top y ps

```text
top = muestra los procesos en tiempo real
ps  = muestra una fotografía de los procesos en ese momento
```

Ejemplos:

```bash
top
ps
ps aux
```

---

## Práctica realizada

Ejecuté:

```bash
sleep 300 &
```

Después busqué el proceso con:

```bash
pgrep -a sleep
```

Identifiqué su PID y lo terminé con:

```bash
kill PID
```

También utilicé:

```bash
top
```

para observar procesos, usuarios y consumo de CPU y memoria.

---

## Lo que aprendí

Aprendí que:

1. Un programa guardado se convierte en proceso cuando se ejecuta.
2. Cada proceso tiene un PID.
3. `top` muestra procesos en tiempo real.
4. `%CPU` muestra consumo de procesador.
5. `%MEM` muestra consumo de memoria.
6. `sleep 300 &` crea un proceso de espera en segundo plano.
7. `pgrep -a sleep` permite encontrar ese proceso.
8. `kill PID` pide terminar un proceso.
9. No debo terminar procesos desconocidos.
10. Nunca debo intentar terminar el PID 1 por práctica.

## Resumen

```text
Programa = instrucciones guardadas
Proceso  = programa ejecutándose
PID      = número del proceso
top      = monitor de procesos en tiempo real
kill     = pide terminar un proceso
```
