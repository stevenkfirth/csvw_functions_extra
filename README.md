# csvw_functions_extra
Python functions for CSVW files providing extra functionality beyond the CSVW standards

## Installation

`pip install git+https://github.com/stevenkfirth/csvw_functions_extra`

The python package [`csvw_functions`](https://github.com/stevenkfirth/csvw_functions) will also need to be installed.

## API

### get_normalized_metadata_table_group_dict

Description: Returns a normalized version of a CSVW metadata file.

```python
csvw_functions_extra.get_normalized_metadata_table_group_dict(
        metadata_document_location
        )
```
- **metadata_document_location** *(str)*: The filepath or url of the CSVW metadata file containing a Table Group object.

Returns *(dict)*: A dictionary of the normalized CSVW Table Group object.


### get_available_csv_file_names

Description: Returns the CSV file names of all tables in a CSVW metadata file.

```python
csvw_extra_functions.get_available_csv_file_names(
        metadata_document_location
)
```
- **metadata_document_location** *(str)*: The filepath or url of the CSVW metadata file containing a Table Group object.

Returns *(list)*: A list of the `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name` value in each table.


### download_table_group

Description: Reads a CSVW metadata file and downloads the CSV files from remote locations. This makes use of the [https://purl.org/berg/csvw_functions_extra](#CSVW-vocabulary) vocabulary. 

```python
csvw_functions_extra.download_table_group(
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

Returns *(str)*: The local filename of the updated CSVW metadata file containing the new URLs for the newly downloaded tables.


### get_metadata_table_group_dict

Description: Returns a CSVW metadata Table Group object.

```python
csvw_functions_extra.get_metadata_table_group_dict(
        data_folder,
        metadata_filename
        )
```

Arguments:
- **data_folder** *(str)*: The filepath of a local folder where the normalized CSVW metadata file is saved.
- **metadata_filename** *(str)*: The filename of a CSVW metadata file which has been created by the [`download_table_group`](#download_table_group) method and is located in the data folder.

Returns *(dict)*: A dictionary of the CSVW Table Group object.


### get_metadata_table_dict

Description: Returns a CSVW metadata Table object.

```python
csvw_functions_extra.get_metadata_table_dict(
        sql_table_name,
        metadata_table_group_dict=None,
        data_folder=None,
        metadata_filename=None
        )
```

Arguments:
- **sql_table_name** *(str)*: The `https://purl.org/berg/csvw_functions_extra/vocab/sql_table_name` value of the table.
- **metadata_table_group_dict** *(dict)*: A dictionary of a metadata Table Group object, such as the return value of [`get_metadata_table_group_dict`](#get_metadata_table_group_dict).
- **data_folder** *(str)*: The filepath of a local folder where the normalized CSVW metadata file is saved.
- **metadata_filename** *(str)*: The filename of a CSVW metadata file which has been created by the [`download_table_group`](#download_table_group) method and is located in the data folder.

Returns *(dict)*: A dictionary of the CSVW Table object.

Notes: If supplied the `metadata_table_group_dict` will be used to access the table object. If not supplied then the table object is accessed using the file located using `data_folder` and `metadata_filename`.


### get_metadata_column_dict

Description: Returns a CSVW metadata Column object.

```python
csvw_functions_extra.get_metadata_column_dict(
        column_name,
        sql_table_name,
        metadata_table_group_dict=None,
        data_folder=None,
        metadata_filename=None
        )
```

Arguments:
- **column_name** *(str)*: The `name` value of a column in a CSVW TableSchema object.
- **sql_table_name** *(str)*: The `https://purl.org/berg/csvw_functions_extra/vocab/sql_table_name` value of the table.
- **metadata_table_group_dict** *(dict)*: A dictionary of a metadata Table Group object, such as the return value of [`get_metadata_table_group_dict`](#get_metadata_table_group_dict).
- **data_folder** *(str)*: The filepath of a local folder where the normalized CSVW metadata file is saved.
- **metadata_filename** *(str)*: The filename of a CSVW metadata file which has been created by the [`download_table_group`](#download_table_group) method and is located in the data folder.

Notes: If supplied the `metadata_table_group_dict` will be used to access the table object. If not supplied then the table object is accessed using the file located using `data_folder` and `metadata_filename`.

Returns *(dict)*: A dictionary of the CSVW Column object.


### get_metadata_sql_table_names

Description: Returns a list of the SQL table names in the CSVW metadata file.

```python
csvw_functions_extra.get_metadata_sql_table_names(
        metadata_table_group_dict=None,
        data_folder=None,
        metadata_filename=None
        )
```

Arguments:
- **metadata_table_group_dict** *(dict)*: A dictionary of a metadata Table Group object, such as the return value of [`get_metadata_table_group_dict`](#get_metadata_table_group_dict).
- **data_folder** *(str)*: The filepath of a local folder where the normalized CSVW metadata file is saved.
- **metadata_filename** *(str)*: The filename of a CSVW metadata file which has been created by the [`download_table_group`](#download_table_group) method and is located in the data folder.

Notes: If supplied the `metadata_table_group_dict` will be used to access the table object. If not supplied then the table object is accessed using the file located using `data_folder` and `metadata_filename`.

Returns *(list)*: A list of the `https://purl.org/berg/csvw_functions_extra/vocab/sql_table_name` values of all tables in the CSVW metadata file.


### get_metadata_columns_codes

Description: Returns lookup dictionaries for the NEED lookup codes for one or more columns.

```python
csvw_functions_extra.get_metadata_columns_codes(
        column_names,
        sql_table_name,
        metadata_table_group_dict = None,
        data_folder = None,
        metadata_filename=None
        )
```

Arguments:
- **column_name** *(str)*: The `name` value of a column in a CSVW TableSchema object.
- **sql_table_name** *(str)*: The `https://purl.org/berg/csvw_functions_extra/vocab/sql_table_name` value of the table.
- **metadata_table_group_dict** *(dict)*: A dictionary of a metadata Table Group object, such as the return value of [`get_metadata_table_group_dict`](#get_metadata_table_group_dict).
- **data_folder** *(str)*: The filepath of a local folder where the normalized CSVW metadata file is saved.
- **metadata_filename** *(str)*: The filename of a CSVW metadata file which has been created by the [`download_table_group`](#download_table_group) method and is located in the data folder.

Returns *(dict of dicts)*: A dictionary with:
- keys: the names of the column(s)
- values: a dictionary with keys as lookup codes and values as code descriptions.


### import_table_group_to_sqlite

Description: Reads a CSVW metadata file and imports the CSV data into a SQLite database. This makes use of the [https://purl.org/berg/csvw_functions_extra](##CSVW-vocabulary) vocabulary.

Method:

1. If not already present, a SQLite database named `database_name` is created in the `data_folder`.
2. For each table in the TableGroup object, the local CSV file is located in the `data_folder` using `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name`.
3. The CSV file is imported into the SQLite database into a table named using `https://purl.org/berg/csvw_functions_extra/vocab/sql_table_name`. 
4. Primary key field(s) are set up using the information in the CSVW TableSchema `primaryKey` value.
5. Indexes are set up on columns if `https://purl.org/berg/csvw_functions_extra/vocab/sqlsetindex` is True.

Call signature:

```python
csvw_functions_extra.import_table_group_to_sqlite(
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

Description: Adds an SQlite index to a column in a SQlite database.

```python
csvw_functions_extra.add_index(
        fields,
        table_name,
        data_folder,
        database_name,
        unique=False,
        verbose=False
        )
```

Arguments:
- **fields** *(str or list): The field(s) (i.e. columns) to add the index to.
- **table_name** *(str)*: The name of the table in the SQLite database. 
- **data_folder** *(str)*: The filepath of a local folder where the SQLite database is stored.
- **database_name** *(str)*: The name of the SQLite database, relative to the data_folder.
- **unique** *(bool)*: If True, then a unique index is created.


### get_all_table_names_in_database

Description: Returns a list of all table names in the database.

```python
csvw_functions_extra.get_all_table_names_in_database(
        data_folder,
        database_name        
        )
```

Arguments:
- **data_folder** *(str)*: The filepath of a local folder where the SQLite database is stored.
- **database_name** *(str)*: The name of the SQLite database, relative to the data_folder.

Returns *(list)*: A list of all table names in the SQLite database.


### get_sql_table_names_in_database

Description: Returns a list of table names in the database which are also present in the CSVW metadata file.

```python
csvw_functions_extra.get_sql_table_names_in_database(
        data_folder,
        database_name,
        metadata_filename
        )
```

Arguments:
- **data_folder** *(str)*: The filepath of a local folder where the SQLite database is stored.
- **database_name** *(str)*: The name of the SQLite database, relative to the data_folder.
- **metadata_filename** *(str)*: The filename of a CSVW metadata file which has been created by the [`download_table_group`](#download_table_group) method and is located in the data folder.

Returns: A list of table names in the database which are also present as `https://purl.org/berg/csvw_functions_extra/vocab/sql_table_name` values in the CSVW metadata file.


### get_where_clause_list

Description: Returns a WHERE clause for use in a SQL statement.

```python
csvw_functions_extra.get_where_clause_list(
        d
        )
```

Arguments:
- **d** *(dict)*: A dictionary of items to filter on where the keys are the field (column) names and the values are data values to filter on.

Returns *(str)*: A WHERE string for use in a SQL statement.


### run_sql

Description: Runs an SQL query on the database and returns the result.

```python
csvw_functions_extra.run_sql(
        sql_query,
        data_folder,
        database_name,
        verbose=False
        )
```

Arguments:
- **sql_query** *(str)*: A SQL query.
- **data_folder** *(str)*: The filepath of a local folder where the SQLite database is stored.
- **database_name** *(str)*: The name of the SQLite database, relative to the data_folder.

Returns *(list)*: A list of dictionaries where each dictionary contains one set of results - keys are the field (column) names and values are the data values.


### convert_to_iterator

Description: Converts a value to a list.

```python
csvw_functions_extra.convert_to_iterator(
        x
        )
```

Arguments:
**x** *(int, float, string, list...): The value to be converted to an iterator.

Returns *(list)*: A list of value(s)
- A number is converted to a list of the number, e.g. `2` -> `[2]`
- A string to a list of the string, e.g. `'abc'` -> `['abc']`
- A list (or other iterable) remains the same, e.g. `[1,2,3]` -> `[1,2,3]`


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
            
