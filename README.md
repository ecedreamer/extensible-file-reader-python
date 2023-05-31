### Extensible File Reader Project ###
Project demonstrate a simple plugin architecture. Currently, txt_reader
is a core reader engine and json_reader and csv_reader are plugin reader
engines. We can add a new plugin reader engine by implementing the
ProcessorInterface class and putting it to the correct directory. 

#### Pluggalbe folder structure ####
```text
src/pluggable_readers
|
├── __init__.py
├── csv_reader
│   ├── __init__.py
│   ├── csv_reader.py
│   └── manifest.json
|
└── json_reader
    ├── __init__.py
    ├── json_reader.py
    └── manifest.json
```

To run the script, go inside a project directory and run following commands
```commandline
export PYTHONPATH=$pwd:$pwd/src

python3 src/main.py
```
