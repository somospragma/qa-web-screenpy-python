#!/usr/bin/env python3
"""
Script de configuración inicial para el proyecto qa-web-screenpy-python
Configura el entorno de desarrollo con herramientas de seguridad
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command, description):
    """Ejecutar comando y manejar errores"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {description}: {e}")
        print(f"Salida: {e.stdout}")
        print(f"Error: {e.stderr}")
        return False


def setup_environment():
    """Configurar entorno de desarrollo"""
    print("🚀 Configurando entorno de desarrollo seguro...")
    
    # Crear archivo .env si no existe
    env_file = Path(".env")
    if not env_file.exists():
        print("📝 Creando archivo .env...")
        with open(".env", "w") as f:
            f.write("TARGET_URL=https://www.pragma.co/es/\n")
            f.write("HEADLESS_MODE=true\n")
            f.write("BROWSER_TIMEOUT=30\n")
        print("✅ Archivo .env creado")
    
    # Instalar dependencias
    commands = [
        ("pip install --upgrade pip", "Actualizando pip"),
        ("pip install -r requirements.txt", "Instalando dependencias"),
        ("pre-commit install", "Configurando pre-commit hooks"),
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            print(f"⚠️  Falló: {description}")
    
    # Ejecutar análisis inicial
    print("\n🔍 Ejecutando análisis inicial de seguridad...")
    
    analysis_commands = [
        ("safety check", "Verificando vulnerabilidades en dependencias"),
        ("bandit -r . -ll", "Análisis estático de seguridad"),
        ("flake8 . --count --statistics", "Análisis de calidad de código"),
    ]
    
    for command, description in analysis_commands:
        run_command(command, description)
    
    print("\n🎉 Configuración completada!")
    print("\n📋 Próximos pasos:")
    print("1. Revisar el archivo .env y ajustar configuraciones")
    print("2. Ejecutar: pytest features/ para correr las pruebas")
    print("3. Revisar reportes de seguridad generados")


if __name__ == "__main__":
    setup_environment()