# Errors

Any API request could potentially result in an error. An error response is indicated by an HTTP status code other than 200.

<!-- theme: info -->
> See [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) for a list of standard HTTP response codes and their meanings.

<!-- theme: warning -->
> Many errors can be resolved by adjusting the way you make the API request, so please review the corresponding documentation carefully!

## Authorization API Error Response Format

| Response (Error) | |
|---|---|
| error | An error code |
| error_description | The description of the error |
| error_id | A unique ID for this specific error. Please provide this error id when you ask for help with an error. |

### Common Authorization API Errors

| HTTP Status Code | Error Message | What it means | What you should do |
|------------------|---------------|---------------|--------------------|
| `400` | The request is missing a required parameter, includes an unsupported parameter value, or is otherwise malformed. | The request can't be processed as-is. | Verify each parameter in the request URL to confirm each one has a proper value and no required request parameters are missing. |
| `401` | The provided authorization grant is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client. | A value provided in the request is either incorrect or expired. | Authorization Codes are single use, so this error is expected for duplicate requests. Otherwise, review each value in the request.<br><br>For SSO integrations, if there was a Redirect URI value, confirm that it's pre-registered on the OAuth Application and is properly escaped in the request. Also, check that you've included the `sso` scope in the request and that scope is enabled on the corresponding OAuth Application. |
| `404` | Not Found | There was no resource associated with the request, or the request URL is incorrect. | Check the request URL to confirm it's structured correctly and all parameters are provided. For `/userinfo` requests, confirm the provided access token is for the Authorization Code grant type for SSO. |
| `415` | Unsupported Media Type | The content type of the request was set incorrectly | This could happen if your request doesn't explicitly set the `Content-Type` header to `application/x-www-form-urlencoded` when required. Ensure that your request data is also form encoded. |

### Interactive SSO Errors

> Note: errors for interactive OAuth SSO integrations may be shown directly on the screen during the login process

| Error Message | What it means | What you should do |
|---------------|---------------|--------------------|
| The requested client id is unknown or unauthorized. | The `client_id` query string parameter doesn't match the OAuth Application's client id value. | Review the OAuth Application client id and ensure the `client_id` parameter in the Authorization URL matches the provided value. |
| The requested Redirect URI isn't registered for this client. | The `redirect_uri` query string parameter doesn't match what's configured on the OAuth Application. | Review how you're constructing the Authorization URL and confirm it's exactly the same as the OAuth Application and properly [URL encoded](https://en.wikipedia.org/wiki/URL_encoding). The entire redirect URI needs to match, not just the base server. |
| A requested scope isn't authorized for this application. | Review the list of scopes you're including in the Authorization URL. You can only request scopes that are enabled on the OAuth Application record. You don't need to request all of them if you don't need them.<br><br>Typically for an SSO-only integration, `sso` is the only required scope. |
| The authorization server does not support this response type | The value of the `response_type` parameter isn't supported, or the parameter is missing from the Authorization URL query string. | Typically for an SSO-only integration, it should be set to `code` for the OAuth Authorization Code grant type. |

## Data API Error Response Format

| Response (Error) | |
|---|---|
| error | The description of the error |
| error_id | A unique ID for this specific error. Please provide this error id when you ask for help with an error. |

### Common Data API Errors

