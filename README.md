------to get required package
pip install -r requirements.txt
or
pip install fastapi uvicorn redis
pip install sqlalchemy psycopg2-binary


------run below command to run the app:
python -m venv venv
venv\Scripts\activate.bat
uvicorn app.main:app --reload   


then open below url on browser

http://127.0.0.1:8000/docs

http://127.0.0.1:8000/


GET http://localhost:8000/api/dashboard/
