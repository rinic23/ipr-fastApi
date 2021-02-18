FROM python:3.8
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install -r requirements.txt
# EXPOSE 27689
ADD . /app
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "27689"]