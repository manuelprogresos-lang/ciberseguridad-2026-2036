# Día 1 — Preparación y terminal Linux

## Objetivo

Aprender a moverte por Linux y crear tu primer registro de progreso.

## Tareas

### 1. Comprueba tu sistema

```bash
whoami
pwd
uname -a
```

Escribe en tus notas qué crees que muestra cada comando.

### 2. Practica navegación

```bash
ls
ls -la
cd 01-FUNDAMENTOS/01-linux
pwd
cd ../..
```

### 3. Crea un archivo de práctica

```bash
mkdir -p laboratorio/notas
touch laboratorio/notas/dia-01.txt
nano laboratorio/notas/dia-01.txt
```

Escribe:
- qué aprendiste;
- qué comando te costó;
- qué quieres repetir mañana.

### 4. Haz tu primer commit

```bash
git status
git add .
git commit -m "Completo el día 1"
```

## Prueba final

Sin mirar, explica:
- qué hace `pwd`;
- qué diferencia hay entre `ls` y `ls -la`;
- qué hace `cd ..`;
- qué hace `mkdir -p`;
- para qué sirve `git status`.
