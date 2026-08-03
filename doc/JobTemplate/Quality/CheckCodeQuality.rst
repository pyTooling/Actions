.. _JOBTMPL/CheckCodeQuality:
.. index::
   single: Bandit; CheckCodeQuality Template
   single: pylint; CheckCodeQuality Template
   single: radon; CheckCodeQuality Template
   single: GitHub Action Reusable Workflow; CheckCodeQuality Template

CheckCodeQuality
################

The ``CheckCodeQuality`` job template runs three independent code quality checks on the package sources:

* security scanning with :term:`bandit`,
* code metrics and complexity with :term:`radon`, and
* linting with :term:`pylint`.

Each check is a separate job with its own enable parameter, so a repository can adopt them one at a time. All three are
disabled by default in :ref:`JOBTMPL/CompletePipeline`, because an established code base rarely passes linting on the
first run.

.. topic:: Features

   * Static Application Security Testing (SAST) using :term:`bandit`, published as a report page in the pipeline
     summary when findings exist.
   * Raw code metrics, cyclomatic complexity, Halstead complexity metrics and the maintainability index using
     :term:`radon`.
   * Code linting using :term:`pylint`.
   * Each check can be enabled or disabled independently.

.. topic:: Behavior

   The template defines three independent jobs, which run in parallel:

   ``Bandit`` - enabled by :ref:`JOBTMPL/CheckCodeQuality/Input/bandit`

   1. Checkout repository.
   2. Setup Python (:ref:`JOBTMPL/CheckCodeQuality/Input/python_version`) and install :term:`bandit`.
   3. Run the security scan over :ref:`JOBTMPL/CheckCodeQuality/Input/package_directory`.
   4. Publish the findings as a report page using :term:`Test Reporter` - only when the scan found something.

   ``Radon`` - enabled by :ref:`JOBTMPL/CheckCodeQuality/Input/radon`

   1. Checkout repository.
   2. Setup Python (:ref:`JOBTMPL/CheckCodeQuality/Input/python_version`) and install :term:`radon`.
   3. Report raw code metrics.
   4. Report cyclomatic complexity.
   5. Report Halstead complexity metrics.
   6. Report the maintainability index.

   .. note::

      The *Radon* job writes its results into the job log only. There is no artifact and no threshold, so the job
      cannot fail on a bad metric - it is informational.

   ``PyLint`` - enabled by :ref:`JOBTMPL/CheckCodeQuality/Input/pylint`

   1. Checkout repository.
   2. Setup Python (:ref:`JOBTMPL/CheckCodeQuality/Input/python_version`) and install :term:`pylint` as well as the
      package's own dependencies (:ref:`JOBTMPL/CheckCodeQuality/Input/requirements`), because the linter imports the
      code it checks.
   3. Run the linter over :ref:`JOBTMPL/CheckCodeQuality/Input/package_directory`.

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`actions/setup-python`
   * :gh:`dorny/test-reporter`
   * pip

     * :term:`bandit` (:pypi:`PyPI package <bandit>`)
     * :term:`radon` (:pypi:`PyPI package <radon>`)
     * :term:`pylint` (:pypi:`PyPI package <pylint>`)
     * Python packages specified via :ref:`JOBTMPL/CheckCodeQuality/Input/requirements` parameter (``PyLint`` job
       only).


.. _JOBTMPL/CheckCodeQuality/Instantiation:

Instantiation
*************

The following instantiation example creates a ``CodeQuality`` job derived from job template ``CheckCodeQuality``
version ``@r7``. The package directory comes from :ref:`JOBTMPL/Parameters`, so that job is a dependency.

.. code-block:: yaml

   jobs:
     Params:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r7
       with:
         package_name: myPackage

     CodeQuality:
       uses: pyTooling/Actions/.github/workflows/CheckCodeQuality.yml@r7
       needs:
         - Params
       with:
         python_version:    ${{ needs.Params.outputs.python_version }}
         package_directory: ${{ needs.Params.outputs.package_directory }}
         artifact:          ${{ fromJson(needs.Params.outputs.artifact_names).codequality }}
         bandit:            'true'
         radon:             'true'
         pylint:            'false'


