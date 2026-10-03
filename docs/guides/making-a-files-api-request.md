# Making a Files API request

In this guide, you will follow a step by step process to upload a new Person Photo.

> Note: This guide uses [HTTPie](https://httpie.io/), a cross-platform tool for making HTTP requests on the command line. Other popular tools for doing this include [Curl](https://curl.se/), [Insomnia](https://insomnia.rest/products/insomnia), and [Postman](https://www.postman.com/product/api-client/). Many tools and libraries are interoperable with the Veracross API, since it's based on standards such as OAuth, HTTP, and JSON. However, you may need to adjust the examples to match how your chosen tool works.

## Before You Begin

The available Files API endpoints and their corresponding operations are listed on the left, under the **FILES API** header. You can click into each listing for more details. Each page will show the API request path, parameters, and fields.

For the purposes of this guide, you'll be making requests to:
- [Create Person Photo](../../reference/Files-API.yaml/paths/~1person_photo/post)
- [Read Person Photo](../../reference/Files-API.yaml/paths/~1person_photo~1{id}/get)

You can refer back to different parts of the API endpoint page throughout this guide.

## Step 1: Configure the required OAuth Application details

All requests to the Files API require authorization with an OAuth Access Token. You'll need to create these tokens yourself with the Authorization API, but first you'll need to get the details from your registered OAuth Application.

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

Each request documentation shows the scopes it needs:
- [Create Person Photo](../../reference/Files-API.yaml/paths/~1person_photo/post): `files:person_photo:create`
- [Read Person Photo](../../reference/Files-API.yaml/paths/~1person_photo~1{id}/get): `files:person_photo:read`

> Note: All Files API scopes start with the `files:` prefix.

Here's what it looks like to enable the required scopes on an OAuth Application in Axiom:

![example-oauth-application-files-api-scopes](https://assets.veracross.com/_documentation/api/images/example-oauth-application-files-api-scopes.png)

> Note: OAuth Applications can only be configured by school users with the `OAuth_App_Admin` role.

Apart from this guide, schools will typically hear the list of scopes that each Vendor/Partner needs to enable the data access that their integration requires from that Vendor/Partner during the integration process. Only the minimum required scopes should be made active. Schools are in control of their own data, and may possibly decline to enable certain requested scopes on a case by case basis.

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

Next, you need to get an access token via the Authorization API. The technical documentation for each endpoint is listed to the left under the "Authorization API" header. The concepts described in this step are also explained in [Access Tokens](../concepts/access-tokens.md), so be sure to review that page for more details.

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

Request:
```
$ http --print b --form POST https://accounts.veracross.com/api-sandbox/oauth/token grant_type=client_credentials client_id=3121633c13ce45dc94946ff2b33622b7 client_secret=${VC_OAUTH_CLIENT_SECRET} scope='files:person_photo:create files:person_photo:read'
```

Response:
```json
{
  "access_token": "6826395b0f7b85b164b4721fdf2e9c87f6d7a30c7846b75d3692debe1c65af1e",
  "created_at": 1730783650,
  "expires_in": 3600,
  "scope": "files:person_photo:create files:person_photo:read",
  "token_type": "Bearer"
}
```

<!-- theme: warning -->
> Note: This particular Access Token won't actually work for you... you'll need to make your own!

## Step 3: Create a new File record

Now you're ready to use the Files API. All requests follow this format:

```
https://api.veracross.com/{school_route}/v3/files/{request path}
```

Per the documentation for [Create Person Photo](../../reference/Files-API.yaml/paths/~1person_photo/post), the request path for this endpoint is `person_photo`. Replace the school route with what you learned in the previous step. In this case the full Files API request URL is:
`https://api.veracross.com/api-sandbox/v3/files/person_photo`

You'll need to provide the Access Token from the previous step as the `Authorization` header in the request. The token value should be prefixed with the `token_type` as instructed by the token request, which is `Bearer`. Therefore in this case the full header is:
`Authorization: Bearer 6826395b0f7b85b164b4721fdf2e9c87f6d7a30c7846b75d3692debe1c65af1e`

Finally, the request documentation page states that a `data.person_id` field is required in the request body:
```json
{
  "data": {
    "person_id": 21580
  }
}
```

> Note: The actual value of `data.person_id` must be a valid ID from that school. Various types of Person records can be loaded through the Data API, for example [List Students](../docs/guides/making-a-data-api-request.md)

You can assemble these pieces to make a HTTP `POST` request to the endpoint URL:
```
$ http --print b POST https://api.veracross.com/api-sandbox/v3/files/person_photo Authorization:'Bearer 6826395b0f7b85b164b4721fdf2e9c87f6d7a30c7846b75d3692debe1c65af1e' data:='{"person_id": 21580}' | jq
```

Response:
```json
{
  "data": {
    "id": 4190
  },
  "upload_url": "https://veracross-files-api-inbox-us-east-1.s3.amazonaws.com/api-sandbox/e7b8c8d2-3f4b-4a2e-9a3b-5f6a7b8c9d0e?x-amz-meta-jwt=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7ImNsaWVudF9yb3V0ZSI6ImFwaS1zYW5kYm94IiwiY2xhc3NpZmljYXRpb25faWQiOi0xMCwiZmlsZV9wayI6Mzg4ODN9LCJpYXQiOjE2MzcyODUwODMsImV4cCI6MTYzNzI4NTM4M30.pP-Jp5vzDZAVjsHoUtIUD-94-Idodz-dTjEBx5k1LJk&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=Z8G7H6F5J4K3L2M1N0O9%2F20241105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241105T053803Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=e3f1c2d4a5b6e7f8c9d0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2"
}
```

As expected from the endpoint documentation page, the `data.id` shows the ID of the new File record we just created. However, we haven't uploaded a file yet.

## Step 4: Upload a file blob

In order to upload a file blob, we need to use the `upload_url` field from the response in previous step, with the following considerations:
1. Make the request using the **PUT** method
2. Provide the file blob in **binary format**
3. Request authorization is part of the upload URL, so we don't need to provide an `Authorization` header or access token as we typically would
    - The upload URL is temporary, and will expire after 5 minutes
    - The upload URL is unique to this particular File record, and can only receive a single blob.
4. An otherwise valid file should be provided. In this case, the [documentation](../../reference/Files-API.yaml/paths/~1person_photo/post) defines that as:
    - Allowed file types: `image/jpg`, `image/jpeg`, `image/png`, `image/gif`
    - Max file size: 2 MB

```
$ http --print h PUT "https://veracross-files-api-inbox-us-east-1.s3.amazonaws.com/api-sandbox/e7b8c8d2-3f4b-4a2e-9a3b-5f6a7b8c9d0e?x-amz-meta-jwt=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7ImNsaWVudF9yb3V0ZSI6ImFwaS1zYW5kYm94IiwiY2xhc3NpZmljYXRpb25faWQiOi0xMCwiZmlsZV9wayI6Mzg4ODN9LCJpYXQiOjE2MzcyODUwODMsImV4cCI6MTYzNzI4NTM4M30.pP-Jp5vzDZAVjsHoUtIUD-94-Idodz-dTjEBx5k1LJk&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=Z8G7H6F5J4K3L2M1N0O9%2F20241105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241105T053803Z&X-Amz-Expires=300&X-Amz-SignedHeaders=host&X-Amz-Signature=e3f1c2d4a5b6e7f8c9d0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2" @image.png
```

> Note: The script uses `--print h` because this operation doesn't have a response body when successful. The meaningful part is the HTTP status code of the response.

<!-- theme: warning -->
> Note: Using a file named `image.png` is not required. Replace it with your own image filename as appropriate.

If you upload after the upload URL has expired you will receive an error. In that case, you would need to make a new [Create Person Photo](../../reference/Files-API.yaml/paths/~1person_photo/post) request to get a fresh `upload_url`.

| Successful Response Status Code | Error Response Status Code |
|---------------------------------|----------------------------|
| 200 OK                          | 403 Forbidden              |

<!-- theme: warning -->
> Note: Receiving a `200 OK` response indicates that the image was successfully uploaded. However, the uploaded image will then undergo a validation process based on its File Classification settings, which checks criteria such as file size, allowed extensions, etc. If any validation errors occur, these details will be provided in the subsequent request (Step 5).

Let's assume the file upload passes all validations. Congratulations! The corresponding Person record now has a new photo.

## Step 5: Read the new File record

According to [Read Person Photo](../../reference/Files-API.yaml/paths/~1person_photo~1{id}/get), the `{id}` parameter in the request path is the File record ID, which is the `data.id` field from step 3:

```
$ http --print b GET https://api.veracross.com/api-sandbox/v3/files/person_photo/4190 Authorization:'Bearer 6826395b0f7b85b164b4721fdf2e9c87f6d7a30c7846b75d3692debe1c65af1e' | jq
```

Assuming no errors, `data.download_url` holds the public URL for the image file we just uploaded:
```json
{
  "data": {
    "id": 4190,
    "person_id": 21580,
    "status": 2,
    "error": null,
    "download_url": "https://res.cloudinary.com/veracross/image/upload/w_300,h_300,c_limit/v1731626289/api-sandbox/person_photos/361212cc-042f-4ec1-93ad-6706f7fb6cd7.png",
    "notes": null,
    "last_modified_date": "2024-11-05T06:19:41Z"
  }
}
```

<!-- theme: warning -->
> Note: `data.download_url` holds the public URL of the image we just uploaded. This URL is public and non-expiring, so be cautious about where you use it. Ensure that you do not expose this URL in places where it could be accessed by unauthorized users or vendors. **In a future release, this URL will have a set expiration.**

## Conclusion

This concludes our step by step guide to demonstrate how to use the Files API.

Please contact support if you have any additional questions, and good luck!
