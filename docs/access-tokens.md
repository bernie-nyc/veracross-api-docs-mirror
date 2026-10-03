---
stoplight-id: pnlrcay2wklgy
---

# Access Tokens

All requests to the OneRoster API must be made with an access token. Access tokens are created by making a request to the authorization server with the [OAuth 2.0 Client Credentials](https://oauth.net/2/grant-types/client-credentials/) grant type.

### Security

The use of tokens offers a number of security benefits over other forms of authentication:

1. **Unique**: tokens are specific to our services and can be generated per use or per device
2. **Revocable**: tokens can can be individually revoked at any time without needing to update unaffected credentials
3. **Limited**: tokens can be narrowly scoped to allow only the access necessary for the use case
4. **Random**: tokens are not subject to the types of dictionary or brute force attempts that simpler passwords might be

This explanation is [from GitHub](https://github.blog/2020-07-30-token-authentication-requirements-for-api-and-git-operations/) but applies generally to us as well.

<!-- theme: danger -->
> The access tokens created with client credentials are **only** for secure, server-side access to school data. **Don't** hard code an access token or OAuth Client Secret in mobile apps, or in front-end JavaScript web apps, or publish them to social media.

### Expiration

Access tokens generated via the Client Credentials grant type can't be refreshed. The appropriate pattern is to request a new one when they expire. The expiration time isn't configurable and is currently set to 1 hour.

### Scopes

When you create an access token you must provide the list of scopes you'll need for the API requests you intend to make with that token. Multiple scopes can be requested all at once so a single access token can be used for different API endpoints.

<!-- theme: info -->
> As a best practice we recommend **limiting** the list of scopes attached to a single access token. You should create different access tokens for different areas of data access.

For example, if you want to work with Rostering, you might request the `https://purl.imsglobal.org/spec/or/v1p1/scope/roster-core.readonly` scope. If you also need to work with Gradebook data you can create another access token with `https://purl.imsglobal.org/spec/or/v1p1/scope/gradebook.readonly`, `https://purl.imsglobal.org/spec/or/v1p1/scope/gradebook.createput` and `https://purl.imsglobal.org/spec/or/v1p1/scope/gradebook.delete`. There's no limit to how many access tokens you can create.

The documentation for each API endpoint shows the corresponding scope required to use that endpoint.

You can only create access tokens with scopes that have been pre-approved on your OAuth Application at each school. If you need more scopes (or, realize you don't need a scope any more) let the school know. Scopes directly correspond with what kind of data access is possible, so as a best practice they should only enable scopes that directly correspond to your specific needs.

### Usage

Access tokens need to be created and used for each single school route separately.

Creating an access token for one school then using it in an API request for a different school will result in a `401 Unauthorized` error. Making an API request with an incorrect or expired access token will also result in a `401 Unauthorized` error. See [Errors](errors.md) for more details.

### Request/Response

| Create Access Token Request | |
|---|---|
| URL | `https://accounts.veracross.com/{school route}/oneroster/oauth/token` |
| Method | `POST`
| Content-Type | `application/x-www-form-urlencoded` |
| Body (form encoded): | grant_type=client_credentials<br>client_id=(your client id)<br>client_secret=(your client secret)<br>scope=(list of requested scopes)</br> |

| Create Access Token Response (Success) | |
|---|---|
| access_token | The Access Token you will use for Data API requests |
| created_at | A timestamp when the token was created |
| expires_in | Number of seconds until the access token expires (can be added to the `created_at` timestamp) |
| scope | List of scope privileges that are attached to the token (even though it's "scope" singular, multiple scopes will be listed if you requested more than one) |
| token_type | The type of access token. Currently it will only be `Bearer` |

The response will be JSON formatted.

### Example

> Note: Access token requests should set the Content-Type header to `application/x-www-form-urlencoded` and the fields should be encoded as form data. Some API tools can do this automatically, such as by using the `--form` option in the example below.

```
$ http --print b --form post https://accounts.veracross.com/api-sandbox/oneroster/oauth/token grant_type=client_credentials client_id=XXX client_secret=YYYY scope="https://purl.imsglobal.org/spec/or/v1p1/scope/gradebook.readonly https://purl.imsglobal.org/spec/or/v1p1/scope/gradebook.createput"
```

Response:
```json
{
    "access_token": "your-access-token-here",
    "created_at": 1597685646,
    "expires_in": 3600,
    "scope": "https://purl.imsglobal.org/spec/or/v1p1/scope/gradebook.readonly https://purl.imsglobal.org/spec/or/v1p1/scope/gradebook.createput",
    "token_type": "Bearer"
}
```
