#!/usr/bin/env python
"""
Exemplo simples de uso do TreeDocs
"""

from tree_docs import TreeGenerator

# Gera a documentação do projeto atual
generator = TreeGenerator()
generator.gerar_documentacao(
    nome_projeto="Meu Projeto",
    arquivo_saida="docs/estrutura.md",
    root_dir="."
)

print("✅ Documentação gerada com sucesso!")