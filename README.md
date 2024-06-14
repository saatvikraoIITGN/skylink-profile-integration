# SkyLink Profile Data Integration

## Overview
This project is an API to ingest and transform profile data from the TMC system "Umbrella Faces" into SkyLink's internal profile system.


## Architecture

- **Models:** 
defined a Profile model in Django to outline the schema used for storing profile data in a relational database. This model includes fields like `first_name, last_name, email, phone_number, address, tmc_id, and date_of_birth` which is all the necessary data we need from “Umbrella Faces” 

- **Serializers:** 
For API interactions, serializers are used to convert profile data from complex model instances into JSON format and vice versa. Here, I have integrated hyperlinks to profiles for easier navigation during demo 

- **Views:** 
Using Django Rest Framework’s viewsets, implemented the logic for handling different types of requests (e.g., creating a new profile or fetching an existing profile).

- **URL Routing:** 
I define URL routes that map to the views, making the API accessible through specific endpoints. This includes routing for creating, retrieving, updating, and deleting profiles, as well as error handling paths

- **Database Integration:** 
The project is configured to use Django’s default SQLite3 database for development. This can be easily swapped to a more scalable option like PostgreSQL for production environments

- **Error Handling:**
set up custom error handling to ensure that any issues are clearly communicated back to the user instead of just plain error pages

- **Unit Testing:**
included unit tests to verify that the application functions correctly, ensuring reliability and stability



## Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/yourusername/skylink-profile-integration.git
cd skylink-profile-integration
```

2.	Apply migrations
```bash
python3 manage.py migrate
```

3.	Run the server
```bash
python3 manage.py runserver
```


## Navigation - API Endpoints 
1. Localhost - http://127.0.0.1:8000/

2. API root - http://127.0.0.1:8000/api/

3. Profiles - http://127.0.0.1:8000/api/profiles/
	- Here, you can `GET` and `CREATE` profiles

4. Profile IDs - `http://127.0.0.1:8000/api/profiles/{id}`
	- Here, you can `UPDATE` and `DELETE` single profiles 


We can verify through terminal that correct endpoints are called. Apart from that, we have test cases to check. 


## Running Tests
```bash
python3 manage.py test
```
Total test cases: `8` 
Response: OK 

## Assumptions
	•	Profiles are uniquely identified by tmc_id.
	•	Date of birth is optional.