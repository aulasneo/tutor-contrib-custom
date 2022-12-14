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

Registration extra fields
-------------------------

REGISTRATION_EXTRA_FIELDS: update field visibility options in the registration form.
Visibility options are `required`, `optional` or `hidden`.
Available fields and their defaults are:

- confirm_email (hidden)
- level_of_education (optional)
- gender (optional)
- year_of_birth (optional)
- mailing_address (optional)
- goals (optional)
- honor_code (hidden)
- terms_of_service (required)
- city (hidden)
- country (hidden)

Marketing site
--------------

Set `CUSTOM_ENABLE_MKTG_SITE` to `True` to enable the marketing site.
Add the marketing site url to the `ROOT` element in the `CUSTOM_MKTG_URLS` dict.

- CUSTOM_ENABLE_MKTG_SITE (default: false)
- CUSTOM_MKTG_URLS (default empty dict). Sets the URLs at the header for non authenticated users
    when the marketing site is enabled (CUSTOM_ENABLE_MKTG_SITE=True).
    If the marketing site is enabled, set the following elements:
    - ROOT: url of the marketing site (mandatory)
    - COURSES: url for the 'courses' tab. Set to empty string to remove the tab.
    - HOW_IT_WORKS: url for the 'how it works' tab. Set to empty string to remove the tab.
    - SCHOOLS: url for the 'schools' tab. Set to empty string to remove the tab.

Footer links
------------

Set `CUSTOM_CUSTOM_MKTG_URL_OVERRIDES` to a dict with URLs to override, or '#' to remove.
Valid keys are:

- ABOUT
- ENTERPRISE
- BLOG
- CAREERS
- DONATE

Set `CUSTOM_SUPPORT_SITE_LINK` to add a link to the help center. Set to '#' to remove the link

Set `CUSTOM_CONTACT_US_ENABLE` to True and `CUSTOM_CONTACT_US_CUSTOM_LINK` to a valid url
to add a site with a contact form.

Remove search box in index
--------------------------

Disable the discovery plugin and set `CUSTOM_ENABLE_COURSE_DISCOVERY` to `False`.

Usage
-----

::

    tutor plugins enable custom


License
-------

This software is licensed under the terms of the AGPLv3.