.. seealso::

   :ref:`JOBTMPL/CheckDocumentation`
     Checks documentation coverage rather than code quality.
   :ref:`JOBTMPL/StaticTypeCheck`
     Checks type annotations using mypy.


.. _JOBTMPL/CheckCodeQuality/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/CheckCodeQuality/Inputs>`

+------------------------------------------------------------+----------+--------+---------------------------+
| Parameter Name                                             | Required | Type   | Default                   |
+============================================================+==========+========+===========================+
| :ref:`JOBTMPL/CheckCodeQuality/Input/ubuntu_image_version` | no       | string | ``'26.04'``               |
+------------------------------------------------------------+----------+--------+---------------------------+
| :ref:`JOBTMPL/CheckCodeQuality/Input/python_version`       | no       | string | ``'3.14'``                |
+------------------------------------------------------------+----------+--------+---------------------------+
| :ref:`JOBTMPL/CheckCodeQuality/Input/package_directory`    | yes      | string | — — — —                   |
+------------------------------------------------------------+----------+--------+---------------------------+
| :ref:`JOBTMPL/CheckCodeQuality/Input/artifact`             | yes      | string | — — — —                   |
+------------------------------------------------------------+----------+--------+---------------------------+
| :ref:`JOBTMPL/CheckCodeQuality/Input/requirements`         | no       | string | ``'-r requirements.txt'`` |
+------------------------------------------------------------+----------+--------+---------------------------+
| :ref:`JOBTMPL/CheckCodeQuality/Input/bandit`               | no       | string | ``'true'``                |
+------------------------------------------------------------+----------+--------+---------------------------+
| :ref:`JOBTMPL/CheckCodeQuality/Input/radon`                | no       | string | ``'true'``                |
+------------------------------------------------------------+----------+--------+---------------------------+
| :ref:`JOBTMPL/CheckCodeQuality/Input/pylint`               | no       | string | ``'true'``                |
+------------------------------------------------------------+----------+--------+---------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/CheckCodeQuality/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/CheckCodeQuality/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/CheckCodeQuality/Inputs:

Input Parameters
****************

.. _JOBTMPL/CheckCodeQuality/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/CheckCodeQuality/Input/python_version:

.. include:: ../_python_version.rst


.. _JOBTMPL/CheckCodeQuality/Input/package_directory:

package_directory
=================

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Any path relative to the repository root.
:Description:     Directory containing the package sources to be checked. |br|
                  Usually taken from :ref:`JOBTMPL/Parameters/Output/package_directory`.


.. _JOBTMPL/CheckCodeQuality/Input/artifact:

artifact
========

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Any valid artifact name.
:Description:     Name of the package artifact.

                  .. note::

                     The template currently does not reference this parameter. It is kept because it is declared
                     ``required: true`` and removing it would break consumers that pass it.


.. _JOBTMPL/CheckCodeQuality/Input/requirements:

requirements
============

:Type:            string
:Required:        no
:Default Value:   ``'-r requirements.txt'``
:Possible Values: Any valid list of parameters for ``pip install``.
:Description:     Python dependencies to be installed through *pip*.


.. _JOBTMPL/CheckCodeQuality/Input/bandit:

bandit
======

:Type:            string
:Required:        no
:Default Value:   ``'true'``
:Possible Values: ``'true'`` / ``'false'``
:Description:     Run the *Bandit* job performing Static Application Security Testing (SAST).


.. _JOBTMPL/CheckCodeQuality/Input/radon:

radon
=====

:Type:            string
:Required:        no
:Default Value:   ``'true'``
:Possible Values: ``'true'`` / ``'false'``
:Description:     Run the *Radon* job reporting code metrics, complexity and maintainability.


.. _JOBTMPL/CheckCodeQuality/Input/pylint:

pylint
======

:Type:            string
:Required:        no
:Default Value:   ``'true'``
:Possible Values: ``'true'`` / ``'false'``
:Description:     Run the *PyLint* job performing code linting.


.. _JOBTMPL/CheckCodeQuality/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/CheckCodeQuality/Outputs:

Outputs
*******

This job template has no output parameters.
