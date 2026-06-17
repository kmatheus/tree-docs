#!/bin/bash
# Script para build e publicação do tree-docs no PyPI

set -e  # Para o script se algum comando falhar

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo "========================================"
echo "📦 tree-docs - Script de Publicação"
echo "========================================"
echo ""

# Verifica se está no diretório correto
if [ ! -f "pyproject.toml" ]; then
    echo -e "${RED}❌ Erro: pyproject.toml não encontrado!${NC}"
    exit 1
fi

# Carrega o token do .env
if [ -f ".env" ]; then
    source .env
    echo -e "${GREEN}✅ Token carregado do .env${NC}"
else
    echo -e "${YELLOW}⚠️  Arquivo .env não encontrado${NC}"
    echo -e "${YELLOW}💡 Crie o .env com: PYPI_TOKEN=seu-token-aqui${NC}"
    exit 1
fi

# Verifica se o token existe
if [ -z "$PYPI_TOKEN" ]; then
    echo -e "${RED}❌ Erro: PYPI_TOKEN não definido no .env${NC}"
    exit 1
fi

# Mostra versão atual
CURRENT_VERSION=$(grep 'version = "' pyproject.toml | head -1 | cut -d'"' -f2)
echo -e "${GREEN}📌 Versão atual: $CURRENT_VERSION${NC}"

# Pergunta nova versão
read -p "🆕 Nova versão (Enter para manter $CURRENT_VERSION): " NEW_VERSION

if [ -n "$NEW_VERSION" ]; then
    # Atualiza pyproject.toml
    sed -i "s/version = \"$CURRENT_VERSION\"/version = \"$NEW_VERSION\"/" pyproject.toml
    echo -e "${GREEN}✅ pyproject.toml atualizado: $NEW_VERSION${NC}"
    
    # Atualiza __init__.py
    sed -i "s/__version__ = \"$CURRENT_VERSION\"/__version__ = \"$NEW_VERSION\"/" tree_docs/__init__.py
    echo -e "${GREEN}✅ __init__.py atualizado: $NEW_VERSION${NC}"
    
    # Commit das mudanças
    git add pyproject.toml tree_docs/__init__.py 2>/dev/null || true
    git commit -m "bump version to $NEW_VERSION" 2>/dev/null || echo -e "${YELLOW}ℹ️ Nenhuma mudança para commit${NC}"
    
    VERSION=$NEW_VERSION
else
    VERSION=$CURRENT_VERSION
    echo -e "${YELLOW}ℹ️ Mantendo versão $CURRENT_VERSION${NC}"
fi

echo ""
echo "📦 Buildando o pacote..."
echo ""

# Limpa builds antigos
rm -rf dist/ build/ *.egg-info/ 2>/dev/null || true

# Build
python -m build

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Build concluído com sucesso!${NC}"
else
    echo -e "${RED}❌ Erro no build${NC}"
    exit 1
fi

echo ""
echo "📤 Publicando no PyPI..."
echo ""

# Publica usando o token
twine upload dist/* --username __token__ --password "$PYPI_TOKEN"

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ Versão $VERSION publicada com sucesso!${NC}"
    echo ""
    echo "📦 Para instalar:"
    echo "   pip install --upgrade tree-docs"
    echo ""
    echo "🔗 Ver no PyPI:"
    echo "   https://pypi.org/project/tree-docs/$VERSION/"
else
    echo -e "${RED}❌ Erro ao publicar${NC}"
    exit 1
fi