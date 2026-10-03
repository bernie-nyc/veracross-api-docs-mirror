---
stoplight-id: r7ch4onat59mk
---

# Errors

Any API request could potentially result in an error. An error response is indicated by an HTTP status code other than 20X.

<!-- theme: info -->
> See [IMS OneRoster 1.1 documentation](http://www.imsglobal.org/oneroster-v11-final-specification#_Toc480451999) for a list of standard HTTP response codes and their meanings.

<!-- theme: warning -->
> Many errors can be resolved by adjusting the way you make the API request, so please review the corresponding documentation carefully!

### Common API Errors

| HTTP Status Code | Code Minor | What it means | What you should do |
|------------------|---------------|---------------|--------------------|
| `400` | `bad_request` | The request is invalid and cannot be served. | This typically happens when bad URL parameters are used, check the pagination, field selection, filtering and sorting syntax used in the request. |
| `401` | `unauthorized_request` | There's a scope in the authorization access token that doesn't match the scope required for the endpoint, or the access token is invalid in another way. | Double check the list of scopes you're including in acquiring the access token. See if the token is malformed or expired.<br> You can only request scopes that are enabled on the OAuth Application record. |
| `403` | `forbidden` | The server can be reached and process the request but refuses to take any further action. | |
| `404` | `unknownobject` | There is no resource behind the URI. | This could happen when you request a `sourcedId` that doesn't exist via a path parameter, or if the endpoint requested is unknown. | Make sure that the requested `sourcedId` values exist, the endpoint name follows the OneRoster specification, and that the request URL is in correct format. |
| `500` | | Internal Server Error. | Please contact Veracross with the incident. |

## OneRoster API Error Response Format

```json
{
"statusInfoSet" :
  {
    "imsx_codeMajor" : "success | failure | unsupported"
    "imsx_severity" : "status | warning | error"
    "imsx_description" : "<human readable description>"
    "imsx_codeMinor" : [
      "imsx_codeMinorField": {
        "imsx_codeMinorFieldName" : "<error field name>"
        "imsx_codeMinorFieldName" : "<error field value values>"
      }
    ]
  }
  "error_id" : "<Veracross error id for tracking>"
}
```

<!-- theme: info -->
> When contacting Veracross for support regarding an error, please include the `error_id` to expedite our investigation/response.
