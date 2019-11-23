version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
  db:
    #   Use the Docker Image postgres. This will pull the newest release.
    image: "postgres"
    #   Give the container the name my_postgres. You can changes to something else.
    container_name: "my_postgres"
    #   Setup the username, password, and database name. You can changes these values.
    environment:
      - POSTGRES_USER=john
      - POSTGRES_PASSWORD=pwd0123456789
      - POSTGRES_DB=mydb
    #   Maps port 54320 (localhost) to port 5432 on the container. You can change the ports to fix your needs.
    ports:
      - "54320:5432"
    #   Set a volume some that database is not lost after shutting down the container.
    #   I used the name postgres-data but you can changed it to something else.
    volumes:
      - ./postgres-data:/var/lib/postgresql/data
