# bmat-tv-av
TV/AV repository

# TV API Reference

This API reference is organized by resource type. 
Each resource type has one or more data representations and one or more methods.

## Resource types
#### URIs relative to https://www.bmatapis.com/tv/v1, unless otherwise noted

 ### Channels
 
 | Method | HTTP request | Description |
 |:--|:--|:--|
 | list | **GET  /channels** | Lists the channels that broadcast programs. |
 
 ### Programs
 | Method | HTTP request | Description |
 |:--|:--|:--|
 | list | **GET  /programs** | Gets information about the programs broadcasted. **Required query parameters: startDate, endDate**  |
 
 
<hr>

# Channels: list

Lists the channels that broadcast programs.
### Request
#### HTTP request

**GET https://www.bmatapis.com/tv/v1/channels**

#### Parameters
| Parameter name | Value | Description |
|:--|:--|:--|
| Optional query parameters |
| id | integer | The ID of the channel |
| country | string | The A3 (UN) country code from which channels will be returned. |

#### Request body

**Do not supply a request body with this method.**

### Response

If successful, this method returns a response body with the following structure:

```python
{
  "id": integer,
  "name": string,
  "country": string,
  "country_code": string,
}
```

| Property name | Value | Description |  |
|:--|:--|:--|:--|
| id | integer | The channel id. |  |
| name | string | The name of the channel. |  |
| country | string | The country of the channel. |  |
| country_code | string | The A3 (UN) country code of the channel |  |
| programs | nested object | The list of programs aired on this channel. |  |


<hr>

# Programs: list

Lists the programs aired between dates with their broadcasting data (channel and
time details) aired within the specified time interval and country, and matching the specified title. 

### Request
#### HTTP request

**GET https://www.bmatapis.com/tv/v1/programs**

#### Parameters
| Parameter name | Value | Description |
|:--|:--|:--|
| **Required query parameters** |
| **startDate** | **string** | **The start date to search for programs from, formatted like: 'YYYYMMDD'** |
| **endDate** | **string** | **The end date to search for programs from, formatted like: 'YYYYMMDD'** |
| Optional query parameters |
| title | string | The local title of the program |
| country | string | The A3 (UN) country code from which channels will be returned. |

#### Request body

**Do not supply a request body with this method.**

### Response

If successful, this method returns a response body with the following structure:

```python
{
  "id": integer,
  "original_title": string,
  "local_title": string,
  "year": integer,
  "start_time": string,
  "end_time": string,
  "channel": {
    "id": integer,
    "name": string,
    "country": string,
    "country_code": string
  }
}
```

| Property name | Value | Description | Notes |
|:--|:--|:--|:--|
| id | integer | The id  of the file. |  |
| original_title | string | The original title of the program. |  |
| local_title | string | The local title of the program. |  |
| year | string | The year of the program. |  |
| start_time | string | The start time.  | Formatted as: **'YYYYmmdd - HH:MM'** |
| end_time | string | The end time. | Formatted as: **'YYYYmmdd - HH:MM'** |
| channel | nested object | The channel where the program was aired. |  |
| channel.id | integer | The channel id. |  |
| channel.name | string | The name of the channel where the program was aired. |  |
| channel.country | string | The country of the channel. |  |
| channel.country_code | string | The A3 (UN) country code of the channel |  |


<hr>

### Example response

```python
[
{
"program_id": "12044548",
"program_original_title": "Petits plats en équilibre","program_year": null,
"start_time": "20180101 - 13:00",
"end_time": "20180101 - 13:05",
...
},
{
"channel_id": "11939294",
"channel_name": "RTÉ News: One O'Clock",
"program_year": 2001,
"start_time": "20180101 - 13:00",
"end_time": "20180101 - 13:50",
},
...
]
```
