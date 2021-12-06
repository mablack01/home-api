# home-api
This project is a Python API wrapper to access information on a home owner's property. The application utilizes [Flask](https://flask.palletsprojects.com/en/2.0.x/) for the API base.

## Documentation
API documentation is generated using Swagger and `flask-restx`.

While the application is running, you can find documentation on the following page: http://localhost:5000/
![Documentation](https://i.imgur.com/4H8eulV.png)

## Setup
In order to use this project, you must install a version of python3 and pip3. You can check if you have the proper version install by using the following commands: 
```
python --version
pip --version
```
Additionally if you do not have `virtualenv` installed on your machine, run the following command:

### Windows
```
py -m pip install --user virtualenv
```
### MacOS/Linux
```
python3 -m pip install --user virtualenv
```
Once you have the correct packages installed, you can follow the next few steps to set up your virtual environment and install the requirements.
1. Create a virtual environment
   ### Windows
   ```
   py -m venv env
   ```
   ### MacOS/Linux
   ```
   python3 -m venv env
   ```
2. Activate your environment
   ### Windows
   ```
   .\env\Scripts\activate
   ```
   ### MacOS/Linux
   ```
   source env/bin/activate
   ```
3. Install the requirements
   ### Windows
   ```
   py -m pip install -r requirements.txt
   ```
   ### MacOS/Linux
   ```
   python3 -m pip install -r requirements.txt
   ```
4. Run the application
   ### Windows
   ```
   py start.py
   ```
   ### MacOS/Linux
   ```
   python3 start.py
   ```
5. Deactivate your environment (when you are done!)\n
   This step is simple, just run the following command:
   ```
   deactivate
   ```

If you made it to step 4 your application should be live. You can access the endpoints via `http://127.0.0.1:5000/`.

## Next Steps
- Create a mock api wrapper so that we can write unit tests for the `/home/septic` endpoint without having access to the Home Canary API.
- Implement the authentication pseudocode using JWT and a SQL database, wrapping the `/home/` endpoints for authenticated users only.
