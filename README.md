### Criando projeto

```python
import formicary.create_project
```

### Links

Github: https://github.com/thalesgibbon/formicary.git

Pypi Teste: https://test.pypi.org/project/formicary/

### desenvolvimento
criar os arquivos wheels
```python setup.py sdist bdist_wheel```

push no pypi
```python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*```

instalar a lib
```pip install formicary```

instalar a lib test
```pip install --index-url https://test.pypi.org/simple/ formicary```

instalar especifica versao
```pip install --index-url https://test.pypi.org/simple/ formicary==0.5```

desinstalar a biblioteca
```pip uninstall formicary```

??? atualizar lib
```python -m pip install --upgrade pip```

identificar as versoes das libs
```pip freeze```

criar requirement
```pip freeze > requirements.txt```

instalar requirement
```pip install -r requirements.txt```