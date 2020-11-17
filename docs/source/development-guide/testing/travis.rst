Travis CI
==========================

.. warning::

    **THIS SECTION IS CURRENTLY UNDER CONSTRUCTION.**
    Docs may be missing or inaccurate.
    If you have questions or would like to help please open an issue on GitHub_.

.. _GitHub: https://github.com/chaoss/augur/issues

The Travis CI configuration can be found in the ``.travis.yml`` file in the root of the repository. It runs both the metrics and API tox suites in Python 3.6, 3.7, and 3.8. It uses the same testing dataset; the Docker container is started inside the Travis VM before the tests run, which means that all incoming PRs have access to the test data.