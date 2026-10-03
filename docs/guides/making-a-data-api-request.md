# Making a Data API Request

In this guide, you will follow a step by step process to make a request to the Data API.

Refer to our [API Request diagram](../diagrams/api-request.md) for an overview diagram of a Data API request.

<!-- theme: info -->
> Note: This guide uses [HTTPie](https://httpie.io/), a cross-platform tool for making HTTP requests on the command line. Other popular tools for doing this include [Curl](https://curl.se/), [Insomnia](https://insomnia.rest/products/insomnia), and [Postman](https://www.postman.com/product/api-client/). Many tools and libraries are interoperable with the Veracross API, since it's based on standards such as OAuth, HTTP, and JSON. However, you may need to adjust the examples to match how your chosen tool works.

## Before You Begin: Decide what kind of data you need

Before you can make an API request, you need to decide what data you want to work with.

The available Data API endpoints and their corresponding operations are listed on the left, under the "Data API" header. You can click into each listing for more details. Each page will show the API request path, parameters, and fields.

For the purposes of this guide, you'll be making a request to [list Student records](../../reference/Data-API.yaml/paths/~1students/get). You can refer back to different parts of the API endpoint page throughout this guide.

## Step 1: Configure the required OAuth Application details

All requests to the Data API require authorization with an OAuth Access Token. You'll need to create these tokens yourself with the Authorization API, but first you'll need to get the details from your registered OAuth Application.

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
If you're working with Veracross schools and have become an Integration Partner, schools can choose "Start Integration" from the partners listing. Then visit the [Partner Portal](https://portals.veracross.com/partners) to review your OAuth Application details.

If you're already working with a Veracross school but don't yet see that school listed on the [Partner Portal](https://portals.veracross.com/partners), ask them to invite you according to [our guide for setting up a new Partner](https://community.veracross.com/s/article/Setting-Up-New-Integration-Partners-in-Veracross-API).

Or, visit this page to learn more about [becoming a Veracross Partner](https://www.veracross.com/integrations/).

<!-- type: tab-end -->

### Understand which scopes are required

The [List Students documentation](../../reference/Data-API.yaml/paths/~1students/get) shows that the scope you need is called "List Students". This will be formatted as `students:list` in the Authorization API request.

The scope required for that API request is shown in the documentation here:
![endpoint-operation-scopes-list](https://assets.veracross.com/_documentation/api/images/endpoint-operation-scopes-list.png)

<!--
type: tab
title: For Schools
-->
Add scope(s) to OAuth Application.

<!--
type: tab
title: For Vendors/Partners
-->
Communicate required scope(s) -- Let your schools know which scopes you need, so they can add them to your OAuth Application.

<!-- type: tab-end -->

Here's what it looks like to enable `List Students` on an OAuth Application in Axiom:

![example-oauth-application-active-scope](https://assets.veracross.com/_documentation/api/images/example-oauth-application-active-scope-3.png)

> Note: OAuth Applications can only be configured by school users with the `OAuth_App_Admin` role.

Apart from this guide, schools will typically hear the list of scopes that each Vendor/Partner needs to enable the data access that their integration requires from that Vendor/Partner during the integration process. Only the minimum required scopes should be made active. Schools are in control of their own data, and may possibly decline to enable certain requested scopes on a case by case basis.

### Review OAuth Application details

At this point, everything should be prepared to create an access token.

<!--
type: tab
title: For Schools
-->
Visit the OAuth Application record's "General" category:

![example-axiom-oauth-application-details](https://assets.veracross.com/_documentation/api/images/example-axiom-oauth-application-details.png)

<!--
type: tab
title: For Vendors/Partners
-->
Visit the Partner Portal "School Integrations" screen:

![example-partner-portal-oauth-application-details](https://assets.veracross.com/_documentation/api/images/example-partner-portal-oauth-application-details.png)

<!-- type: tab-end -->

## Step 2: Create an Access Token

Now you're ready to make an API request, although not to the Data API yet. First, you need to get an access token via the Authorization API. The technical documentation for each endpoint is listed to the left under the "Authorization API" header. The concepts described in this step are also explained in [Access Tokens](../concepts/access-tokens.md), so be sure to review that page for more details.

All requests to the Authorization API follow this format:

```
https://accounts.veracross.com/{school_route}/{request path}
```

[Create Access Token](../../reference/Authorization-API.yaml/paths/~1oauth~1token/post) requests are to the `oauth/token` path. Therefore in this case the full request URL is:
`https://accounts.veracross.com/api-sandbox/oauth/token`

> Note: The appropriate `school route` is shown for each school in the Partner Portal, or it can be provided by each school. For reference, it's the same for the other Veracross apps at the school such as Axiom and Portals.
>
> Don't forget to update that part of the URL when you copy/paste from documentation!

You'll also need to provide details from the OAuth Application record: `client_id`, `client_secret`, and `scope`. Since this request is independent of a user session, you'll want to use the "Client Credentials" `grant_type` (see [Access Tokens](../concepts/access-tokens.md) for more details).

> Note: Access token requests should set the Content-Type header to `application/x-www-form-urlencoded` and the fields should be encoded as form data. Some API tools can do this automatically, such as by using the `--form` option in the example below.

Making that request, you should receive a JSON formatted string that includes an `access_token` field. That's the value you'll need for the next step.

```
$ http --print b --form POST https://accounts.veracross.com/api-sandbox/oauth/token grant_type=client_credentials client_id=3121633c13ce45dc94946ff2b33622b7 client_secret=${VC_OAUTH_CLIENT_SECRET} scope=students:list
```

Response:
```json
{
    "access_token": "6826395b0f7b85b164b4721fdf2e9c87f6d7a30c7846b75d3692debe1c65af1e",
    "created_at": 1621438379,
    "expires_in": 3600,
    "scope": "students:list",
    "token_type": "Bearer"
}
```

<!-- theme: warning -->
> Note: This particular Access Token won't actually work for you... you'll need to make your own!

## Step 3: Make a Data API request

Now you're finally ready to get some data. All requests to the Data API follow this format:

```
https://api.veracross.com/{school_route}/v3/{request path}
```

Per the documentation for [List Students](../../reference/Data-API.yaml/paths/~1students/get), the request path for this endpoint is `students`. Replace the school route with what you learned in the previous step. In this case the full Data API request URL is:
`https://api.veracross.com/api-sandbox/v3/students`

You'll need to provide the Access Token from the previous step as the `Authorization` header in the request. The token value should be prefixed with the `token_type` as instructed by the token request, which is `Bearer`. Therefore in this case the full header is:
`Authorization: Bearer 6826395b0f7b85b164b4721fdf2e9c87f6d7a30c7846b75d3692debe1c65af1e`

Finally, you can assemble these pieces to make a HTTP `GET` request to the endpoint URL:

```
$ http --print b GET https://api.veracross.com/api-sandbox/v3/students Authorization:'Bearer 6826395b0f7b85b164b4721fdf2e9c87f6d7a30c7846b75d3692debe1c65af1e' x-page-size:2 | jq
```

Response:
```json
{
  "data": [
    {
      "id": 21580,
      "first_name": "Marc",
      "last_name": "Abbott",
      "email_1": null,
      "grade_level": 6,
      "school_level": 3,
      "last_modified_date": "2020-11-09T22:19:00Z"
    },
    {
      "id": 41278,
      "first_name": "Sheila",
      "last_name": "Abbott",
      "email_1": null,
      "grade_level": 3,
      "school_level": 2,
      "last_modified_date": "2020-11-09T21:34:00Z"
    }
  ]
}
```

For demonstration purposes, the page size is set to only two records in order to show the full response without being overwhelming. See [Pagination](../concepts/pagination.md) for more details.

## Conclusion

This concludes our step by step guide to demonstrate how to make a request to the Data API. Visit our [API Request diagram](../diagrams/api-request.md) for a quick reference.

Please contact support if you have any additional questions, and good luck!
