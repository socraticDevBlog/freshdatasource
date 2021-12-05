FROM python

WORKDIR /code

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY src/ .

CMD [ "python", "./api.py" ]

