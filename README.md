```buildoutcfg
cd ~/xspce

PROJECT_ROOT=$(pwd)
export PYTHONPATH=$PROJECT_ROOT/src/py:$PROJECT_ROOT/tests:$PYTHONPATH
python -m unittest discover
```

