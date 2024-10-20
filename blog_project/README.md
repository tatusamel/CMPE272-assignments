# Django Blog Application

## Running the Application

### Prerequisites

- Docker and Docker Compose must be installed.

### Build and Run the Container

1. Clone the repository:

   ```
   git clone <repository_url>
   cd blog_project
   ```

2. Build and start the container using Docker Compose:

   ```
   docker-compose up --build
   ```

3. Access the application at `http://localhost:8000`.

### Database Migration

To run the database migrations:

```
docker-compose run web python manage.py migrate
```

### Accessing the Admin Panel

1. Create a superuser:

   ```
   docker-compose run web python manage.py createsuperuser
   ```

2. Access the admin panel at `http://localhost:8000/admin`.

```

```
