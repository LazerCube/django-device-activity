============
Device activity
============

Device activity is a simple Django app that records a user device activity.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Install "django-device-activity", you'll have to make sure that user-agents is installed first::

    pip install pyyaml ua-parser user-agents
    pip install django-device-activity


2. Add "device_activity" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'device_activity',
    ]

3. Add ``DeviceMiddleware`` in ``settings.py``:

    MIDDLEWARE_CLASSES = (
        # other middlewares...
        'device-activity.middleware.DeviceMiddleware',
      )
