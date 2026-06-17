"""
Testes para o TreeDocs
"""

import os
import tempfile
import unittest
from pathlib import Path

from tree_docs import TreeGenerator, Config


class TestTreeGenerator(unittest.TestCase):
    """Testes para o TreeGenerator"""
    
    def setUp(self):
        """Configura ambiente de teste"""
        self.temp_dir = tempfile.mkdtemp()
        self.old_cwd = os.getcwd()
        os.chdir(self.temp_dir)
        
        # Cria estrutura de teste
        os.makedirs("src/sub")
        os.makedirs("tests")
        os.makedirs("docs")
        
        with open("src/__init__.py", "w") as f:
            f.write("# Test")
        with open("src/main.py", "w") as f:
            f.write("# Main")
        with open("README.md", "w") as f:
            f.write("# README")
    
    def tearDown(self):
        """Limpa ambiente de teste"""
        os.chdir(self.old_cwd)
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_generator_basic(self):
        """Testa geração básica"""
        generator = TreeGenerator()
        generator.gerar_documentacao(
            nome_projeto="teste",
            arquivo_saida="docs/teste.md",
            root_dir="."
        )
        
        self.assertTrue(os.path.exists("docs/teste.md"))
        
        with open("docs/teste.md", "r") as f:
            content = f.read()
            self.assertIn("teste/", content)
            self.assertIn("src", content)
            self.assertIn("README.md", content)
    
    def test_custom_config(self):
        """Testa configuração personalizada"""
        config = Config(
            max_depth=2,
            ignore_dirs={"tests"}
        )
        generator = TreeGenerator(config)
        generator.gerar_documentacao(
            nome_projeto="teste",
            arquivo_saida="docs/teste.md",
            root_dir="."
        )
        
        with open("docs/teste.md", "r") as f:
            content = f.read()
            self.assertNotIn("tests", content)


if __name__ == "__main__":
    unittest.main()