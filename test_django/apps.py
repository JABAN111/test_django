from django.apps import AppConfig
# from edx_django_utils.plugins import PluginURLs, PluginSettings


class Test(AppConfig):
    # name = 'amazNew.apps.AmazNewConfig.amazNew'
    # name = 'amazNew.apps.AmazNewConfig.amazNew'
    name = "test"
    print('ТЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭЭСТ ' * 200)
    plugin_app = {
        "url_config": {
            # ProjectType.LMS p.s. const LMS equal to "lms.djangoapp"
            'lms.djangoapp': {
                "namespace": 'test',
                "regex": '^test/',
                "relative_path": 'urls'
            }
        }
    }
