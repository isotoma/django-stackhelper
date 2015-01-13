from __future__ import print_function

import os
import sys

from django.core.management.base import BaseCommand
from django.conf import settings

from stackhelper import diff


class Command(BaseCommand):

    args = '<directory>'
    help = 'generates configuration files in the chosen directory'

    def handle(self, *args, **options):

        if not hasattr(self, 'stdout'):
            self.stdout = sys.stdout

        if len(args) != 1:
            self.print_help(sys.argv[0], sys.argv[1])
            return
        else:
            outputdir = args[0]
            template_path = os.path.join(
                self.project_root(),
                "stack_templates"
            )
            for path, d in diff(template_path, outputdir):
                self.stdout.write(path)
                self.stdout.write(d)

    def project_root(self):
        """ Locate the root of the django project.
        There is probably a much better way of doing this. """
        # possibly put templates in installed applications
        # and loop through them?
        return __import__(settings.SETTINGS_MODULE).__path__[0]
