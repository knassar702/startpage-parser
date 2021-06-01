from setuptools import setup


setup(
    name="startpage-parser",
    version='1.0.0',
    description='parsing search results from startpage search engine (based on google.com results)',
    py_modules=["startpage"],
    package_dir={'':'src'},
    url='https://github.com/knassar702/startpage-parser',
    python_requires='>=3.6',
    install_requires=['bs4','requests']
)
