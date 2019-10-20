@echo off
rd /s .\build
rd /s .\dist
python setup.py sdist bdist_wheel
python -m twine upload -u crazyj dist/* --verbose


