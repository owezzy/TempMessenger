from mock import patch
from time import sleep

import pytest

from fakeredis import FakeStrictRedis
from nameko.containers import ServiceContainer
from nameko.testing.services import entrypoint_hook

from temp_messenger.service import (
    MessageService,
    WebServer,
    sort_messages_by_expiry
)


@pytest.fixture
def fake_strict_redis():
    with patch(
            'temp_messenger.dependencies.redis.StrictRedis', FakeStrictRedis
    ) as fake_strict_redis:
        yield fake_strict_redis
        fake_strict_redis().flushall()


@pytest.fixture
def config(web_config):
    return dict(
        AMQP_URI='pyamqp://guest:guest@localhost',
        REDIS_URL='redis://localhost:6379/0',
        **web_config
    )


@pytest.fixture
def uuid4():
    with patch('temp_messenger.dependencies.redis.uui4') as uuid4:
        yield uuid4


@pytest.fixture
def message_svc(config, fake_strict_redis):
    message_svc = ServiceContainer(MessageService, config)
    message_svc.start()

    return message_svc


@pytest.fixture
def web_server(config, fake_strict_redis):
    web_server = ServiceContainer(WebServer, config)
    web_server.start()

    return web_server


@pytest.fixture
def message_lifetime():
    with patch(
            'temp_messenger.dependencies.redis.MESSAGE_LIFETIME', 100
    ) as lifetime:
        yield lifetime
