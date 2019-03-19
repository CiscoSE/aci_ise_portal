# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3-onbuild

ADD . .

RUN pip install -r requirements.txt

# EXPOSE port 8080 to allow communication to/from server
EXPOSE 8080

# CMD specifcies the command to execute to start the server running.
CMD ["./web_start.sh"]
# done!
