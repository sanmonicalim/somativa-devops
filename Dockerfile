# Usa uma imagem oficial do Python como base
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requisitos para o container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o container
COPY . .

# Comando para rodar a aplicação
CMD ["python", "app.py"]