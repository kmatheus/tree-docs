"""
Configurações padrão do TreeDocs
"""

from typing import Dict, Set

class DEFAULTS:
    """Configurações padrão para o gerador"""
    
    # Pastas a ignorar automaticamente
    IGNORE_DIRS: Set[str] = {
        "venv", "__pycache__", ".git", ".pytest_cache",
        "migrations", "node_modules", ".idea", ".vscode",
        "logs", "media", "static", "docs", "__pycache__",
        "dist", "build", "*.egg-info", ".tox", ".mypy_cache",
        ".coverage", "htmlcov", ".pytest_cache"
    }
    
    # Emojis por extensão de arquivo
    EMOJIS: Dict[str, str] = {
        '.py': '🐍 ',
        '.md': '📝 ',
        '.yml': '⚙️ ',
        '.yaml': '⚙️ ',
        '.sh': '</> ',
        '.json': '📊 ',
        '.txt': '📄 ',
        '.env': '🌿 ',
        '.envrc': '🌿 ',
        '.gitignore': '♦️ ',
        '.dockerfile': '🐳 ',
        '.Dockerfile': '🐳 ',
        '.toml': '📦 ',
        '.lock': '🔒',
        '.js': '📜 ',
        '.ts': '📘 ',
        '.jsx': '⚛️ ',
        '.tsx': '⚛️ ',
        '.css': '🎨 ',
        '.html': '🌐 ',
        '.xml': '📋 ',
        '.sql': '🗄️ ',
        '.go': '🐹 ',
        '.rs': '🦀 ',
        '.java': '☕ ',
        '.cpp': '⚡ ',
        '.c': '⚡ ',
        '.h': '🔧 ',
    }
    
    # Comentários padrão para pastas comuns
    PASTA_COMENTARIOS: Dict[str, str] = {
        "backend": "Configurações principais do Backend",
        "frontend": "Configurações principais do Frontend",
        "core": "Núcleo da aplicação - Funcionalidades compartilhadas",
        "api": "Endpoints da API REST",
        "services": "Lógica de negócio e serviços",
        "tests": "Testes unitários e de integração",
        "migrations": "Migrações do banco de dados",
        "models": "Modelos de dados",
        "serializers": "Serializers para API",
        "views": "Views e controladores",
        "utils": "Funções utilitárias",
        "templates": "Templates HTML",
        "static": "Arquivos estáticos (CSS, JS, imagens)",
        "media": "Arquivos de mídia (uploads)",
        "config": "Arquivos de configuração",
        "scripts": "Scripts auxiliares",
        "docker": "Configurações Docker",
        "kubernetes": "Manifestos Kubernetes",
        "helm": "Charts Helm",
        "terraform": "Configurações Terraform",
        "ansible": "Playbooks Ansible",
        "github": "Configurações GitHub",
        "gitlab": "Configurações GitLab",
        "vscode": "Configurações VS Code",
        "idea": "Configurações IntelliJ/PyCharm",
    }
    
    # Comentários padrão para arquivos comuns
    ARQUIVO_COMENTARIOS: Dict[str, str] = {
        # Python/Django
        "settings.py": "Configurações do projeto",
        "urls.py": "Rotas da aplicação",
        "wsgi.py": "Configuração WSGI para deploy",
        "asgi.py": "Configuração ASGI para deploy",
        "models.py": "Modelos do banco de dados",
        "serializers.py": "Serializers para API REST",
        "views.py": "Views/ViewSets da API",
        "admin.py": "Configuração do Django Admin",
        "apps.py": "Configuração do app Django",
        "manage.py": "Script de gerenciamento do Django",
        
        # Documentação
        "README.md": "Documentação principal do projeto",
        "LICENSE": "Licença do projeto",
        "CHANGELOG.md": "Histórico de versões",
        "CONTRIBUTING.md": "Guia de contribuição",
        "CODE_OF_CONDUCT.md": "Código de conduta",
        "SECURITY.md": "Política de segurança",
        
        # Configuração Python
        "pyproject.toml": "Configuração do projeto e dependências",
        "setup.py": "Script de instalação do pacote",
        "requirements.txt": "Dependências do projeto",
        "requirements-dev.txt": "Dependências de desenvolvimento",
        ".flake8": "Configuração do Flake8",
        ".isort.cfg": "Configuração do isort",
        ".black": "Configuração do Black",
        "mypy.ini": "Configuração do Mypy",
        "pytest.ini": "Configuração do Pytest",
        
        # Ambiente
        ".env": "Variáveis de ambiente",
        ".env.example": "Exemplo de variáveis de ambiente",
        ".envrc": "Configuração do direnv",
        ".gitignore": "Arquivos ignorados no Git",
        ".dockerignore": "Arquivos ignorados no Docker",
        
        # CI/CD
        ".gitlab-ci.yml": "Pipeline CI/CD do GitLab",
        ".github/workflows/": "Workflows GitHub Actions",
        ".travis.yml": "Configuração Travis CI",
        "Jenkinsfile": "Pipeline Jenkins",
        
        # Docker
        "Dockerfile": "Imagem Docker para desenvolvimento",
        "Dockerfile.prod": "Imagem Docker para produção",
        "docker-compose.yml": "Orquestração de containers Docker",
        
        # Kubernetes
        "deployment.yaml": "Deployment Kubernetes",
        "service.yaml": "Service Kubernetes",
        "ingress.yaml": "Ingress Kubernetes",
        "configmap.yaml": "ConfigMap Kubernetes",
        "secret.yaml": "Secret Kubernetes",
        "hpa.yaml": "Horizontal Pod Autoscaler",
        
        # Frontend
        "package.json": "Dependências Node.js",
        "package-lock.json": "Lock de dependências Node",
        "yarn.lock": "Lock de dependências Yarn",
        "webpack.config.js": "Configuração Webpack",
        "vite.config.js": "Configuração Vite",
        "tsconfig.json": "Configuração TypeScript",
        
        # Scripts
        "entrypoint.sh": "Script de entrada do container",
        "entrypoint.prod.sh": "Script de entrada (produção)",
        "start.sh": "Script de inicialização",
        "build.sh": "Script de build",
        "deploy.sh": "Script de deploy",
        
        # Outros
        "Makefile": "Comandos automatizados",
        "gunicorn_conf.py": "Configuração do Gunicorn",
        "celery.py": "Configuração do Celery",
        "tasks.py": "Tarefas assíncronas",
    }