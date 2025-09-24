.. _ACTION:
.. index::
   single: GitHub Action

Overview
########

The following 2 actions are provided by **Actions**:

.. include:: Actions.rst


.. _ACTION/Instantiation:
.. index::
   single: GitHub Action; Instantiation

Instantiation
*************

.. code-block:: yaml

   jobs:
     <JobName>:
       steps:
         - ...

         - name: <Name>
           uses: ./with-post-step
           with:
             <Param1>: <Value1>
             <Param2>: <Value2>
