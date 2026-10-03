# Breaking Changes Policy

We may publish incremental non-breaking changes to API endpoints. Examples of **non-breaking** changes include:

- New endpoints created, or new scopes added for existing endpoints
- Adding optional parameters added to existing endpoints, or changing the default value of parameters
- Adding new request headers, or changing the default value of request headers
- Adding new fields to response objects. When you make API requests, your system **must** be prepared to receive more fields than you might have in the past
- Adding more top level keys besides `data` and `value_lists`
- Different values for fields which seem unchanging day-to-day. For example, if we change the access token expiration, that would be a non-breaking change. Whenever possible, your system should avoid hard-coding assumptions about values in API responses, and instead process the API response as provided
- Adding new errors or HTTP response codes
- Rephrased or reworded error messages. Avoid building app logic based on the specific wording of specific error messages. Instead, app logic should be based on HTTP response status codes
