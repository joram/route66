FROM yobasystems/alpine-docker

RUN apk add --no-cache python3-dev py3-pip\
    && pip install --upgrade pip

WORKDIR /app
COPY ./route66/requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY ./route66/ /app
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
