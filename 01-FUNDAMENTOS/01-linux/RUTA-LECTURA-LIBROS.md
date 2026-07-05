# Ruta de lectura con los libros de Linux

## Objetivo

Usar los dos libros como apoyo, sin perder el orden de tu plan de 30 dias.

## Semana 1: base de Linux

### Dia 1: terminal y rutas

- Nota principal: `00-INICIO/DIA-01.md`
- Apoyo: `How-Linux-Works.pdf`
- Practica: `pwd`, `ls`, `cd`, `mkdir`, `touch`, `nano`

### Dia 2: archivos, carpetas y discos

- Nota principal: `dia-02discos.md`
- Apoyo: `How-Linux-Works.pdf`
- Practica: `df -h`, `du -sh`, `mount`, `lsblk`

### Dia 3: usuarios, grupos y permisos

- Nota principal: `dia-03-usuarios-grupos-permisos.md`
- Apoyo: ambos libros
- Practica: `whoami`, `id`, `groups`, `ls -l`, `chmod`

### Dia 4: procesos y servicios

- Nota principal: `dia-04-procesos-servicios.md`
- Apoyo: `How-Linux-Works.pdf`
- Practica: `ps`, `top`, `systemctl`, `journalctl`

### Dia 5: paquetes y actualizaciones

- Nota principal: `dia-05_Paquetes_Actualizaciones.md`
- Apoyo: `linux-basics-for-hackers.pdf`
- Practica: `apt update`, `apt search`, `apt show`

### Dia 6: logs basicos

- Nota principal: `dia-6_logsbasico_linux.md`
- Apoyo: ambos libros
- Practica: `journalctl`, `tail`, `grep`, `less`

### Dia 7: repaso

- Entrega: `guia-20-comandos.md`
- Tarea: explicar cada comando con tus propias palabras y un ejemplo.

## Como juntar lo de ChatGPT

El enlace compartido de ChatGPT no se pudo leer automaticamente desde aqui. Para integrarlo:

1. Abre el chat compartido.
2. Copia las partes importantes.
3. Pegalas en un archivo nuevo dentro de `16-RECURSOS/notas-chatgpt/`.
4. Despues las convertimos en notas por tema: Linux, redes, Python, blue team, web, etc.

## Formato para cada nota nueva

```markdown
# Tema

## Que aprendi

## Comandos

## Ejemplo probado

## Dudas

## Proximo paso
```
