# -*- coding: utf-8 -*-
"""Test Module for sphinx_rtd_theme."""


class Foo:

    """Docstring for class Foo.

    This text tests for the formatting of docstrings generated from output
    ``sphinx.ext.autodoc``. Which contain reST, but sphinx nests it in the
    ``<dl>``, and ``<dt>`` tags. Also, ``<tt>`` is used for class, method names
    and etc, but those will *always* have the ``.descname`` or
    ``.descclassname`` class.

    Normal ``<tt>`` (like the <tt> I just wrote here) needs to be shown with
    the same style as anything else with ````this type of markup````.

    It's common for programmers to give a code example inside of their
    docstring::

        from test_py_module import Foo

        myclass = Foo()
        myclass.dothismethod('with this argument')
        myclass.flush()

        print(myclass)


    Here is a link to :py:meth:`capitalize`.
    Here is a link to :py:meth:`__init__`.

    """

    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    bar = 1

    flox = 1.5   #: Doc comment for Foo.flox. One line only.

