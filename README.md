# Environment setup

### Automation Testing Framework
Framework to run data-related tests on Database MS SQL SERVER.
Tests are based on pytest framework.There are basic SQL-based tests.

## Name and description of project
Project pythonPytest contains determined automated test cases


## Create virtual environment for tests execution
```bash
pip install -r requirements.txt
```

## Run tests
```bash
pytest
pytest -v -s Tests/ --html=report.html
pytest tests/ --html-report=./report --title='PYTEST REPORT'
```

