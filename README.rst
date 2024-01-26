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

Passwords policy
~~~~~~~~~~~~~~~~~~~~~~~~~

See `the documentation <https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/password.html>`_
for more information about setting a password policy.
The list of validators can be found in the `edx repository <https://github.com/openedx/edx-platform/blob/master/common/djangoapps/util/password_policy_validators.py>`_.

Currently the available validators are:

.. csv-table:: Password validators
    :header: "Validator", "Options"

    "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", "--"
    "common.djangoapps.util.password_policy_validators.MinimumLengthValidator",   "min_length"
    "common.djangoapps.util.password_policy_validators.MaximumLengthValidator",   "max_length"
    "common.djangoapps.util.password_policy_validators.AlphabeticValidator",      "min_alphabetic"
    "common.djangoapps.util.password_policy_validators.NumericValidator",         "min_numeric"
    "common.djangoapps.util.password_policy_validators.UppercaseValidator",       "min_upper"
    "common.djangoapps.util.password_policy_validators.LowercaseValidator",       "min_lower"
    "common.djangoapps.util.password_policy_validators.PunctuationValidator",     "min_punctuation"
    "common.djangoapps.util.password_policy_validators.SymbolValidator",          "min_symbol"

The default value is:

::

        [
            {
                'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
            },
            {
                'NAME': 'common.djangoapps.util.password_policy_validators.MinimumLengthValidator',
                'OPTIONS': {'min_length': 2}
            },
            {
                'NAME': 'common.djangoapps.util.password_policy_validators.MaximumLengthValidator',
                'OPTIONS': {'max_length': 75}
            }
        ]

Note that the type of the value is `list`. Setting this configuration will overwrite the default.


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

Set `CUSTOM_ENABLE_DYNAMIC_REGISTRATION_FIELDS` to True (default False) to enable this feature.

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

Default MKTG_URLS:

::

        "MKTG_URLS": {
            'ABOUT': '/about',
            'ACCESSIBILITY': '/accessibility',
            'AFFILIATES': '/affiliate-program',
            'BLOG': '/blog',
            'CAREERS': '/careers',
            'CONTACT': '/support/contact_us',
            'COURSES': '/course',
            'DONATE': '/donate',
            'ENTERPRISE': '/enterprise',
            'FAQ': '/student-faq',
            'HONOR': '/edx-terms-service',
            'HOW_IT_WORKS': '/how-it-works',
            'MEDIA_KIT': '/media-kit',
            'NEWS': '/news-announcements',
            'PRESS': '/press',
            'PRIVACY': '/edx-privacy-policy',
            'ROOT': <LMS base url>,
            'SCHOOLS': '/schools-partners',
            'SITE_MAP': '/sitemap',
            'TOS': '/edx-terms-service',
            'TOS_AND_HONOR': '/edx-terms-service',
            'TRADEMARKS': '/trademarks',
            'WHAT_IS_VERIFIED_CERT': '/verified-certificate'
        },


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

Footer social links
~~~~~~~~~~~~~~~~~~~

Set SOCIAL_MEDIA_FOOTER_URLS to a dict of social links. E.g.:

::

    SOCIAL_MEDIA_FOOTER_URLS = {
        'tumblr': '<insert_tumblr_url_here>',
        'reddit': '<insert_reddit_url_here>',
        'twitter': '<insert_twitter_url_here>',
        'google_plus': '<insert_google_plus_url_here>',
        'youtube': '<insert_youtube_url_here>',
        'linkedin': '<insert_linkedin_url_here>',
        'meetup': '<insert_meetup_url_here>',
        'facebook': '<insert_facebook_url_here>',
    }


Social sharing links
~~~~~~~~~~~~~~~~~~~~

Set CUSTOM_SOCIAL_SHARING_SETTINGS as a dict with the following settings:

Change the defaults to enable social sharing urls in the dashboard (set CUSTOM_COURSE_URLS)
and the certificates.

New defaults are:

::

    'SOCIAL_SHARING_SETTINGS': {
        'CUSTOM_COURSE_URLS': True,
        'DASHBOARD_FACEBOOK': True,
        'FACEBOOK_BRAND': "{{ CUSTOM_FACEBOOK_BRAND }}",
        'DASHBOARD_TWITTER': True,
        'DASHBOARD_TWITTER_TEXT': None,
        'TWITTER_BRAND': "{{ CUSTOM_TWITTER_BRAND }}",
        'CERTIFICATE_FACEBOOK': True,
        'CERTIFICATE_FACEBOOK_TEXT': None,
        'CERTIFICATE_TWITTER': True,
        'CERTIFICATE_TWITTER_TEXT': None,
        'CERTIFICATE_LINKEDIN_MODE_TO_CERT_NAME': {
                'honor': '{platform_name} Honor Code Credential for {course_name}',
                'verified': '{platform_name} Verified Credential for {course_name}',
                'professional': '{platform_name} Professional Credential for {course_name}',
                'no-id-professional': '{platform_name} Professional Credential for {course_name}',
        }
    },


