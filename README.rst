==================
django-stackhelper
==================

Generate configuration files for other parts of your Django stack.

As well as your django application, your stack might contain other components,
such as:

 * nginx
 * apache
 * memcached
 * redis
 * varnish

Any or all of these will need some configuration to work with your application.
Writing these configuration files by hand can be error prone and needs to be
coordinated around changes to your software.

This django application will help you manage these files. You might want to
pair this with django-json-settings, or something else that provides local
settings, so you can easily configure your stack ona per-environment basis.

Workflow
========

Packaging template configuration files
--------------------------------------

During application development, template files for other production stack
components are placed in the "stack" directory of your django project::

  mysite/
      myapp/
          ...
      stack_templates/
          apache/
              apache.conf
          varnish/
              varnish.vcf

Building configuration files for the current environment
--------------------------------------------------------

A management command is provided to generate configuration files based on the
current settings for the project in the current environment. 

If you are running inside a virtual environment then the files will be written to::

    <sys.prefix>/etc
    
Otherwise you will need to provide a destination directory as an argument.
    
Creating production configuration files
---------------------------------------

Since files are placed in <sys.prefix>/etc when run in a virtual environment,
you can symlink these directly into place if you wish:

For example, it produces the files::

    <sys.prefix>/etc/apache/apache.conf
    <sys.prefix>/etc/varnish/varnish.vcf

You can link them straight into your config::

    ln -s <sys.prefix>/etc/apache/apache.conf /etc/apache2/sites-available/mysite.conf



Alternatively, it may be that these files may not be suitable for use in
production yet - some settings may not be available to the django application
and so it requires further manual changes. In this case, review these
files, editing them as required, and placing them in the right location.

Running stackhelper
===================

The following management commands are provided:

stack_generate
--------------

Usage: manage.py stack_generate [--force] [--template-path=<PATH>] [directory]

Generates new versions of configuration files in the specified directory,
if specified. Otherwise to <sys.prefix>/etc if in a virtual environment.

Files will not be overwritten unless --force is specified.

Templates will be searched for in project_root/stack_templates unless specified in stack_generate

stack_diff
----------

Usage: manage.py stack_diff [directory]

Prints out differences if the generated files would be different. Returns 0
if the files are all identical, or 1 if the files should be regenerated.



