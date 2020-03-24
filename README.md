# graphql-flask

## Database API

To run the database api run:

```
python3 app/db_api.py
```

The server will run on http://127.0.0.1:5000/


## Queries

To run a graphql query go to http://127.0.0.1:5000/graphql

### List all matches

```
{
  matchesList {
    edges {
      node {
        id
        matchName
        matchDate
        matchScore
        matchStatus
      }
    }
  }
}
```

### Create a match

```
mutation {
  createMatch(input: {matchName: "tot vs nap", matchDate: "2020-03-01 22:00:00", matchStatus: "finished", matchScore: "3-2"}) {
    match {
      matchId
      matchName
      matchDate
      matchScore
      matchStatus
    }
  }
}
```

### Update a match

The input match_id is mandatory.

```
mutation {
  updateMatch(input: {match_id: "2", matchName: "tot vs meme", matchDate: "2020-04-01"}) {
     match{
      matchId
      matchName
      matchDate
      matchScore
      matchStatus
    }
  }
}
```

### Delete a match

```
mutation {
  deleteMatch(input:{matchId: "2"}){
    matches {
      matchId
      matchName
      matchDate
      matchScore
      matchStatus
    }
  }
}
```


## APP API

To run the app api run:

```
python3 app/app_api.py
```
The server will run on http://127.0.0.1:8080/

### fetch matches

fetch all matches:

```
curl localhost:8080/get_all
```

fetch matches by date:

```
curl "localhost:8080/filter_by_date?date=2020-03-02"
```

feth matches by id:

```
curl "localhost:8080/filter_by_id?id=2"
```

