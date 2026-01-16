# elt-pipeline-assignment-hgi
Instruction to run the task:

**1. Clone the repo:**
git clone https://github.com/naabs-eng/elt-pipeline-assignment-hgi.git
cd elt-pipeline-assignment-hgi

**2. Build and start the pipeline provided you have docker running:**
docker-compose up --build
This command will build all Docker images and start the PostgreSQL database, Metabase, and the ELT pipeline container.
The ELT pipeline will run automatically on the schedule we have set (default: every hour).

**3. Steps to connect to DB to check data from terminal:**
docker ps
docker exec -it <container_name> bash ##name of DB container to be provided
psql -U user -d telecom

SELECT * FROM staging_churn LIMIT 5;
SELECT * FROM reporting_churn LIMIT 5;

**4. Access metabase for Reporting:**
Go to http://localhost:3000.
Connect Metabase to the PostgreSQL database:
Host: db
Port: 5432
Database: telecom
Username: user
Password: password



