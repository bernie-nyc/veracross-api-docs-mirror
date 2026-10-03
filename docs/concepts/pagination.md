# Pagination

All collection responses from the Data API are paginated. This means you might not see all of the data in a single API request, and several requests will be needed to load all of the data. The default page size is 100 records, but you can request a custom page size between 1 and 1000 records as needed via the optional page size header.

<!-- theme: warning -->
> Handling pagination is mandatory and can't be bypassed.

The page number starts at `1`, and you can request subsequent pages by increasing the value of the page number header. If a collection response includes fewer records than the page size (including zero records) then you have reached the end of the data. Subsequent requests for page numbers after the end of the data will continue to be empty, so it's best to always check the number of records in a response before issuing a request for the next page number.

### Headers

| Request Header | Default | Allowed Values | Optional/Required |
|----------------|---------|----------------|-------------------|
| `X-Page-Number` | 1 | Min: 1, Max: No limit | Optional |
| `X-Page-Size` | 100 | Min: 1, Max: 1000 | Optional |
