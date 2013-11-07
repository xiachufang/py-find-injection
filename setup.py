from setuptools import setup, find_packages


setup(
    name="py_find_injection",
    version="0.1",
    author="James Brown",
    author_email="jbrown@uber.com",
    url="http://github.com/uber/py_find_injection",
    description="simple python ast consumer which searches for common SQL injection attacks",
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Topic :: Security",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(exclude=["tests"]),
    entry_points={
        "console_scripts": [
            "py-find-injection = py_find_injection:main",
        ]
    },
    tests_require=["nose==1.3.0", "mock==1.0.1"],
    test_suite="nose.collector",
    long_description="""py_find_injection

Walks the AST and looks for arguments to cursor.execute or session.execute; then
determines whether string interpolation, concatenation or the .format() call is used
on those arguments. Not at all comprehensive, but better than nothing.
"""
)
