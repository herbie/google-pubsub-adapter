from unittest import mock
from unittest.mock import Mock
from django.test import TestCase
from google_pubsub_adapter.publisher import GooglePubsubPublisher


class GooglePubsubPublisherTestCase(TestCase):

    @mock.patch('google_pubsub_adapter.publisher.google_pubsub_publisher.PublisherClient')
    @mock.patch('google_pubsub_adapter.publisher.google_pubsub_publisher.JSONRenderer')
    def test_send_message(self, mock_json_renderer, mock_google_client):
        with self.settings(GCLOUD_PUBSUB_PROJECT_ID='pubsub'):
            mock_publisher = mock_google_client()
            mock_json_render = mock_json_renderer()
            mock_publisher.topic_path.return_value = 'topic_path'

            serializer_mock = Mock(data={'type': 'type', 'payload': {"field": "value"}})

            mock_json_render.render.return_value = serializer_mock.data

            message_mock = Mock()
            message_mock.get_serializer.return_value = serializer_mock

            publisher = GooglePubsubPublisher()
            publisher.send_message(message_mock)

            mock_publisher.topic_path.assert_called_with('pubsub', 'type')
            mock_publisher.publish.assert_called_with('topic_path', data=serializer_mock.data)




