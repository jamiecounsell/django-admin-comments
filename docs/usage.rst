=====
Usage
=====

-  Install Django Admin Comments:

   ::

       $ pip install django-admin-comments

-  Add it to your \`INSTALLED_APPS`:

   .. code:: python

       INSTALLED_APPS = (
           ...
           'admin_comments',
           ...
       )

- Run database migrations

   .. code:: bash

       $ manage.py migrate

- Now, simply add the \`CommentInline` to any \`ModelAdmin`

   .. code:: python

       from admin_comments.admin import CommentInline

       class MyModelAdmin(admin.ModelAdmin):
           model = MyModel
           inlines = [CommentInline,]
