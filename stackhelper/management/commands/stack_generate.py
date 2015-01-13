from __future__ import print_function

import os
import sys
from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings

from stackhelper import generate


class Command(BaseCommand):

    args = '<directory>'
    help = 'generates configuration files in the chosen directory'
    option_list = BaseCommand.option_list + (
        make_option('--force',
                    action="store_true",
                    default=False,
                    help="Force overwriting of existing files"),
    )

    def handle(self, *args, **options):
        if len(args) == 0:
            outputdir = os.path.join(sys.prefix, "etc")
        elif len(args) > 1:
            self.print_help(sys.argv[0], sys.argv[1])
            return
        else:
            outputdir = args[0]

        message = "Writing configuration files to %r" % outputdir
        if hasattr(self, 'stdout'):
            self.stdout.write(message)
        else:
            print(message)
        if not os.path.exists(outputdir):
            os.mkdir(outputdir)
        template_path = os.path.join(self.project_root(), "stack_templates")
        generate(template_path, outputdir, options['force'])

    def project_root(self):
        """ Locate the root of the django project.
        There is probably a much better way of doing this. """
        # possibly put templates in installed applications
        # and loop through them?
        return __import__(settings.SETTINGS_MODULE).__path__[0]
