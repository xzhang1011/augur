Testing database
=================

.. warning::

    **THIS SECTION IS CURRENTLY UNDER CONSTRUCTION.**
    Docs may be missing or inaccurate.
    If you have questions or would like to help please open an issue on GitHub_.

.. _GitHub: https://github.com/chaoss/augur/issues

The testing database is updated with each new release of Augur that updates the database schema. It is built by running a full collection against ``chaoss/augur`` (this project), then dumping the database into a regular PostgreSQL container. The default credentials are::

  host: "localhost"
  name: "test_data"
  port: 5432
  user: "augur"
  password: "augur"
