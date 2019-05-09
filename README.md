Jupyter Notebooks
=================

Collection of random experiments

* [01_Collect_Slicer_Dashboard_Stats.ipynb](http://nbviewer.jupyter.org/github/jcfr/jupyter-notebooks/blob/master/01_Collect_Slicer_Dashboard_Stats.ipynb)
* [02_Update_Slicer_CLI_buildsystem_to_download_test_data_from_midas.ipynb](http://nbviewer.jupyter.org/github/jcfr/jupyter-notebooks/blob/master/02_Update_Slicer_CLI_buildsystem_to_download_test_data_from_midas.ipynb)
* [05_SlicerStartupTimes.ipynb](http://nbviewer.jupyter.org/github/jcfr/jupyter-notebooks/blob/master/05_SlicerStartupTimes.ipynb)
* [26_Slicer_Licenses.ipynb](http://nbviewer.jupyter.org/github/jcfr/jupyter-notebooks/blob/master/26_Slicer_Licenses.ipynb)
* [27_Slicer_Mailing_Lists.ipynb](http://nbviewer.jupyter.org/github/jcfr/jupyter-notebooks/blob/master/27_Slicer_Mailing_Lists.ipynb)

Prerequisites
-------------

* Install [git](https://git-scm.com/)
* Install [docker](https://docs.docker.com/engine/installation/)

Usage
-----

```
git clone git://github.com/jcfr/jupyter-notebooks.git
cd jupyter-notebooks
docker run -P -v $(pwd):/home/jovyan/work -d -p 8888:8888 jupyter/scipy-notebook start-notebook.sh
xdg-open http://127.0.0.1:8888
```

Licensing
---------

All software is licensed under the Apache 2.0 License. See LICENSE_Apache_20 file for details.

All Works of Art are licensed under the Creative Commons Attribution-ShareAlike 4.0.
See LICENSE_CC_BY_SA_40 file for details.

