del dist /Q /F
python setup.py sdist
twine upload dist/*
pause