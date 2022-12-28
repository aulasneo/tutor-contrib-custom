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