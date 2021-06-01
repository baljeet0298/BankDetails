# BankDetails
REST service that can fetch bank details

## Tech Stack
Python, flask, PostgreSQL, Heroku(hosted app), clever-cloud(hosted db)

HostingURL:  https://salty-temple-85776.herokuapp.com/
No homepage is there in the hosting URL, sharing below URL with some query 
https://salty-temple-85776.herokuapp.com/api/branches/autocomplete?q=RTGS&limit=3&offset=1


Curl Commands:

curl -X GET "https://salty-temple-85776.herokuapp.com/api/branches?q=banglore&limit=4&offset=0"

curl -X GET "https://salty-temple-85776.herokuapp.com/api/branches/autocomplete?q=RTGS&limit=3&offset=0"
