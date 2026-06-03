Returns configured bot/platform IDs.

Responses

-   application/json
    
-   401
    
    Unauthorized
    
-   403
    
    Forbidden
    

Request Example for get/api/v1/im/bots

Shell Curl

```curl
curl http://localhost:6185/api/v1/im/bots \
  --header 'X-API-Key: YOUR_SECRET_TOKEN'
```

cURLCopy

cURLCopy

Test Request(get /api/v1/im/bots)

Status: 200Status: 401Status: 403

Show Schema 

```json
{
  "status": "ok",
  "message": null,
  "data": {
    "bot_ids": [
      "string"
    ]
  }
}
```

JSONCopy

JSONCopy

OK

Upload a file and get attachment\_id for later use in chat/message APIs.

Body

required

multipart/form-data

-   file
    
    Type: stringFormat: binary
    
    required
    
    binary data, used to describe files
    

Responses

-   application/json
    
-   401
    
    Unauthorized
    
-   403
    
    Forbidden
    

Request Example for post/api/v1/file

Shell Curl

```curl
curl http://localhost:6185/api/v1/file \
  --request POST \
  --header 'Content-Type: multipart/form-data' \
  --header 'X-API-Key: YOUR_SECRET_TOKEN' \
  --form 'file=@filename'
```

cURLCopy

cURLCopy

Test Request(post /api/v1/file)

Status: 200Status: 401Status: 403

Show Schema 

```json
{
  "status": "ok",
  "message": null,
  "data": {
    "attachment_id": "string",
    "filename": "string",
    "type": "string"
  }
}
```

JSONCopy

JSONCopy

OK

Get an uploaded attachment file by attachment\_id.

Query Parameters

-   attachment\_id
    
    Type: string
    
    required
    
    Attachment ID returned by POST /api/v1/file.
    

Responses

-   application/octet-stream
    
-   401
    
    Unauthorized
    
-   403
    
    Forbidden
    

Request Example for get/api/v1/file

Shell Curl

```curl
curl 'http://localhost:6185/api/v1/file?attachment_id=' \
  --header 'X-API-Key: YOUR_SECRET_TOKEN'
```

cURLCopy

cURLCopy

Test Request(get /api/v1/file)

Status: 200Status: 401Status: 403

Show Schema 

```json
@filename
```

Copy

Copy

OK

List chat sessions for the specified username.

Query Parameters

-   page
    
    Type: integer
    
    min:  
    
    1
    
    Integer numbers.
    
-   page\_size
    
    Type: integer
    
    min:  
    
    1
    
    max:  
    
    100
    
    Integer numbers.
    
-   platform\_id
    
    Type: string
    
    Optional platform filter
    
-   username
    
    Type: string
    
    required
    
    Target username.
    

Responses

-   application/json
    
-   401
    
    Unauthorized
    
-   403
    
    Forbidden
    

Request Example for get/api/v1/chat/sessions

Shell Curl

```curl
curl 'http://localhost:6185/api/v1/chat/sessions?page=1&page_size=20&platform_id=&username=' \
  --header 'X-API-Key: YOUR_SECRET_TOKEN'
```

cURLCopy

cURLCopy

Test Request(get /api/v1/chat/sessions)

Status: 200Status: 401Status: 403

Show Schema 

```json
{
  "status": "ok",
  "message": null,
  "data": {
    "sessions": [
      {
        "session_id": "string",
        "platform_id": "string",
        "creator": "string",
        "display_name": null,
        "is_group": 1,
        "created_at": "2026-06-03T12:45:35.016Z",
        "updated_at": "2026-06-03T12:45:35.016Z"
      }
    ],
    "page": 1,
    "page_size": 1,
    "total": 1
  }
}
```

JSONCopy

JSONCopy

OK

Send message directly to platform bot by umo + message chain payload.

Body·

required

application/json

-   message
    
    required
    
    -   Type: string
        
    
-   umo
    
    Type: string
    
    required
    
    Unified message origin. Format: platform:message\_type:session\_id
    

Responses

-   application/json
    
-   401
    
    Unauthorized
    
-   403
    
    Forbidden
    

Request Example for post/api/v1/im/message

Shell Curl

```curl
curl http://localhost:6185/api/v1/im/message \
  --request POST \
  --header 'Content-Type: application/json' \
  --header 'X-API-Key: YOUR_SECRET_TOKEN' \
  --data '{
  "umo": "webchat:FriendMessage:openapi_probe",
  "message": "ping from api key"
}'
```

cURLCopy

cURLCopy

plain

Test Request(post /api/v1/im/message)

Status: 200Status: 401Status: 403

Show Schema 

```json
{
  "status": "ok",
  "message": null,
  "data": {
    "additionalProperty": "anything"
  }
}
```

JSONCopy

JSONCopy

OK

Returns all available AstrBot config files that can be selected by Chat API using config\_id/config\_name.

Responses

-   application/json
    
-   401
    
    Unauthorized
    
-   403
    
    Forbidden
    

Request Example for get/api/v1/configs

Shell Curl

```curl
curl http://localhost:6185/api/v1/configs \
  --header 'X-API-Key: YOUR_SECRET_TOKEN'
```

cURLCopy

cURLCopy

Test Request(get /api/v1/configs)

Status: 200Status: 401Status: 403

Show Schema 

```json
{
  "status": "ok",
  "message": null,
  "data": {
    "configs": [
      {
        "id": "string",
        "name": "string",
        "path": "string",
        "is_default": true
      }
    ]
  }
}
```

JSONCopy

JSONCopy

OK