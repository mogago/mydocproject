=============================
Usando el tema RTD localmente 
=============================

Para usar el `tema de Read the Docs`_ de `forma local`_ debemos seguir los pasos descritos en cualquiera de los siguientes dos enlaces:

- https://github.com/readthedocs/sphinx_rtd_theme
- https://sphinx-rtd-theme.readthedocs.io/en/latest/

.. _tema de Read the Docs: https://sphinx-rtd-theme.readthedocs.io/en/latest/
.. _forma local: https://docs.readthedocs.io/en/stable/faq.html#i-want-to-use-the-read-the-docs-theme-locally

1. Habiendo instalado ``sphinx-rtd-theme``, agregar al archivo ``docs/source/conf.py`` la extensión ``sphinx_rtd_theme``:

.. code-block:: python

    import sphinx_rtd_theme

    extensions = [
        ...
        "sphinx_rtd_theme",
    ]

    html_theme = "sphinx_rtd_theme"


2. Desde el directorio ``docs/`` actualizar los archivos html:

.. code-block:: bash

    make html

3. Abrir la página ``index.html`` para comprobar que se haya actualizado el tema localmente:

.. figure:: images/11_rtd-theme-local.png
   :align: center

   Tema de Read the Docs locamente
