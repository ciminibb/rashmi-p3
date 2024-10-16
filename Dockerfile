# Base the Docker image off of a lightweight version of Python 3.9. Remember,
# any Docker image is several other images layered on top of one another. This
# line brings in our base image.
FROM python:3.9-slim

# This environment variable is set to ensure that Python output is sent directly
# to the console, without being buffered. This is desirable behavior in our
# solution, where printing output to the console should precede writing it to a
# file.
ENV PYTHONUNBUFFERED=1

# Here, we instruct Docker to run the <mkdir> command in Linux, which creates a
# directory. The structure referenced, </home/data/output>, is specified in the
# assignment description.
RUN mkdir -p /home/data/output

# Set the working directory inside the container to the folder where our Python
# script will live.
WORKDIR /app

# Copy all necessary files to the container, at their desired locations. Again,
# the Python script should live in </app> and the TXT files should live in
# </home/data>. The COPY key word places given files at the given location.
COPY scripts.py /app/
COPY IF.txt /home/data/
COPY AlwaysRememberUsThisWay.txt /home/data/

# CMD specifies what should happen when the container starts. In this case, we
# want it to run the Python script.
CMD ["python", "/app/scripts.py"]
