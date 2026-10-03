---
stoplight-id: bd08d5lpygdl1
---

# Using the OneRoster API

### Base URL

The base URL for requests to the OneRoster API is `https://oneroster.veracross.com/{school route}/ims/oneroster/v1p1/` followed by the endpoint path.

You are responsible for filling in the `school route` portion of the URL to match the school you're working with.

> Note: The appropriate `school route` is shown for each school in the Partner Portal, or it can be provided by each school. For reference, it's the same for the other Veracross apps at the school such as Axiom and Portals.

An example request to the `schools` endpoint would look like this (where `api-sandbox` is an example school route):

```text
https://oneroster.veracross.com/api-sandbox/ims/oneroster/v1p1/schools
```

### Security

Please only make requests using the `https` protocol. **Don't** build your integration to expect that `http` will redirect to `https` automatically.

### Authorization

All requests to OneRoster API endpoints should include the `Authorization` header with your access token. You can review our documentation for creating access tokens [here](access-tokens.md).

| Request Header | Default | Allowed Values | Optional/Required |
|----------------|---------|----------------|-------------------|
| `Authorization` | (none) | `Bearer your-access-token-here` | Required for OneRoster API endpoints<br>Note that there is a single white space between the token type value and the access token value, and this is all one header.<br>For example: `Authorization: Bearer your-access-token-here` |

### Request Format

API requests should be made with the appropriate HTTP Method that corresponds to the OneRoster API operation you're trying to perform.

<!-- theme: warning -->
> Remember, not all theoretically possible operations are turned on for every API endpoint.

| API Operation | HTTP Method | Required Scope (suffix) | Description |
|---------------|-------------|----------------|---------|
| List | GET | `readonly` | View list of records (collection) |
| Read | GET | `readonly` | View a single record (resource) |
| Create | PUT | `createput` | Create a new record |
| Update | PUT | `createput` | Update properties of a single record |
| Delete | DELETE | `delete` | Delete a single record |

#### Creating/Updating Data

When creating or updating records via the OneRoster API, the record data should be sent in the request body as a JSON object. The root object should have a "{endpoint object}" field, which is an object including any fields you intend to include in the create/update operation.

<!-- theme: info -->
> We have implemented a modified method of creating gradebook records that we recommend using. In this model the sourcedId is omitted from the path. When you create records with this method you will conveniently recieve the created record directly in the response body.
> - `PUT https://oneroster.veracross.com/{school_route}/ims/oneroster/v1p1/categories`
> - `PUT https://oneroster.veracross.com/{school_route}/ims/oneroster/v1p1/LineItems`
> - `PUT https://oneroster.veracross.com/{school_route}/ims/oneroster/v1p1/results`

For example, if you wanted to create a new Line Item Category, the request body could look like this:

```json
// http put oneroster.veracross.com/api-sandbox/ims/oneroster/v1p1/categories

{
  "category": {
    "title": "My new Line Item Category"
  }
}

// 'sourcedId' is an optional field, if you would like to use a specific value you may provided it here. The only required field for creation is the 'title'.

// The response of '201' (Created Successfully) will be accompanied by the created record object in the response body.
{
  "category": [
    {
      "sourcedId": "abc123",
      "status": "active",
      "dateLastModified": "some datetime",
      "title": "My new Line Item Category"
    }
  ]
}
```

If you then needed to update the title for this Line Item Category, the request body would look like this:

```json
// http put oneroster.veracross.com/api-sandbox/ims/oneroster/v1p1/categories/abc123

{
  "category": {
    "title": "My updated Line Item Category"
  }
}

// `sourcedId` field is not updatable and the `dateLastModified` value will be determined at the time of the data record change in a Veracross school
```

<!-- theme: info -->
> When creating records, refer to the endpoint documentation for the list of required and optional fields to be used in the request body. Update requests only require the fields you are updating to be included in the request body.

### Response Format

If a OneRoster API endpoint returns a response, the response data will be a JSON formatted string.

- Update and delete operations typically don't return a response object. You will need to check the HTTP response code to verify that your API request was successful.
- When creating a record with the modifieds method, the 201 ('Created Successfully') response will contain the created record. If using the standard endpoint the response will be empty.
- Collection endpoints (eg, those **without** an "id" at the end of the URL) will return an array of objects for the endpoint object (it will always be an array even if there are zero or one objects returned).
- Resource endpoints (eg, those **with** an "id" at the end of the URL) will return an object for the endpoint object.
