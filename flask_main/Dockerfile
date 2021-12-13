FROM tensorflow/tensorflow
# specify the current wd
WORKDIR /app

# migrate all local files in the computer to the remote container
#ENV APP /app
COPY . ./

# Use pip to install the project requirements
RUN pip install -r requirements.txt 

# Run the web server upon startup with eight threads, the entry point is application.py
CMD exec gunicorn --bind :8081 --workers 1 --threads 8 --timeout 0 st_lit:app

#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 application:app