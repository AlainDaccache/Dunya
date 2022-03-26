from airflow import settings
session = settings.Session()
users = session.execute("SELECT * FROM users").fetchall()
print(users)
session.close()