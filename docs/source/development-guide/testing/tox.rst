Tox
==========================

.. warning::

    **THIS SECTION IS CURRENTLY UNDER CONSTRUCTION.**
    Docs may be missing or inaccurate.
    If you have questions or would like to help please open an issue on GitHub_.

.. _GitHub: https://github.com/chaoss/augur/issues

Augur uses ``tox`` to manage its test suites. Once the ``pytest`` cases have been written, they should be added to a test suite (if they have not been added to another already) in the ``tox.ini`` file in the root directory. ``tox`` will pass all environment variables prefixed with ``AUGUR_`` to the shell where it runs the tests, and also sets some defaults for logging and ``pytest`` reporting.