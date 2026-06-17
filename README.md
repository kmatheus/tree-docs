# 🌳 TreeDocs

[![PyPI version](https://badge.fury.io/py/tree-docs.svg)](https://badge.fury.io/py/tree-docs)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/kmatheus/tree-docs.svg)](https://github.com/kmatheus/tree-docs/stargazers)

Gerador automático de árvore de diretórios com emojis e comentários para documentação em Markdown.

## ✨ Features

- 🚀 **Geração automática** da estrutura de diretórios
- 🎨 **Emojis** para identificar tipos de arquivos
- 📝 **Comentários** explicativos para pastas e arquivos
- 🎯 **Alinhamento** profissional dos comentários
- 🔧 **Altamente configurável**
- 💻 **CLI** e **API Python** disponíveis
- 📦 **Zero dependências** externas

## 📦 Instalação

### Via pip (recomendado)

```bash
pip install tree-docs
```

### Via pipx (para CLI)

```bash
pipx install tree-docs
```

### Desenvolvimento

```bash
git clone https://github.com/seu-usuario/tree-docs.git
cd tree-docs
pip install -e ".[dev]"
```

## 🚀 Uso Rápido

### CLI (Linha de comando)

```bash
# Uso básico
tree-docs -d . -o docs/estrutura.md -n "Meu Projeto"

# Com profundidade limitada
tree-docs -d . --max-depth 3 -o docs/estrutura.md

# Ignorando pastas específicas
tree-docs -d . --ignore "venv,__pycache__,.git" -o docs/estrutura.md

# Ajuda
tree-docs --help
```

### API Python

```python
from tree_docs import TreeGenerator

# Uso básico
generator = TreeGenerator()
generator.gerar_documentacao(
    nome_projeto="Meu Projeto",
    arquivo_saida="docs/estrutura.md"
)

# Com configuração personalizada
from tree_docs import Config

config = Config(
    max_depth=3,
    ignore_dirs={"venv", "__pycache__"}
)
generator = TreeGenerator(config)
generator.gerar_documentacao("Meu Projeto", "docs/estrutura.md")
```

## 📝 Exemplo de Saída

```bash
meu-projeto/
├── 📁 backend                                                                  # Configurações principais do Django
│   ├── 🐍 __init__.py
│   ├── 🐍 asgi.py                                                              # Configuração ASGI para deploy
│   ├── 🐍 settings.py                                                          # Configurações do projeto
│   ├── 🐍 urls.py                                                              # Rotas globais
│   └── 🐍 wsgi.py                                                              # Configuração WSGI
├── 📁 core                                                                     # App Core - Funcionalidades compartilhadas
│   ├── 🐍 __init__.py
│   ├── 🐍 admin.py                                                             # Configuração do Admin
│   ├── 🐍 apps.py                                                              # Configuração do app
│   ├── 🐍 models.py                                                            # Modelos de dados
│   └── 🐍 views.py                                                             # Views da API
└── 📄 README.md                                                                # Documentação principal
```

## ⚙️ Configuração Avançada

```python
from tree_docs import TreeGenerator, Config

# Configuração personalizada
config = Config(
    max_depth=5,
    ignore_dirs={"venv", "__pycache__", ".git"},
    project_name="meu-projeto",
    output_file="docs/estrutura.md",
    
    # Comentários personalizados
    pasta_comentarios={
        "custom": "Minha pasta personalizada"
    },
    arquivo_comentarios={
        "config.py": "Arquivo de configuração do sistema"
    }
)

generator = TreeGenerator(config)
generator.gerar_documentacao()
```

## 📚 Documentação
Documentação completa disponível em: https://tree-docs.readthedocs.io

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, leia o guia de contribuição.

1. Fork o projeto
2. Crie sua branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença
Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## 👤 Autor
Kelvin Matheus - Fullstack Developer

GitHub: [@kmatheus](https://github.com/kmatheus)

LinkedIn: [Kelvin Matheus](https://www.linkedin.com/in/kelvin-matheusdev/)

## ⭐ Agradecimentos

- Todos os contribuidores que ajudaram a melhorar esta ferramenta
- Comunidade Python por manter a linguagem incrível