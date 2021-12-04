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