# Py-Shell-Script-Parser
 simple shell script parser program in python.

This program parse through a given command line by line and categorizes them accordingally into three: Executable commands, files, urls.

**EXAMPLE**
```#!/bin/bash
samtools a.fa > b.fa
python -m pip install -r requirements.txt
```

will be filtered as

Files:['a.fa','b.fa','requirements.txt']
Exes:['samtools','python']
url:[]

