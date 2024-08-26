from setuptools import setup, find_packages

setup(
    name='amazNew',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        #парсить сюда requerements.txt?
    ],
    entry_points={
        "lms.djangoapp": [
            "test = test_django.apps:Test",
        ],
        "cms.djangoapp": [
        ],
    }
)
