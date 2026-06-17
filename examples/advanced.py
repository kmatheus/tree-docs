#!/usr/bin/env python
"""
Exemplo avançado de uso do TreeDocs com configuração personalizada
"""

from tree_docs import TreeGenerator, Config

# Configuração personalizada
config = Config(
    max_depth=4,
    ignore_dirs={"venv", "__pycache__", ".git"},
    project_name="Projeto Avançado",
    output_file="docs/estrutura_avancada.md",
    
    # Comentários personalizados
    pasta_comentarios={
        "custom": "Minha pasta personalizada",
        "backend": "Backend da aplicação",
        "frontend": "Frontend da aplicação",
    },
    arquivo_comentarios={
        "config.py": "Arquivo de configuração do sistema",
        "custom.py": "Código personalizado",
    }
)

# Gera a documentação
generator = TreeGenerator(config)
generator.gerar_documentacao(
    nome_projeto="Projeto Avançado",
    arquivo_saida="docs/estrutura_avancada.md",
    root_dir="."
)

print("✅ Documentação avançada gerada com sucesso!")