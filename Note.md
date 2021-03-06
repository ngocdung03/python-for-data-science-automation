### Setting up environment
- Find Material/ DS4B_101O_COURSE/ 000_environment-setup/ 01_conda_environment.yml
- Open new Terminal on VScode, copy the line `conda env create -f 000_environment_setup/01_conda_environment.yml`
- Find Python interpreter by '101' in commamd palette search
- Update environment file with new modifications: `conda env update --file 000_environment_setup/01_conda_environment.yml --prune`
- Export environment
- Allow others to recreate my environment: `conda create -f envname.yml`
- List env: `conda env list`
- Remove env
### Extensions
- iPython Kernel used by Jupyter Notebook extension will match your current Python Interpreter so Environments will match. 
### Practice with .py and .ipynb
- Must ensure both terminal and interactive Python use Python interpreter: *Python 3.7.1 64-bit (conda)  ~/envs/ds4b101p/bin/python*
- Interactive Python #%%: to start the session running the interactive notebook.
    - Then click Run Cell 
- When to use Python Interactive Session:
    - Making plots or Viewing help docs quickly
    - Otherwise, using Terminal is much faster to quickly see results.
- Send selected codes to interactive windown: Setting/search Jupyter send
- R user extension: Requires R library "languages"
### Jumpstart
- ETL - Extract, Transform, Loading: The process of ingesting data and processing it into a format that can be used for analysis.
- REPL: an interactive environment for runnign Python Scripts
- `# %% [Markdown]`
- File Not Found Error: By Default, Jupyter Notebooks have a working directory that is located in the folder of the file. This different than VSCode projects.
  - Search for jupyter directory, on *Jupyter: Notebook File Root*, change into ${workspaceFolder}
  - Restart Python Interactive Session
- The reorganization makes a copy: Otherwise there would be a recursive reference (df would reference the joined data and the reorganized data, at the same time, which is impossible). To compensate pandas makes a copy and points df to the new reorgainzed data frame.
- Plotnine uses data in long format
- Pandas Excel Engines: Pandas useds Excel reader/writers to perform the Input/Output (IO) operations. This means you will need to have the Excel engine installed to leverage the backend. 
- Why databases:
  - Easy to set up
  - Helps you convert a business process to data
  - Helps with automation
- Support databases: Make sure you have added the python driver neede by dialects supported with SQL Alchemy. For example, PostgreSQL uses psycopg2 as the default driver. You'd need to add this in your Conda Environment.
- The easiest way to learn how to connect to a database is to Google: "sql alchemy connect to postgress"
- It is a good idea to close a database connection when finished with reading/writing the data. Open connections can reduce the performance of applications
- Database schema: this is the architechture of your database. It has a name.
- Extract, Transform, Load steps are great candidates for automation. They are lengthy and chang infrequently (since databases don't typically change that often).
- Creating package:
  - my_pandas_extensions: package
  - database.py: module
  - __init__.py: initializes a Python package with modules denoted by filenames.
- In Python, Objects get methods and attributes from the classes that they inherit from.
- Attributes: The meta-data that exists for an object. Think of the dimensions of a data frame has an attribute called "shape".
- Pandas & Numpy work together: Pandas adds the data frame and series structure along with methods to work with data. Numpy adds the low-level function to perform the work, like sum, mean, std, log, etc...
- Numpy uses special data types (eg int64) that extend the Python builtin data types (eg int), which are optimized for memory allocation.
- Dictionary: In function development, key-word-args (**kwargs) are dictionaries. Dictionaries are used in the df.renames() and df.agg() functions for column renaming and aggregations. 
- List: commonly used for iteration. In function development, the *args are lists of arguements without keys. 
- Tuple: immutable list, used in Pandas for storing data frame shape and multi-index column names.
- Regex:
  - "term": contains "term"
  - "^term": starts with "term"
  - "term$": ends with "term"
  - (term1)|(term2): matches "term1" or "term2"


