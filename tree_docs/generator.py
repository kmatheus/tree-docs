"""
Núcleo do gerador de árvore de diretórios
"""

import os
import datetime
from typing import Optional, Set, Dict, List, Tuple
from pathlib import Path

from .defaults import DEFAULTS
from .config import Config


class TreeGenerator:
    """
    Gerador de árvore de diretórios com emojis e comentários
    
    Exemplo:
        >>> generator = TreeGenerator()
        >>> generator.gerar_documentacao(
        ...     nome_projeto="meu-projeto",
        ...     arquivo_saida="docs/estrutura.md"
        ... )
    """
    
    def __init__(self, config: Optional[Config] = None):
        """
        Inicializa o gerador
        
        Args:
            config: Configuração personalizada (opcional)
        """
        self.config = config or Config()
        self.config.merge_with_defaults(DEFAULTS)
        
        self.root_dir = "."
        self.max_depth = self.config.max_depth
        
        # Atalhos para as configurações
        self.ignore_dirs = self.config.ignore_dirs
        self.emojis = self.config.emojis
        self.pasta_comentarios = self.config.pasta_comentarios
        self.arquivo_comentarios = self.config.arquivo_comentarios
    
    def gerar_comentario(self, diretorio_pai: str, item: str, is_dir: bool) -> Optional[str]:
        """
        Gera comentário explicativo para um item
        
        Args:
            diretorio_pai: Diretório pai do item
            item: Nome do item
            is_dir: True se for diretório
            
        Returns:
            Comentário ou None se não houver
        """
        if is_dir:
            # Verifica se o item está nos comentários de pasta
            if item in self.pasta_comentarios:
                return self.pasta_comentarios[item]
            
            # Comentário genérico para pastas de API
            if 'api' in diretorio_pai or diretorio_pai.endswith('/api'):
                nome_limpo = item.replace('_', ' ').title()
                return f"API de {nome_limpo}"
            
            return None
        
        # Arquivo
        if item in self.arquivo_comentarios:
            return self.arquivo_comentarios[item]
        
        # Padrões para arquivos Python
        if item.endswith('.py'):
            nome = item[:-3]
            if 'test' in nome.lower():
                return "Testes unitários"
            if 'serializer' in nome.lower():
                return "Serializers para API"
            if 'view' in nome.lower():
                return "Views da API"
            if 'model' in nome.lower():
                return "Modelos de dados"
            if 'admin' in nome.lower():
                return "Configuração do Admin"
            if 'urls' in nome.lower():
                return "Rotas da aplicação"
            if 'utils' in nome.lower():
                return "Funções utilitárias"
        
        return None
    
    def gerar_arvore(
        self,
        diretorio: str = ".",
        prefixo: str = "",
        nivel: int = 0
    ) -> str:
        """
        Gera a árvore de diretórios recursivamente
        
        Args:
            diretorio: Diretório atual
            prefixo: Prefixo para formatação da árvore
            nivel: Nível atual de profundidade
            
        Returns:
            String com a árvore formatada
        """
        if nivel > self.max_depth:
            return ""
        
        resultado: List[str] = []
        
        try:
            itens = [i for i in os.listdir(diretorio) if not i.startswith('.')]
        except PermissionError:
            return ""
        
        # Filtra itens ignorados
        itens = [i for i in itens if i not in self.ignore_dirs]
        
        # Se não há itens, retorna indicador de pasta vazia
        if not itens:
            if diretorio != ".":
                return f"{prefixo}    └── ..."
            return ""
        
        # Separa pastas e arquivos
        pastas: List[str] = []
        arquivos: List[str] = []
        
        for item in itens:
            caminho = os.path.join(diretorio, item)
            if os.path.isdir(caminho):
                pastas.append(item)
            else:
                arquivos.append(item)
        
        # Ordena e junta (pastas primeiro)
        pastas.sort()
        arquivos.sort()
        itens_ordenados = pastas + arquivos
        
        # Coleta dados de cada item
        itens_com_dados: List[Tuple[str, bool, Optional[str], str]] = []
        for item in itens_ordenados:
            caminho = os.path.join(diretorio, item)
            is_dir = os.path.isdir(caminho)
            comentario = self.gerar_comentario(diretorio, item, is_dir)
            itens_com_dados.append((item, is_dir, comentario, caminho))
        
        # Calcula o tamanho máximo para alinhamento
        max_len = 0
        for item, is_dir, _, _ in itens_com_dados:
            linha = f"{prefixo}{'├── '}{'📁 ' if is_dir else '🐍 '}{item}"
            max_len = max(max_len, len(linha))
        
        # Gera a saída
        for i, (item, is_dir, comentario, caminho) in enumerate(itens_com_dados):
            is_ultimo = (i == len(itens_com_dados) - 1)
            
            # Define caracteres da árvore
            if is_ultimo:
                conector = "└── "
                prefixo_filho = prefixo + "    "
            else:
                conector = "├── "
                prefixo_filho = prefixo + "│   "
            
            # Emoji apropriado
            if is_dir:
                emoji = "📁 "
            else:
                ext = os.path.splitext(item)[1].lower()
                emoji = self.emojis.get(ext, '📄 ')
            
            # Monta a linha
            linha_base = f"{prefixo}{conector}{emoji}{item}"
            
            # Adiciona comentário alinhado à direita
            if comentario:
                espacos = max_len - len(linha_base) + 2
                if espacos < 2:
                    espacos = 2
                resultado.append(f"{linha_base}{' ' * espacos}# {comentario}")
            else:
                resultado.append(linha_base)
            
            # Processa subdiretórios
            if is_dir:
                sub = self.gerar_arvore(caminho, prefixo_filho, nivel + 1)
                if sub:
                    resultado.append(sub)
        
        return "\n".join(resultado)
    
    def gerar_documentacao(
        self,
        nome_projeto: str = "projeto",
        arquivo_saida: str = "docs/estrutura_projeto.md",
        root_dir: str = "."
    ) -> None:
        """
        Gera a documentação completa em Markdown
        
        Args:
            nome_projeto: Nome do projeto
            arquivo_saida: Caminho do arquivo de saída
            root_dir: Diretório raiz do projeto
        """
        self.root_dir = root_dir
        
        # Cria diretório de saída se não existir
        os.makedirs(os.path.dirname(arquivo_saida) or ".", exist_ok=True)
        
        # Gera a árvore
        arvore = self.gerar_arvore(root_dir)
        
        # Prepara o conteúdo
        conteudo: List[str] = []
        conteudo.append(f"# 🌳 Estrutura do Projeto - {nome_projeto}\n")
        conteudo.append(f"\n*Gerado em: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*\n")
        conteudo.append("\n```bash\n")
        conteudo.append(f"{nome_projeto}/\n")
        conteudo.append(arvore)
        conteudo.append("\n```\n")
        
        # Legenda
        conteudo.append("\n## 📖 Legenda\n\n")
        conteudo.append("| Emoji | Significado |\n")
        conteudo.append("|-------|-------------|\n")
        legendas = [
            ("📁", "Pasta/Diretório"),
            ("🐍", "Arquivo Python"),
            ("📝", "Documentação (MD)"),
            ("⚙️", "Configuração (YAML)"),
            ("</>", "Script Shell"),
            ("📊", "Dados (JSON)"),
            ("📄", "Arquivo texto"),
            ("🌿", "Variáveis de ambiente"),
            ("♦️", "Git"),
            ("🐳", "Docker"),
            ("📦", "Pacote Python"),
            ("🔒", "Arquivo de lock"),
        ]
        for emoji, desc in legendas:
            conteudo.append(f"| {emoji} | {desc} |\n")
        
        conteudo.append("\n> **Nota:** Pastas marcadas com `...` estão vazias ou contêm apenas arquivos ignorados.\n")
        
        # Escreve o arquivo
        with open(arquivo_saida, "w", encoding="utf-8") as f:
            f.write("".join(conteudo))
            f.flush()
            os.fsync(f.fileno())
        
        print(f"✅ Documentação gerada com sucesso: {arquivo_saida}")