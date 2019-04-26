FROM python:2.7
COPY hello.py /hello.py
CMD ["python", "/hello.py"]
