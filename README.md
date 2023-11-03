# csvw_functions_extra
Python functions for CSVW files providing extra functionality beyond the CSVW standards

## Installation

`pip install git+https://github.com/stevenkfirth/csvw_functions_extra`

The python package [`csvw_functions`](https://github.com/stevenkfirth/csvw_functions) will also need to be installed.

## API

### download_table_group

Description: Reads a CSVW metadata file and downloads the CSV files from remote locations. This makes use of the [https://purl.org/berg/csvw_functions_extra](#CSVW-vocabulary) vocabulary. 

Method (for individual CSV files):

1. For each table in the TableGroup object, the CSV file is downloaded using the url in `https://purl.org/berg/csvw_functions_extra/vocab/csv_download_url`.
2. The CSV is saved in the `data_folder` using the filename in `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name`
3. If the CSV file has an associated metadata file, this is downloaded using the url in `https://purl.org/berg/csvw_functions_extra/vocab/metadata_download_url`
4. If step 3 occurs, the associated metadata file is saved in the `data_folder` using the filename in `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name` with the additional suffix in `https://purl.org/berg/csvw_functions_extra/vocab/metadata_file_suffix`.

Method (for ZIP files):

1. 


Call signature:

```python
download_table_group(
        metadata_document_location,
        data_folder,
        csv_file_name=None,  
        overwrite_existing_files=False,
        verbose=False
        )
```

Arguments:
- **metadata_document_location** *(str)*: The filepath or url of the CSVW metadata file containing a Table Group object.
- **data_folder** *(str)*: The filepath of a local folder where the downloaded CSV data is to be saved to.
- **csv_file_names** *(str or list)*: The csv_file_name values of the tables to be downloaded. If None then all tables are downloaded.
- **overwrite_existing_files** *(bool)*: If True, then any existing CSV files in data_folder will be overwritten. If False, then no download occurs if there is an existing CSV file in data_folder.
- **verbose** *(bool)*: If True, then this function prints intermediate variables and other useful information.

Returns: The local filename of the updated CSVW metadata file containing the new URLs for the newly downloaded tables.

Return type: *str*


### import_table_group_to_sqlite

Description: Reads a CSVW metadata file and imports the CSV data into a SQLite database. This makes use of the [https://purl.org/berg/csvw_functions_extra](##CSVW-vocabulary) vocabulary.

Method:

1. If not already present, a SQLite database named `database_name` is created in the `data_folder`.
2. For each table in the TableGroup object, the local CSV file is located in the `data_folder` using `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name`.
3. The CSV file is imported into the SQLite database into a table named using `https://purl.org/berg/csvw_functions_extra/vocab/sql_table_name`. 

Call signature:

```python
import_table_group_to_sqlite(
        metadata_document_location,
        data_folder,
        database_name,
        csv_file_name=None, 
        remove_existing_tables=False,
        verbose=False
```

Arguments:
- **metadata_document_location** *(str)*: The local filename of the csvw metadata file containing a Table Group object. This could be the filename returned by the [download_table_group](#download_table_group) function.
- **data_folder** *(str)*: The filepath of a local folder where the downloaded CSV data is located and the SQLite database is stored.
- **database_name** *(str)*: The name of the SQLite database, relative to the data_folder.
- **csv_file_names** *(str or list)*: The csv_file_name values of the tables to be imported. If None then all CSV files are imported.
- **overwrite_existing_tables** *(bool)*: If True, then before importing the CSV data any associated existing table in the database is removed and recreated.
- **verbose (bool)**: If True, then this function prints intermediate variables and other useful information.

Returns: None


## CSVW vocabulary

### Vocabulary on CSVW column metadata objects

- `https://purl.org/berg/csvw_functions_extra/vocab/sqlsetindex`: Boolean. If `true` then an SQLite index is set up on this column when the data is imported into the database.

### Vocabulary on CSVW table metadata objects

- `https://purl.org/berg/csvw_functions_extra/vocab/csv_download_url`: The url where the remote CSV file can be downloaded from.

- `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name`: The name for the newly downloaded CSV file.

- `https://purl.org/berg/csvw_functions_extra/vocab/metadata_download_url`: The url where an associated metadata file for the CSV file can be downloaded from.

- `https://purl.org/berg/csvw_functions_extra/vocab/metadata_file_suffix`: A suffix to use when saving the associated metadata file.

- `https://purl.org/berg/csvw_functions_extra/vocab/sql_table_name`: The name to be used for the database table when importing the CSV file into a SQLite database.
            
