# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 14:49:13 2023

@author: cvskf
"""
import unittest

import csvw_functions
import csvw_functions_extra 
import os

fp_table_group_metadata='extra_tables-metadata.json'

class EXTRA(unittest.TestCase):
    ""
        
        
    def _test_download_table_group(self):
        ""
        
        csvw_functions_extra.download_table_group(
            metadata_document_location=fp_table_group_metadata,
            data_folder='_data',
            csv_file_name='Local_Authority_District_to_Region_December_2022.csv',
            overwrite_existing_files=True,
            verbose=True
            )
        
        
    def test_import_table_group_to_sqlite(self):
        ""
        
        csvw_functions_extra.import_table_group_to_sqlite(
            '_data\extra_tables-metadata.json',
            data_folder='_data',
            database_name='data.sqlite',
            csv_file_name='Local_Authority_District_to_Region_December_2022.csv',
            remove_existing_tables=True,
            verbose=True
            )
        
        
        
if __name__=="__main__":
    
    unittest.main()

