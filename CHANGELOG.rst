Changelog
=========

Upcoming release
----------------

- Prevent ``AttributeError`` when trying to humanize ``None`` value (`#6`_),
  thanks to `@earlbread`_ for the report.

.. _#6: https://github.com/vitalk/flask-humanize/pull/6
.. _@earlbread: https://github.com/earlbread

0.3.0 (2016-03-26)
------------------

- ``PyPI`` package has been renamed into ``Flask-Humanize`` (`#4`_). Thanks to
  `@singingwolfboy`_, `@eg0r`_ and `@egorsmkv`_.

.. _#4: https://github.com/vitalk/flask-humanize/issues/4
.. _@singingwolfboy: https://github.com/singingwolfboy
.. _@egorsmkv: https://github.com/egorsmkv
.. _@eg0r: https://github.com/eg0r

0.2.0 (2016-01-25)
------------------

- Support UTC time. Thanks to `@diginikkari`_ for the complete PR (`#2`_).

.. _#2: https://github.com/vitalk/flask-humanize/pull/2
.. _@diginikkari: https://github.com/diginikkari

0.1.0 (2015-11-04)
------------------

- Set package status to beta.

- Unset locale after each request.

- Fix compatibility with python 2.6 version.

- Add test suite; use ``pytest-flask`` for testing.

0.0.1 (2015-10-29)
------------------

First release on PyPi.
