FROM python:3.8
WORKDIR /com.docker.devenvironments.code
WORKDIR /com.docker.devenvironments.code/app
WORKDIR /com.docker.devenvironments.code/app/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
CMD ["python", "./converterMOA2mm.py"]
