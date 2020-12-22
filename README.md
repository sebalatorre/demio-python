# demio-python
Wrapper for the DemioAPI for python projects.
Go to the [DemioAPI documentation](https://publicdemioapi.docs.apiary.io/) for details on the fields that will be returned on each API call.

## How to use
Import this library where you want to use it and create an object of "DemioAPI" with the parameters "api_key" and "api_secret". As always, keep those values on evironment constants.
```python
demio = demio = DemioAPI(api_key, api_secret)
```

### Ping
Will return True is succesful or False if failed.
```python
response = demio.ping
```

### Events
Will return all events. Response in json format.
```python
response = demio.events
```

### Upcoming Events
Will return all upcoming events. Response in json format.
```python
response = demio.upcoming_events
```

### Event
Will return the event of the given id. You can specify a second parameter: active, as true or False. Response in json format.
```python
response = demio.event(id)
```

### Event Date
Will return the date of the given date id and event id. Response in json format.
```python
response = demio.event_date(event_id, date_id)
```

### Event Date Participants
Will return the paticipants of a given date id and event id. You can add a third parameter: status. Response in json format.
```python
response = demio.event_date_participants(event_id, date_id)
```

### Register
Register an attendee to an event. It will return the unique join link of the attendee if succesful. Response in json format.
```python
response = demio.register(event_id, first_name, last_name, email)
```

# Enjoy!
