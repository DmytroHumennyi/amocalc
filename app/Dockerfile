FROM python:3.8
WORKDIR src/
COPY requirements.txt .
RUN apt-get update && apt --yes install python3
RUN pip install -r requirements.txt
COPY src/ .
CMD ["python", "./converterMOA2mm.py"]
