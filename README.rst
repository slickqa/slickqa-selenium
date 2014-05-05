==================
Slick Selenium API
==================

Part of the slick project

-------
Purpose
-------

The Slick selenium api is a higher level api for interacting with selenium 2 (aka webdriver).  The purpose is to
handle many of the redundant things you always have to handle with UI testing transparently.  Namely:

1. Waiting for UI elements to exist before using them
2. A decent page class abstraction to help with building better tests
3. Debugging information (finding out what went wrong when an error happens)
4. Logging (for tracing purposes, finding out where something went wrong, or started to go wrong)

When doing automated testing, one thing that usually causes higher maintenance costs is having to re-run a test to
diagnose an issue.  Often if you don't have proper information when you need to figure out what went wrong, you don't
even know if it is a test failure or a product failure.  Information is one of the major factors that separates good
automation from bad.

This API's purpose is to help you to first not have as many errors, second to be able to quickly diagnose and fix
what errors come, and finally to be able to easily write good maintainable and readable tests.

-----
Usage
-----

TODO

------------
Installation
------------

You can install this api by using `pip <https://pip.pypa.io/en/latest/>`_::

  pip install slickqa-selenium

This should install this api, and all the requisite dependencies.



