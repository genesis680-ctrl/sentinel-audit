#!/bin/bash
echo "--- SENTINEL AUDIT: INSTALADOR AUTOMATICO ---"
pkg update && pkg upgrade -y
pkg install python -y
pip install pypdf requests
mkdir -p engine rules reports utils
touch utils/__init__.py
chmod +x setup.sh main.py
echo "[+] Ambiente configurado com sucesso!"
