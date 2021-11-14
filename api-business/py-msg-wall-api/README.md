# python Flask message-wall api 🐍🧱
## simplest http rest api

imagine a shared wall where you can write down message for all your friends to read.

this wall can be written to and read from via http requests.

to keep things simple, data is saved to an embedded database. 

## CR(UD)
for many reasons, we starts by letting anyone Create a new message and Read all messages.

Update? can't seem to find a use case for that. Unless original poster can authenticate and modify his own post. We're not there yet.

Delete? Same rationale as for Update + some kind of moderator/administrator could purge outrageous posts. Hopefully we won't need that feature.

### Create
HTTP Post.

- content-type: `application/json`
- body (key-value):
  - text: message_string
- return: ID

ex.: `curl --header "Content-Type: application/json" --request POST http://localhost:5000/message --data "{\"text\":\"message 3\"}"`

### Read
- list all messages
  - `curl -v http://localhost:5000/messages`
- get single message by ID
  - `curl -v http://localhost:5000/message/1`

### stack
- python Flask
    - "Flask is a micro web framework written in Python"
    - [https://flask.palletsprojects.com/en/2.0.x/#](https://flask.palletsprojects.com/en/2.0.x/#)
- SQLite
  - "SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine"
  - [https://www.sqlite.org/index.html](https://www.sqlite.org/index.html)
- Nginx
  - "Nginx (pronounced "engine X",[8] /ˌɛndʒɪnˈɛks/ EN-jin-EKS), stylized as NGINX, nginx or NginX, is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache."
  - [nginx.org](nginx.org)
- Gunicorn
  - "The Gunicorn "Green Unicorn" (pronounced jee-unicorn or gun-i-corn)[2] is a Python Web Server Gateway Interface (WSGI) HTTP server."
  - [https://gunicorn.org/](https://gunicorn.org/)