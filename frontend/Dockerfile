FROM python:3.10.1-slim

ENV WORK_DIR=/app
WORKDIR $WORK_DIR

RUN pip install --upgrade --no-cache-dir pip && \
    pip install --no-cache-dir streamlit

COPY ./app .

EXPOSE 8501

CMD ["bash", "./run-app.sh"]
