import bootstrap_carousel

install_requires = [
    'django',
    'south',
    'django_nose',
    'pillow',
]

long_description = '''
django-bootstrap-carousel implement the carousel component for
bootstrap in Django. See the project page for more information:
https://github.com/cdchen/django-bootstrap-carousel

'''

from setuptools import setup

setup(
    name='django_bootstrap_carousel',
    version=str(bootstrap_carousel.__version__),
    description='Django Bootstrap Carousel Component',
    long_description=long_description,
    author='cdchen',
    author_email='cdchen@nicestudio.com.tw',
    url='https://github.com/cdchen/django-bootstrap-carousel',
    download_url=('https://github.com/cdchen/django-bootstrap-carousel/'
                  'tarball/master'),
    license='MIT License',
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
)
