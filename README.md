Jupyter Notebooks
=================

Collection of random experiments

* [01 Collect Slicer Dashboard Stats.ipynb](http://nbviewer.jupyter.org/github/jcfr/jupyter-notebooks/blob/master/01%20Collect%20Slicer%20Dashboard%20Stats.ipynb)

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

