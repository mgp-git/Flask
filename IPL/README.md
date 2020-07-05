To run as a containerized application
*************************************
1. Pre-requisite:
   A. Create docker volume, Ex cmd: docker volume create sql-data
 
2. docker image build example cmd: docker image build -t <dockerhub_username>/<repo_name>:<version> <build_context>   

3. Running the application:
   A. use docker run command, and mount the volume created in step 1. This is requried for persisting the DB across restarts.
      Ex run command: docker container run -idt -p 5000:5000 --rm -v sql-data:/usr/src/database <dockerhub_username>/<repo_name>:<version>

To run as standalone application
********************************
1. Configurations required:
   A. Set or export 'SQLALCHEMY_DATABASE_URI' environment variable to set a PATH for DB to be created.

2. To run the application:
   python start_app.py

This will create a webserver on the localhost with default port of 5000. 
So, to access the server go to http://localhost:5000

