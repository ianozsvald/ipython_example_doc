from setuptools import setup, find_packages

setup(
    name='example_doc',
    version='0.0.1',
    description='eg(module_or_fn) gives example documentation',
    long_description="some long desc",
    author='Maintained by Ian Ozsvald',
    author_email='ian@ianozsvald.com',
    url='https://github.com/ianozsvald/',
    license='',
    packages=['example_doc'],
    #packages = find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)

