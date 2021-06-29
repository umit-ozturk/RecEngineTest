Dice
====

Dice Recommendation Exercise

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html


Installation
--------------

Firstly to install the project you should extract the environment file under dice folder.

After that;

    $ docker-compose -f local.yml up -d

When everything finished you can reach to site under http://127.0.0.1:8000

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser


Also you should import the users and artists to system from csv otherwise system will not working properly.

    $ docker-compose -f local.yml run django python manage.py load_user --path rec_engine/data/users.csv

    $ docker-compose -f local.yml run django python manage.py load_artist --path rec_engine/data/artists.csv


And to see logs

    $ docker-compose -f local.yml logs --follow


Folder Structure
--------------

compose / keeps docker files
config / django configs.
dice / backend folder contains apps, templates and staticfiles
docs / project docs.
locale / translations files
rec_engine / recommendation engine folder
requirements / project requirements


API Endpoints
--------------


{{domain}}/api/users/ --> CRUD operations.
  {{domain}}/api/users/me --> current user details.

{{domain}}/api/artists/ --> CRUD operations.
  {{domain}}/artists/list-all-interested-users/?artist_id=999 --> List of users which interest with related artist.


{{domain}}/api/recommendations/ --> CRUD operations.
  {{domain}}/recommendations/recommend-close-artist/ --> Give a recommendation for user with related method
  {{domain}}/recommendations/recommend-per-cluster/ --> Give a recommendation for user with related method


Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy dice

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html

Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd dice
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog

Deployment
----------

The following details how to deploy this application.

Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html


ScreenShots
----------

.. image:: /docs/screenshots/1.png
  :width: 400

.. image:: /docs/screenshots/2.png
  :width: 400

.. image:: /docs/screenshots/3.png
  :width: 400

.. image:: /docs/screenshots/4.png
  :width: 400

.. image:: /docs/screenshots/5.png
  :width: 400

.. image:: /docs/screenshots/6.png
  :width: 400

.. image:: /docs/screenshots/7.png
  :width: 400

.. image:: /docs/screenshots/8.png
  :width: 400

.. image:: /docs/screenshots/9.png
  :width: 400

.. image:: /docs/screenshots/10.png
  :width: 400

.. image:: /docs/screenshots/11.png
  :width: 400

.. image:: /docs/screenshots/12.png
  :width: 400

.. image:: /docs/screenshots/13.png
  :width: 400

.. image:: /docs/screenshots/14.png
  :width: 400

.. image:: /docs/screenshots/15.png
  :width: 400

.. image:: /docs/screenshots/16.png
  :width: 400

.. image:: /docs/screenshots/17.png
  :width: 400

.. image:: /docs/screenshots/18.png
  :width: 400

.. image:: /docs/screenshots/19.png
  :width: 400
