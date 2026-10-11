.. # Load pre-defined aliases and graphical characters like © from docutils
   # <file> is used to denote the special path
   # <Python>\Lib\site-packages\docutils\parsers\rst\include
.. include:: <isonum.txt>
.. include:: <mmlalias.txt>

.. # |degree|, |br| and |hr|, the style roles and :pycode: are registered by the
   # 'pyTooling.Sphinx' extension, so they are declared once for every project instead of being
   # copied into each one's prolog.

.. role:: bashcode(code)
   :language: bash
   :class: highlight

.. role:: jsoncode(code)
   :language: json
   :class: highlight
