#!/usr/bin/env python
"""
Interface de linha de comando para o TreeDocs
"""

import argparse
import sys
from pathlib import Path

from .generator import TreeGenerator
from .config import Config


def main() -> int:
    """Ponto de entrada principal da CLI"""
    
    parser = argparse.ArgumentParser(
        prog="tree-docs",
        description="Gerador de árvore de diretórios para documentação em Markdown",
        epilog="Exemplo: tree-docs -d . -o docs/estrutura.md -n 'Meu Projeto'"
    )
    
    parser.add_argument(
        "-d", "--directory",
        default=".",
        help="Diretório raiz para escanear (padrão: .)"
    )
    
    parser.add_argument(
        "-o", "--output",
        default="docs/estrutura_projeto.md",
        help="Arquivo de saída (padrão: docs/estrutura_projeto.md)"
    )
    
    parser.add_argument(
        "-n", "--name",
        default=None,
        help="Nome do projeto (padrão: nome do diretório)"
    )
    
    parser.add_argument(
        "--max-depth",
        type=int,
        default=5,
        help="Profundidade máxima da árvore (padrão: 5)"
    )
    
    parser.add_argument(
        "--ignore",
        default="venv,__pycache__,.git,.pytest_cache,migrations,node_modules,.idea,.vscode,logs,media,static,__pycache__,dist,build,*.egg-info",
        help="Pastas a ignorar (separadas por vírgula)"
    )
    
    parser.add_argument(
        "--no-emojis",
        action="store_true",
        help="Desativa emojis na saída (útil para terminais sem suporte)"
    )
    
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"tree-docs {__import__('tree_docs').__version__}"
    )
    
    args = parser.parse_args()
    
    # Define o nome do projeto
    project_name = args.name or Path(args.directory).name
    
    # Configura pastas a ignorar
    ignore_dirs = set(args.ignore.split(','))
    
    # Cria configuração
    config = Config(
        ignore_dirs=ignore_dirs,
        max_depth=args.max_depth,
        project_name=project_name,
        output_file=args.output
    )
    
    # Gera a documentação
    try:
        generator = TreeGenerator(config)
        generator.gerar_documentacao(
            nome_projeto=project_name,
            arquivo_saida=args.output,
            root_dir=args.directory
        )
        return 0
    except KeyboardInterrupt:
        print("\n⚠️  Operação cancelada pelo usuário")
        return 1
    except Exception as e:
        print(f"❌ Erro: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())