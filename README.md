# Smarttraffic-Webpage
This repo runs the Webpage of the Smarttraffic project.

## INSTALL

Python: 3.7 or +
The project is pyenv-friendly. You may want to [install pyenv](https://github.com/pyenv/pyenv) or, even better, install [anyenv](https://github.com/riywo/anyenv).

Check that you have the correct python version:
```
$ cat .python-version
3.7.0
$ python -V
Python 3.7.0
```

To manage requirements, we use [pipenv](https://pipenv.readthedocs.io/en/latest/). Install it:
```
$ pip install pipenv
```

Now install the necessary dev requirements:
```
$ pipenv install --dev
Installing dependencies from Pipfile.lock (4f9dd2)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ ...
...
```

Get into the virtual environment pipenv created for you:
```
$ pipenv shell
```
You're ready to start hacking.

## Develop

To start the dev server:
```
$ python manage.py runserver
```
You'll find the app is running on http://127.0.0.1:8000

Translating strings:
Use `trans` on your templates.

Then do the translation on the .po files throughout your project.
```
$ python manage.py makemessages --locale=es --locale=it
```

Added all the needed strings? Now you need to compile these .po files:
```
$ python manage.py compilemessages
```

Committing your work:
It's easier if you use [git flow](https://github.com/nvie/gitflow):

Tag your release using current YYYYMMDD. For example:
```
$ git flow release start 20180918
$ git flow release finish 20180918
$ git push --all
$ git push --tags
```

## Deployment
Build the container:
```
$ docker/build.sh latest
```
We use `latest` because that tag is used in `docker/compose/smwebsite/docker-compose.yml`.

Build the static files and populate the volume with them:
```
$ docker-compose -f docker/compose/smwebsite/docker-compose.yml run smwebsite /build-staticfiles.sh
```

Restart the service:
```
$ docker-compose -f docker/compose/smwebsite/docker-compose.yml down
$ docker-compose -f docker/compose/smwebsite/docker-compose.yml up -d
```
