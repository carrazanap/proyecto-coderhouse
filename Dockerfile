FROM python:3.7
WORKDIR /code
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD ./code /code/
ADD ./data ./data/
ADD notebook.ipynb .
#CMD ["python","dashboard.py"]
#CMD ["jupyter", "lab","--ip=0.0.0.0","--allow-root","--no-browser"]