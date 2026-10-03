# Using the Data API

### Base URL

The base URL for requests to the Data API is `https://api.veracross.com/{school_route}/v3/` followed by the endpoint path.

You are responsible for filling in the `school route` portion of the URL to match the school you're working with.

> Note: The appropriate `school route` is shown for each school in the Partner Portal, or it can be provided by each school. For reference, it's the same for the other Veracross apps at the school such as Axiom and Portals.

An example request to the `students` endpoint would look like this (where `api-sandbox` is an example school route):

```
https://api.veracross.com/api-sandbox/v3/students
```

### Security

Please only make requests using the `https` protocol. **Don't** build your integration to expect that `http` will redirect to `https` automatically.

### Authorization

All requests to Data API endpoints should include the `Authorization` header.

| Request Header | Default | Allowed Values | Optional/Required |
|----------------|---------|----------------|-------------------|
| `Authorization` | (none) | `Bearer your-access-token-here` | Required for Data API endpoints<br>Note that there is a single white space between the token type value and the access token value, and this is all one header.<br>For example: `Authorization: Bearer your-access-token-here` |

### Request Format

API requests should be made with the appropriate HTTP Method that corresponds to the Data API operation you're trying to perform.

<!-- theme: warning -->
> Remember, not all theoretically possible operations are turned on for every API endpoint.

| API Operation | HTTP Method | Required Scope (suffix) | Description |
|---------------|-------------|----------------|---------|
| List | GET | `list` | View list of records (collection) |
| Create | POST | `create` | Create a new record |
| Read | GET | `read` | View a single record (resource) |
| Update | PATCH | `update` | Update properties of a single record |
| Delete | DELETE | `delete` | Delete a single record |

#### Creating/Updating Data

When creating or updating records via the Data API, the record data should be sent in the request body as a JSON object. The root object should have a `data` field, which is an object including any fields you intend to include in the create/update operation. It isn't necessary to include _every_ possible field in _every_ create/update operation.

<!-- theme: info -->
> All "update" operations in the Data API are `PATCH` updates. These updates only write to the fields you provide, and fields not provided in an update won't be affected. Another kind of update uses `PUT`, which replaces the entire object all at once. The new Veracross Data API only supports `PATCH` updates.

For example, if you wanted to update the notes for a Student Logistics Request, the request body would look like this:

```json
// http post api.veracross.com/api-sandbox/v3/student_logistics_requests/13579

{
  "data": {
    "request_notes": "Here's some updated request notes"
  }
}
```

### Response Format

If a Data API endpoint returns a response, the response data will be a JSON formatted string.

- Update and delete operations don't return a response object, so you will need to check the HTTP response code to verify that your API request was successful.
- When creating a record, the data object will only contain the `id` field, and the value will be the new record id.
- Collection endpoints (eg, those **without** an "id" in the URL) will return an array of objects for the `data` field (it will always be an array even if there are zero or one objects returned).
- Resource endpoints (eg, those **with** an "id" in the URL) will return an object for the `data` field.

| Response | |
|---|---|
| data | - an array of record data (list operations) <br>- a single record data object (read/create operations)<br>- not present (other operations) |
| value_lists | An array of value list objects<br>See [Value Lists](./value-lists.md) for details |
