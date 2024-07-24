Change log
==========

Unreleased
----------

- Feat: Upgrade to Quince
- Depr: Remove unneeded COMPLETION_AGGREGATOR_URL (fixed in https://github.com/openedx/edx-platform/pull/30331)
- Fix: Correct default value of MAX_FAILED_LOGIN_ATTEMPTS_ALLOWED: 6
- Depr: Remove unneeded ENABLE_BIG_BLUE_BUTTON and ENABLE_COURSE_LIVE.
  Both are enabled by default as per https://github.com/openedx/edx-platform/pull/33998/
- Fix: Replace pkg_resources by importlib_resources

Version 16.2.2 (2024-06-26)
----------
Add COURSE_BLOCKS_API_EXTRA_FIELDS setting, with default to [('course', 'other_course_settings')]

Version 16.2.1 (2024-02-19)
----------

Fixed bug in setting video upload pipeline

Version 16.2.0 (2024-02-16)
----------

Enable OpenSearch index configuration

Version 16.1.0 (2024-01-26)
----------

Enable video upload feature by default.

Version 16.0.1 (2024-01-10)
----------
Fix: add android and ios sku to the default mode (https://github.com/openedx/edx-platform/pull/31512)

Version 16.0.0 (2023-11-17)
----------
Upgrade to Palm

Version 15.1.0 (2023-09-25)
----------

Add settings to modify the rate limits for API calls.

Version 14.0.1 (2023-09-06)
----------

Add capability to disable and/or adjust the maximum student failed login attempts.

Version 15.0.0 (2023-09-07)
----------

Setup compatibility with tutor 15 and Olive
Remove unused ALLOWED_HOSTS in caddyfile patch
Remove deprecated ASSUME_ZERO_GRADE_IF_ABSENT_FOR_ALL_TESTS and ENABLE_PERSISTENT_GRADES
(https://github.com/openedx/edx-platform/pull/30978)
Remove deprecated BLOCK_STRUCTURES_SETTINGS['PRUNING_ACTIVE'] (https://github.com/openedx/public-engineering/issues/31)
Replace Google UA settings with GOOGLE_ANALYTICS_4_ID
Remove unneeded patches
Remove unneeded setting to enable persistent grades.
Remove deprecated CUSTOM_ENABLE_SELF_PACED_COURSES.
Add CUSTOM_ENABLE_DYNAMIC_REGISTRATION_FIELDS
Add CUSTOM_ENABLE_BIG_BLUE_BUTTON


Version 14.0.0 (2023-08-29)
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