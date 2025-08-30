# Usa uma imagem oficial do Python, mais segura e menor
FROM python:3.12-slim

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho no container
WORKDIR /app

# Instala dependências (primeiro para cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Coleta arquivos estáticos
RUN python manage.py collectstatic --noinput

# Remove a criação de superusuário no Dockerfile para maior segurança.
# Crie o superusuário de forma interativa ou via script.
# Exemplo de comando para criar superusuário manualmente:
# docker-compose run --rm seu_servico python manage.py createsuperuser

# Porta que o app vai escutar
EXPOSE 8000

# Comando para rodar o Gunicorn
CMD ["gunicorn", "sao_pedro.wsgi:application", "--bind", "0.0.0.0:8000"]