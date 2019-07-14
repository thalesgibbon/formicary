### Links

Github: https://github.com/thalesgibbon/formicary.git

Pypi Teste: https://test.pypi.org/project/formicary/

### desenvolvimento
criar os arquivos wheels
```python setup.py sdist bdist_wheel```

push no pypi
```python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*```

instalar a biblioteca
```python -m pip install --index-url https://test.pypi.org/simple/ --no-deps formicary```

desinstalar a biblioteca
```pip uninstall formicary```