Remove search box in index
~~~~~~~~~~~~~~~~~~~~~~~~~~

Disable the discovery plugin and set `CUSTOM_ENABLE_COURSE_DISCOVERY` to `False`.

Additional sites
~~~~~~~~~~~~~~~~

Enable additional Django sites by adding the URLs to the ``ALLOWED_HOSTS`` list.

Remember to add the url to Django's sites and create a DNS CNAME entry pointing to the LMS host.

Bulk enrollment
~~~~~~~~~~~~~~

By default, bulk enrollments via CSV is not enabled. This plugin will enable bulk enrollments by default.
To disable bulk enrollments, set ``CUSTOM_ALLOW_AUTOMATED_SIGNUPS`` to ``False``.

OAUTH2 secrets
~~~~~~~~~~~~~~

Set ``CUSTOM_SOCIAL_AUTH_OAUTH_SECRETS`` with all the OAuth2 secrets. E.g.:

::

    SOCIAL_AUTH_OAUTH_SECRETS:
        facebook: 98765432181bbe3a2596efa8ba7abcde
        google-oauth2: abcdef123456789101112131
        linkedin-oauth2: 4D3Cb2aB1C0dEFGH
        azuread-oauth2: abcdef12341yHlmOrR8D3vlV1cD2VtL7k9xk9DSB8vw=

Disable registration form
~~~~~~~~~~~~~~~~~~~~~~~~~

Set ``CUSTOM_ALLOW_PUBLIC_ACCOUNT_CREATION`` to ``False`` to disable the public
registration form.

Set ``CUSTOM_ENABLE_REQUIRE_THIRD_PARTY_AUTH`` to ``True`` to disable user/password
login and registration and force registering via a third party identity provider.

Google Analytics
~~~~~~~~~~~~~~~~

Set ``CUSTOM_GOOGLE_ANALYTICS_4_ID`` to your Google Analytics 4 ID.
Then rebuild openedx and mfe.

Course Live
~~~~~~~~~~~

Set `CUSTOM_ENABLE_COURSE_LIVE` to False (custom default True) to disable the course live feature.
To disable Big Blue Button support, set `CUSTOM_ENABLE_BIG_BLUE_BUTTON` to False (custom default True).

Then run `tutor {dev|local|k8s} init --limit custom` to enable it.

Maximum login failures allowed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set `CUSTOM_ENABLE_MAX_FAILED_LOGIN_ATTEMPTS` (enabled by default) to False to
disable account locking after multiple failed attempts.
Set `CUSTOM_MAX_FAILED_LOGIN_ATTEMPTS_ALLOWED` (default 6) and
`CUSTOM_MAX_FAILED_LOGIN_ATTEMPTS_LOCKOUT_PERIOD_SECS` (default 1800) to adjust the feature.

Rate limits for API calls
~~~~~~~~~~~~~~~~~~~~~~~~~

Open edX uses `django-ratelimit <https://django-ratelimit.readthedocs.io/en/stable/index.html>`_
to limit the number of received requests from the same source in certain time periods.
We include the following settings to modify the default behavior:

