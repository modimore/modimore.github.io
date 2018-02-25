Title: BreezeBlocks
Date: 2018-02-18
Tags: Programming, Python, SQL

BreezeBlocks is a Python package for RDBMS-independent SQL generation. From
Python objects representing the schema of a database, you can build and execute
queries and other statements.

Compared to other packages that meet a similar need, BreezeBlocks follows more
of an Active Statement model than and Active Record model. A SQL statement's
representation has an execute method that will handle the details of getting a
database connection and managing a transaction. The user should only need to
be responsible for shaping the statement the way they want.

The source code is available on [GitHub][github], the documentation is on
[Read the Docs][rtd], and it is available to download from [PyPi][pypi].

[github]: https://github.com/modimore/BreezeBlocks
[pypi]: https://pypi.python.org/pypi/breezeblocks/
[rtd]: https://breezeblocks.readthedocs.io/en/latest
