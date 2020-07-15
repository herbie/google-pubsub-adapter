# Google Pubsub Adapter

This Adapter is based on Django and provides a way to publish messages to Google Pubsub.

It is meant to be used with [Herbie](https://github.com/herbie/herbie).

## Getting started

#### Using with Herbie

The package already provides a Django app that just needs to be registered in the main Django app using Herbie.

1. Add the package to the project _requirements.txt_

CHANGE LATER WHEN PUBLISHED
```
    git+https://github.com/herbie/herbie@package-herbie
```

2. Update the requirements
```
    pip install -r requirements.txt -U
```

3. Add the adapter App to Django Installed Apllications:

```
INSTALLED_APPS = [
    ...
    'google_pubsub_adapter.apps.HerbieGooglePubsubAdapterConfig',
    ...
]
```

4. Create the Topics according to the Business Schemas

```
python manage.py init_pubsub
```

An example Django application using this adapter can be found at the [Herbie Sandbox](https://github.com/herbie/sandbox) repository.
