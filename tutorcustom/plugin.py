from glob import glob
import os
import importlib_resources

from tutor import hooks

from .__about__ import __version__

config = {
    'defaults': {
        # openedx-common-settings
        "FACEBOOK_BRAND": "",
        "TWITTER_BRAND": "",
        "BADGR_ENABLE_NOTIFICATIONS": True,
        "DEFAULT_MOBILE_AVAILABLE": True,
        "ENABLE_COMPREHENSIVE_THEMING": True,
        # Set to True to prevent using username/password login and registration and only allow
        #   authentication with third party auth
        "ENABLE_REQUIRE_THIRD_PARTY_AUTH": False,
        #  If enabled, courses with a catalog_visibility set to "none" will still appear in search results.
        "SEARCH_SKIP_SHOW_IN_CATALOG_FILTERING": False,  # True by default
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
            "suggested_prices": "",
            'android_sku': None,
            'ios_sku': None,
        },  # Default is audit mode
        "MKTG_URL_LINK_MAP": {
            'ABOUT': 'about',
            'BLOG': 'blog',
            'CONTACT': 'contact',
            'COURSES': 'courses',
            'DONATE': 'donate',
            'FAQ': 'help',
            'HONOR': 'honor',
            'PRESS': 'press',
            'PRIVACY': 'privacy',
            'ROOT': 'root',
            'SITEMAP.XML': 'sitemap_xml',
            'TOS': 'tos',
            'TOS_AND_HONOR': 'edx-terms-service',
            'WHAT_IS_VERIFIED_CERT': 'verified-certificate'
        },
        "SUPPORT_SITE_LINK": '',
        "SECURITY_PAGE_URL": '#',
        "ENTERPRISE_MARKETING_FOOTER_QUERY_PARAMS": {},
        "SOCIAL_SHARING_SETTINGS": {
            'CUSTOM_COURSE_URLS': True,
            'DASHBOARD_FACEBOOK': True,
            'FACEBOOK_BRAND': "{{ CUSTOM_FACEBOOK_BRAND }}",
            'DASHBOARD_TWITTER': True,
            # 'DASHBOARD_TWITTER_TEXT': None,
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
        "ENABLE_DYNAMIC_REGISTRATION_FIELDS": False,
        "MAX_FAILED_LOGIN_ATTEMPTS_ALLOWED": 6,
        "MAX_FAILED_LOGIN_ATTEMPTS_LOCKOUT_PERIOD_SECS": 1800,
        "ELASTIC_SEARCH_INDEX_PREFIX": "",

        # openedx-lms-common-settings
        "ENABLE_COURSE_DISCOVERY": True,
        "AUTHENTICATION_BACKENDS": [],
        "SOCIAL_AUTH_OAUTH_SECRETS": {},

        # openedx-lms-production-settings
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

        # openedx-cms-common-settings
        "ENABLE_VIDEO_UPLOAD_PIPELINE": True,
        "VIDEO_UPLOAD_PIPELINE_ROOT_PATH": "videos",
        "VIDEO_UPLOAD_PIPELINE_VEM_S3_BUCKET": "{% if S3_STORAGE_BUCKET is defined %}{{ S3_STORAGE_BUCKET }}"
                                               "{% else %}'Please set VIDEO_UPLOAD_PIPELINE_VEM_S3_BUCKET with "
                                               "the bucket name'{% endif %}",
        "VIDEO_IMAGE_UPLOAD_ENABLED": True,

        # common-env-features
        "ALLOW_HIDING_DISCUSSION_TAB": True,
        "CUSTOM_COURSES_EDX": True,
        "ALLOW_COURSE_STAFF_GRADE_DOWNLOADS": True,
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
        "COURSE_BLOCKS_API_EXTRA_FIELDS": [
            ('course', 'other_course_settings')
        ],
        "LICENSING": True,
        "SKIP_EMAIL_VALIDATION": False,
        "ENABLE_ENTERPRISE_INTEGRATION": False,
        "ALLOW_AUTOMATED_SIGNUPS": True,
        "ALLOW_PUBLIC_ACCOUNT_CREATION": True,
        "ENABLE_MAX_FAILED_LOGIN_ATTEMPTS": True,

        # others waffle flags, switches and settings created at init time
        "ENABLE_CERTIFICATES_AUTOGENERATION": True,
        "ENABLE_ANONYMOUS_COURSEWARE_ACCESS": True,
        "ENABLE_COURSE_EXIT_PAGE": True,
        "MFE_PROGRESS_MILESTONES": True,
        "MFE_PROGRESS_MILESTONES_STREAK_CELEBRATION": True,
        "MFE_COURSEWARE_SEARCH": True,
        "ENABLE_NAVIGATION_SIDEBAR": True,

        # caddyfile patch
        "CADDYFILE_PATCH": '',

    }
}

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
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

# init script
with open(
        str(importlib_resources.files("tutorcustom") / "templates" / "custom" / "tasks" / "lms" / "init"),
        encoding="utf-8",
) as task_file:
    hooks.Filters.CLI_DO_INIT_TASKS.add_item(("lms", task_file.read()))

# Add the "templates" folder as a template root
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    str(importlib_resources.files("tutorcustom") / "templates")
)

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("custom/build", "plugins"),
        ("custom/apps", "plugins"),
    ],
)

# Load patches from files
for path in glob(str(importlib_resources.files("tutorcustom") / "patches" / "*")):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))
