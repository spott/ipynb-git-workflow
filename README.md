Working on an IPython Notebook under version control
====================================================

Testing a scheme to allow working on IPython Notebooks
under version control. Based on Stackoverflow answer:
http://stackoverflow.com/a/20844506/121704

Instructions
------------

Place `ipynb_output_filter.py` in your path and ensure that it is executable.

- Add the following line to `~/.gitattributes`

```
*.ipynb    filter=dropoutput_ipynb
```

- Run the commands:

```
git config --global core.attributesfile ~/.gitattributes
git config --global filter.dropoutput_ipynb.clean ~/bin/ipynb_output_filter.py
git config --global filter.dropoutput_ipynb.smudge cat
```

Note
~~~~

If you want to enable this filter selectively, the file to modify is
`.git/info/attributes`.
