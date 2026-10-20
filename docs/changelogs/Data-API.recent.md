# Data API - Recent Changelog

## October 2026

### 2026-10-19

#### Other Changes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | A breaking change was detected but the version is still `3.0.0` |

#### GET /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `grading_period_group_id` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.grading_period_group_id` to the response with the `200` status |

#### GET /academics/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `grading_period_group_id` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.grading_period_group_id` to the response with the `200` status |

#### GET /academics/config/grading_periods

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `active` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.active` to the response with the `200` status |

#### GET /academics/config/grading_periods/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.active` to the response with the `200` status |

#### PATCH /academics/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.grading_period_group_id` |

#### POST /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.grading_period_group_id` |

### 2026-10-15

#### Other Changes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | A breaking change was detected but the version is still `3.0.0` |

#### GET /person_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.account_type` became read-only for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.external_username` became read-only for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person_id` became read-only for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.primary_portal` became read-only for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `mfa_status` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.mfa_status` to the response with the `200` status |

#### GET /person_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.account_type` became read-only for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.external_username` became read-only for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person_id` became read-only for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.primary_portal` became read-only for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `mfa_status` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.mfa_status` to the response with the `200` status |

#### PATCH /person_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-10-08

#### GET /development/gifts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `gift_reference_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.gift_reference_id` to the response with the `200` status |

#### GET /development/gifts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.gift_reference_id` to the response with the `200` status |

#### GET /events/group_events

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.internal_location_resource_description` to the response with the `200` status |

#### GET /events/group_events/{event_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.internal_location_resource_description` to the response with the `200` status |

#### GET /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.merged_from` to the response with the `200` status |

#### GET /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.merged_from` to the response with the `200` status |

### 2026-10-06

#### GET /finance/ap_disbursements

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.settled` to the response with the `200` status |

#### GET /finance/ap_disbursements/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.settled` to the response with the `200` status |

#### PATCH /finance/ap_disbursements/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.settled` |

#### POST /finance/ap_disbursements

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.settled` |

## September 2026

### 2026-09-23

#### Other Changes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | A breaking change was detected but the version is still `3.0.0` |

#### GET /academics/rooms

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.abbreviation` response property's maxlength was increased from `8` to `20` for the response status `200` |

#### GET /academics/rooms/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.abbreviation` response property's maxlength was increased from `8` to `20` for the response status `200` |

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.room.abbreviation` response property's maxlength was increased from `8` to `20` for the response status `200` |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.room.abbreviation` response property's maxlength was increased from `8` to `20` for the response status `200` |

#### GET /resource_reservations/reservations

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.resource_abbreviation` response property's maxlength was increased from `8` to `20` for the response status `200` |

#### GET /resource_reservations/reservations/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.resource_abbreviation` response property's maxlength was increased from `8` to `20` for the response status `200` |

#### PATCH /resource_reservations/reservations/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.resource_abbreviation` request property's maxlength was increased from `8` to `20` |

### 2026-09-22

#### Other Changes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | A breaking change was detected but the version is still `3.0.0` |

#### GET /academics/class_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.room.abbreviation` response property's maxlength was increased from `8` to `20` for the response status `200` |

#### GET /resource_reservations/resources

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.abbreviation` response property's maxlength was increased from `8` to `20` for the response status `200` |

#### GET /resource_reservations/resources/{resource_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.abbreviation` response property's maxlength was increased from `8` to `20` for the response status `200` |

#### PATCH /resource_reservations/resources/{resource_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.abbreviation` request property's maxlength was increased from `8` to `20` |

#### POST /resource_reservations/resources

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.abbreviation` request property's maxlength was increased from `8` to `20` |

### 2026-09-21

#### GET /ethnicities

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /person_ethnicities

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-09-16

#### GET /genders

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /person_citizenships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /person_citizenships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /resident_statuses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /withdrawal_reasons

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-09-09

#### GET /academics/config/grade_levels

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /convert_parent_to_staff

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## August 2026

### 2026-08-31

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.cancelled` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.posted` to the response with the `200` status |

#### GET /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.cancelled` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.posted` to the response with the `200` status |

#### PATCH /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.cancelled` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.posted` |

### 2026-08-28

#### Other Changes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | A breaking change was detected but the version is still `3.0.0` |

#### GET /security_roles

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

### 2026-08-21

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `internal_group_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.internal_group_id` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.track_class_attendance` to the response with the `200` status |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.internal_group_id` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.track_class_attendance` to the response with the `200` status |

#### GET /standardized_tests/scores

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `created_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_after_created_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_before_created_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.created_date` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` to the response with the `200` status |

#### GET /standardized_tests/scores/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.created_date` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` to the response with the `200` status |

#### GET /standardized_tests/tests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `created_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_after_created_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_before_created_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.created_date` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` to the response with the `200` status |

#### GET /standardized_tests/tests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.created_date` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` to the response with the `200` status |

#### PATCH /standardized_tests/scores/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.created_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.last_modified_date` |

#### PATCH /standardized_tests/tests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.created_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.last_modified_date` |

#### POST /standardized_tests/tests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.created_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.last_modified_date` |

### 2026-08-20

#### GET /relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `related_person_is_deceased` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.related_person_is_deceased` to the response with the `200` status |

#### GET /relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.related_person_is_deceased` to the response with the `200` status |

### 2026-08-19

#### GET /athletics/coaches/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /class_permissions/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-08-17

#### GET /programs/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `internal_course_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `internal_group_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_after_begin_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_after_end_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_before_begin_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_before_end_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `school_level_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.course_name` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.internal_group_id` to the response with the `200` status |

### 2026-08-07

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `unpaid_only` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `vendor_id` |

### 2026-08-06

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `query` request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `query` request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `query` request parameter `unpaid_only` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `query` request parameter `vendor_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.external_po_number` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.external_po_url` to the response with the `200` status |

#### GET /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.external_po_number` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.external_po_url` to the response with the `200` status |

#### PATCH /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.external_po_number` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.external_po_url` |

#### POST /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.external_po_number` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.external_po_url` |

### 2026-08-04

#### GET /staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.departments` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.school_levels` to the response with the `200` status |

#### GET /staff_faculty/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.departments` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.school_levels` to the response with the `200` status |

## July 2026

### 2026-07-31

#### GET /portal_membership

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /portal_membership/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /portal_membership/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.do_not_pay` |

### 2026-07-29

#### GET /directory/staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.biography` response property's maxlength was increased from `3000` to `4000` for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.photo_url` response property's maxlength was unset from `250` for the response status `200` |

### Older updates

For older updates, please refer to the [full changelog history](./docs/changelogs/Data-API.full.md).

