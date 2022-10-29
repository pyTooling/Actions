StaticTypeCheck
###############

collect static type check result with `mypy`, and
    optionally upload results as an HTML report.
    Example `commands`:

    1. Regular package

      ```yml
      commands: mypy --html-report htmlmypy -p ToolName
      ```

    2. Parent namespace package

      ```yml
      commands: |
        touch Parent/__init__.py
        mypy --html-report htmlmypy -p ToolName
      ```

    3. Child namespace package

      ```yml
      commands: |
        cd Parent
        mypy --html-report ../htmlmypy -p ToolName
      ```

Instantiation
*************

Simple Example
==============

.. code-block:: yaml

   TBD

Complex Example
===============



.. code-block:: yaml

   TBD

Template Parameters
*******************

TBD 1
=====

TBD

TBD 1
=====

TBD

Template Results
****************

*None*
