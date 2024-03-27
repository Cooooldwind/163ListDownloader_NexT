del dist /Q /F
python -m build
twine upload dist/*
pause