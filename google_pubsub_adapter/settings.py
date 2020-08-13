import os
from django.conf import settings

settings.GCLOUD_PUBSUB_PROJECT_ID = os.environ["GCLOUD_PUBSUB_PROJECT_ID"]
