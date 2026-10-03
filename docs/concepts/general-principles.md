# General Principles

The Veracross API uses modern programming techniques. These include:

- HTTP-based API requests using JSON data format
- REST-style POST/GET/PATCH/DELETE verbs for create/read/update/delete operations
- TLS encryption required for all requests (e.g., HTTPS)
- Paginated response data
- OAuth 2.0 Access Tokens
- Single Sign On (SSO) via OAuth 2.0 or OpenID Connect 1.0 (OIDC)
- Granular OAuth Scopes for permission control

### Data Liveliness

The Veracross API is a "pull" based system. Vendor/partner systems make API requests to the Veracross API, and the Veracross API responses provide the latest data for that school.

Changes made through the Veracross API are immediately visible in other applications, and changes in Veracross applications are immediately available though the API.

<!-- theme: info -->
> Note: How often data shown in Partner applications is refreshed depends on that particular integration. Schools should work directly with their partners to understand Partner integration logic.

### OAuth Applications

In order to use the Veracross API, you must have a pre-approved OAuth Application configured. This includes our API Sandbox and separately for each school you work with.

Review [Access Tokens](./access-tokens.md) for additional details.

### Working with dates & times

Most date & time fields that store school data are implicitly in the school's local time zone. There are also system-managed date/time fields on many endpoints which are UTC.

<!--
title: Example API response data
-->
```json
{
    "data": {
        "start_date": "2026-03-11",
        "start_time": "13:58:02",
        "last_modified_date": "2001-02-03T04:05:06Z"
    }
}
```

The endpoint documentation pages show the data type and format for each field. Date/time fields are strings with a `format` property defined by the [OpenAPI format registry](https://spec.openapis.org/registry/format/#values).

| Field | Data Type & Format Code |  Example | Format Definition |
|-------|-------------------------|----------|-------------------|
| Date (only) | `string<date>` | `"2026-03-11"` | date as defined by `full-date` - [RFC3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6) |
| Time (only) | `string<time-local>` | `"13:58:02"` | [RFC3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6) time without the timezone component |
| Date + Time timestamp | `string<date-time>` | `"2001-02-03T04:05:06Z"` | date and time as defined by `date-time` - [RFC3339](https://www.rfc-editor.org/rfc/rfc3339#section-5.6) |
