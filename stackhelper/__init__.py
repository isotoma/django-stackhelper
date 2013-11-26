
import os
from django.conf import settings
from jinja2 import jinja2

def templates(path):
    """ A generator of tuples of templates of the form (data, name) """
    if os.path.exists(template_path):
        for d in os.listdir(template_path):
            for f in os.listdir(os.path.join(template_path, d)):
                data = open(os.path.join(template_path, d, f)).read()
                yield (data, os.path.join(d, f))

def settings_dict():
    sd = {}
    for k in dir(settings):
        sd[k] = getattr(settings, k)
    return sd

def generate(self, template_path, outputdir):
    environment = jinja2.Environment()
    sd = settings_dict()
    for data, name in templates(template_path):
        t = environment.from_string(data, globals=sd)
        path = os.path.join(outputdir, name)
        self.stdout.write("Writing %r" % path)
        d = os.path.dirname(path)
        if not os.path.exists(d):
            os.mkdir(d)
        out = open(path, "w")
        out.write(t.render())
        out.close()


