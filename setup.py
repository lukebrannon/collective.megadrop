from setuptools import setup, find_packages
import os

version = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'collective', 'megadrop', 'version.txt')).read().strip()

version = version

setup(name='collective.megadrop',
      version=version,
      description="Integrates mega dropdown menu with Plone global navigation.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Luke Brannon',
      author_email='luke@laplone.org',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.registry',
          'plone.behavior',
          'plone.directives.form',
          'zope.schema',
          'zope.interface',
          'zope.component',
          'lxml', 
          'plone.app.blocks', 
          'plone.app.textfield',
          'plone.app.tiles',
          'plone.tiles',
      ],
      extras_require={
        'tests': ['collective.testcaselayer',]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
