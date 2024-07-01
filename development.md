# Django Project - Development

## Development in `localhost` with a custom domain

THe domain that you will develop on it is `api.dev.localhost` you willl find it in `.env` if you want to change it anytime 

If you changed the domain don't forguet to change the CORS enabled domains while generating the project so the nbackend will put it in the list of allowed hosts in the settings of django project by changing `BACKEND_CORS_ORIGINS`. 


After performing those steps you should be able to open: http://api.dev.localhost and it will be served by your stack in `localhost`.

Check all the corresponding available URLs in the section at the end.

## The .env file

The `.env` file is the one that contains all your configurations, generated keys and passwords, etc.

Depending on your workflow, you could want to exclude it from Git, for example if your project is public. In that case, you would have to make sure to set up a way for your CI tools to obtain it while building or deploying your project.

One way to do it could be to add each environment variable to your CI/CD system, and updating the `docker-compose.yml` file to read that specific env var instead of reading the `.env` file.

### Pre-commits and code linting


we are using a tool called [pre-commit](https://pre-commit.com/) for code linting and formatting.

When you install it, it runs right before making a commit in git. This way it ensures that the code is consistent and formatted even before it is committed.

You can find a file `.pre-commit-config.yaml` with configurations at the root of the project.

commit message have to be orgonized like this "feat : Create new feature 1" by using a commit tag with a clear message :

    feat: A new feature or functionality is added.
    fix: A bug fix or correction is made.
    docs: Documentation updates or additions.
    style: Changes that do not affect the meaning of the code (e.g., formatting, missing semicolons).
    refactor: Code refactoring without changing its external behavior.
    test: Adding or modifying tests.
    chore: Maintenance tasks, build process, etc., without user-facing changes.
    perf: Performance improvements.
    ci: Changes to CI/CD configuration files and scripts.
    build: Changes that affect the build system or external dependencies.
    init: Initialize project "MyProject"

#### Install pre-commit to run automatically

`pre-commit` is already part of the dependencies of the project, but you could also install it globally if you prefer to, following [the official pre-commit docs](https://pre-commit.com/).

After having the `pre-commit` tool installed and available, you need to "install" it in the local repository, so that it runs automatically before each commit.

Using Poetry, you could do it with:

```bash
❯ poetry run pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

Now whenever you try to commit, e.g. with:

```bash
git commit
```

...pre-commit will run and check and format the code you are about to commit, and will ask you to add that code (stage it) with git again before committing.

Then you can `git add` the modified/fixed files again and now you can commit.

#### Running pre-commit hooks manually

you can also run `pre-commit` manually on all the files, you can do it using Poetry with:

```bash
❯ poetry run pre-commit run --all-files
check for added large files..............................................Passed
check toml...............................................................Passed
check yaml...............................................................Passed
ruff.....................................................................Passed
ruff-format..............................................................Passed
eslint...................................................................Passed
prettier.................................................................Passed
```

## URLs

The production or staging URLs would use these same paths, but with your own domain.

### Development URLs

Development URLs, for local development.


Backend: http://api.dev.localhost

Automatic Interactive Docs (Swagger UI):  http://api.dev.localhost/api/doc/

Automatic Alternative Docs (ReDoc): http://api.dev.localhost/api/redoc/

Adminer: http://api.dev.localhost:8080

Traefik UI: http://api.dev.localhost:8090

