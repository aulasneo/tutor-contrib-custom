Change log
==========

Unreleased
----------

Set tutor dependency to 14.x.x

Version 0.7.0 (2023-08-17)
----------

Add support for AUTH_PASSWORD_VALIDATORS.
Update default MKTG_URL_LINK_MAP.

Version 0.6.1 (2023-06-28)
----------

Add Google Analytics support

Version 0.6.0 (2023-06-16)
----------

Add CUSTOM_SOCIAL_AUTH_OAUTH_SECRETS to set OAuth2 secrets.
Add CUSTOM_ALLOW_PUBLIC_ACCOUNT_CREATION to disable the public registration form.
Add CUSTOM_ENABLE_REQUIRE_THIRD_PARTY_AUTH to force authentication via third
party provider.

Version 0.5.0 (2023-02-23)
----------

Enable bulk enrollments by default.
Improve support of marketing urls.
Enable patching caddyfile with CUSTOM_CADDYFILE_PATCH.
Enable enterprise integration by default.
Allow multiple sites
Enable third party authentication with CUSTOM_AUTHENTICATION_BACKENDS setting


Version 0.4.1 (2023-01-16)
----------
Fix CUSTOM_ENABLE_COURSE_DISCOVERY.

Version 0.4.0 (2022-12-30)
----------

Add CUSTOM_ENABLE_COURSE_DISCOVERY to disable the search box at the home page.

Version 0.3.0 (2022-12-29)
----------

Add settings for marketing site.


Version 0.2.2 (2022-12-28)
-------------

Add patch for Nutmeg to fix 'Pages' view in Studio.

Version 0.1.3
-------------

Add footer links

Version 0.1.2
-------------

Add an init routine in the LMS service to set some features from waffle flags,
waffle switches or other Django configurations. They are enabled by default.

- ENABLE_CERTIFICATES_AUTOGENERATION
- ENABLE_SELF_PACED_COURSES
- ENABLE_ANONYMOUS_COURSEWARE_ACCESS
- ENABLE_PERSISTENT_GRADES
- ENABLE_COURSE_EXIT_PAGE

Version 0.1.1
-------------

* Add SKIP_EMAIL_VALIDATION (default: False)