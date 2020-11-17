Testing
===============

.. warning::

    **THIS SECTION IS CURRENTLY UNDER CONSTRUCTION.**
    Docs may be missing or inaccurate.
    If you have questions or would like to help please open an issue on GitHub_.

.. _GitHub: https://github.com/chaoss/augur/issues

Augur's core testing infrastructure consists of 4 key components:

1. A testing database packaged as a Docker container
2. Unit tests, written using pytest_
3. tox_ configuration
4. `Travis CI`_ configuration

.. _pytest: https://docs.pytest.org/en/latest/
.. _tox: https://tox.readthedocs.io/en/latest/
.. _Travis CI: https://travis-ci.org/

These 4 components are used to build a reproducible and thorough testing suite for Augur. Each of the respective pages will talk in detail about the mechanics of each components, but first a brief explanation of how they are used together. The unit tests are the core of the testing infrastructure, and are written using ``pytest``. They can either be run directly, or as part of a larger test suite using ``tox``. Travis CI uses the ``tox`` suites and the testing database to check each build.

There is additional testing infrastructure in place for the documentation and Docker builds, but these are secondary to the unit tests.

.. toctree::

   unit-tests
   tox
   travis
   dataset
