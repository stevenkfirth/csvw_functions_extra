# csvw_functions_extra
Python functions for CSVW files providing extra functionality beyond the CSVW standards

## Installation

`pip install git+https://github.com/stevenkfirth/csvw_functions_extra`

The python package [`csvw_functions`](https://github.com/stevenkfirth/csvw_functions) will also need to be installed.

## API

### get_normalized_metadata_table_group_dict

Description: Returns a normalized version of a CSVW metadata file.

```python
get_normalized_metadata_table_group_dict(
        metadata_document_location
        )
```
- **metadata_document_location** *(str)*: The filepath or url of the CSVW metadata file containing a Table Group object.

Returns: A dictionary of the normalized CSVW Table Group object.


### get_available_csv_file_names

Description: Returns the CSV file names of all tables in a CSVW metadata file.

```python
csvw_extra_functions.get_available_csv_file_names(
        metadata_document_location
)
```
- **metadata_document_location** *(str)*: The filepath or url of the CSVW metadata file containing a Table Group object.

Returns: A list of the `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name` value in each table.


### download_table_group

Description: Reads a CSVW metadata file and downloads the CSV files from remote locations. This makes use of the [https://purl.org/berg/csvw_functions_extra](#CSVW-vocabulary) vocabulary. 

```python
download_table_group(
        metadata_document_location,
        data_folder,
        csv_file_names=None,  
        overwrite_existing_files=False,
        verbose=False
        )
```

Method (for individual CSV files):

1. For each table in the TableGroup object, the CSV file is downloaded using the url in `https://purl.org/berg/csvw_functions_extra/vocab/csv_download_url`.
2. The CSV is saved in the `data_folder` using the filename in `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name`
3. If the CSV file has an associated metadata file, this is downloaded using the url in `https://purl.org/berg/csvw_functions_extra/vocab/metadata_download_url`
4. If step 3 occurs, the associated metadata file is saved in the `data_folder` using the filename in `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name` with the additional suffix in `https://purl.org/berg/csvw_functions_extra/vocab/metadata_file_suffix`.
5. A new version of the CSVW metadata file is also saved in the data folder.

Method (for ZIP files):

1. 






Arguments:
- **metadata_document_location** *(str)*: The filepath or url of the CSVW metadata file containing a Table Group object.
- **data_folder** *(str)*: The filepath of a local folder where the downloaded CSV data is to be saved to.
- **csv_file_names** *(str or list)*: The csv_file_name values of the tables to be downloaded. If None then all tables are downloaded.
- **overwrite_existing_files** *(bool)*: If True, then any existing CSV files in data_folder will be overwritten. If False, then no download occurs if there is an existing CSV file in data_folder.
- **verbose** *(bool)*: If True, then this function prints intermediate variables and other useful information.

Returns: The local filename of the updated CSVW metadata file containing the new URLs for the newly downloaded tables.

Return type: *str*


### get_metadata_table_group_dict

Description: Returns a CSVW metadata Table Group object.

```python
get_metadata_table_group_dict(
        data_folder,
        metadata_filename
        )
```

Arguments:
- **metadata_filename** *(str)*: The filename of a CSVW metadata file which has been created by the [`download_table_group`](#download_table_group) method and is located in the data folder.

Returns: A dictionary of the CSVW Table Group object.


### get_metadata_table_dict

```python
get_metadata_table_dict(
        sql_table_name,
        metadata_table_group_dict=None,
        data_folder=None,
        metadata_filename=None
        )
```


### get_metadata_column_dict

```python
get_metadata_column_dict(
        column_name,
        table_name,
        metadata_table_group_dict=None,
        data_folder=None,
        metadata_filename=None
        )
```

### get_metadata_sql_table_names

```python
get_metadata_sql_table_names(
        metadata_table_group_dict=None,
        data_folder=None,
        metadata_filename=None
        )
```


### get_metadata_columns_codes

```python
get_metadata_columns_codes(
        column_names,
        table_name,
        metadata_table_group_dict = None,
        data_folder = None,
        metadata_filename=None
        )
```


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
        csv_file_names=None, 
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


### add_index

```python
add_index(
        fields,
        table_name,
        data_folder,
        database_name,
        unique=False,
        verbose=False
        )
```

### convert_to_iterator

```python
convert_to_iterator(
        x
        )
```

### get_table_names_in_database

```python
get_table_names_in_database(
        data_folder,
        database_name        
        )
```


### get_sql_table_names_in_database

```python
get_sql_table_names_in_database(
        data_folder,
        database_name,
        )
```

Returns: A list ...

### get_where_clause_list

```python
get_where_clause_list(
        d
        )
```

### run_sql

```python
run_sql(
        sql_query,
        data_folder,
        database_name,
        verbose=False
        )
```




## CSVW vocabulary

### Vocabulary on CSVW column metadata objects

- `https://purl.org/berg/csvw_functions/vocab/codes`: (JSON object) An object (dictionary) relating any codes using in the column data to a string with the meaning of the codes. 

- `https://purl.org/berg/csvw_functions/vocab/column_notes`: (string) A description of the contents of the column.

- `https://purl.org/berg/csvw_functions_extra/vocab/sqlsetindex`: Boolean. If `true` then an SQLite index is set up on this column when the data is imported into the database.

### Vocabulary on CSVW table metadata objects

- `https://purl.org/berg/csvw_functions_extra/vocab/csv_download_url`: The url where the remote CSV file can be downloaded from.

- `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name`: The name for the newly downloaded CSV file.

- `https://purl.org/berg/csvw_functions_extra/vocab/metadata_download_url`: The url where an associated metadata file for the CSV file can be downloaded from.

- `https://purl.org/berg/csvw_functions_extra/vocab/metadata_file_suffix`: A suffix to use when saving the associated metadata file.

- `https://purl.org/berg/csvw_functions_extra/vocab/sql_table_name`: The name to be used for the database table when importing the CSV file into a SQLite database.
            
