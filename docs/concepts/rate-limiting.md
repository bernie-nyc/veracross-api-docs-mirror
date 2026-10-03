# Rate Limiting

All requests to the Data API are subject to rate limiting. The basis of the limit is the Access Tokens.

Each Access Token is limited to 300 requests every 3 minutes from the first request. Every 3 minutes, the limit will reset. When the rate limit is exceeded, an HTTP `429 Too many requests` response will be issued, see [Errors](./errors.md) for more details.

### Response Headers

Each response from the Data API will include rate limiting headers. You can use these headers to avoid exceeding the allotted request capacity.

| Response Header | Description |
|--------------------|--------------|
| `X-Rate-Limit-Limit` | The maximum number of requests per limit period. |
| `X-Rate-Limit-Remaining` | The number of requests remaining in the current limiting period. |
| `X-Rate-Limit-Reset` | The timestamp when the current limiting period resets. |
