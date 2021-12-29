#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='Alpha',
    version='3.0',
    description='An intelligent virtual assistant for daily use',
    long_description=open('README.md').read(),
    author='Gabs Ma',
    author_email='nuggetcatsoftware@gmail.com',
    url='https://github.com/nuggetcatsoftware/Alpha',
    packages=['audio'],
    install_requires=[
        'requests>=2.5.3',
        'ChatterBot>=1.0.8',
        'chatterbot-corpus>=1.2.0',
        'win10toast>=0.9',
        'wikipedia>=1.4.0',
        'pyttsx3>=2.90',
        'Eel>=0.12.4',
        'SpeechRecognition>=3.8.1',
        'pprintpp>=0.4.0',
        'PyAutoGUI>=0.9.52',
        'psutil>=5.7.3',
        'playsound>=1.2.2'
    ],
    license=open('LICENSE').read()
)
