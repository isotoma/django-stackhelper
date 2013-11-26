import os
from setuptools import setup

README=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-stackhelper",
    version="0.1",
    packages=["stackhelper"],
    include_package_data=True,
    license="Apache Software License",
    description="A Django application to help you configure other components of your deployment stack",
    long_description=README,
    url="http://github.com/isotoma/django-stackhelper",
    author="Doug Winter",
    author_email="doug.winter@isotoma.com",
)
