#!/usr/bin/env python3
"""
Script para incrementar versão semanticamente (Semantic Versioning).

Uso:
    python scripts/bump_version.py [major|minor|patch]
    
Exemplos:
    python scripts/bump_version.py patch   # 1.0.0 -> 1.0.1
    python scripts/bump_version.py minor   # 1.0.1 -> 1.1.0
    python scripts/bump_version.py major   # 1.1.0 -> 2.0.0
    
Convenção:
    - MAJOR: Mudanças incompatíveis (breaking changes)
    - MINOR: Novas funcionalidades (compatíveis)
    - PATCH: Correções de bugs
"""
import sys
import os
import re
from datetime import datetime

VERSION_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'VERSION')

def read_version():
    """Lê a versão atual do arquivo"""
    if not os.path.exists(VERSION_FILE):
        print(f"❌ Arquivo VERSION não encontrado em: {VERSION_FILE}")
        sys.exit(1)
    
    with open(VERSION_FILE, 'r') as f:
        return f.read().strip()

def write_version(version):
    """Escreve nova versão no arquivo"""
    with open(VERSION_FILE, 'w') as f:
        f.write(version)

def bump_version(bump_type='patch'):
    """Incrementa a versão conforme o tipo"""
    current = read_version()
    
    # Validar formato
    match = re.match(r'^(\d+)\.(\d+)\.(\d+)$', current)
    if not match:
        print(f"❌ Versão inválida: '{current}'. Formato esperado: MAJOR.MINOR.PATCH")
        sys.exit(1)
    
    major, minor, patch = map(int, match.groups())
    
    # Incrementar
    if bump_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'patch':
        patch += 1
    else:
        print(f"❌ Tipo inválido: '{bump_type}'. Use: major, minor ou patch")
        sys.exit(1)
    
    new_version = f"{major}.{minor}.{patch}"
    
    # Salvar
    write_version(new_version)
    
    # Resumo
    print(f"\n{'='*50}")
    print(f"📦 Versão atualizada com sucesso!")
    print(f"{'='*50}")
    print(f"   Anterior:  {current}")
    print(f"   Nova:      {new_version}")
    print(f"   Tipo:      {bump_type.upper()}")
    print(f"   Data:      {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"{'='*50}\n")
    
    # Gerar comando git sugerido
    print("📝 Próximos passos sugeridos:")
    print(f"   git add VERSION")
    print(f'   git commit -m "release: bump version {current} -> {new_version}"')
    print(f"   git tag -a v{new_version} -m 'Release v{new_version}'")
    print(f"   git push origin main --tags")
    print()
    
    return new_version

def show_current():
    """Mostra a versão atual"""
    current = read_version()
    print(f"📦 Versão atual: {current}")
    return current

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in ['--show', '-s', 'show']:
        show_current()
    elif len(sys.argv) > 1:
        bump_version(sys.argv[1])
    else:
        print("📦 Sistema de Versionamento - Semantic Versioning")
        print(f"\nVersão atual: {read_version()}")
        print("\nUso: python bump_version.py [major|minor|patch]")
        print("\nExemplos:")
        print("  python bump_version.py patch   # Correção de bug")
        print("  python bump_version.py minor   # Nova funcionalidade")
        print("  python bump_version.py major   # Mudança incompatível")
        print("  python bump_version.py --show  # Mostrar versão atual")