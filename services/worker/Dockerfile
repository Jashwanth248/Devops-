FROM python:3.12-slim
RUN useradd --create-home --uid 10001 appuser
WORKDIR /app
COPY worker.py .
USER 10001
CMD ["python","worker.py"]
