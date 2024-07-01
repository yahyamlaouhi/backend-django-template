# Django Project - Backend

## Requirements

* [Docker](https://www.docker.com/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

## Local Development

* Start the stack with Docker Compose:

```bash
docker-compose down && docker-compose up -d
```

* Now you can open your browser and interact with these URLs:


Backend endpoint: http://api.dev.localhost/

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://api.dev.localhost/api/doc/

Adminer, database web administration: http://localhost:8080

Traefik UI, to see how the routes are being handled by the proxy: http://localhost:8090

**Note**: The first time you start your stack, it might take a minute for it to be ready. While the backend waits for the database to be ready and configures everything. You can check the logs to monitor it.

To run the Tests:

```bash
docker compose run --rm app sh -c "python manage.py test"
```

To check the logs, run:

```bash
docker compose logs
```

To check the logs of a specific service, add the name of the service, e.g.:

```bash
docker compose logs backend
```

If your Docker is not running in `localhost` (the URLs above wouldn't work) you would need to use the IP or domain where your Docker is running.

## Backend local development, additional details

### General workflow

By default, the dependencies are managed with [Poetry](https://python-poetry.org/), go there and install it.

From `./app/` you can install all the dependencies with:

```console
$ poetry install
```

Then you can start a shell session with the new environment with:

```console
$ poetry shell
```

Make sure your editor is using the correct Python virtual environment.


### Enabling Open User Registration

By default the backend has user registration disabled, but there's already a route to register users. If you want to allow users to register themselves, you can set the environment variable `USERS_OPEN_REGISTRATION` to `True` in the `.env` file.

After modifying the environment variables, restart the Docker containers to apply the changes. You can do this by running:

```console
$ docker compose up -d
```


### Docker Compose Override

During development, you can change Docker Compose settings that will only affect the local development environment in the file `docker-compose.override.yml`.


```console
$ docker compose up -d
```

To get inside the container with a `bash` session you can start the stack with:

```console
$ docker compose up -d
```

and then `exec` inside the running container:

```console
$ docker compose exec backend bash
```

You should see an output like:

```console
root@7f26072f31c4:/app#
```

that means that you are in a `bash` session inside your container, as a `root` user, under the `/app` directory, this directory has another directory called "app" inside, that's where your code lives inside the container: `/app/app`.

```
### Backend tests

To test the backend run:

```bash

docker compose run --rm app sh -c "python manage.py test"

```

The tests run with unnittest, modify and add tests for every app  

If you use GitHub Actions with the project the tests will run automatically.


#### Test Coverage

When the tests are run, a file `htmlcov/index.html` is generated, you can open it in your browser to see the coverage of the tests.

### Migrations

As during local development your app directory You will you need to create migrations files after adding models .


```console
$ docker compose run --rm app sh -c "python manage.py makemigrations"

$ docker compose run --rm app sh -c "python manage.py migrate"

```
