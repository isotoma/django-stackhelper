from django.core.management.base import BaseCommand
import os, sys
from django.conf import settings
import jinja2

class Command(BaseCommand):

    args = '<directory>'
    help = 'generates configuration files in the chosen directory'

    def handle(self, *args, **options):
        if len(args) != 1:
            self.print_help(sys.argv[0], sys.argv[1])
            return
        else:
            outputdir = args[0]
            self.stdout.write("Writing configuration files to %r" % outputdir)
            if not os.path.exists(outputdir):
                os.mkdir(outputdir)
            self.generate(outputdir)

    def project_root(self):
        """ Locate the root of the django project. There is probably a much better way of doing this. """
        # possibly put templates in installed applications and loop through them?
        return __import__(settings.SETTINGS_MODULE).__path__[0]

    def templates(self):
        """ A generator of tuples of templates of the form (data, name) """
        template_path = os.path.join(self.project_root(), "stack_templates")
        if os.path.exists(template_path):
            for d in os.listdir(template_path):
                for f in os.listdir(os.path.join(template_path, d)):
                    data = open(os.path.join(template_path, d, f)).read()
                    yield (data, os.path.join(d, f))

    def settings_dict(self):
        sd = {}
        for k in dir(settings):
            sd[k] = getattr(settings, k)
        return sd

    def generate(self, outputdir):
        environment = jinja2.Environment()
        sd = self.settings_dict()
        for data, name in self.templates():
            t = environment.from_string(data, globals=sd)
            path = os.path.join(outputdir, name)
            self.stdout.write("Writing %r" % path)
            d = os.path.dirname(path)
            if not os.path.exists(d):
                os.mkdir(d)
            out = open(path, "w")
            out.write(t.render())
            out.close()