| HTTP Status Code | Error Message | What it means | What you should do |
|------------------|---------------|---------------|--------------------|
| `400` | The provided JSON object was invalid<br>_(or)_</br>If provided, the request body must be a JSON object<br>_(or)_<br>The request body "data" field must be a JSON object | When creating or updating a record, a valid JSON object should be provided in the request body. This error can happen when the request body can't be parsed or it's the wrong structure. | Review your HTTP request logic to make sure the request body is a valid JSON object.<br>When creating or updating records, the JSON object should have a `data` field, which is an object with the fields and values you intend to create or update. |
| `400` | An unknown data field was provided: (field name) | When creating or updating a record, the `data` object included a field that isn't expected. | 1. Review the structure of the data object you're sending with the request<br>2. Check that all the fields you're sending are listed on the documentation page for that Data API endpoint. |
| `400` | Unknown parameters were provided: (parameter names) | When sending an API request, the URL query string included a field that isn't expected. | 1. Review the query string you're sending with the request<br>2. Check that all the fields you included listed as parameters on the documentation page for that Data API endpoint. |
| `400` | The URL path is missing required parameters: (parameter names) | When sending an API request, the URL includes a value in curly braces `{like_this}` | 1. Review the URL path of the request<br>2. Check that all URL path segments that are parameters (indicated with curly braces) are instead replaced with the appropriate values and don't include the braces. |
| `400` | Creating a record requires providing at least one writable field | The proper data fields required to create the record weren't provided or the provided JSON object is missing a `data` field. | 1. Review the JSON object you're providing with the create operation. It should be a JSON object with a `data` field, and the `data` object should include the fields you want to include to create the record<br>2. Check that you're sending all the required fields that are listed on the documentation page for that Data API endpoint. |
| `401` | An authorization header with a bearer token is required | The HTTP request was missing an `Authorization` header with a `Bearer` value. | Review your HTTP request logic and make sure you're including an `Authorization` header. The value should include your access token in the format: `Bearer your-access-token-here`<br>See [Access Tokens](/docs/concepts/access-tokens.md) for details. |
| `401` | The provided access token is missing a required scope: (scope name) | You might see this error for a request that needs an OAuth scope, but that specific scope wasn't included when the access token was created with the Authorization API. | 1. Check that you're making the API request to the appropriate URL path<br>2. Check that you're making the HTTP request with the appropriate method (`GET`, `POST`, `PATCH`, `DELETE`) since each operation typically requires a separate scope<br>3. Check the documentation for that endpoint to learn which OAuth Scope is required for that Data API operation<br>4. Review your logic that uses the Authorization API to create access tokens; specifically regarding which OAuth scopes you're requesting. Make sure that you're including the scope from step 3<br>See [Access Tokens](/docs/concepts/access-tokens.md) for details. |
| `401` | The provided access token is unknown | We couldn't find the access token you provided at the school you made the request for. | Review the access token value you sent in the `Authorization` header. The value should include your access token in the format: `Bearer your-access-token-here`. Access tokens can only be used for requests to the same school you created it for and can't be shared for requests to different schools.<br>See [Access Tokens](/docs/concepts/access-tokens.md) for details. |
| `401` | The provided access token has expired | The access token you provided is no longer valid. | All access tokens will automatically expire after a period of time. When an access token expires, you should create a new one via the Authorization API.<br>See [Access Tokens](/docs/concepts/access-tokens.md) for details. |
| `401` | The provided access token has been revoked | Revocation of an access token means it can no longer be used for API requests. A token can be revoked automatically (when the maximum number of active tokens is exceeded) or manually (via the Authorization API, or via the "Revoke all Access Tokens" Action on the OAuth Application record). | 1. When an access token is revoked you can create a new one via the Authorization API. See [Access Tokens](/docs/concepts/access-tokens.md) for details. Review how many access tokens you're creating to avoid having older tokens automatically revoked.<br>2. If you haven't exceeded the maximum active token limit and didn't manually revoke your access token, check with the related school to understand if they revoked access tokens for your OAuth Application. |
| `404` | The requested client is unknown | The URL for your request was structured incorrectly or there was an invalid value in the "school route" portion of the URL. | Data API requests have the format: `https://api.veracross.com/{school_route}/v3/request_path_goes_here`<br>You might see this error if you made the request to `v3/school_route` or the school route was otherwise incorrect.<br>See the "Base URL" section of [Using the Data API](/docs/concepts/using-the-data-api.md) for details. |
| `404` | The requested endpoint wasn't found | The URL for your request was structured incorrectly or there was an invalid value for the "request path" portion of the URL. | Data API requests have the format: `https://api.veracross.com/{school_route}/v3/request_path_goes_here`<br>You might see this error if you made the request to `{school_route}/v3` directly without an additional request path. The appropriate request path is listed at the top of the page for each Data API endpoint. Path elements shown in curly braces are values that should be replaced in the actual request. |
| `405` | Request Method Not Allowed | Each API endpoint will only respond to certain HTTP methods, but this request used a method which hasn't been enabled. | 1. Check that you're making the HTTP request with the appropriate method (`GET`, `POST`, `PATCH`, `DELETE`)<br>2. Check the documentation for that endpoint to learn which HTTP method should be used for that Data API operation. |
| `406` | The requested content type isn't supported | The request was made for a content type other than JSON. | The Data API only supports JSON. API requests should be made in a way that signals that you also support JSON.<br>This can be done via either of these approaches:<br>1. Set the `Accept` header in your request to `application/json`, `application/*`, or `*/*`<br>2. Add `.json` as a URL path suffix. For example, sending a request like `students.json` will override the `Accept` header. |
| `406` | The requested encoding isn't supported | The request was made requiring encoding(s) that aren't supported on the server. | Review the `Accept-Encoding` header in your request. Any encoding may be requested as long as `deflate`, `identity`, or `*` is acceptable. This error can occur if all of those encodings are prohibited with `q=0`. |
| `409` | The record(s) you are creating already exist and may not be duplicated | A record created by the API request is a duplicate of an existing database record. | 1. Review the data object you're sending with the request for values you may have already sent in a previous request.<br>2. Make a "list" request to find existing records that match the one you intended to create. |
| `429` | Too Many Requests | The Data API rate limit has been exceeded. | Check the `X-Rate-Limit-Reset` header for a timestamp. This is the point after which the number of remaining requests will be reset. You can re-try any failed API requests after this point.<br/>See [Rate Limiting](./rate-limiting.md) for details. |
| `500` | An unknown error has occurred | Something went wrong while we tried to process the API request. | Please contact Veracross with the `error_id` value from the response object. That specific error id will help us look up additional diagnostic information for that specific request. |
