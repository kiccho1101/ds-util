# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ds_util', 'ds_util.tests']

package_data = \
{'': ['*']}

install_requires = \
['mecab-python3>=1.0.3,<2.0.0',
 'numpy>=1.20.3,<2.0.0',
 'pandas>=1.2.4,<2.0.0',
 'psutil>=5.8.0,<6.0.0',
 'scikit-learn>=0.24.2,<0.25.0',
 'torch>=1.8.1,<2.0.0']

setup_kwargs = {
    'name': 'ds-util',
    'version': '0.2.1',
    'description': 'Util scripts for data science projects and Kaggle.',
    'long_description': None,
    'author': 'kiccho1101',
    'author_email': 'youodf11khp@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
