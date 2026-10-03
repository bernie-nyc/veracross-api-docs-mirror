# Access Tokens

All requests to the Data API must be made with an access token. Access tokens are created by making a request to the Authorization API.

Access Tokens created during the SSO process by the Authorization Code grant type can retrieve [User Info](../../reference/Authorization-API.yaml/paths/~1oauth~1userinfo/get) about the logged in user. OIDC integrations receive the same User Info via `id_token` in the response.

### Security

The use of tokens offers a number of security benefits over other forms of authentication:

1. **Unique**: tokens are specific to our services and can be generated per use or per device
2. **Revocable**: tokens can can be individually revoked at any time without needing to update unaffected credentials
3. **Limited**: tokens can be narrowly scoped to allow only the access necessary for the use case
4. **Random**: tokens are not subject to the types of dictionary or brute force attempts that simpler passwords might be

This explanation is [from GitHub](https://github.blog/2020-07-30-token-authentication-requirements-for-api-and-git-operations/) but applies generally to us as well.

<!-- theme: danger -->
> The access tokens created with client credentials are **only** for secure, server-side access to school data. **Don't** hard code an access token or OAuth Client Secret in mobile apps, or in front-end JavaScript web apps, or publish them to social media.

### Revoking Access Tokens and Resetting Client Secrets

Both access tokens and client secrets can be revoked or reset as a self-service action.  This is important if you believe they have been exposed or compromised in any way.

<!--
type: tab
title: For Schools
-->

**Revoke access tokens**

1. Visit the affected OAuth Application record in Axiom
2. Run the "Revoke All Access Tokens" Action Menu item
3. Once complete, all access tokens for that application are no longer valid
4. New access tokens can be created as needed with the existing OAuth Application credentials

**Reset a client secret**

1. Visit the affected OAuth Application record in Axiom
2. Run the "Reset Client Secret" Action Menu item
3. Once complete, a new client secret is generated and the previous one is no longer valid. New access tokens cannot be created with the old OAuth Application credentials
4. Update any systems that use the OAuth Application credentials to use the new client secret. Notify the related vendor/partner of the change (if any)

<!--
type: tab
title: For Vendors/Partners
-->

**Revoke access tokens**

Vendors/partners can revoke access tokens using the Authorization API [Revoke Token](../../reference/Authorization-API.yaml/paths/~1oauth~1revoke/post) endpoint.

**Reset a client secret**

Contact the school to reset the OAuth Application client secret. Once the secret value has been reset, you can find the updated values in the Partner Portal under the School Integrations section.

<!-- type: tab-end -->

### Relationship with OAuth SSO

The Authorization API supports the following OAuth 2.0 grant types:

| Grant Type         | Suitable for                                                                                           |
|--------------------|--------------------------------------------------------------------------------------------------------|
| Client Credentials | "server to server" authentication where data access happens independent of any specific user's session |
| Authorization Code | SSO integrations and data access associated with an individual user                                    |
| Refresh Token      | renewing tokens created via the Authorization Code grant type                                          |

Access tokens created with the Client Credentials grant type are independent from user sessions or SSO. They are still attached to individual OAuth Applications for each school, but are for design for back-end, server-to-server API requests.

Access tokens can't be shared between API requests to different schools. You will need to generate separate access tokens for each OAuth Application that has been configured for you.

### Expiration

Access tokens generated for the Client Credentials grant type can't be refreshed. The appropriate pattern is to request a new one when they expire. The expiration time isn't configurable and is currently set to 1 hour.

Access tokens generated for the Authorization Code grant type are renewed by requesting a new token using the `refresh_token` grant type. For these requests, only the `grant_type`, `client_id`, and `refresh_token` fields are required in the request.

### Scopes

When you create an access token you must provide the list of scopes you'll need for the API requests you intend to make with that token. Multiple scopes can be requested all at once so a single access token can be used for different API endpoints.

<!-- theme: info -->
> As a best practice we recommend **limiting** the list of scopes attached to a single access token. You should create different access tokens for different areas of data access.

For example, if you want to work with Master Attendance records, you might request the `master_attendance:list` and `master_attendance:update` scopes. If you also need to work with Student Logistics Requests you can create another access token with `student_logistics_requests:list` and related scopes.

The documentation for each API endpoint shows the corresponding scope required to use that endpoint. Be sure to confirm that a scope is published before you request it for an access token. For example, just because a certain endpoint offers a `list` operation *doesn't* mean that a `delete` operation is available.

You can only create access tokens with scopes that have been pre-approved on your OAuth Application at each school. If you need more scopes (or, realize you don't need a scope any more) let us know. Scopes directly correspond with what kind of data access is possible, so as a best practice we will only enable scopes that directly correspond to your specific needs.

### Limits

OAuth Applications are limited in terms of how many access tokens can be created at once. The limit is currently set to a maximum of 10 active tokens per OAuth Application. For tokens created with the Authorization Code grant type, the limit is per user for that application. When another token is created, the oldest active token will be revoked automatically.

### Usage

Access tokens need to be created and used for each single school route separately.

Creating an access token for one school then using it in an API request for a different school will result in a `401 Unauthorized` error. Making an API request with an incorrect or expired access token will also result in a `401 Unauthorized` error. See [Errors](errors.md) for more details.

### Request/Response

| Create Access Token Request | |
|---|---|
| URL | `https://accounts.veracross.com/{school_route}/oauth/token` |
| Method | `POST`
| Content-Type | `application/x-www-form-urlencoded` |
| Body (form encoded): | Depends on the grant type; For example:<br><br>grant_type=client_credentials<br>client_id=(your client id)<br>client_secret=(your client secret)<br>scope=(list of requested scopes)</br> |

| Create Access Token Response (Success) | |
|---|---|
| access_token | The Access Token you will use for Data API requests |
| created_at | A timestamp when the token was created |
| expires_in | Number of seconds until the access token expires (can be added to the `created_at` timestamp) |
| refresh_token | The Refresh Token used to create a new Access Token when it expires (_only present for Authorization Code & Refresh Token grant type responses_) |
| id_token | The ID Token is a signed JWT that contains user info (_only present for Authorization Code & Refresh Token grant type responses with the `openid` scope_) |
| scope | List of scope privileges that are attached to the token (even though it's "scope" singular, multiple scopes will be listed if you requested more than one) |
| token_type | The type of access token. Currently it will only be `Bearer` |

The response will be JSON formatted. For more details, see the related [Create Access Token](../../reference/Authorization-API.yaml/paths/~1oauth~1token/post) endpoint documentation.

### Example

> Note: Access token requests should set the Content-Type header to `application/x-www-form-urlencoded` and the fields should be encoded as form data. Some API tools can do this automatically, such as by using the `--form` option in the example below.

```
$ http --print b --form post https://accounts.veracross.com/api-sandbox/oauth/token grant_type=client_credentials client_id=XXX client_secret=YYYY scope="students:list students:read"
```

Response:
```json
{
    "access_token": "your-access-token-here",
    "created_at": 1597685646,
    "expires_in": 3600,
    "scope": "students:list students:read",
    "token_type": "Bearer"
}
```
