# Hive Network Agent Kit Server

## Getting Started

First, setup the environment:

```
$ python -m venv ./venv
# $ python3 -m venv ./venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
```

You need to specify an `OPENAI_API_KEY` in a _.env_ file in this directory.

Make a copy of the [.env.example](.env.example) file and rename it to _.env_.

Then, run the development server:

```
python main.py
```

Then call the API endpoint `/api/chat` to see the result:

```
curl --location 'localhost:8000/api/chat' \
--header 'Content-Type: application/json' \
--data '{ "messages": [{ "role": "user", "content": "Hello" }] }'
```

Open [http://localhost:8000/docs](http://localhost:8000/docs) with your browser to see the Swagger UI of the API.

## Learn More

https://hivenetwork.ai
