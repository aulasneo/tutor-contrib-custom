Customizer plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================

Plugin to customize settings of Open edX.

It provides a good set of default for most Open edX settings, and allows to configure
many settings from the ``conf.yml`` file.

Installation
------------

::

    pip install git+https://github.com/aulasneo/tutor-contrib-custom

Configuration
-------------

Set configuration variables prepended with `CUSTOM_` to change the defaults.

Check the `config` dict in the `plugin.py` for available variables and their default values.

Registration extra fields
~~~~~~~~~~~~~~~~~~~~~~~~~


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
~~~~~~~~~~~~~~

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

If CUSTOM_ENABLE_MKTG_SITE is true:
    - Set marketing URLs in CUSTOM_MKTG_URLS
Else:
    - Set the marketeting URLs in CUSTOM_MKTG_URL_LINK_MAP

Any setting configured in CUSTOM_MKTG_URL_OVERRIDES will override CUSTOM_MKTG_URLS and CUSTOM_MKTG_URL_LINK_MAP.

Footer links
~~~~~~~~~~~~

Set `CUSTOM_MKTG_URL_OVERRIDES` to a dict with URLs to override, or '#' to remove.
Valid keys are:

- ABOUT
- ENTERPRISE
- BLOG
- AFFILIATES
- CAREERS
- DONATE
- MEDIA_KIT
- NEWS
- TOS_AND_HONOR
- PRIVACY
- ACCESSIBILITY
- TOS
- HONOR
- SITE_MAP
- AFFILIATES
- COOKIE
- CCPA

Set `CUSTOM_SUPPORT_SITE_LINK` to add a link to the help center. Set to '#' to remove the link

Set `CUSTOM_SECURITY_PAGE_URL` to set the url of the security page

How are footer links displayed:

All these links are visible if not set to "#".


Navigation links:
- ABOUT
- ENTERPRISE
- BLOG
- NEWS
- HELP_CENTER (from CUSTOM_SUPPORT_SITE_LINK)
- CONTACT (This is not set here. Set CONTACT_US_CUSTOM_LINK in the site configuration)
- CAREERS
- DONATE

Legal links:
- TOS_AND_HONOR
- PRIVACY
- ACCESSIBILITY
- SITE_MAP
- TOS (available only if TOS_AND_HONOR is not '#')
- HONOR (available only if TOS_AND_HONOR is not '#')

Connect links (not visible in the standard views):
- BLOG
- CONTACT (This is not set here. Set CONTACT_US_CUSTOM_LINK in the site configuration)
- HELP_CENTER (from CUSTOM_SUPPORT_SITE_LINK)
- SECURITY (from CUSTOM_SECURITY_PAGE_URL)
- MEDIA_KIT
- DONATE

Business links (not visible in the standard views):
- ABOUT
- ENTERPRISE (plus a set of query parameters set in CUSTOM_ENTERPRISE_MARKETING_FOOTER_QUERY_PARAMS)
- AFFILIATES
- CAREERS
- NEWS

More info links (not visible in the standard views):
- TOS_AND_HONOR
- TOS (available only if TOS_AND_HONOR is not '#')
- HONOR (available only if TOS_AND_HONOR is not '#')
- PRIVACY
- COOKIE
- ACCESSIBILITY
- CCPA
- SITE_MAP
- TRADEMARKS

Header links
~~~~~~~~~~~~~

- HOW_IT_WORKS
- COURSES
- SCHOOLS

Remove search box in index
~~~~~~~~~~~~~~~~~~~~~~~~~~

Disable the discovery plugin and set `CUSTOM_ENABLE_COURSE_DISCOVERY` to `False`.

Additional sites
~~~~~~~~~~~~~~~~

Enable additional Django sites by adding the URLs to the ``ALLOWED_HOSTS`` list.

Remember to add the url to Django's sites and create a DNS CNAME entry pointing to the LMS host.

Usage
-----

::

    tutor plugins enable custom


License
-------

This software is licensed under the terms of the AGPLv3.