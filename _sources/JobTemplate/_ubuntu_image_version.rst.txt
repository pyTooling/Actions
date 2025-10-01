ubuntu_image_version
====================

:Type:            string
:Required:        no
:Default Value:   ``'24.04'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
                  for available Ubuntu image versions.
:Description:     Version of the Ubuntu image used to run the job.

                  .. note::

                     Unfortunately, GitHub Actions has only a `limited set of functions <https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#functions>`__,
                     thus, the usual Ubuntu image name like ``'ubuntu-24.04'`` can't be split into image name and image
                     version.
