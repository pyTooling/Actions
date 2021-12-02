FROM python:3.9-slim-bullseye
COPY tip.py /tip.py
RUN pip install PyGithub --progress-bar off
ENTRYPOINT ["/tip.py"]
