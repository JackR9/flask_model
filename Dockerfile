FROM python:3.7.2-slim

RUN mkdir /code

COPY requirements.txt /code/

RUN pip install -r /code/requirements.txt

COPY model.pickle /code/

COPY /templates/index.html /code/templates/

COPY style.css /code/

COPY fifaapiwithhtml.py /code/

EXPOSE 5000

CMD ["python","/code/fifaapiwithhtml.py"]
