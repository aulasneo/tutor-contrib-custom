Customizer plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================

Plugin to customize settings of Open edX.

It provides a good set of default for most Open edX settings.

Installation
------------

::

    pip install git+https://github.com/aulasneo/tutor-contrib-custom

Configuration
-------------

Set configuration variables prepended with `CUSTOM_` to change the defaults.

Check the `config` dict in the `plugin.py` for available variables and their default values.

Usage
-----

::

    tutor plugins enable custom


License
-------

This software is licensed under the terms of the AGPLv3.