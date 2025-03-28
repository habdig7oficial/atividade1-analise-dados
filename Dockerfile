# sudo docker build -t ex_analise_dados .  && sudo docker run --volumne ./:/mnt ex_analise_dados 

FROM python:latest

WORKDIR /mnt

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["bash"]