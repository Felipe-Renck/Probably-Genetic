# Backend

## Instructions to run this project locally:  
  
1. Download and install PostgreSQL and pgAdmin: https://www.postgresql.org/download/
2. Create a new database with the following properties:
  ```text  
        host="localhost",
        database="dbtest",
        user="postgres",
        password="Novonoia1!"
```
3. Install requirements:  
  
```console  
$ pip install -r requirements.txt  
```  
  
3. Set up DB:   
   
```console  
$ python manage.py makemigrations   
$ python manage.py migrate   
```  
   
4. Run the app:   
  
```console   
$ python manage.py runserver  
```   
