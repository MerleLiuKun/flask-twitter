from setuptools import setup

setup(
    name="Flask-Twitter",
    version="0.1.0",
    url="https://github.com/MerleLiuKun/flask-twitter",
    license="MIT",
    author="LiuKun",
    author_email="merle.liukun@gmail.com",
    description="A simple twitter api v2 extension for flask",
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    py_modules=["flask_twitter"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    python_requires=">=3.6",
    install_requires=[
        "Flask",
        "python-twitter-v2",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
