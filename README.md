### run app
```shell
python manage.py runserver 8004
```

### export requirements
```shell
conda env export > environment.yml
```

### restore requirements from environment.yml
```shell
conda env create -f environment.yml
```