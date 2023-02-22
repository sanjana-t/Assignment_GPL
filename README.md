# Assignment_GPL

Project Name - TradingProject

Django startProject Name - MainAPP

Django startapp Name - Candle

-----candle

---candle/model.py 
- Created a basic model named UploadFile that accepts the input of file and timeframe.
- The file uploaded is uploaded on to the server.
- forms.py for ease of input.
- Created a model Candle to save all objects which are present in the csv_file.

---candle/views.py
- Created a view to save the form with name upload_file.
- Created a view as save_candle to use the file on server and generate objects that can be directly saved on database.
- Created a view called candle_timeframe that basically converts the list of objects to one output based on timeframe given.
- view (candle_timeframe) also generates a json file and stores on server for the candles in db.
- Created a download view which automatically downloads the generated json file to the user's system on trigerring the api.

---candle/urls.py
- All urls path included

-----test_imgs
- Json response and admin panel data is attached 

--To Run
- Download the files 
- create virtual environment (python -m venv venv) and install django
- Activate your venv 
- run python manage.py runserver 



