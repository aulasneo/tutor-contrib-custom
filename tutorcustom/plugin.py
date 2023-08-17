from glob import glob
import os
import pkg_resources

from tutor import hooks

from .__about__ import __version__


########################################
# CONFIGURATION
########################################

config = {
    'defaults': {
        # openedx-common-settings
        "FACEBOOK_BRAND": "",
        "TWITTER_BRAND": "",
        "BADGR_ENABLE_NOTIFICATIONS": True,
        "BLOCK_STRUCTURES_SETTINGS_PRUNING_ACTIVE": True,
        "DEFAULT_MOBILE_AVAILABLE": True,
        "ENABLE_COMPREHENSIVE_THEMING": True,
        # Set to True to prevent using username/password login and registration and only allow
        #   authentication with third party auth
        "ENABLE_REQUIRE_THIRD_PARTY_AUTH": False,
        "SEARCH_SKIP_SHOW_IN_CATALOG_FILTERING": False,
        "WIKI_ENABLED": False,
        "COURSE_MODE_DEFAULTS": {
            "name": "Honor",
            "slug": "honor",
            "bulk_sku": None,
            "currency": "usd",
            "description": None,
            "expiration_datetime": None,
            "min_price": 0,
            "sku": None,
            "suggested_prices": ""
        },
        "SOCIAL_MEDIA_FOOTER_URLS": {},
        "COMPLETION_AGGREGATOR_URL": "https://",
        "MKTG_URL_OVERRIDES": {},
        "MKTG_URLS": {},
        "MKTG_URL_LINK_MAP": {
            'ABOUT': 'about',
            'CONTACT': 'contact',
            'FAQ': 'help',
            'COURSES': 'courses',
            'ROOT': 'root',
            'TOS': 'tos',
            'HONOR': 'honor',
            'TOS_AND_HONOR': 'edx-terms-service',
            'PRIVACY': 'privacy',
            'PRESS': 'press',
            'BLOG': 'blog',
            'DONATE': 'donate',
            'SITEMAP.XML': 'sitemap_xml',
            'WHAT_IS_VERIFIED_CERT': 'verified-certificate',
        },
        "SUPPORT_SITE_LINK": '#',
        "SECURITY_PAGE_URL": '#',
        "ENTERPRISE_MARKETING_FOOTER_QUERY_PARAMS": '',
        "GOOGLE_ANALYTICS_ACCOUNT": '',
        "GOOGLE_ANALYTICS_TRACKING_ID": '',

        # openedx-lms-common-settings
        "REGISTRATION_EXTRA_FIELDS": '',
        "ENABLE_COURSE_DISCOVERY": True,
        "AUTHENTICATION_BACKENDS": [],
        "SOCIAL_AUTH_OAUTH_SECRETS": {},

        # openedx-lms-production-settings
        "LMS_SOCIAL_SHARING_SETTINGS": {
            'CUSTOM_COURSE_URLS': True,
            'DASHBOARD_FACEBOOK': True,
            'FACEBOOK_BRAND': "{{ CUSTOM_FACEBOOK_BRAND }}",
            'DASHBOARD_TWITTER': True,
            'TWITTER_BRAND': "{{ CUSTOM_TWITTER_BRAND }}",
            'CERTIFICATE_FACEBOOK': True,
            'CERTIFICATE_TWITTER': True,
            'CERTIFICATE_LINKEDIN': True,
        },
        'ALLOWED_HOSTS': [],
        "ENABLE_REQUIRE_THIRD_PARTY_AUTH": False,
        "AUTH_PASSWORD_VALIDATORS": [
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
        ],

        # openedx-cms-production-settings
        "CMS_SOCIAL_SHARING_SETTINGS": {
            'CUSTOM_COURSE_URLS': True,
        },

        # common-env-features
        "ALLOW_HIDING_DISCUSSION_TAB": True,
        "CUSTOM_COURSES_EDX": True,
        "ALLOW_COURSE_STAFF_GRADE_DOWNLOADS": True,
        "ASSUME_ZERO_GRADE_IF_ABSENT_FOR_ALL_TESTS": True,
        "CUSTOM_CERTIFICATE_TEMPLATES_ENABLED": True,
        "ENABLE_ANNOUNCEMENTS": True,
        "ENABLE_AUTOMATED_SIGNUPS_EXTRA_FIELDS": True,
        "ENABLE_BULK_ENROLLMENT_VIEW": True,
        "ENABLE_BULK_USER_RETIREMENT": True,
        "ENABLE_CHANGE_USER_PASSWORD_ADMIN": True,
        "ENABLE_MKTG_SITE": False,
        "ENABLE_ORA_TEAM_SUBMISSIONS": True,
        "ENABLE_ORA_USERNAMES_ON_DATA_EXPORT": True,
        "ENABLE_ORA_USER_STATE_UPLOAD_DATA": True,
        "ENABLE_PASSWORD_RESET_FAILURE_EMAIL": True,
        "ENABLE_SPECIAL_EXAMS": True,
        "ENABLE_UNICODE_USERNAME": True,
        "ENABLE_V2_CERT_DISPLAY_SETTINGS": True,
        "ENTRANCE_EXAMS": False,
        "SHOW_PROGRESS_BAR": True,
        "ENABLE_OTHER_COURSE_SETTINGS": True,
        "LICENSING": True,
        "SKIP_EMAIL_VALIDATION": False,
        "ENABLE_ENTERPRISE_INTEGRATION": False,
        "ALLOW_AUTOMATED_SIGNUPS": True,
        "ALLOW_PUBLIC_ACCOUNT_CREATION": True,

        # others waffle flags, switches and settings created at init time
        "ENABLE_CERTIFICATES_AUTOGENERATION": True,
        "ENABLE_SELF_PACED_COURSES": True,
        "ENABLE_ANONYMOUS_COURSEWARE_ACCESS": True,
        "ENABLE_PERSISTENT_GRADES": True,
        "ENABLE_COURSE_EXIT_PAGE": True,

        # caddyfile patch
        "CADDYFILE_PATCH": '',

    }
}

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        # Add your new settings that have default values here.
        # Each new setting is a pair: (setting_name, default_value).
        # Prefix your setting names with 'CUSTOM_'.
        (f"CUSTOM_{key}", value)
        for key, value in config['defaults'].items()
    ]
)

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        # Add your new settings that have default values here.
        # Each new setting is a pair: (setting_name, default_value).
        # Prefix your setting names with 'CUSTOM_'.
        ("CUSTOM_VERSION", __version__),
    ]
)

hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        # Add settings that don't have a reasonable default for all users here.
        # For instance: passwords, secret keys, etc.
        # Each new setting is a pair: (setting_name, unique_generated_value).
        # Prefix your setting names with 'CUSTOM_'.
        # For example:
        # ("CUSTOM_SECRET_KEY", "{{ 24|random_string }}"),
    ]
)

hooks.Filters.CONFIG_OVERRIDES.add_items(
    [
        # Danger zone!
        # Add values to override settings from Tutor core or other plugins here.
        # Each override is a pair: (setting_name, new_value). For example:
        # ("PLATFORM_NAME", "My platform"),
    ]
)


########################################
# INITIALIZATION TASKS
########################################

# To run the script from templates/custom/tasks/myservice/init, add:
hooks.Filters.COMMANDS_INIT.add_item((
    "lms",
    ("custom", "tasks", "lms", "init"),
))


########################################
# DOCKER IMAGE MANAGEMENT
########################################

# To build an image with `tutor images build myimage`, add a Dockerfile to templates/custom/build/myimage and write:
# hooks.Filters.IMAGES_BUILD.add_item((
#     "myimage",
#     ("plugins", "custom", "build", "myimage"),
#     "docker.io/myimage:{{ CUSTOM_VERSION }}",
#     (),
# )

# To pull/push an image with `tutor images pull myimage` and `tutor images push myimage`, write:
# hooks.Filters.IMAGES_PULL.add_item((
#     "myimage",
#     "docker.io/myimage:{{ CUSTOM_VERSION }}",
# )
# hooks.Filters.IMAGES_PUSH.add_item((
#     "myimage",
#     "docker.io/myimage:{{ CUSTOM_VERSION }}",
# )


########################################
# TEMPLATE RENDERING
# (It is safe & recommended to leave
#  this section as-is :)
########################################

hooks.Filters.ENV_TEMPLATE_ROOTS.add_items(
    # Root paths for template files, relative to the project root.
    [
        pkg_resources.resource_filename("tutorcustom", "templates"),
    ]
)

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    # For each pair (source_path, destination_path):
    # templates at ``source_path`` (relative to your ENV_TEMPLATE_ROOTS) will be
    # rendered to ``destination_path`` (relative to your Tutor environment).
    [
        ("custom/build", "plugins"),
        ("custom/apps", "plugins"),
    ],
)


########################################
# PATCH LOADING
# (It is safe & recommended to leave
#  this section as-is :)
########################################

# For each file in tutorcustom/patches,
# apply a patch based on the file's name and contents.
for path in glob(
    os.path.join(
        pkg_resources.resource_filename("tutorcustom", "patches"),
        "*",
    )
):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))
