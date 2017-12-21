#!/bin/bash

#This is a script that runs my Selenium tests with nosetests logging.
#It puts the results into /Repors/ in a dated file.
#type attribute can be changed to only run some tests.
# __init__.py had to be added to Pages and Objects to make them Python packages,
# otherwise nosetest would not import them.
#Kacper 14/12/2017

filename=`date +%F-%T`

nosetests -v logintest.py --nologcapture --with-xunit --xunit-file=..\/Reports\/\login$filename.xml -a type=smoke
nosetests -v searchtest.py --nologcapture --with-xunit --xunit-file=..\/Reports\/search$filename.xml -a type=smoke
