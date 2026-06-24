#!/usr/bin/env bash
set -euo pipefail

echo "🛡️ Preparando tu carpeta de aprendizaje..."

if ! command -v python3 >/dev/null 2>&1; then
  echo "Aviso: Python 3 no está instalado."
else
  echo "✓ Python: $(python3 --version)"
fi

if ! command -v git >/dev/null 2>&1; then
  echo "Aviso: Git no está instalado."
else
  echo "✓ Git: $(git --version)"
fi

mkdir -p laboratorio/{datos-sinteticos,capturas,notas}

if [ ! -d .git ] && command -v git >/dev/null 2>&1; then
  git init
  git branch -M main 2>/dev/null || true
  echo "✓ Repositorio Git iniciado."
fi

chmod +x 11-PROYECTOS/01-analizador-logs/analizador.py

echo
echo "Preparación terminada."
echo "Empieza con:"
echo "  cat 00-INICIO/DIA-01.md"
echo
echo "Primer proyecto de demostración:"
echo "  cd 11-PROYECTOS/01-analizador-logs"
echo "  python3 analizador.py datos.log"
