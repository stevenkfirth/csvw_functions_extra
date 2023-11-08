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

For each table in the TableGroup object, the method is:

i) For individual CSV files:

1. The CSV file is downloaded using the url in `https://purl.org/berg/csvw_functions_extra/vocab/csv_download_url`.
2. The CSV is saved in the `data_folder` using the filename in `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name`

ii) For ZIP files:

1. The ZIP file is downloaded using the url in `https://purl.org/berg/csvw_functions_extra/vocab/zip_download_url`.
2. The ZIP is saved in the `data_folder` using the filename in `https://purl.org/berg/csvw_functions_extra/vocab/zip_file_name`
3. The CSV file is extracted from the ZIP file using the path in `https://purl.org/berg/csvw_functions_extra/vocab/csv_zip_extract_path`. 
4. The CSV is saved in the `data_folder` using the filename in `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name`

iii) If an associated metadata file is present (this is separate to the CSVW metadata file):

1. This is downloaded using the url in `https://purl.org/berg/csvw_functions_extra/vocab/metadata_download_url`
2. If step 3 occurs, the associated metadata file is saved in the `data_folder` using the filename in `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name` with the additional suffix in `https://purl.org/berg/csvw_functions_extra/vocab/metadata_file_suffix`.

iv) For all cases:

1. A new version of the normalized CSVW metadata file is also saved in the data folder, with Table `url` values linking to the newly downloaded CSV files.

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

Description: Returns lookup dictionaries for the lookup codes for one or more columns.

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
        metadata_filename,
        data_folder,
        database_name,
        csv_file_names=None, 
        remove_existing_tables=False,
        verbose=False
```

Arguments:
- **metadata_filename** *(str)*: The filename of a CSVW metadata file which has been created by the [`download_table_group`](#download_table_group) method and is located in the data folder.
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


### get_field_names

Description: Returns a list of the field names in a database table.

```python
csvw_functions_extra.get_field_names(
        table_name,
        data_folder,
        database_name,
        verbose=False
        )
```

Arguments:
- **table_name** *(str)*: The name of the table in the SQLite database. 
- **data_folder** *(str)*: The filepath of a local folder where the SQLite database is stored.
- **database_name** *(str)*: The name of the SQLite database, relative to the data_folder.

Returns *(list)*: A list of all field names of the table in the SQLite database.


### get_row_count

Description: Returns the number of rows from a table.

```python
csvw_functions_extra.get_row_count(
        table_name,
        data_folder
        database_name,
        filter_by=None,
        group_by=None,
        verbose=False
        )
```

Arguments:
- **table_name** *(str)*: The name of the table in the SQLite database. 
- **data_folder** *(str)*: The filepath of a local folder where the SQLite database is stored.
- **database_name** *(str)*: The name of the SQLite database, relative to the data_folder.
- **filter_by** *(dict)*: A dictionary with information to filter the rows - see [`get_where_string`](#get_where_string).
- **group_by** *(list)*: A list of field names to group by.

Returns *(list)*: A list of result dictionaries.


### get_rows

Description: Returns one or more rows from a table in the database.

```python
csvw_functions_extra.get_rows(
        table_name,
        data_folder,
        database_name,
        filter_by = None,  
        fields = None,  
        verbose = False
        )
```

Arguments:
- **table_name** *(str)*: The name of the table in the SQLite database. 
- **data_folder** *(str)*: The filepath of a local folder where the SQLite database is stored.
- **database_name** *(str)*: The name of the SQLite database, relative to the data_folder.
- **filter_by** *(dict)*: A dictionary with information to filter the rows - see [`get_where_string`](#get_where_string).
- **fields** *(list)*: A list of field names to return.

Returns *(list)*: A list of result dictionaries.


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
**x** *(int, float, string, list, tuple, None): The value to be converted to an iterator.

Returns *(list)*: A list of value(s), where:
- A number is converted to a list of the number, e.g. `2` -> `[2]`
- A string to a list of the string, e.g. `'abc'` -> `['abc']`
- A list (or other iterable) remains the same, e.g. `[1,2,3]` -> `[1,2,3]`
- `None` is converted to an empty list, e.g. `None` -> `[]`


### get_field_string

Description: Converts a list of field names into a string for use in a SQL query.

```python
get_field_string(
        fields = None
        )
