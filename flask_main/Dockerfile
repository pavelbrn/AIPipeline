FROM tensorflow/tensorflow
# specify the current wd
WORKDIR /app

# migrate all local files in the computer to the remote container
#ENV APP /app
#COPY . ./

# Use pip to install the project requirements
RUN pip install -r requirements.txt 
EXPOSE 8501
COPY . /app
ENTRYPOINT ["streamlit", "run"]
# Run the web server upon startup with eight threads, the entry point is application.py
#CMD exec gunicorn --bind :8081 --workers 1 --threads 8 --timeout 0 application:app
CMD ["st_lit.py"]
#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 application:app