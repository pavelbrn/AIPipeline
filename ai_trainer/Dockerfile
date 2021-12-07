FROM tensorflow/tensorflow:latest-gpu
WORKDIR /app
COPY . .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# this is the command that runs the app
CMD ["python", "cnn_patho.py"]

#docker run -v /Users/<path>:/app