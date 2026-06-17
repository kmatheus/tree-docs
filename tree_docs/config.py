"""
Configuração personalizada para o TreeDocs
"""

from typing import Dict, Set, Optional
from dataclasses import dataclass, field

@dataclass
class Config:
    """Configuração do TreeDocs"""
    
    # Pastas a ignorar
    ignore_dirs: Set[str] = field(default_factory=set)
    
    # Emojis personalizados
    emojis: Dict[str, str] = field(default_factory=dict)
    
    # Comentários personalizados para pastas
    pasta_comentarios: Dict[str, str] = field(default_factory=dict)
    
    # Comentários personalizados para arquivos
    arquivo_comentarios: Dict[str, str] = field(default_factory=dict)
    
    # Profundidade máxima
    max_depth: int = 5
    
    # Projeto
    project_name: str = "projeto"
    
    # Arquivo de saída
    output_file: str = "docs/estrutura_projeto.md"
    
    def merge_with_defaults(self, defaults):
        """Mescla configurações com os padrões"""
        
        # Mescla ignore_dirs
        if not self.ignore_dirs:
            self.ignore_dirs = defaults.IGNORE_DIRS.copy()
        else:
            self.ignore_dirs = defaults.IGNORE_DIRS | self.ignore_dirs
        
        # Mescla emojis
        if not self.emojis:
            self.emojis = defaults.EMOJIS.copy()
        else:
            self.emojis = {**defaults.EMOJIS, **self.emojis}
        
        # Mescla pasta_comentarios
        if not self.pasta_comentarios:
            self.pasta_comentarios = defaults.PASTA_COMENTARIOS.copy()
        else:
            self.pasta_comentarios = {**defaults.PASTA_COMENTARIOS, **self.pasta_comentarios}
        
        # Mescla arquivo_comentarios
        if not self.arquivo_comentarios:
            self.arquivo_comentarios = defaults.ARQUIVO_COMENTARIOS.copy()
        else:
            self.arquivo_comentarios = {**defaults.ARQUIVO_COMENTARIOS, **self.arquivo_comentarios}