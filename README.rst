.. image:: https://img.shields.io/travis/eikendev/ttrss/master
    :alt: Build status
    :target: https://travis-ci.org/github/eikendev/ttrss/builds/

.. image:: https://img.shields.io/pypi/status/ttrss
    :alt: Development status
    :target: https://pypi.org/project/ttrss/

.. image:: https://img.shields.io/pypi/l/ttrss
    :alt: License
    :target: https://pypi.org/project/ttrss/

.. image:: https://img.shields.io/pypi/pyversions/ttrss
    :alt: Python version
    :target: https://pypi.org/project/ttrss/

.. image:: https://img.shields.io/pypi/v/ttrss
    :alt: Version
    :target: https://pypi.org/project/ttrss/

.. image:: https://img.shields.io/pypi/dm/ttrss
    :alt: Downloads
    :target: https://pypi.org/project/ttrss/

Usage
=====

This tool can be used to synchronize feeds from a `Tiny Tiny RSS <https://tt-rss.org/>`_ server.
If you're a bit like me and prefer reading your feeds through the browser, you'll sure have been in the situation of not being able to access your feeds due to the lack of an internet connection.
``ttrss`` will help you to read articles offline in a very simple manner.

For a quick introduction, let me show how you would use the tool to get started.

.. code:: bash

    ttrss synchronize -d ~/news/ --url https://ttrss.example.com/ --username example --keyring-service ttrss.example.com

As can be seen above, you have to specify a directory where all unread articles will be saved in.
Additionally, server information and login credentials must be provided.
For now, the only way of specifying a password is by using the ``keyring`` command line tool, which is passed the ``--username`` and the ``--keyring-service``.

Installation
============

From PyPI
---------

.. code:: bash

    pip install ttrss

From Source
-----------

.. code:: bash

    ./setup.py install

Fedora
------

.. code:: bash

    sudo dnf copr enable eikendev/ttrss
    sudo dnf install python3-ttrss

Configuration
=============

A configuration file can be saved to ``~/.config/ttrss/config.ini`` to avoid specifying the path and other information for each invocation.
Of course, ``$XDG_CONFIG_HOME`` can be set to change your configuration path.
Alternatively, the path to the configuration file can be set via the ``--config-file`` argument.

.. code:: ini

    [GENERAL]
    RootDir = ~/news/
    Url = https://ttrss.example.com/
    Username = example
    KeyringService = ttrss.example.com

Development
===========

The source code is located on `GitHub <https://github.com/eikendev/ttrss>`_.
To check out the repository, the following command can be used.

.. code:: bash

    git clone https://github.com/eikendev/ttrss.git
