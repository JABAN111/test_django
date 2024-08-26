from django.apps import AppConfig
# from edx_django_utils.plugins import PluginURLs, PluginSettings


class TestConfig(AppConfig):
    # name = 'amazNew.apps.AmazNewConfig.amazNew'
    # name = 'amazNew.apps.AmazNewConfig.amazNew'
    name = "test_django"
    print('test_django ' * 200)
    plugin_app = {
        "url_config": {
            # ProjectType.LMS p.s. const LMS equal to "lms.djangoapp"
            'lms.djangoapp': {
                "namespace": 'test_django',
                "regex": '^test/',
                "relative_path": 'test_django.urls'
            }
        }
    }
