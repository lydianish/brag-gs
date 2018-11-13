# brag-gs
A Google Scholar API for BRAG

## Installation

```bash
pip install --user pipenv
cd brag-gs
pipenv install scholarly flask flask_restful
```

## Running the server locally

```bash
python server.py
```
The API will run locally on port `5002`.

## Example

A request for an author's information and publications:
``` 
GET http://localhost:5002/author?name=sophie+limou
```

Response:
```json
{
    "message": "Internal Server Error"
}
```