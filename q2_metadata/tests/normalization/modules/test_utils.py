# ----------------------------------------------------------------------------
# Copyright (c) 2017-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest
from q2_metadata.normalization._norm_utils import get_intersection


class NormalizationUtilsTests(unittest.TestCase):

    def test_get_intersection(self):

        err_message = 'No metadata columns associated with yaml rules.'

        with self.assertRaises(ValueError) as val_err:
            get_intersection([], ['something'])
        message = str(val_err.exception)
        self.assertEqual(message, err_message)

        with self.assertRaises(ValueError) as val_err:
            get_intersection(['a'], ['b'])
        message = str(val_err.exception)
        self.assertEqual(message, err_message)

        intersect = get_intersection(['a', 'b', 'c'], ['a', 'b', 'd'])
        self.assertEqual(intersect, ['a', 'b'])


if __name__ == '__main__':
    unittest.main()
