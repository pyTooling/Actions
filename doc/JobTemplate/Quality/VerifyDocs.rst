.. _JOBTMPL/VerifyDocs:
.. index::
   single: GitHub Action Reusable Workflow; VerifyDocs Template

VerifyDocs
##########

The ``VerifyDocs`` job template checks that the first Python code example in :file:`README.md` still runs against the
current code. A broken example is a documentation defect the test suite cannot catch, because the example lives in
Markdown and is never imported by the tests.

.. topic:: Features

   * Install the package from the checked out sources, so the example runs against the branch and not against a
     released version.
   * Extract the first ``py`` or ``python`` fenced code block from :file:`README.md`.
   * Execute the extracted snippet and fail the job if it raises.

.. topic:: Behavior

   1. Checkout repository.
   2. Setup Python.
   3. Install the package from the checked out sources using ``pip3 install .``.
   4. Extract the first Python code block from :file:`README.md` and write it to :file:`tests/docs/example.py`.
   5. Print the extracted snippet into the job log, so a failure can be understood without reproducing it locally.
   6. Run the snippet with :file:`tests/docs` as working directory.

   .. attention::

      The job requires an existing :file:`tests/docs` directory, and it fails if :file:`README.md` contains no Python
      code block at all.

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`actions/setup-python`


.. _JOBTMPL/VerifyDocs/Instantiation:

Instantiation
*************

The following instantiation example creates a ``VerifyDocs`` job derived from job template ``VerifyDocs`` version
``@r7``.

.. code-block:: yaml

   jobs:
     VerifyDocs:
       uses: pyTooling/Actions/.github/workflows/VerifyDocs.yml@r7
       with:
         python_version: '3.14'


.. seealso::

   :ref:`JOBTMPL/CheckDocumentation`
     Checks how much of the API carries doc-strings, while ``VerifyDocs`` checks that the documented example works.


.. _JOBTMPL/VerifyDocs/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/VerifyDocs/Inputs>`

+------------------------------------------------------+----------+--------+-------------+
| Parameter Name                                       | Required | Type   | Default     |
+======================================================+==========+========+=============+
| :ref:`JOBTMPL/VerifyDocs/Input/ubuntu_image_version` | no       | string | ``'26.04'`` |
+------------------------------------------------------+----------+--------+-------------+
| :ref:`JOBTMPL/VerifyDocs/Input/python_version`       | no       | string | ``'3.14'``  |
+------------------------------------------------------+----------+--------+-------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/VerifyDocs/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/VerifyDocs/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/VerifyDocs/Inputs:

Input Parameters
****************

.. _JOBTMPL/VerifyDocs/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/VerifyDocs/Input/python_version:

.. include:: ../_python_version.rst


.. _JOBTMPL/VerifyDocs/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/VerifyDocs/Outputs:

Outputs
*******

This job template has no output parameters.
