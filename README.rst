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
coordinated around changes.

This django application will help you manage these files.

Workflow
========

Packaging template configuration files
--------------------------------------

During application development, template files for other production stack components are placed in the "stack" directory of your django project::

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
current settings for the project in the current environment. Output files are
put by default in the stack_generated directory in the root of the project.

Creating production configuration files
---------------------------------------

These files may not be suitable for use in production yet - some settings may
not be available to the django application and so it requires further manual
changes. We recommend reviewing these files, editing them as required, and placing them in the right location.

It can be helpful to create a stack_live directory alongside stack_generated,
and then symlinking your configurations into their final location under /etc or
whatever.

Running stackhelper
===================

The following management commands are provided:

stack_status
------------

Reports on any configuration files that need to change, with a summary of diffs if any.

stack_generate
--------------

Generates new versions of configuration files in the stack output directory.

