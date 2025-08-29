# Makefile para projeto Django

# Nome do ambiente virtual
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Se estiver no Windows, alterar para:
# PYTHON = $(VENV)\Scripts\python.exe
# PIP = $(VENV)\Scripts\pip.exe

# Comando padrão
all: help

# Criar ambiente virtual
venv:
	python3 -m venv $(VENV)
	@echo "Ambiente virtual criado em $(VENV)"

# Ativar e instalar dependências
install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Dependências instaladas"

# Rodar migrações
migrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

# Criar superusuário
createsuperuser:
	$(PYTHON) manage.py createsuperuser

# Rodar o servidor de desenvolvimento
run:
	$(PYTHON) manage.py runserver

# Limpar arquivos .pyc e cache
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	@echo "Arquivos temporários removidos"

# Help
help:
	@echo "Makefile Django Commands:"
	@echo "  make venv              - Criar ambiente virtual"
	@echo "  make install           - Instalar dependências"
	@echo "  make migrate           - Rodar migrações"
	@echo "  make createsuperuser   - Criar superusuário"
	@echo "  make run               - Rodar servidor"
	@echo "  make clean             - Limpar cache e arquivos .pyc"
