Unit tests
===============

.. warning::

    **THIS SECTION IS CURRENTLY UNDER CONSTRUCTION.**
    Docs may be missing or inaccurate.
    If you have questions or would like to help please open an issue on GitHub_.

All unit tests are written using the pytest_ framework. They are located in the ``tests/`` folder, and are further split up into subdirectories for metrics (``test_metrics``), API routes (``test_routes``), and workers (``workers``). More test files or directories can be added as needed.

Metrics
--------
The metrics should test both the repo and repo group version of the metric, and should use the default repo group ID (``10``) and the default repo ID (``25430``) when querying the database. The tests themselves should just check that it returns some actual data (i.e. the length of the response is > 0), as writing unit tests for the theoretical "correctness" of a metric's calculation is currently outside the scope of the tests.

Routes
-------
API routes, similarly to the regular unit tests, should use the default repo group ID and repo ID. In the same vein, they should also just test for a 200 response code (no error) and that the length of the response is > 0; since we are already testing the metrics themselves as well, these tests primarily serve to check the endpoint creation logic is intact and that the server works correctly.

There is a file called ``runner.py`` in ``test_routes/`` that is responsible for starting and stopping the backend server. It's used in conjunction with Tox, so you should not run this file directly and instead should use the Tox suite for the API tests.

Workers
--------
There are not any worker tests at the current moment, simply due to lack of bandwidth to work on them. There is a prototype of an extremly simple worker test for the repo info worker; we recommend using this as a starting point.

.. _GitHub: https://github.com/chaoss/augur/issues
.. _pytest: https://docs.pytest.org/en/latest/