# ----------------------------------------------------------------------------
# Copyright (c) 2016-2020, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


def get_intersection(variables_rules: list, md_columns: list) -> list:
    """
    Get the names of the metadata variables that have associated rules.

    Parameters
    ----------
    variables_rules : list
        Names of variables that have associated rules.
    md_columns : list
        Names of the variables in the metadata table.

    Returns
    -------
    intersection : list
       Metadata variables that have associated rules.
    """
    intersection = set(variables_rules) & set(md_columns)
    if not len(intersection):
        raise ValueError(
            "No metadata columns associated with yaml rules."
        )
    return sorted(intersection)


def get_variables_rules_dir(rules_dir: str, RULES: str) -> str:
    """
    Get the path to the folder where
    the .yml rules files are located.

    TEMPORARY FUNCTION TO PASS THE DEFAULT FOLDER CONTAINING OUR 8 RULES
    (A REAL USER SHOULD PASS ANOTHER FOLDER LOCATION TO '--p-rules-dir')

    Parameters
    ----------
    rules_dir : str
        Path passed on command.

    Returns
    -------
        Folder path.
    """
    variables_rules_dir = str(rules_dir)
    if not variables_rules_dir:
        variables_rules_dir = RULES
    return variables_rules_dir

