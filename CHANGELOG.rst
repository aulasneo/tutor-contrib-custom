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