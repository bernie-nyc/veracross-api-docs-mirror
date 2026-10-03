# Creating an SSO Integration

Veracross can operate as an Identity Provider (IDP) for vendor/partner sites looking to build Single Sign-On (SSO) integrations. This means that school users such as Faculty, Staff, Students, etc can use their Veracross Account to log in to vendor/partner sites without needing a separate password for each site.

Refer to our [OAuth SSO Login Flow](../docs/diagrams/oauth-sso-login-flow.md) for an overview diagram of each possible step of a user login flow.

## Before You Begin: Is this integration required?

It **isn't** necessary to set up an SSO integration to build server-side data processing applications that use the Data API. Visit [Using the Data API](../concepts/using-the-data-api.md) for more details.

However, if you have a site that school users should log into with their Veracross Accounts, you're in the right place! That can be accomplished with an SSO integration.

## Step 1: Configure the required OAuth Application details

At Veracross, SSO integrations are managed with OAuth Applications.

<!-- theme: info -->
> Note: this step is only required for first time setup. If you already know the details for your OAuth Application you may continue to Step 2.

#### If you don't have an OAuth Application yet

<!--
type: tab
title: For Schools
-->
[Follow this guide](https://community.veracross.com/s/article/Setting-Up-New-Integration-Partners-in-Veracross-API) to invite a Partner and create an OAuth Application on their behalf.

Or, [visit this page](https://community.veracross.com/s/article/Creating-an-OAuth-Application-School-Workflow) for details about how to create an OAuth Application manually for internal use.

<!--
type: tab
title: For Vendors/Partners
-->
If you're working with Veracross schools and have become an Integration Partner, schools can choose "Start Integration" from our partners listing. Then visit the [Partner Portal](https://portals.veracross.com/partners) to review your OAuth Application details.

If you're already working with a Veracross school but don't yet see that school listed on the [Partner Portal](https://portals.veracross.com/partners), ask them to invite you according to [our guide for setting up a new Partner](https://community.veracross.com/s/article/Setting-Up-New-Integration-Partners-in-Veracross-API).

Or, visit this page to learn more about [becoming a Veracross Partner](https://www.veracross.com/integrations/).

<!-- type: tab-end -->

### Enable the required scope

The OAuth Application must have one of the following scopes enabled:

| Description          | Access Name       | Suitable for                    |
|----------------------|-------------------|---------------------------------|
| SSO (Single Sign-On) | `sso`             | OAuth 2.0 integrations          |
| OpenID Connect (OIDC)| `openid`          | OpenID Connect 1.0 integrations |

OAuth Applications that *aren't* used for SSO integrations *shouldn't* have these scopes enabled.

<!--
type: tab
title: For Schools
-->
The scopes are available on the vendor/partner's OAuth Application record in Axiom:

| OAuth 2.0 integrations | OpenID Connect 1.0 integrations |
|------------------------|---------------------------------|
| ![example-oauth-application-sso-scope](https://assets.veracross.com/_documentation/api/images/example-oauth-application-sso-scope-2.png) | ![example-oauth-application-openid-scope](https://assets.veracross.com/_documentation/api/images/example-oauth-application-openid-scope.png) |

> Note: OAuth Applications can only be configured by school users with the `OAuth_App_Admin` role.

<!--
type: tab
title: For Vendors/Partners
-->
You can verify the scopes are enabled for your OAuth Applications in the Partner Portal:

| OAuth 2.0 integrations | OpenID Connect 1.0 integrations |
|------------------------|---------------------------------|
| ![example-oauth-application-sso-scope](https://assets.veracross.com/_documentation/api/images/example-partner-integration-sso-scope-2.png) | ![example-oauth-application-openid-scope](https://assets.veracross.com/_documentation/api/images/example-partner-integration-openid-scope.png) |

<!-- type: tab-end -->

## Step 2: Begin the User Authorization Flow

From this point forward, the specific configuration steps for a school to set up an SSO integration are the responsibility of the vendor/partner. The implementation will depend on how each has decided to implement OAuth/OIDC in their systems. In most cases we expect that vendors will use publicly available code libraries (not provided by Veracross) to integrate with an Veracross as Identity Provider.

Some vendors/partners may be automatically configured by providing the OIDC configuration endpoint:

```
https://accounts.veracross.com/SCHOOL_ROUTE_HERE/.well-known/openid-configuration
```

The vendor/partner sites can begin the user authorization flow by redirecting users to the app's Authorization URL, which should generally be in this format:

```
https://accounts.veracross.com/SCHOOL_ROUTE_HERE/oauth/authorize?client_id=CLIENT_ID_HERE&redirect_uri=REDIRECT_URI_HERE&scope=SCOPES_HERE&response_type=code
```

You'll need to fill in the `ALL_CAPS` parts of this example URL before using it. The `SCOPES_HERE` part must be filled with a list of scopes to request. The list should be space separated (and URL encoded, eg `%20`). The list must include `sso` or `openid` from Step 1, depending on if your SSO integration is OAuth or OIDC.

<!--
type: tab
title: For Schools
-->
The values are available from the OAuth Application record in Axiom.

<!--
type: tab
title: For Vendors/Partners
-->
The OAuth Application information is available in the Partner Portal for each school you integrate with.

<!-- type: tab-end -->

> Note: Make sure the Redirect URI you plan to use is registered on the school's OAuth Application record, and that it's escaped in the URL query string.

If they aren't already logged in to Veracross, users will see their school's Veracross login page. The OAuth Application description will be shown as a cue that they'll be sent to this site after logging in:

<!--
focus: false
-->
![A Veracross Login Page](https://assets.veracross.com/_documentation/api/images/vc-login-page.png)

At this point the user can log in to Veracross as they normally would. If their account has been configured to use an external identity provider (eg, Google, Okta, Azure AD, etc) then they'll be redirected through that service. Users logging in to a vendor/partner site via SSO won't be shown a separate "consent" screen, which is sometimes used with public OAuth SSO implementations. This is because the OAuth Application scopes are approved ahead of time by an `OAuth_App_Admin` user at the school.

For more details about this step, see the related [Authorize](../../reference/Authorization-API.yaml/paths/~1oauth~1authorize/get) request documentation.

## Step 3: Receive the Authorization Code from the Redirect URI

After the user has logged in to Veracross they'll be redirected to the configured Redirect URI with an Authorization Code. The request will come to your system in this format:

```
https://YOUR_REDIRECT_URI?code=98754a0eb37966140ffd9570f770aae755cfd08cd7032469454ab1f57a18f3
```

If you're using an OAuth library to process the login flow, then this step may be handled automatically. Regardless, you'll need to use the authorization code to create an access token, which is the next step.

## Step 4: Exchange the Authorization Code for an Access Token

Next, the user's Authorization Code should be exchanged for an Access Token. This is done with `POST` request to the `oauth/token` endpoint in the Authorization API. The response will be a JSON object that includes the access token.

Authorization Codes expire after 10 minutes and are single-use. If you request an access token for an authorization code that's expired or has already been used, the server will respond with an "invalid grant" error.

Example of response for an OAuth integration:

```json
{
  "access_token": "v3r4cr0ssv3r4cr0ssv3r4cr0ssv3r4cr0ssv3r4cr0ssv3r4cr0ssv3r4cr0ssv",
  "refresh_token": "r3fr3shr3fr3shr3fr3shr3fr3shr3fr3shr3fr3shr3fr3shr3fr3shr3fr3sh",
  "created_at": 1599229410,
  "expires_in": 3600,
  "scope": "sso",
  "token_type": "Bearer"
}
```

For an OIDC integration, you would see the same response but with a signed JWT `id_token` key:

```json
{
  "access_token": "v3r4cr0ssv3r4cr0ssv3r4cr0ssv3r4cr0ssv3r4cr0ssv3r4cr0ssv3r4cr0ssv",
  "refresh_token": "r3fr3shr3fr3shr3fr3shr3fr3shr3fr3shr3fr3shr3fr3shr3fr3shr3fr3sh",
  "id_token": "JwT0k3nJwT0k3nJwT0k3n.JwT0k3nJwT0k3nJwT0k3nJwT0k3nJwT0k3nJwT0k3n.JwT0k3nJwT0k3nJwT0k3n",
  "created_at": 1599229410,
  "expires_in": 3600,
  "scope": "openid",
  "token_type": "Bearer"
}
```

> Note: You must include the OAuth Application's client secret in the POST request for an access token. Remember, the client secret value must be kept confidential and should only be used for server-to-server requests.

For more details about this step, see the related [Create Access Token](../../reference/Authorization-API.yaml/paths/~1oauth~1token/post) request documentation.

## Step 5: Request User Info (with the Access Token)

The final step of the OAuth SSO process is to request information about the user who is logging in. The request must include the `Authorization: Bearer ACCESS_TOKEN` header using the access token value created in the previous step.

The response will be a JSON object containing basic user information:

```json
{
  "sub": "1234",
  "preferred_username": "john.doe",
  "email": "john.doe@example.com",
  "roles": [
    "Parent",
    "Coach",
    "Staff",
    "Faculty",
    "Donor"
  ]
}
```

The response structure is intended to be OIDC compatible, so it should work with authentication systems expecting OIDC fields. Integrations using the `openid` scope receive User Info via the `id_token` JWT and don't need to make an additional request.

The details about this request are found in the [User Info](../../reference/Authorization-API.yaml/paths/~1oauth~1userinfo/get) request documentation.

It's prudent to validate user info properties **before** allowing users to log in. For example, if your site is intended for students, you can check that `Student` is one of the users roles. The list of roles and their descriptions is found in [this product documentation page](https://community.veracross.com/s/article/Person-Role-Definitions).

> Note: for school users, `sub` is their internal account id. It uniquely identifies a user at a specific school. It must be combined with the school route to become globally unique. For example, different users at different schools might have the same `sub` value. Also note that schools may configure their own format for `preferred_username`, so it should only be used for display purposes (eg, some schools use email, some schools use other id's, etc).

## Conclusion

This concludes our step-by-step guide to demonstrate how to make an SSO integration. Visit our [OAuth SSO Login Flow](../docs/diagrams/oauth-sso-login-flow.md) for a quick reference.

Please contact support if you have any additional questions, and good luck!
