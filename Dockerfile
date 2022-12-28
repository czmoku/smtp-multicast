FROM python:3.9
EXPOSE 1025
RUN python -m pip install aiosmtpd
COPY main.py .
CMD ["python", "-u", "./main.py"] 