# ----------------------------------------------------------------------------
# Copyright (c) 2017-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

# from ._format import MetadataFormat, MetadataDirectoryFormat
# from ._type import MetadataX

from ._tabulate import tabulate
from ._distance import distance_matrix
from ._normalize import normalize
from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

__all__ = ['tabulate', 'distance_matrix', 'normalize']