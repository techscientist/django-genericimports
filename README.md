# django-genericimports

**STATUS**: beta

**NOTE**: I know there is no code at all, it will get pushed when we're on beta3, which should be reached around 24/Jan/2015. This documentation is also incomplete, should be ready at the same date. Thanks for understanding.

Django application to import data regardless of data/field/thirdparty types or headers. This importer is focused on functionality, completeness, data cleanliness and reporting, not on speed itself.

# Features
- Support CSV, XLS and XLSX
- Agnostic to data types or headers
- Non estandard fields are supported trough functions
- Support required unbound fields (fields required in your model but absent in your import file) 
- Support callbacks to apply after a succesful import
- Support for optional data in the import file (columns that repeat themselves)
- Support Foreignkeys
- ***Report system with statistics and records on each import***
- ***Failed entries are saved in a separate file and accesible through the report***
- ***Third party access to the imports with email reports.***
- Support django CMS
- Available as management command or admin action

# Future improvements

- Speed (really difficult, this one)
- Support ManyToMany fields
- Remove lambdas to remove eval() from the code and replace it with functions
- Optional logging (forced right now)
- Optional profiling (so you can know how well did this do in your box)
- pip support
- Figure out a way of doing bulk_inserts with ID's

# Supported on
- Django 1.5/1.6/1.7
- Python 2.7.x/3.3.x up

# Requirements
- redis

# Disclaimer
Please note that this application was made to cover all use cases and it sanitizes the data. It's not meant to be fast, at least at this stage of development. Feel free to send your optimization patches.

# How to install

To install this application use pip:

$ pip intall django-genericimports

# Setting up

The application requires you to have a working redis installation and internally it uses python-rq to manage the tasks. I will put an example configuration that you can copypaste into your settings (unless you havve specific redis settings, in which case youu should check the django-rq documentation)

REDI CONFIIG EXAMPLE HERE

The next thing you need to do is create a mapping of your fields

EXAMPLE MAPPING HERE

# How does it work

It's a looooong explanation. If you don't have time to read the code docs, you can visit (explantion link here)

# Why did you do this

Mainly because i was ******* ***** ****** tired of doing import scripts for all the projects that I worked on, the second reason is that it doesn't seem to be any open source truly generic importer that does the job right, so I felt it was necessary to do it. Of course there are really cool import applications out there, and maybe they suit you better than this one. This importer was born to satisfy the need to import 400k+ records files not only from us, but foor thirdparties as well that don't get the sanitization really well using a quite complex set of related models with multiple behaviours.

I know it's not the best approach, an it is slow as hell, but that is why I opensourced it, so everyone could improve  it. By the way I'm quite a fan of commenting the code, so you will find tons of comments in it, even some comments that are obviously obvious, but hey, not only 10+ y/exp programmers will be looking at this.

# License

This application is licensed in BSD 2-Clause license. This application was developed while at work on Havas Worldwide London, so part of the kudos goes to them as well.

# Authors

- Oscar Carballal Prego <oscar.carballal@gmail.com>
- Max Barry <max.barry@havasww.com>
