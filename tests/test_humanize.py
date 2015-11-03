#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from flask import url_for
from flask_humanize.compat import text_type


def b(string):
    return string.encode('utf-8') if isinstance(string, text_type) else string


class TestInit:

    def test_register_themself(self, app, h):
        assert app.extensions['humanize'] is h

    def test_register_before_request_callback(self, app, h):
        assert h._set_locale in app.before_request_funcs[None]

    def test_register_after_request_callback(self, app, h):
        assert h._unset_locale in app.after_request_funcs[None]

    def test_register_template_filter(self, app, h):
        assert h._humanize in app.jinja_env.filters.values()


class TestHumanize:

    def test_naturalday(self, client):
        assert client.get(url_for('naturalday')).data == b'today'

    def test_naturaltime(self, client):
        assert client.get(url_for('naturaltime')).data == b'now'

    def test_naturaldelta(self, client):
        assert client.get(url_for('naturaldelta')).data == b'7 days'

    def test_naturaldate(self, client):
        assert client.get(url_for('naturaldate')).data == b'Apr 21 1987'


class TestL10N:

    def test_locale_selector(self, client, h):
        @h.localeselector
        def get_locale():
            return 'ru_RU'

        assert client.get(url_for('naturalday')).data == b(u'сегодня')
        assert client.get(url_for('naturaltime')).data == b(u'сейчас')
        assert client.get(url_for('naturaldelta')).data == b(u'7 дней')

    @pytest.mark.options(humanize_default_locale='ru_RU')
    def test_default_locale(self, client):
        assert client.get(url_for('naturaltime')).data == b(u'сейчас')

    def test_fallback_to_default_if_no_translations_for_locale(self, client, h):
        @h.localeselector
        def get_locale():
            return 'tlh'

        assert client.get(url_for('naturaltime')).data == b'now'
