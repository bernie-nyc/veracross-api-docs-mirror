# Authorization API - Recent Changelog

## October 2025

### 2025-10-27

#### GET /oauth/userinfo

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the media type `application/json` for the response with the status `415` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the non-success response with the status `401` |

#### POST /oauth/introspect

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the non-success response with the status `404` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the media type `application/json` for the response with the status `415` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the non-success response with the status `401` |

#### POST /oauth/revoke

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the media type `application/json` for the response with the status `401` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the media type `application/json` for the response with the status `415` |

#### POST /oauth/token

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `client_secret` became required |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the media type `application/xml` from the request body |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the media type `application/json` for the response with the status `415` |

### 2025-10-02

#### POST /oauth/token

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the non-success response with the status `400` |

## September 2025

### 2025-09-15

#### POST /oauth/token

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the optional property `error_id` to the response with the `401` status |

## February 2025

### 2025-02-24

#### POST /oauth/token

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the optional property `error_id` to the response with the `401` status |

## October 2023

### 2023-10-12

#### GET /oauth/userinfo

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the non-success response with the status `404` |

## July 2023

### 2023-07-20

#### GET /oauth/userinfo

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `email` became optional |

#### POST /oauth/token

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `refresh_token` to request property `grant_type` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the optional property `refresh_token` |

### 2023-07-18

#### GET /oauth/userinfo

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the optional property `roles` |

## April 2023

### 2023-04-12

#### GET /oauth/userinfo

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `email` |

## January 2023

### 2023-01-27

#### POST /oauth/introspect

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the media type `application/json` from the request body |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the media type `application/x-www-form-urlencoded` to the request body |

#### POST /oauth/revoke

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the media type `application/json` from the request body |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the media type `application/x-www-form-urlencoded` to the request body |

#### POST /oauth/token

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the media type `application/json` from the request body |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the media type `application/x-www-form-urlencoded` to the request body |

## June 2022

### 2022-06-24

#### GET /oauth/authorize

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the non-success response with the status `415` |

## December 2020

### 2020-12-07

Initial documentation published

## April 2019

### 2019-04-08

First Authorization API release

### Older updates

For older updates, please refer to the [full changelog history](./docs/changelogs/Authorization-API.full.md).

