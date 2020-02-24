# bmat-tv-av
TV/AV repository

**Asignment notes:** 
- The readable HTML interface is at: **http://34.66.114.233/tv/programs/**. It includes a view to search for programs by date.
- For testing replace the API root by **http://34.66.114.233/tv/v1/**.
- For the purposes of this asignment, Basic Authentication is also available. (username + password)
- **Testing credentials:**
    | Username | Password |
    |---|---|
    | bmatapis_admin | bmatapis!test |
    | bmat_operations | neversleep |
    | bmat_devs | neversleep |


# TV API Reference

The API can be accessed via HTML interface at the API endpoints. 
API endpoints return data in JSON format when using the `?format=json` query parameter in the request.
This reference guide is organized by resource type. 
Each resource type has one or more data representations and one or more methods.



## Authorization:
To access the API resources, users must make the requests with a valid API Token.
Users with valid credentials, can make a POST request to http://www.bmatapis.com/tv/v1/api-token-auth/ passing the **username** & **password** parameters, and a Token will be returned.
#### Example response:
```python
{
    "token": "4246918ab412693d82081990re3886b33fa8f688"
}
```

<hr>

## Resource types
#### URIs relative to http://www.bmatapis.com/tv/v1/, unless otherwise noted.

 ### Channels
 
 | Method | HTTP request | Description |
 |:--|:--|:--|
 | list | **GET  <br>/channels** | Lists the channels that broadcast programs. |
 
 ### Programs
 | Method | HTTP request | Description |
 |:--|:--|:--|
 | list | **GET <br>/programs** | Gets information about the programs broadcasted. |
 | get | **GET <br>/programs/*****primary_key*** | Gets the details about the program. |

 
<hr>

# Channels: list

Lists the channels that broadcast programs.

### Request
#### HTTP request

**GET http://www.bmatapis.com/tv/v1/channels/**

#### Request body

**Do not supply a request body with this method.**

### Response

If successful, this method returns a response body with the following structure:

```python
{
  "count": integer,
  "next": string,
  "previous": string,
  "results": [
    {
      "url": string,
      "uid": integer,
      "name": string,
      "country": string
    },
    ...
  ]
}
```

| Property name | Value | Description | Notes |
|:--|:--|:--|:--|
| count | integer | The quantity of channels returned. |  |
| next | string | The url of the next page. |  |
| previous | string | The url of the previous page. |  |
| results | object | The list of channels with details in the page. | Not all details are returned. |

<hr>

# Programs: get

Returns the properties of a program.

### Request
#### HTTP request


**GET http://www.bmatapis.com/tv/v1/programs/***primary_key*/


#### Parameters
| Parameter name | Value | Description |
|:--|:--|:--|
| **Required query parameters** |
| **primary_key** | **integer** | **The primary key identifier.** |


#### Request body

**Do not supply a request body with this method.**

### Response

If successful, this method returns a response body with the following structure:

```python
{
  "program": {
    "uid": integer,
    "original_title": string,
    "local_title": string,
    "year": integer,
    "channel": {
      "url": string
      "uid": integer,
      "name": string,
      "country": string
    }
  },
  "url": string
  "start_date": string,
  "start_time": string,
  "duration": number
}
```

| Property name | Value | Description | Notes |
|:--|:--|:--|:--|
| url | string | The url of the program time. |  |
| program.uid | integer | The ID  of the program. | Unique |
| program.original_title | string | The original title of the program. |  |
| program.local_title | string | The local title of the program. |  |
| program.year | string | The year of the program. |  |
| channel | nested object | The channel where the program was aired. |  |
| channel.id | integer | The channel id. |  |
| channel.name | string | The name of the channel where the program was aired. |  |
| channel.country | string | The country of the channel. |  |
| start_date | string | The start date.  | Formatted as: **'YYYY-mm-dd'** |
| start_time | string | The start time. | Formatted as: **'HH:MM'** |
| duration | number | The duration in seconds. |  |

<hr>

### Example response

```python
{
  "program": {
    "url": "http://www.bmatapis.com/tv/v1/programs/4239",
    "uid": 4424900793,
    "original_title": "Neven's Irish Food Trails",
    "local_title": "Neven's Irish Food Trails",
    "year": "2017",
    "channel": {
      "url": "http://34.66.114.233/tv/v1/channels/2/",
      "uid": 69036687,
      "name": "RTE 1",
      "country": "Ireland"
    }
  },
  "start_date": "2018-02-28",
  "start_time": "20:30",
  "duration": 1800,
  "url": "http://34.66.114.233/tv/v1/programs/2/"
}
```
<hr>

# Programs: list

Returns a list of the programs aired, with all their properties. Paginated by 10 programs.

### Request
#### HTTP request

**GET http://www.bmatapis.com/tv/v1/programs/**

#### Request body

**Do not supply a request body with this method.**

### Response

If successful, this method returns a response body with the following structure:

```python
{
  "count": integer,
  "next": string,
  "previous": string,
  "results": [
    {
      "program": {
        "url": string,
        "uid": integer,
        "original_title": string,
        "local_title": string,
        "year": integer,
        "channel": {
          "uid": integer,
          "name": string,
          "country": string
        }
      },
      "start_date": string,
      "start_time": string,
      "duration": integer
    },...
  ]
}
```

| Property name | Value | Description | Notes |
|:--|:--|:--|:--|
| count | integer | The quantity of programs returned. |  |
| next | string | The url of the next page. |  |
| previous | string | The url of the previous page. |  |
| results | object | The list of programs with their details in the page. |  |

<hr>

### Example response

```python
{
  [
    {
      "program": {
        "url":"http://www.bmatapis.com/tv/v1/programs/3/",
        "uid": 461044,
        "original_title": "À communiquer",
        "local_title": "À communiquer",
        "year": "n/a",
        "channel": {
          "uid": 384303590,
          "name": "HD1 (France)",
          "country": "France"
        }
      },
      "start_date": "2018-02-28",
      "start_time": "00:00",
      "duration": 83700
    },...
  ]
}

```
