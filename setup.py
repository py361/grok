from setuptools import setup, find_packages

setup(
    name='grok',
    version='0.9',
    author='Grok Team',
    author_email='grok-dev@zope.org',
    url='https://launchpad.net/grok',
    download_url='svn://svn.zope.org/repos/main/grok/trunk#egg=grok-dev',
    description='Grok: Now even cavemen can use Zope 3!',
    long_description=open('README.txt').read(),
    license='ZPL',

    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe=False,
    install_requires=['setuptools',
                      'martian',
                      'simplejson',
                      'pytz',
                      'ZODB3',
                      'zope.annotation',
                      'zope.app.catalog',
                      'zope.app.component',
                      'zope.app.container',
                      'zope.app.folder',
                      'zope.app.intid',
                      'zope.app.pagetemplate',
                      'zope.app.publication',
                      'zope.app.publisher',
                      'zope.app.testing',
                      'zope.component',
                      'zope.configuration',
                      'zope.dottedname',
                      'zope.deprecation',
                      'zope.event',
                      'zope.formlib',
                      'zope.interface',
                      'zope.lifecycleevent',
                      'zope.pagetemplate',
                      'zope.publisher',
                      'zope.schema',
                      'zope.security',
                      'zope.testing',
                      'zope.traversing',
                      'zope.testbrowser',
                      'zope.app.twisted',
                      'zope.app.securitypolicy',
                      'zope.app.zcmlfiles',
                      'zc.catalog',
                      ],
)
