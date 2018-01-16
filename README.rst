Django Admin Comments
=============================

|image1| |image2| |image3| |image4|

A reusable Django application that adds simple admin-panel comments
to any model, allowing Django Administrators to communicate
on certain objects more easily.

|image5|

Quickstart
----------

-  Install Django Admin Comments:

   ::

       $ pip install django-admin-comments

-  Add it to your ``INSTALLED_APPS``:

   .. code:: python

       INSTALLED_APPS = (
           ...
           'admin_comments',
           ...
       )

- Run database migrations

   .. code:: bash

       $ manage.py migrate

- Now, simply add the ``CommentInline`` to any ``ModelAdmin``

   .. code:: python

       from admin_comments.admin import CommentInline

       class MyModelAdmin(admin.ModelAdmin):
           model = MyModel
           inlines = [CommentInline,]

Settings
--------

-  ``ADMIN_COMMENTS_SHOW_EMPTY``: Should the comment forms display an empty
   form field by default? (Default: ``False``)

   Example:

   .. code:: python

       ADMIN_COMMENTS_SHOW_EMPTY = True

-  ``ADMIN_COMMENTS_FORM_CLASS``: Override the default class used for the comment
   form. (Default: ``"admin_comments.forms.CommentInlineForm"``)

   Example:

   .. code:: python

       ADMIN_COMMENTS_FORM_CLASS = "myapp.forms.MyCustomCommentForm"

-  ``ADMIN_COMMENTS_FORMSET_CLASS``: Override the default class used for the comment
   formset. (Default: ``"admin_comments.forms.CommentInlineFormset"``)

   Example:

   .. code:: python

       ADMIN_COMMENTS_FORMSET_CLASS = "myapp.forms.MyCustomCommentFormSet"

Features
--------

-  Generic comment model to add comments to any object
-  Simple configuration without the overhead of the Django Comments Framework
-  Overridable Form and Formset classes

Support
-------

**Python**

-  2.7
-  3.4
-  3.5
-  3.6

**Django**

-  1.8
-  1.9
-  1.10
-  1.11
-  2.0

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_dev.txt
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ tox

Credits
-------

Original inspiration from Dryice Liu's answer on the following post:

https://stackoverflow.com/a/30338979/3768332

Tools used in rendering this package:

-  `Cookiecutter`_
-  `cookiecutter-djangopackage`_

.. _django-mailer: https://github.com/pinax/django-mailer
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-djangopackage: https://github.com/pydanny/cookiecutter-djangopackage

.. |image1| image:: https://img.shields.io/pypi/v/django-admin-comments.svg
   :target: https://pypi.python.org/pypi/django-admin-comments
.. |image2| image:: https://img.shields.io/travis/jamiecounsell/django-admin-comments.svg
   :target: https://travis-ci.org/jamiecounsell/django-admin-comments
.. |image3| image:: https://img.shields.io/codecov/c/github/jamiecounsell/django-admin-comments.svg
   :target: https://codecov.io/gh/jamiecounsell/django-admin-comments
.. |image4| image:: https://img.shields.io/badge/Fork%20on%20Github--brightgreen.svg?colorB=4dbf30
   :target: https://github.com/jamiecounsell/django-admin-comments/
.. |image5| image:: https://user-images.githubusercontent.com/2321599/34967909-e8eb0032-fa33-11e7-81c2-460c7104a82a.png
