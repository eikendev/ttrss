.. image:: https://img.shields.io/pypi/status/ttrss.svg
   :target: https://pypi.org/project/ttrss/

.. image:: https://img.shields.io/pypi/l/ttrss.svg
   :target: https://pypi.org/project/ttrss/

.. image:: https://img.shields.io/pypi/pyversions/ttrss.svg
   :target: https://pypi.org/project/ttrss/

.. image:: https://img.shields.io/pypi/v/ttrss.svg
   :target: https://pypi.org/project/ttrss/

.. image:: https://img.shields.io/pypi/dm/ttrss.svg
   :target: https://pypi.org/project/ttrss/

Usage
=====

This tool can be used to interact with a `Tiny Tiny RSS <https://tt-rss.org/>`_ server through the command line.
The main purpose of ``ttrss`` is to download the unread articles to the local machine.
If you're a bit like me and prefer reading your feeds through the browser, you'll sure have been in the situation of not being able to access your feeds due to the lack of an internet connection.
``ttrss`` will help you to read articles offline in a very simple manner.

For a quick introduction, let me show how you would use the tool to get started.
::

    $ ttrss synchronize -d ~/news/ --url https://ttrss.example.com/ --username example --keyring-service ttrss.example.com

As can be seen above, you have to specify a directory where all unread articles will be saved in.
Additionally, server information and login credentials must be provided.
For now, the only way of specifying a password is by using the ``keyring`` command line tool, which is passed the ``--username`` and the ``--keyring-service``.

Installation
============

From PyPI
---------
::

   pip install ttrss

From Source
-----------
::

   ./setup.py install

Configuration
=============

A configuration file can be saved to ``~/.config/ttrss/config.ini`` to avoid specifying the path and other information for each invocation.
Of course, ``$XDG_CONFIG_HOME`` can be set to change your configuration path.
Alternatively, the path to the configuration file can be set via the ``--config-file`` argument.
::

    [GENERAL]
    RootDir = ~/news/
    Url = https://ttrss.example.com/
    Username = example
    KeyringService = ttrss.example.com
