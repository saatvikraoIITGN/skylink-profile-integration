# SkyLink Profile Data Integration

## Overview
This project is an API to ingest and transform profile data from the TMC system "Umbrella Faces" into SkyLink's internal profile system.

## Setup Instructions
1. Clone the repository
```bash
git clone https://github.com/yourusername/skylink-profile-integration.git
cd skylink-profile-integration
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3.	Apply migrations
```bash
python3 manage.py migrate
```

4.	Run the server
```bash
python3 manage.py runserver
```



## Running Tests
```bash
python3 manage.py test
```


## Assumptions
	•	Profiles are uniquely identified by tmc_id.
	•	Date of birth is optional.