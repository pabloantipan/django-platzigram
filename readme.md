### Useful commands
```$ django-admin```

```$ python mange.py```

Django shell
```$ python manage.py shell```

### Start server
```$ python manage.py runserver```

### Create new app
```$ python manage.py startapp posts```

### Do migrations 

Apply changes to db
```$ python manage.py migrate```

Seek for changes to apply to archives
```$ python manage.py makemigrations```


### Data model using
```>>> from post.models import User```
```>>> pablo = User.objects.create()```
```>>> pablo.id```
```>>> pablo.first_name = 'Pablo'```
```>>> pablo.save()```
```>>> pablo.delete()```