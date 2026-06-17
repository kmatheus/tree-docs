"""
TreeDocs - Gerador automático de árvore de diretórios para documentação em Markdown

Uma ferramenta simples e poderosa para gerar documentação visual da estrutura
de seus projetos, com emojis, comentários e formatação profissional.

Exemplo de uso:
    >>> from tree_docs import TreeGenerator
    >>> generator = TreeGenerator()
    >>> generator.gerar_documentacao("Meu Projeto", "docs/estrutura.md")
"""

from .generator import TreeGenerator
from .config import Config
from .defaults import DEFAULTS
from .cli import main

__version__ = "0.1.3"
__all__ = ["TreeGenerator", "Config", "DEFAULTS", "main"]
