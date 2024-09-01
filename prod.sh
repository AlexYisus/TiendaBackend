#!/usr/bin/env bash
set -o errexit  # Exit on first command that fails

# Activar el entorno virtual si lo estás usando
# source /path/to/your/venv/bin/activate

# Aplicar migraciones
python manage.py migrate

# Iniciar el servidor Django
gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
