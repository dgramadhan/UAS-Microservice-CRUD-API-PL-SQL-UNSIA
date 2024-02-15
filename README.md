# UAS-Microservice-CRUD-API-PL-SQL-UNSIA

Untuk menjalankan aplikasi ini dapat dengan menjalankan :
```git clone https://github.com/dgramadhan/UAS-Microservice-CRUD-API-PL-SQL-UNSIA.git```

Lalu setelah selesai project ini di cloning, masuk ke folder project tersebut. Install library dan jalankan aplikasi dengan:
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Aplikasi dapat di jalankan pada ```http://localhost:8000``` atau ```http://127.0.0.1:8000```, 8000 disini digunakan sebagai port default unutk mengakses aplikasi.

Untuk melakukan migrasi database, dapat menjalankan perintah :
```alembic upgrade head```
atau dapat dengan cara menlakukan restore file dump (file hasil dari dump) yang ada pada project ini.


Dokumentasi API pada postman dapat dilihat pada link dibawah ini : 
```
https://documenter.getpostman.com/view/26413086/2sA2r3YkNH
```
atau dapat melakukan import pada postman dengan menggunakan file postman collection pada project ini.


