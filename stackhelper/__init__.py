
import os
from django.conf import settings
import jinja2
import difflib
from StringIO import StringIO

def templates(template_path):
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

def gen_templates(template_path):
    environment = jinja2.Environment()
    sd = settings_dict()
    for data, name in templates(template_path):
        t = environment.from_string(data, globals=sd)
        s = t.render()
        yield name, s

def gen_templates_with_path(template_path, outputdir):
    for name, contents in gen_templates(template_path):
        path = os.path.join(outputdir, name)
        yield path, contents
            
def make_directories(path):
    d = os.path.dirname(path)
    if not os.path.exists(d):
        os.makedirs(d)
    
def generate(template_path, outputdir, force=False):
    for path, contents in gen_templates_with_path(template_path, outputdir):
        make_directories(path)
        if os.path.exists(path) and not force:
            raise SystemExit("Will not clobber %r, quitting" % path)
        open(path, "w").write(contents)

def diff(template_path, outputdir):
    for path, contents in gen_templates_with_path(template_path, outputdir):
        if os.path.exists(path):
            existing = open(path).read()
            d = difflib.unified_diff(existing.splitlines(), contents.splitlines())
            yield path, "\n".join(d)
        else:
            yield path, contents
            