* CUSTOM_RATELIMIT_ENABLE (default True): Globally enable the rate limit function.
* CUSTOM_RATELIMIT_RATE (default '120/m'): Limit to access the `/oauth2/access_token/ API <https://github.com/openedx/edx-platform/blob/3d33b8cf9a62589bf964621f0a63b419837872c5/openedx/core/djangoapps/oauth_dispatch/views.py#L99>`_
* CUSTOM_LOGISTRATION_RATELIMIT_RATE (default '100/5m'): Limit the `user logins <https://github.com/openedx/edx-platform/blob/3d33b8cf9a62589bf964621f0a63b419837872c5/openedx/core/djangoapps/user_authn/views/login.py#L502>`_ per source
* CUSTOM_LOGISTRATION_PER_EMAIL_RATELIMIT_RATE (default '30/m' per email): Limit the `user logins <https://github.com/openedx/edx-platform/blob/3d33b8cf9a62589bf964621f0a63b419837872c5/openedx/core/djangoapps/user_authn/views/login.py#L502>`_ per email
* CUSTOM_LOGISTRATION_API_RATELIMIT (default '20/m'): Limit the `MFEContextView API calls <https://github.com/openedx/edx-platform/blob/3d33b8cf9a62589bf964621f0a63b419837872c5/openedx/core/djangoapps/user_authn/api/views.py#L22>`_
* CUSTOM_LOGIN_AND_REGISTER_FORM_RATELIMIT (default '100/5m'): Limit the number of gets to the `login and registration form view <https://github.com/openedx/edx-platform/blob/3d33b8cf9a62589bf964621f0a63b419837872c5/openedx/core/djangoapps/user_authn/views/login_form.py#L132>`_.
* CUSTOM_RESET_PASSWORD_TOKEN_VALIDATE_API_RATELIMIT (default '30/7d'): Limit the number of `password reset token validations <https://github.com/openedx/edx-platform/blob/3d33b8cf9a62589bf964621f0a63b419837872c5/openedx/core/djangoapps/user_authn/views/password_reset.py#L674>`_.
* CUSTOM_RESET_PASSWORD_API_RATELIMIT (default '30/7d'): Limit `password resets <https://github.com/openedx/edx-platform/blob/3d33b8cf9a62589bf964621f0a63b419837872c5/openedx/core/djangoapps/user_authn/views/password_reset.py#L714>`_.
* CUSTOM_OPTIONAL_FIELD_API_RATELIMIT (default '10/h'): Not used
* CUSTOM_REGISTRATION_VALIDATION_RATELIMIT (default '30/7d'): Limit requests to the `registration validation API <https://github.com/openedx/edx-platform/blob/3d33b8cf9a62589bf964621f0a63b419837872c5/openedx/core/djangoapps/user_authn/views/register.py#L853>`_ (POST /api/user/v1/validation/registration/)
* CUSTOM_REGISTRATION_RATELIMIT (default '60/7d'): Limit requests to the `registration API <https://github.com/openedx/edx-platform/blob/3d33b8cf9a62589bf964621f0a63b419837872c5/openedx/core/djangoapps/user_authn/views/register.py#L540>`_.
* CUSTOM_DEFAULT_THROTTLE_RATES: Limit calls to APIView subclasses. It must be a dict with values to override.
Defaults: 'user': '60/minute', 'service_user': '800/minute', 'registration_validation': '30/minute', 'high_service_user': '2000/minute',

For rate formats, see the `ratelimit documentation <https://django-ratelimit.readthedocs.io/en/stable/usage.html>`_.
To disable a rate limit, set it to None.

Caddyfile patches
~~~~~~~~~~~~~~~~~

Use ``CADDYFILE_PATCH``, ``CADDYFILE_LMS``, ``CADDYFILE_CMS`` and ``CADDYFILE_GLOBAL`` to
add caddyfile directives to each section.

E.g.:

::

    CUSTOM_CADDYFILE_LMS: "redir / /login"

Other course settings
~~~~~~~~~~~~~~~~~~~~~

The ``Other course settings`` field editable in Studio's advanced settings is now
enabled by default. To disable, set ``CUSTOM_ENABLE_OTHER_COURSE_SETTINGS: False``.
To make this field available via the course blocks API, make sure it is included
in the course blocks API extra fields (see next).

Course blocks API extra fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``COURSE_BLOCKS_API_EXTRA_FIELDS`` setting defines which additional fields are
returned by the blocks api (``https://${LMS_HOST}/api/courses/v2/blocks/``).
This API is managed by the `BlocksView <https://github.com/openedx/edx-platform/blob/285f1fbfd758c1bb51f8e6af66adfdc42080df87/lms/djangoapps/course_api/blocks/views.py#L30>`_ view.

The new default is ``[('course', 'other_course_settings')]``.

Video uploads feature enable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Video uploads is enabled now by default.
Use the following variables to customize it behaviour:

- CUSTOM_ENABLE_VIDEO_UPLOAD_PIPELINE: Set to False to disable (enabled by default)
- CUSTOM_VIDEO_UPLOAD_PIPELINE_ROOT_PATH: Path inside the S3 bucket to store videos. By default "videos".
- CUSTOM_VIDEO_UPLOAD_PIPELINE_VEM_S3_BUCKET: Set the S3 bucket name. By default it uses the tutor-contrib-s3's configuration S3_STORAGE_BUCKET.
- CUSTOM_VIDEO_IMAGE_UPLOAD_ENABLED: Set to False to disable the possibility to upload a cover image to the video
  (enabled by default). To activate a change in this setting you must initialize Tutor




Usage
-----

::

    tutor plugins enable custom


License
-------

This software is licensed under the terms of the AGPLv3.