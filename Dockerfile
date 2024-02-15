# Use uma imagem base do Ubuntu
FROM ubuntu:latest

# Atualize o índice de pacotes e instale o Python e o FFmpeg
RUN apt-get update && \
    apt-get install -y python3 python3-pip ffmpeg

COPY . /app

RUN pip3 install -r /app/requirements.txt

# Defina o diretório de trabalho padrão
WORKDIR /app

# Comando padrão para execução
# CMD ["/bin/bash"]
CMD ["python3", "main.py"]
