FROM python:3.9-slim-bullseye
COPY releaser.py /releaser.py
RUN pip install PyGithub --progress-bar off
CMD ["/releaser.py"]