```

Arguments:
- **fields** *(str, list or None)*: The field name(s)

Returns *(str)*: A string of the field names, where: 
- `None` is converted to `*`
- A string is converted to a quoted string, e.g. `'field'` -> `' "field1" '`
- A list is converted to a series of quoted strings separated by commas, e.g. `['field1','field2']` -> `' "field1","field2" '`

### get_group_by_string

Description: Converts a list of field names into two strings for use in GROUP BY clauses in a SQL query.

```python
get_group_by_string(
        group_by = None
        )
```

Arguments:
- **group_by** *(str, list or None)*: The field name(s) to group by

Returns *(tuple)*: A two-item tuple of (*group_by_fields*,*group_by_string*), where:
- `None` is converted to `('', '')`
- `'field1'` is converted to `(' "field1", ', 'GROUP BY "field1" ')`
- `['field1','field2']` is converted to `(' "field1","field2", ', 'GROUP BY "field1","field2" ')`


### get_where_string

Description: Converts a dictionary of field names and values into a string for use in WHERE clauses in a SQL query.

```python
get_where_string(
        filter_by = None 
        )
```

Arguments:
- **group_by** *(dict or None)*: The field name(s) and values to filter by

Returns *(str)*: A string to use in a WHERE clause, where:
- `None` is converted to `''`
- `{'field1': 1}` is converted to `' WHERE ("field1" = 1)'`
- `{'field1': 1, 'field2': 'a'}` is converted to `' WHERE ("field1" = 1) AND ("field2" = "a")'`
- `{'field1': [1,2]}` is converted to `' WHERE ("field1" IN (1,2))'`
- `{'field1': ['a','b']}` is converted to `' WHERE ("field1" IN ("a","b"))'`
- `{'field1': {'BETWEEN':[1,2]}}` is converted to `' WHERE ("field1" BETWEEN (1 AND 2))'`
- `{'field1': {'BETWEEN':['a','b']}}` is converted to `' WHERE ("field1" BETWEEN ("a" AND "b"))'`


## CSVW vocabulary

### Vocabulary on CSVW column metadata objects

- `https://purl.org/berg/csvw_functions/vocab/codes`: (JSON object) An object (dictionary) relating any codes using in the column data to a string with the meaning of the codes. 

- `https://purl.org/berg/csvw_functions/vocab/column_notes`: (string) A description of the contents of the column.

- `https://purl.org/berg/csvw_functions_extra/vocab/sqlsetindex`: Boolean. If `true` then an SQLite index is set up on this column when the data is imported into the database.

### Vocabulary on CSVW table metadata objects

#### Required:

- `https://purl.org/berg/csvw_functions_extra/vocab/csv_file_name`: The name for the newly downloaded CSV file. The CSV file is saved in the data folder using this name.

- `https://purl.org/berg/csvw_functions_extra/vocab/sql_table_name`: The name to be used for the database table when importing the CSV file into a SQLite database.

#### For CSV file downloads:

- `https://purl.org/berg/csvw_functions_extra/vocab/csv_download_url`: The url where the remote CSV file can be downloaded from.

#### For ZIP downloads:

- `https://purl.org/berg/csvw_functions_extra/vocab/zip_download_url`: The url where the remote ZIP file can be downloaded from.

- `https://purl.org/berg/csvw_functions_extra/vocab/zip_file_name`: The name for the newly downloaded ZIP file. The ZIP file is saved in the data folder using this name.

- `https://purl.org/berg/csvw_functions_extra/vocab/csv_zip_extract_path`: The path to extract the CSV file from the ZIP file.
            
#### Optional:

- `https://purl.org/berg/csvw_functions_extra/vocab/metadata_download_url`: The url where an associated metadata file for the CSV file can be downloaded from.

- `https://purl.org/berg/csvw_functions_extra/vocab/metadata_file_suffix`: A suffix to use when saving the associated metadata file.


            
