# Data API - Full Changelog

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

### 2026-07-28

#### GET /finance/ap_disbursements

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the `query` request parameter `on_or_after_last_modified_date`, the `format` was widened from `date` to `date-time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the `query` request parameter `on_or_before_last_modified_date`, the `format` was widened from `date` to `date-time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.input_date` response's property `format` changed from `date` to `date-time` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.last_modified_date` response's property `format` changed from `date` to `date-time` for status `200` |

#### GET /finance/ap_disbursements/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.input_date` response's property `format` changed from `date` to `date-time` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.last_modified_date` response's property `format` changed from `date` to `date-time` for status `200` |

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the `query` request parameter `on_or_after_last_modified_date`, the `format` was widened from `date` to `date-time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the `query` request parameter `on_or_before_last_modified_date`, the `format` was widened from `date` to `date-time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.last_modified_date` response's property `format` changed from `date` to `date-time` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.input_date` to the response with the `200` status |

#### GET /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.last_modified_date` response's property `format` changed from `date` to `date-time` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.input_date` to the response with the `200` status |

#### PATCH /finance/ap_disbursements/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.input_date` request property `format` was widened from `date` to `date-time` |

#### PATCH /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.input_date` |

### 2026-07-17

#### GET /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `track_class_attendance` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `trigger_imperfect_attendance` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.track_class_attendance` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.trigger_imperfect_attendance` to the response with the `200` status |

### 2026-07-16

#### GET /academics/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.track_class_attendance` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.trigger_imperfect_attendance` to the response with the `200` status |

#### PATCH /academics/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.track_class_attendance` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.trigger_imperfect_attendance` |

#### POST /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.track_class_attendance` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.trigger_imperfect_attendance` |

### 2026-07-07

#### GET /finance/gl_accounts/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.gl_account_long_description` to the response with the `200` status |

#### GET /finance/gl_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.gl_account_long_description` to the response with the `200` status |

### 2026-07-01

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.do_not_pay` to the response with the `200` status |

#### GET /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.do_not_pay` to the response with the `200` status |

#### PATCH /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.do_not_pay` |

## June 2026

### 2026-06-29

#### GET /finance/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.ap_description` response property's maxlength was increased from `50` to `200` for the response status `200` |

#### GET /finance/ap_invoice_items/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.ap_description` response property's maxlength was increased from `50` to `200` for the response status `200` |

#### PATCH /finance/ap_invoice_items/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.ap_description` request property's maxlength was increased from `50` to `200` |

#### POST /finance/ap_invoices/{invoice_id}/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.ap_description` request property's maxlength was increased from `50` to `200` |

### 2026-06-26

#### GET /finance/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.tax_amount` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.tax_type.description` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.tax_type.tax_percent` to the response with the `200` status |

#### GET /finance/ap_invoice_items/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.tax_amount` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.tax_type.description` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.tax_type.tax_percent` to the response with the `200` status |

#### GET /finance/tax_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.tax_percent` to the response with the `200` status |

#### GET /finance/tax_types/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.tax_percent` to the response with the `200` status |

#### PATCH /finance/ap_invoice_items/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.tax_amount` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.tax_type.description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.tax_type.tax_percent` |

#### POST /finance/ap_invoices/{invoice_id}/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.tax_amount` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.tax_type` |

### 2026-06-25

#### GET /households

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.phone` became read-only for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.phone` response property's maxlength was unset from `30` for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `active_address` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `primary_address_country` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `secondary_address_1_country` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `secondary_address_2_country` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.active_address` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_city` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_country` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_line_1` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_line_2` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_line_3` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_phone` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_state_or_province` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_zip` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_city` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_country` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_line_1` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_line_2` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_line_3` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_phone` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_state_or_province` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_zip` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_city` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_country` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_line_1` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_line_2` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_line_3` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_phone` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_state_or_province` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_zip` to the response with the `200` status |

#### GET /households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.phone` became read-only for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.phone` response property's maxlength was unset from `30` for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `active_address` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `primary_address_country` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `secondary_address_1_country` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `secondary_address_2_country` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.active_address` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_city` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_country` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_line_1` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_line_2` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_line_3` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_phone` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_state_or_province` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_zip` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_city` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_country` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_line_1` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_line_2` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_line_3` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_phone` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_state_or_province` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_zip` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_city` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_country` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_line_1` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_line_2` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_line_3` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_phone` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_state_or_province` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_zip` to the response with the `200` status |

#### PATCH /households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-06-22

#### DELETE /person_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-06-17

#### GET /finance/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.tax_amount` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.tax_type.description` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.tax_type.tax_percent` from the response with the `200` status |

#### GET /finance/ap_invoice_items/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.tax_amount` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.tax_type.description` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.tax_type.tax_percent` from the response with the `200` status |

#### GET /finance/tax_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.tax_percent` from the response with the `200` status |

#### GET /finance/tax_types/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.tax_percent` from the response with the `200` status |

#### PATCH /finance/ap_invoice_items/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.tax_amount` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.tax_type.description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.tax_type.tax_percent` |

#### POST /finance/ap_invoices/{invoice_id}/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.tax_amount` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.tax_type` |

### 2026-06-16

#### GET /person_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the `query` request parameter `external_username`, the maxlength was set to `255` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.account_type` read-only status was removed for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.external_username` read-only status was removed for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person_id` read-only status was removed for the status `200` |

#### GET /person_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.account_type` read-only status was removed for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.external_username` read-only status was removed for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person_id` read-only status was removed for the status `200` |

### 2026-06-10

#### GET /households

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the `query` request parameter `on_or_after_last_modified_date`, the type/format was changed from `string`/`` to `string`/`date-time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the `query` request parameter `on_or_before_last_modified_date`, the type/format was changed from `string`/`` to `string`/`date-time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.phone` read-only status was removed for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.active_address` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.primary_address_city` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.primary_address_country` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.primary_address_line_1` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.primary_address_line_2` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.primary_address_line_3` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.primary_address_phone` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.primary_address_state_or_province` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.primary_address_zip` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_1_city` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_1_country` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_1_line_1` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_1_line_2` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_1_line_3` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_1_phone` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_1_state_or_province` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_1_zip` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_2_city` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_2_country` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_2_line_1` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_2_line_2` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_2_line_3` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_2_phone` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_2_state_or_province` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.secondary_address_2_zip` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `active_address` enum value from the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `primary_address_country` enum value from the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `secondary_address_1_country` enum value from the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `secondary_address_2_country` enum value from the `value_lists.items.fields.items` response property for the response status `200` |

#### GET /households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.phone` read-only status was removed for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.active_address` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.primary_address_city` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.primary_address_country` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.primary_address_line_1` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.primary_address_line_2` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.primary_address_line_3` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.primary_address_phone` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.primary_address_state_or_province` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.primary_address_zip` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_1_city` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_1_country` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_1_line_1` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_1_line_2` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_1_line_3` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_1_phone` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_1_state_or_province` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_1_zip` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_2_city` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_2_country` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_2_line_1` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_2_line_2` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_2_line_3` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_2_phone` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_2_state_or_province` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.secondary_address_2_zip` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `active_address` enum value from the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `primary_address_country` enum value from the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `secondary_address_1_country` enum value from the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `secondary_address_2_country` enum value from the `value_lists.items.fields.items` response property for the response status `200` |

#### PATCH /households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API removed  |

### 2026-06-08

#### GET /households

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the `query` request parameter `on_or_after_last_modified_date`, the type/format was generalized from `string`/`date-time` to `string`/`` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the `query` request parameter `on_or_before_last_modified_date`, the type/format was generalized from `string`/`date-time` to `string`/`` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.phone` became read-only for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.phone` response property's maxlength was unset from `30` for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `active_address` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `primary_address_country` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `secondary_address_1_country` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `secondary_address_2_country` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.active_address` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_city` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_country` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_line_1` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_line_2` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_line_3` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_phone` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_state_or_province` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_address_zip` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_city` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_country` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_line_1` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_line_2` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_line_3` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_phone` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_state_or_province` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_1_zip` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_city` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_country` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_line_1` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_line_2` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_line_3` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_phone` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_state_or_province` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.secondary_address_2_zip` to the response with the `200` status |

#### GET /households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.phone` became read-only for the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.phone` response property's maxlength was unset from `30` for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `active_address` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `primary_address_country` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `secondary_address_1_country` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `secondary_address_2_country` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.active_address` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_city` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_country` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_line_1` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_line_2` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_line_3` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_phone` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_state_or_province` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_address_zip` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_city` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_country` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_line_1` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_line_2` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_line_3` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_phone` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_state_or_province` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_1_zip` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_city` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_country` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_line_1` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_line_2` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_line_3` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_phone` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_state_or_province` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.secondary_address_2_zip` to the response with the `200` status |

#### PATCH /households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /households

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.active_address` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_1_city` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_1_country` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_1_line_1` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_1_line_2` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_1_line_3` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_1_phone` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_1_state_or_province` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_1_zip` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_2_city` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_2_country` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_2_line_1` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_2_line_2` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_2_line_3` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_2_phone` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_2_state_or_province` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.secondary_address_2_zip` |

## May 2026

### 2026-05-28

#### GET /event_representatives

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /household_vehicles

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /household_vehicles/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-05-26

#### GET /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.attendance_return_time` response's property type/format changed from `string`/`time-local` to `string`/`date-time` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.attendance_time` response's property type/format changed from `string`/`time-local` to `string`/`date-time` for status `200` |

#### GET /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_return_time` response's property type/format changed from `string`/`time-local` to `string`/`date-time` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_time` response's property type/format changed from `string`/`time-local` to `string`/`date-time` for status `200` |

#### PATCH /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_return_time` request property type/format changed from `string`/`time-local` to `string`/`date-time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_time` request property type/format changed from `string`/`time-local` to `string`/`date-time` |

#### POST /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_return_time` request property type/format changed from `string`/`time-local` to `string`/`date-time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_time` request property type/format changed from `string`/`time-local` to `string`/`date-time` |

### 2026-05-22

#### GET /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.attendance_return_time` response's property type/format changed from `string`/`date-time` to `string`/`time-local` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.attendance_time` response's property type/format changed from `string`/`date-time` to `string`/`time-local` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.extended_care_arrival_time` response's property type/format changed from `string`/`date-time` to `string`/`time-local` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.extended_care_leave_time` response's property type/format changed from `string`/`date-time` to `string`/`time-local` for status `200` |

#### GET /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_return_time` response's property type/format changed from `string`/`date-time` to `string`/`time-local` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_time` response's property type/format changed from `string`/`date-time` to `string`/`time-local` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.extended_care_arrival_time` response's property type/format changed from `string`/`date-time` to `string`/`time-local` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.extended_care_leave_time` response's property type/format changed from `string`/`date-time` to `string`/`time-local` for status `200` |

#### PATCH /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_return_time` request property type/format changed from `string`/`date-time` to `string`/`time-local` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_time` request property type/format changed from `string`/`date-time` to `string`/`time-local` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.extended_care_arrival_time` request property type/format changed from `string`/`date-time` to `string`/`time-local` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.extended_care_leave_time` request property type/format changed from `string`/`date-time` to `string`/`time-local` |

#### POST /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_return_time` request property type/format changed from `string`/`date-time` to `string`/`time-local` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_time` request property type/format changed from `string`/`date-time` to `string`/`time-local` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.extended_care_arrival_time` request property type/format changed from `string`/`date-time` to `string`/`time-local` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.extended_care_leave_time` request property type/format changed from `string`/`date-time` to `string`/`time-local` |

### 2026-05-20

#### GET /transcripts/{person_id}/transcript_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `related_class.class_grade_conversion_scale` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `class_enrollment_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.related_class` to the response with the `200` status |

## April 2026

### 2026-04-29

#### DELETE /person_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API removed  |

#### GET /events/event_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.full_name` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.notes` to the response with the `200` status |

#### GET /events/event_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.full_name` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.notes` to the response with the `200` status |

#### PATCH /events/event_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.notes` |

#### POST /events/event_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.notes` |

### 2026-04-15

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.ap_gl_account_id` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.approval_person_id` to the response with the `200` status |

#### GET /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.ap_gl_account_id` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.approval_person_id` to the response with the `200` status |

#### GET /finance/gl_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /finance/gl_accounts/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/gl_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.posting_prohibited` to the response with the `200` status |

#### GET /finance/projects

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `archived` |

#### PATCH /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.ap_gl_account_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.approval_person_id` |

#### POST /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.vendor` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.ap_gl_account_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.approval_person_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.vendor_id` |

### 2026-04-09

#### GET /academics/student_daily_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.teacher` response's property type/format changed from `integer`/`` to `string`/`` for status `200` |

### 2026-04-08

#### GET /finance/ap_disbursements

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.cash_gl_account_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.vendor_id` |

#### GET /finance/ap_disbursements/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.cash_gl_account_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.vendor_id` |

#### PATCH /finance/ap_disbursements/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.vendor` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.cash_gl_account_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.vendor_id` |

#### POST /finance/ap_disbursements

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.vendor` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.cash_gl_account_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.vendor_id` |

## March 2026

### 2026-03-26

#### GET /finance/gl_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.gl_account_full_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.gl_base_account_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.gl_base_account` |

#### GET /finance/gl_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.gl_account_full_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.gl_base_account_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.gl_base_account` |

### 2026-03-24

#### GET /transcripts/{person_id}/transcript_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.subject.description` response's property type/format changed from `integer` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `subject.description` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_credit_completion_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_credit_completion_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `transfer_school_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `transfer_school_legacy_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.credit_completion_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.transfer_school_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.transfer_school_legacy_id` |

### 2026-03-20

#### Multiple Endpoints

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the `format` property to date/time fields in the documentation |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the `readOnly` property to many fields that weren't updatable in the documentation |

### 2026-03-19

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `student_group` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.student_group` |

### 2026-03-02

#### GET /behavior_incident_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /behavior_incident_types/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /behavior_incident_types/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## February 2026

### 2026-02-10

#### GET /person_enrollment_history

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /person_enrollment_history/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-02-05

#### GET /person_visas

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /person_visas/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /person_visas/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-02-02

#### GET /standardized_tests/scores

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /standardized_tests/scores/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /standardized_tests/tests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /standardized_tests/tests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /standardized_tests/scores/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /standardized_tests/tests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /standardized_tests/tests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## January 2026

### 2026-01-30

#### GET /standardized_tests/score_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /standardized_tests/score_types/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /standardized_tests/test_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /standardized_tests/test_types/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /standardized_tests/score_types/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /standardized_tests/test_types/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /standardized_tests/score_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /standardized_tests/test_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-01-23

#### GET /academics/teacher_daily_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.item_status` response property's maxlength was increased from `11` to `16` |

### 2026-01-22

#### POST /behavior

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.assigned_to_person_id` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.incident_type` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.reporting_person_id` became optional |

### 2026-01-14

#### DELETE /person_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /person_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /person_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /person_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-01-09

#### POST /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.place_of_birth` |

#### POST /households

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.address_line_1` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.address_line_2` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.address_line_3` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.city` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.country` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.phone` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.state_or_province` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.zip` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.primary_address_line_1` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.primary_address_line_2` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.primary_address_line_3` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.primary_city` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.primary_country` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.primary_phone` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.primary_state_or_province` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.primary_zip` |

### 2026-01-08

#### POST /households

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## December 2025

### 2025-12-19

#### GET /events/athletics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `event_type` from the `value_lists.items.fields.items` response property |

#### GET /events/group_events/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `event_type` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `school_level` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.has_multiple_resources` |

#### PATCH /events/athletics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /events/group_events/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /events/athletics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /events/group_events

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-12-18

#### GET /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.place_of_birth` |

#### GET /admission/applicants/{applicant_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.place_of_birth` |

#### PATCH /admission/applicants/{applicant_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.place_of_birth` |

### 2025-12-11

#### GET /events/group_events

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.has_multiple_resources` |

#### GET /events/group_events/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.has_multiple_resources` |

### 2025-12-04

#### GET /events/athletics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.destination_organization` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.transportation_resource` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.destination_organization_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.public` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.transportation_resource_id` |

#### GET /events/athletics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.destination_organization` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.transportation_resource` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.destination_organization_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.public` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.transportation_resource_id` |

#### GET /events/group_events

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.resource_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.public` |

#### GET /events/group_events/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.resource_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.public` |

## November 2025

### 2025-11-17

#### GET /behavior

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `assigned_to_person_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `reporting_person_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `student_id` |

### 2025-11-13

#### GET /events/athletics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /events/athletics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-11-12

#### GET /events/athletics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /events/athletics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## October 2025

### 2025-10-28

#### GET /events/athletics_opponents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /events/athletics_opponents/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-10-24

#### GET /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.direct_deposit_account` response's property type/format changed from `number` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.direct_deposit_bank` response's property type/format changed from `number` to `string` |

#### POST /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.direct_deposit_account` request property type/format changed from `number` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.direct_deposit_account` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.direct_deposit_bank` request property type/format changed from `number` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.direct_deposit_bank` request property's maxlength was set to `20` |

### 2025-10-03

#### GET /transportation/trips

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.destination_address` response property's maxlength was increased from `100` to `120` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.origination_address` response property's maxlength was increased from `100` to `120` |

#### GET /transportation/trips/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.destination_address` response property's maxlength was increased from `100` to `120` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.origination_address` response property's maxlength was increased from `100` to `120` |

## September 2025

### 2025-09-19

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.house` |

### 2025-09-18

#### GET /events/athletics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `on_or_after_end_date`, the maxlength was set to `10` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `on_or_before_end_date`, the maxlength was set to `10` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.campus_departure_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.campus_return_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.class_departure_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.end_date` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.end_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.event_type_description` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.internal_team_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.school_level_description` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.start_date` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.start_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.venue_departure_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.event_type_description` response property's maxlength was unset from `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.school_level_description` response property's maxlength was unset from `50` |

#### GET /events/athletics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.campus_departure_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.campus_return_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.class_departure_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.end_date` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.end_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.event_type_description` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.internal_team_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.school_level_description` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.start_date` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.start_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.venue_departure_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.event_type_description` response property's maxlength was unset from `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.school_level_description` response property's maxlength was unset from `50` |

#### GET /events/group_events

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `on_or_after_end_date`, the maxlength was set to `10` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `on_or_before_end_date`, the maxlength was set to `10` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.campus_departure_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.campus_description` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.campus_return_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.class_departure_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.end_date` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.end_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.event_type_description` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.internal_group_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.school_level_description` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.start_date` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.start_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.student_group_description` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.venue_departure_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.campus_description` response property's maxlength was unset from `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.event_type_description` response property's maxlength was unset from `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.school_level_description` response property's maxlength was unset from `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.student_group_description` response property's maxlength was unset from `20` |

#### GET /events/group_events/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.campus_departure_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.campus_description` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.campus_return_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.class_departure_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.end_date` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.end_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.event_type_description` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.internal_group_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.school_level_description` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.start_date` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.start_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.student_group_description` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.venue_departure_time` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.campus_description` response property's maxlength was unset from `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.event_type_description` response property's maxlength was unset from `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.school_level_description` response property's maxlength was unset from `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.student_group_description` response property's maxlength was unset from `20` |

#### GET /non-academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /non-academics/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /non-academics/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /non-academics/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /non-academics/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /non-academics/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /non-academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /non-academics/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## August 2025

### 2025-08-15

#### GET /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.federal_tax_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.vendor_tax_info` |

#### GET /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.federal_tax_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.vendor_tax_info` |

#### PATCH /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.federal_tax_id` |

#### POST /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.federal_tax_id` |

### 2025-08-13

#### GET /finance/ap_disbursement_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.ap_invoice_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.ap_invoice_item_id` |

#### GET /finance/ap_disbursement_items/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.ap_invoice_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.ap_invoice_item_id` |

#### PATCH /finance/ap_disbursement_items/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.ap_invoice_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.ap_invoice_item_id` |

### 2025-08-12

#### GET /event_groups_members

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /health/all_patients/conditions

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-08-08

#### GET /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.bank_account` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.routing_number` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `inactive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.direct_deposit_account` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.direct_deposit_bank` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.inactive` |

#### GET /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.inactive` |

#### PATCH /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.inactive` |

#### POST /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.inactive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.vendor_id` |

### 2025-08-01

#### GET /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.direct_deposit_account` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.direct_deposit_bank` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.inactive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `inactive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.bank_account` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.routing_number` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.vendor_id` |

#### GET /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.inactive` |

#### PATCH /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.inactive` |

#### POST /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.inactive` |

## July 2025

### 2025-07-31

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `unpaid_only` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `vendor_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.vendor_id` |

#### GET /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.vendor_id` |

#### GET /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.bank_account` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.routing_number` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.vendor_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `inactive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.direct_deposit_account` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.direct_deposit_bank` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.inactive` |

#### GET /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.inactive` |

#### PATCH /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.vendor_id` |

#### PATCH /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.inactive` |

#### POST /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.inactive` |

### 2025-07-30

#### GET /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `internal_group_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.internal_group_id` |

#### GET /academics/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `parent_portal_assignment_display` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `parent_portal_visibility` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `student_portal_assignment_display` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `student_portal_visibility` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.internal_group_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.parent_portal_assignment_display` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.parent_portal_visibility` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.student_portal_assignment_display` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.student_portal_visibility` |

#### GET /academics/student_daily_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `school_year` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `school_year` |

#### PATCH /academics/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.internal_group_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.parent_portal_assignment_display` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.parent_portal_visibility` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.student_portal_assignment_display` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.student_portal_visibility` |

#### POST /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.internal_group_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.parent_portal_assignment_display` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.parent_portal_visibility` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.student_portal_assignment_display` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.student_portal_visibility` |

### 2025-07-25

#### GET /academics/student_daily_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `school_year` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `school_year` |

### 2025-07-24

#### GET /academics/student_daily_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `school_year` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `school_year` |

### 2025-07-23

#### GET /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.inactive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `inactive` |

#### GET /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.inactive` |

#### PATCH /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.inactive` |

### 2025-07-16

#### GET /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `inactive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.inactive` |

#### GET /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.inactive` |

#### PATCH /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.inactive` |

### 2025-07-10

#### GET /resource_reservations/reservations

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.reservation_description` |

#### GET /resource_reservations/reservations/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.reservation_description` |

### 2025-07-04

#### GET /transcripts/{person_id}/gpas

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The query string request parameter `school_year` became optional |

### 2025-07-03

#### GET /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `id` |

## June 2025

### 2025-06-30

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-06-27

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API removed  |

#### GET /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### PATCH /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

### 2025-06-26

#### GET /person_photos

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-06-18

#### GET /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `parent_portal_assignment_display` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `parent_portal_visibility` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `student_portal_assignment_display` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `student_portal_visibility` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `parent_portal_assignment_display` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `parent_portal_visibility` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `student_portal_assignment_display` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `student_portal_visibility` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.course_type` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.parent_portal_assignment_display` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.parent_portal_visibility` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.student_portal_assignment_display` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.student_portal_visibility` |

#### GET /academics/rubric_criteria

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.tag` |

#### GET /academics/rubric_criteria/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.tag` |

#### PATCH /academics/rubric_criteria/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.tag` |

#### POST /academics/rubric_criteria

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.tag` |

### 2025-06-17

#### GET /news

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `external_news_feed` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `external_news_feed` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.external_news_feed` |

#### GET /news/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `external_news_feed` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.external_news_feed` |

### 2025-06-06

#### GET /development/constituents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /development/constituents/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## May 2025

### 2025-05-29

#### GET /transportation/trips

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.stop_number` |

### 2025-05-28

#### DELETE /person_profile_codes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transportation/trips/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.bus_stop_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.stop_number` |

#### POST /person_profile_codes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-05-20

#### GET /person_profile_codes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /person_profile_codes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-05-19

#### GET /academics/assignments/{assignment_id}/grades

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `dropbox_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `publish_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.dropbox_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.publish_status` |

#### GET /academics/assignments/{assignment_id}/grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `dropbox_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `publish_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.dropbox_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.publish_status` |

#### PATCH /academics/assignments/{assignment_id}/grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.dropbox_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.publish_status` |

### 2025-05-14

#### GET /events/athletics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `attendance_taken` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `class_attendance_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `daily_attendance_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `attendance_taken` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.attendance_taken` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.class_attendance_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.daily_attendance_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.display_on_alumni_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.display_on_group_members_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.display_on_parent_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.display_on_staff_faculty_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.display_on_student_calendar` |

#### GET /events/athletics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `attendance_taken` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `class_attendance_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `daily_attendance_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.attendance_taken` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.class_attendance_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.daily_attendance_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.display_on_alumni_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.display_on_group_members_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.display_on_parent_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.display_on_staff_faculty_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.display_on_student_calendar` |

#### GET /events/group_events

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `campus` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `attendance_taken` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `class_attendance_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `daily_attendance_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `event_type` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `attendance_taken` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.attendance_taken` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus_departure_time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus_return_time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.class_attendance_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.class_departure_time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.daily_attendance_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.display_on_alumni_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.display_on_group_members_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.display_on_parent_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.display_on_staff_faculty_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.display_on_student_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.internal_location_resource_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.venue_departure_time` |

#### GET /events/group_events/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `campus` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `attendance_taken` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `class_attendance_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `daily_attendance_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `event_type` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.attendance_taken` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.campus_departure_time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.campus_return_time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.class_attendance_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.class_departure_time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.daily_attendance_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.display_on_alumni_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.display_on_group_members_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.display_on_parent_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.display_on_staff_faculty_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.display_on_student_calendar` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.internal_location_resource_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.venue_departure_time` |

### 2025-05-09

#### GET /finance/gl_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/gl_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-05-07

#### GET /transportation/bus_routes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transportation/bus_routes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transportation/bus_stops

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transportation/bus_stops/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transportation/bus_trips

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transportation/bus_trips/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transportation/schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transportation/schedules/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transportation/trips

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transportation/trips/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-05-06

#### GET /development/constituents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /development/constituents/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /finance/gl_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /finance/gl_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `enrollment_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `enrollment_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.enrollment_status` |

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `enrollment_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.enrollment_status` |

### 2025-05-02

#### GET /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.admissions_notes` |

#### GET /admission/applicants/{applicant_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.admissions_notes` |

#### PATCH /admission/applicants/{applicant_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.admissions_notes` |

## April 2025

### 2025-04-16

#### GET /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `id` |

#### GET /extended_care/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `id` |

#### GET /summer/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `id` |

#### POST /resource_reservations/reservations

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.event_id` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.requesting_person_id` became optional |

### 2025-04-02

#### GET /directory/student

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `campus_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `grade_level_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `homeroom_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `school_level_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `student_group_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `value_lists.items.categories` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `value_lists.items.fields` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `value_lists.items.items` |

## March 2025

### 2025-03-26

#### GET /finance/tax_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `tax_category` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.tax_category` |

#### GET /finance/tax_types/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `tax_category` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.tax_category` |

### 2025-03-25

#### DELETE /event_groups/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /event_groups

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /event_groups/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /event_groups

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-03-20

#### GET /academics/permissions

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course.course_type` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course_type_not` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `course_type_not` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `course_type` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.course.course_type` |

#### GET /academics/permissions/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course.course_type` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course_type_not` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.course.course_type` |

### 2025-03-19

#### GET /events/athletics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.location` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.location` response property's maxlength was unset from `255` |

#### GET /events/athletics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.location` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.location` response property's maxlength was unset from `255` |

### 2025-03-10

#### GET /finance/tax_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `tax_category` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.tax_category` |

#### GET /finance/tax_types/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `tax_category` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.tax_category` |

### 2025-03-04

#### GET /academics/class_attendance_statuses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `takes_daily_attendance_today` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.takes_daily_attendance_today` |

#### GET /academics/class_attendance_statuses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.takes_daily_attendance_today` |

#### GET /athletics/teams

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `campus_id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `campus_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `school_level` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus_id` |

#### GET /athletics/teams/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `campus_id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.campus_id` |

#### GET /attendance_status_codes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /events/athletics_scores/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /athletics/teams/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.campus_id` |

#### PATCH /events/athletics_scores/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /athletics/teams

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.campus_id` |

### 2025-03-03

#### GET /academics/student_daily_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.record_id` |

#### GET /academics/teacher_daily_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.record_id` |

## February 2025

### 2025-02-21

#### GET /academics/class_attendance_statuses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course_type_not` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `course_type_not` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `course_type` |

#### GET /academics/class_attendance_statuses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course_type_not` to the `value_lists.items.fields.items` response property |

### 2025-02-11

#### PATCH /finance/post_ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## January 2025

### 2025-01-30

#### DELETE /events/event_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `classification_not` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `classification_not` |

#### GET /academics/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `classification_not` to the `value_lists.items.fields.items` response property |

#### GET /athletics/teams

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.internal_team_id` |

#### GET /athletics/teams/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.internal_team_id` |

#### GET /events/event_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.group_event_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person_id` read-only status was removed |

#### GET /events/event_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.group_event_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person_id` read-only status was removed |

#### GET /security_roles

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /athletics/teams/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.internal_team_id` |

#### PATCH /events/event_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /athletics/teams

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.internal_team_id` |

#### POST /events/event_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-01-29

#### POST /staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-01-22

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `exclude_from_transcript`, the type/format was changed from `string` to `boolean` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.exclude_from_transcript` |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.exclude_from_transcript` |

#### GET /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `exclude_from_transcript` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.exclude_from_transcript` |

#### GET /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.exclude_from_transcript` |

#### GET /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `exclude_from_transcript`, the type/format was changed from `string` to `boolean` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.exclude_from_transcript` |

#### GET /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.exclude_from_transcript` |

#### GET /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `exclude_from_transcript` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.exclude_from_transcript` |

#### GET /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.exclude_from_transcript` |

#### PATCH /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.exclude_from_transcript` |

#### PATCH /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.exclude_from_transcript` |

#### PATCH /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.exclude_from_transcript` |

#### PATCH /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.exclude_from_transcript` |

#### POST /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.exclude_from_transcript` |

#### POST /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.exclude_from_transcript` |

### 2025-01-17

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `exclude_from_transcript` |

#### GET /finance/purchase_request_workflow_gl_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `exclude_from_transcript` |

### 2025-01-14

#### GET /security_roles

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

### 2025-01-13

#### GET /resource_reservations/reservations

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /resource_reservations/reservations/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /security_roles

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /resource_reservations/reservations/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /resource_reservations/reservations

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-01-09

#### POST /resource_reservations/resources

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.responsible_person_id` became optional |

### 2025-01-03

#### GET /finance/gl_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/gl_accounts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/projects

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/projects/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/tax_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/tax_types/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /finance/vendors/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2025-01-02

#### GET /finance/gl_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /finance/gl_accounts/{gl_account_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /finance/projects

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /finance/projects/{project_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /finance/tax_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /finance/tax_types/{tax_type_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API removed  |

#### GET /finance/vendors/{vendor_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### PATCH /finance/vendors/{vendor_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

## December 2024

### 2024-12-24

#### GET /finance/purchase_request_workflows

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/purchase_request_workflows/{purchase_request_workflow_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-12-20

#### DELETE /person_roles/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /person_roles

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /person_roles/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /staff_faculty/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /person_roles

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-12-17

#### GET /person_roles

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### POST /person_roles

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

### 2024-12-16

#### GET /person_roles

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /person_roles

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-12-11

#### GET /finance/gl_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `accounting_period` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `current_fiscal_year` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.accounting_period` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.annual_budget_num_1` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.budget_remaining` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.current_fiscal_year` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.ytd_budget_num_1` |

#### GET /finance/gl_accounts/{gl_account_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `accounting_period` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `current_fiscal_year` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.accounting_period` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.annual_budget_num_1` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.budget_remaining` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.current_fiscal_year` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.ytd_budget_num_1` |

### 2024-12-09

#### GET /academics/class_attendance_statuses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/class_attendance_statuses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/class_attendance_statuses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## November 2024

### 2024-11-19

#### GET /relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `related_person_role` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `parent_portal_access` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `related_person_role` |

#### GET /relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `related_person_role` to the `value_lists.items.fields.items` response property |

### 2024-11-18

#### GET /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.term_credit_hours` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.total_credits` |

### 2024-11-14

#### GET /resource_reservations/resources

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /resource_reservations/resources/{resource_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /resource_reservations/resources/{resource_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /resource_reservations/resources

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-11-11

#### GET /finance/ap_disbursements

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |

#### GET /relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `parent_portal_access` |

### 2024-11-07

#### GET /finance/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.tax_amount` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.tax_type` |

#### GET /finance/ap_invoice_items/{invoice_item_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.tax_amount` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.tax_type` |

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.inclusive_exclusive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.tax_type` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.total_tax` |

#### GET /finance/ap_invoices/{invoice_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.inclusive_exclusive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.tax_type` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.total_tax` |

#### GET /finance/tax_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/tax_types/{tax_type_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `parent_portal_access` |

#### PATCH /finance/ap_invoice_items/{invoice_item_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.tax_amount` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.tax_type` |

#### PATCH /finance/ap_invoices/{invoice_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.total_tax` |

#### POST /finance/ap_invoices/{invoice_id}/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.tax_amount` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.tax_type` |

### 2024-11-06

#### GET /academics/classes/{internal_class_id}/assignments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.assignment_details` response property's maxlength was unset from `1500` |

#### GET /academics/classes/{internal_class_id}/assignments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.assignment_details` response property's maxlength was unset from `1500` |

#### GET /academics/student_assignments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.assignment.notes` response property's maxlength was unset from `1500` |

#### GET /academics/student_assignments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.assignment.notes` response property's maxlength was unset from `1500` |

### 2024-11-01

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `currently_enrolled` |

#### GET /academics/student_daily_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `record_type_is_not` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `record_type_is_not` |

## October 2024

### 2024-10-31

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_date_withdrawn` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_late_date_enrolled` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_date_withdrawn` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_late_date_enrolled` |

### 2024-10-29

#### GET /events/athletics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `is_series_template` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.series_template` |

#### GET /events/athletics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.series_template` |

#### GET /events/group_events

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `is_series_template` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.series_template` |

#### GET /events/group_events/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.series_template` |

#### GET /volunteer_coordinator/volunteers

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /volunteer_coordinator/volunteers/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-10-22

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `class_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `class_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.class_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.person_name` |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `class_status` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.class_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.person_name` |

#### PATCH /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.class_status` |

### 2024-10-21

#### GET /academics/student_daily_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `item_type`, the maxlength was set to `50` |

#### GET /academics/teacher_daily_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `record_type`, the maxlength was set to `15` |

#### GET /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `email`, the maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `first_name`, the maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `last_name`, the maxlength was set to `50` |

#### GET /admission/applications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `first_name`, the maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `last_name`, the maxlength was set to `50` |

#### GET /admission/households

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `address_1`, the maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `address_2`, the maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `address_3`, the maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `city`, the maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `name`, the maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `postal_code`, the maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `state`, the maxlength was set to `50` |

#### GET /admission/households/{household_id}/members

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `first_name`, the maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `last_name`, the maxlength was set to `50` |

#### GET /admission/relatives

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `email`, the maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `first_name`, the maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `last_name`, the maxlength was set to `50` |

#### GET /alumni/demographics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `first_name`, the maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `last_name`, the maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `maiden_name`, the maxlength was set to `50` |

#### GET /athletics/sports

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `school_level`, the maxlength was set to `50` |

#### GET /classes/{internal_class_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `block_description`, the maxlength was set to `50` |

#### GET /directory/configurations

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `category`, the maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `configuration`, the maxlength was set to `50` |

#### GET /directory/household

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `first_name`, the maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `household_city`, the maxlength was set to `4000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `household_location`, the maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `household_postal_code`, the maxlength was set to `4000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `last_name`, the maxlength was set to `1000` |

#### GET /directory/staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `campus`, the maxlength was set to `4000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `department`, the maxlength was set to `4000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `first_name`, the maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `last_name`, the maxlength was set to `1000` |

#### GET /directory/student

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `campus`, the maxlength was set to `4000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `first_name`, the maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `grade_level`, the maxlength was set to `4000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `homeroom`, the maxlength was set to `4000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `household_city`, the maxlength was set to `4000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `household_location`, the maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `household_postal_code`, the maxlength was set to `4000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `last_name`, the maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `school_level`, the maxlength was set to `4000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `student_group`, the maxlength was set to `4000` |

#### GET /finance/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.tax_type` |

#### GET /finance/ap_invoice_items/{invoice_item_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.tax_type` |

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.inclusive_exclusive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.tax_type` |

#### GET /finance/ap_invoices/{invoice_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.inclusive_exclusive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.tax_type` |

#### GET /finance/tax_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /finance/tax_types/{tax_type_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### PATCH /academics/assignments/{assignment_id}/grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.private_notes_for_teacher` request property's maxlength was set to `1500` |

#### PATCH /academics/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_id` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.virtual_meeting_url` request property's maxlength was set to `2000` |

#### PATCH /academics/classes/{internal_class_id}/assignments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.assignment_details` request property's maxlength was set to `1500` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `256` |

#### PATCH /academics/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_description` request property's maxlength was set to `8000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_title` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.course_id` request property's maxlength was set to `15` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.department_description` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.subject_description` request property's maxlength was set to `50` |

#### PATCH /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_teacher.first_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_teacher.last_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_teacher.middle_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_teacher.preferred_name` request property's maxlength was set to `50` |

#### PATCH /academics/numeric_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grading_period.description` request property's maxlength was set to `50` |

#### PATCH /academics/qualitative_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grading_period.description` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.proficiency_level` request property's maxlength was set to `35` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.rubric.description` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.rubric_category.description` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.rubric_criteria.description` request property's maxlength was set to `800` |

#### PATCH /academics/rubric_categories/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.report_override_description` request property's maxlength was set to `250` |

#### PATCH /academics/rubric_criteria/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `800` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.report_override_description` request property's maxlength was set to `1000` |

#### PATCH /academics/rubric_scale_levels/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.abbreviation` request property's maxlength was set to `35` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `500` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.scale_description` request property's maxlength was set to `200` |

#### PATCH /academics/rubric_scales/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `200` |

#### PATCH /academics/rubrics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.report_override_description` request property's maxlength was set to `500` |

#### PATCH /academics/student_alerts/{person_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.academic_alert` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.family_alert` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.general_alert` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.medical_alert` request property's maxlength was set to `1000` |

#### PATCH /admission/applicants/{applicant_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.email` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.first_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.last_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.middle_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.mobile_phone` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.nick_name` request property's maxlength was set to `50` |

#### PATCH /admission/applications/{application_id}/checklists/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `5000` |

#### PATCH /admission/citizenships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.passport_issuing_authority` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.passport_number` request property's maxlength was set to `30` |

#### PATCH /admission/households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_1` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_2` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_3` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.city` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.county` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.phone` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.postal_code` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.state` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.subdivision` request property's maxlength was set to `50` |

#### PATCH /admission/languages/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `255` |

#### PATCH /admission/relatives/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.email` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.first_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.last_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.maiden_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.middle_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.mobile_phone` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.nick_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.place_of_birth` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.work_phone` request property's maxlength was set to `30` |

#### PATCH /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.first_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.height` request property's maxlength was set to `8` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.jersey_number` request property's maxlength was set to `3` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.last_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.position` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.weight` request property's maxlength was set to `10` |

#### PATCH /athletics/sports/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.abbreviation` request property's maxlength was set to `15` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.school_level` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.subject_description` request property's maxlength was set to `50` |

#### PATCH /athletics/teams/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.team_id` request property's maxlength was set to `20` |

#### PATCH /behavior/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_name` request property's maxlength was set to `80` |

#### PATCH /boarding/dorms/{internal_dorm_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `500` |

#### PATCH /boarding/dorms/{internal_dorm_id}/students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.room_number` request property's maxlength was set to `10` |

#### PATCH /classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.block.abbreviation` request property's maxlength was set to `6` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.block.description` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `500` |

#### PATCH /contact_info/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.business_phone` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.email_1` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.email_2` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.home_phone` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.mobile_phone` request property's maxlength was set to `30` |

#### PATCH /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_description` request property's maxlength was set to `8000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_title` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.course_id` request property's maxlength was set to `15` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.department.description` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.subject.description` request property's maxlength was set to `50` |

#### PATCH /emergency_contacts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_1` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_2` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.business_phone` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.city` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.email_1` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.email_2` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.first_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.home_phone` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.last_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.middle_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.mobile_phone` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.nick_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.postal_code` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.state_province` request property's maxlength was set to `50` |

#### PATCH /extended_care/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_id` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.virtual_meeting_url` request property's maxlength was set to `2000` |

#### PATCH /extended_care/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_description` request property's maxlength was set to `8000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_title` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.course_id` request property's maxlength was set to `15` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.subject_description` request property's maxlength was set to `50` |

#### PATCH /finance/ap_disbursement_items/{disbursement_item_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |

#### PATCH /finance/ap_disbursements/{disbursement_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.payee_name` request property's maxlength was set to `200` |

#### PATCH /finance/ap_invoice_items/{invoice_item_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.ap_description` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.invoice_number` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.tax_type` |

#### PATCH /finance/ap_invoices/{invoice_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.invoice_number` request property's maxlength was set to `30` |

#### PATCH /finance/vendors/{vendor_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.account_number` request property's maxlength was set to `75` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_1` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_2` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_3` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.bank_account` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.city` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.email` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.postal_code` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.routing_number` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.state_province` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.vendor_name` request property's maxlength was set to `200` |

#### PATCH /health/patients/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.allergies_symptoms` request property's maxlength was set to `5000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.current_medications` request property's maxlength was set to `5000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.dental_group_number` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.dental_insurer` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.dental_subscriber_number` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.general_medical_notes` request property's maxlength was set to `5000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.health_group_number` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.health_insurer` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.health_subscriber_number` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.height` request property's maxlength was set to `10` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.medical_id_number` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.weight` request property's maxlength was set to `10` |

#### PATCH /health/patients/{patient_id}/conditions/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `2000` |

#### PATCH /health/patients/{patient_id}/medications/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.dosage_instruction` request property's maxlength was set to `2000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `2000` |

#### PATCH /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `2000` |

#### PATCH /person_reference_number/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.value` request property's maxlength was set to `200` |

#### PATCH /programs/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_id` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.virtual_meeting_url` request property's maxlength was set to `2000` |

#### PATCH /programs/classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.block.abbreviation` request property's maxlength was set to `6` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.block.description` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `500` |

#### PATCH /programs/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_description` request property's maxlength was set to `8000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_title` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.course_id` request property's maxlength was set to `15` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.subject.description` request property's maxlength was set to `50` |

#### PATCH /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_teacher.first_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_teacher.last_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_teacher.middle_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_teacher.preferred_name` request property's maxlength was set to `50` |

#### PATCH /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.extended_care_type` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.internal_notes` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.response_notes` request property's maxlength was set to `1000` |

#### PATCH /summer/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_id` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.virtual_meeting_url` request property's maxlength was set to `2000` |

#### PATCH /summer/classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `500` |

#### PATCH /summer/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_description` request property's maxlength was set to `8000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_title` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.course_id` request property's maxlength was set to `15` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.department_description` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.subject_description` request property's maxlength was set to `50` |

#### PATCH /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_teacher.first_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_teacher.last_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_teacher.middle_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_teacher.preferred_name` request property's maxlength was set to `50` |

#### POST /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_id` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.virtual_meeting_url` request property's maxlength was set to `2000` |

#### POST /academics/classes/{internal_class_id}/assignments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.assignment_details` request property's maxlength was set to `1500` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `256` |

#### POST /academics/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_description` request property's maxlength was set to `8000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_title` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.course_id` request property's maxlength was set to `15` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name` request property's maxlength was set to `100` |

#### POST /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |

#### POST /academics/rubric_categories

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.report_override_description` request property's maxlength was set to `250` |

#### POST /academics/rubric_criteria

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `800` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.report_override_description` request property's maxlength was set to `1000` |

#### POST /academics/rubric_scale_levels

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.abbreviation` request property's maxlength was set to `35` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `500` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.scale_description` request property's maxlength was set to `200` |

#### POST /academics/rubric_scales

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `200` |

#### POST /academics/rubrics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.report_override_description` request property's maxlength was set to `500` |

#### POST /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_1` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_2` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_3` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.city` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.email` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.first_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.last_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.middle_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.nick_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.phone_mobile` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.postal_code` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.state` request property's maxlength was set to `50` |

#### POST /admission/citizenships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.passport_issuing_authority` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.passport_number` request property's maxlength was set to `30` |

#### POST /admission/languages

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `255` |

#### POST /admission/relatives

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_1` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_2` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_3` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.city` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.email` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.first_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.last_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.maiden_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.middle_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.mobile_phone` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.nick_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.place_of_birth` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.postal_code` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.state` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.work_phone` request property's maxlength was set to `30` |

#### POST /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.first_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.height` request property's maxlength was set to `8` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.jersey_number` request property's maxlength was set to `3` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.last_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.position` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.weight` request property's maxlength was set to `10` |

#### POST /athletics/sports

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.abbreviation` request property's maxlength was set to `15` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `100` |

#### POST /athletics/teams

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.team_id` request property's maxlength was set to `20` |

#### POST /behavior

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_name` request property's maxlength was set to `80` |

#### POST /emergency_contacts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_1` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_2` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.business_phone` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.city` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.email_1` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.email_2` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.first_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.home_phone` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.last_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.middle_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.mobile_phone` request property's maxlength was set to `30` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.nick_name` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.postal_code` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.state_province` request property's maxlength was set to `50` |

#### POST /extended_care/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_id` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.virtual_meeting_url` request property's maxlength was set to `2000` |

#### POST /extended_care/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_description` request property's maxlength was set to `8000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_title` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.course_id` request property's maxlength was set to `15` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name` request property's maxlength was set to `100` |

#### POST /finance/ap_disbursements

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.payee_name` request property's maxlength was set to `200` |

#### POST /finance/ap_disbursements/{disbursement_id}/ap_disbursement_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |

#### POST /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.invoice_number` request property's maxlength was set to `30` |

#### POST /finance/ap_invoices/{invoice_id}/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.ap_description` request property's maxlength was set to `50` |

#### POST /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.account_number` request property's maxlength was set to `75` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_1` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_2` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address_3` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.city` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.email` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.postal_code` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.state_province` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.vendor_name` request property's maxlength was set to `200` |

#### POST /health/patients/{patient_id}/conditions

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.new_condition_code_description` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.new_intervention_code_description` request property's maxlength was set to `50` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `2000` |

#### POST /health/patients/{patient_id}/medications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.dosage_instruction` request property's maxlength was set to `2000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `2000` |

#### POST /person_reference_number

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.value` request property's maxlength was set to `200` |

#### POST /programs/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_id` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.virtual_meeting_url` request property's maxlength was set to `2000` |

#### POST /programs/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_description` request property's maxlength was set to `8000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_title` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.course_id` request property's maxlength was set to `15` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name` request property's maxlength was set to `100` |

#### POST /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |

#### POST /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.extended_care_type` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.internal_notes` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.response_notes` request property's maxlength was set to `1000` |

#### POST /summer/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.class_id` request property's maxlength was set to `20` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.description` request property's maxlength was set to `80` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.virtual_meeting_url` request property's maxlength was set to `2000` |

#### POST /summer/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_description` request property's maxlength was set to `8000` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.catalog_title` request property's maxlength was set to `100` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.course_id` request property's maxlength was set to `15` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name` request property's maxlength was set to `100` |

#### POST /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.notes` request property's maxlength was set to `1000` |

### 2024-10-15

#### GET /finance/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.tax_type` |

#### GET /finance/ap_invoice_items/{invoice_item_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.tax_type` |

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.inclusive_exclusive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.tax_type` |

#### GET /finance/ap_invoices/{invoice_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.inclusive_exclusive` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.tax_type` |

#### GET /finance/tax_types

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/tax_types/{tax_type_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /finance/ap_invoice_items/{invoice_item_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.tax_type` |

### 2024-10-14

#### GET /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `internal_class_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.internal_class_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.requestor_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.requestor_name` |

#### GET /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.internal_class_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.requestor_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.requestor_name` |

#### PATCH /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.internal_class_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.requestor_id` |

#### POST /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.internal_class_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.requestor_id` |

### 2024-10-02

#### GET /student_logistics/categories

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /student_logistics/drop_ins

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /student_logistics/reasons

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## September 2024

### 2024-09-30

#### GET /transcripts/{person_id}/gpas

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `gradinng_period` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `grading_period` |

### 2024-09-24

#### GET /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `course_type_exclude` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course_type` to the `value_lists.items.fields.items` response property |

### 2024-09-18

#### GET /classes/{internal_class_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.student_name` |

#### GET /classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.student_name` |

#### GET /events/event_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /events/event_attendance/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### POST /academics/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /academics/courses/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### POST /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /academics/enrollments/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### POST /athletics/sports

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /athletics/sports/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### POST /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /programs/enrollments/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### POST /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /summer/enrollments/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

### 2024-09-17

#### GET /academics/class_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `block_id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `day_id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `grading_period_id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `campus_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `primary_teacher_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `school_level` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_teacher_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_teacher_name` |

#### GET /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `course_type` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course_type_exclude` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `campus_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `internal_course_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `school_level` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_teacher_name` |

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course.course_type` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `campus_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `course_type` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `internal_course_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `school_level` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `school_year` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.course.course_type` |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course.course_type` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.campus_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.campus_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.course.course_type` |

#### GET /events/event_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-09-16

#### GET /events/event_attendance/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-09-12

#### GET /person_reference_number

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `type` |

#### GET /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `extended_care_type` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.send_notification` |

#### GET /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `extended_care_type` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.send_notification` |

#### PATCH /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.send_notification` |

#### POST /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.send_notification` |

## August 2024

### 2024-08-20

#### GET /contact_info

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.household_id` became read-only |

#### GET /contact_info/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.household_id` became read-only |

#### PATCH /contact_info/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## July 2024

### 2024-07-22

#### GET /directory/household

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /directory/staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `names` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.names` |

#### GET /directory/student

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-07-18

#### GET /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.course` |

### 2024-07-17

#### GET /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `role` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `role` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.roles` |

#### GET /admission/applicants/{applicant_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `role` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.roles` |

#### GET /development/constituents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /development/constituents/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /development/gifts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /development/gifts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/ap_disbursement_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/ap_disbursement_items/{disbursement_item_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/ap_disbursements

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/ap_disbursements/{disbursement_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/ap_invoice_items/{invoice_item_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/ap_invoices/{invoice_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/gl_accounts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/gl_accounts/{gl_account_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/projects

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/projects/{project_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /finance/vendors/{vendor_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /finance/ap_disbursement_items/{disbursement_item_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /finance/ap_disbursements/{disbursement_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /finance/ap_invoice_items/{invoice_item_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /finance/ap_invoices/{invoice_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /finance/vendors/{vendor_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /finance/ap_disbursements

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /finance/ap_disbursements/{disbursement_id}/ap_disbursement_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /finance/ap_invoices/{invoice_id}/ap_invoice_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /finance/vendors

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## May 2024

### 2024-05-01

#### GET /calendars/parent_calendars/{parent_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.course.course_id` |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.course.course_id` |

## April 2024

### 2024-04-26

#### GET /calendars/student_calendars/{person_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## March 2024

### 2024-03-25

#### GET /academics/class_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-03-18

#### GET /transcripts/student_info

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transcripts/student_info/{person_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transcripts/{person_id}/academic_classifications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transcripts/{person_id}/academic_classifications/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transcripts/{person_id}/gpas

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transcripts/{person_id}/gpas/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /transcripts/{person_id}/transcript_items

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-03-15

#### GET /report_card/enrollments/{enrollment_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_cards/students/{person_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-03-12

#### GET /athletics/team/{id}/practice_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## January 2024

### 2024-01-31

#### GET /academics/student_alerts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `family_alert` |

### 2024-01-30

#### DELETE /person_reference_number/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /person_reference_number

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /person_reference_number/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /person_reference_number/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /person_reference_number

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-01-29

#### GET /academics/student_alerts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/student_alerts/{person_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/student_alerts/{person_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2024-01-22

#### GET /academics/qualitative_grades

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.rubric_category.descripcion` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.rubric_category.description` |

#### GET /academics/qualitative_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.rubric_category.descripcion` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.rubric_category.description` |

#### PATCH /academics/qualitative_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.rubric_category.descripcion` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.rubric_category.description` |

### 2024-01-11

#### GET /events/athletics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `event_type` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `internal_class_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.internal_class_id` |

#### GET /events/athletics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `event_type` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.internal_class_id` |

#### GET /news

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the 'composer_page_type (parameter)' enum value from the `value_lists.items.fields.items` response property |

#### GET /news/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the 'composer_page_type (parameter)' enum value from the `value_lists.items.fields.items` response property |

### 2024-01-04

#### GET /news

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /news/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## December 2023

### 2023-12-06

#### GET /behavior

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_incident_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_incident_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.on_or_after_incident_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.on_or_before_incident_date` |

#### GET /behavior/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.on_or_after_incident_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.on_or_before_incident_date` |

#### GET /staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.school_level` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `school_level` |

#### GET /staff_faculty/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.school_level` |

#### PATCH /behavior/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.on_or_after_incident_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.on_or_before_incident_date` |

#### POST /behavior

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.on_or_after_incident_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.on_or_before_incident_date` |

### 2023-12-04

#### GET /staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `school_level` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.school_level` |

#### GET /staff_faculty/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `school_level` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.school_level` |

## November 2023

### 2023-11-21

#### GET /events/group_events

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.resource_id` |

#### GET /events/group_events/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.resource_id` |

## October 2023

### 2023-10-31

#### GET /directory/staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2023-10-13

#### GET /academics/student_daily_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/teacher_daily_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2023-10-11

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `course_type_exclude` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course_type` to the `value_lists.items.fields.items` response property |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `course_type_exclude` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course_type` to the `value_lists.items.fields.items` response property |

## September 2023

### 2023-09-12

#### GET /academics/assignments/{assignment_id}/grades

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.last_modified_date` became read-only |

#### GET /academics/assignments/{assignment_id}/grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.last_modified_date` became read-only |

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `course_type` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course_type_exclude` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `course_type` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course_type_exclude` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

#### GET /academics/numeric_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

#### GET /academics/qualitative_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

#### GET /academics/rubric_criteria

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |

#### GET /academics/rubric_criteria/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

#### GET /academics/student_assignments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.last_modified_date` became read-only |

#### GET /academics/student_assignments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.last_modified_date` became read-only |

#### PATCH /academics/assignments/{assignment_id}/grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.last_modified_date` became read-only |

### 2023-09-11

#### GET /alumni/demographics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /alumni/demographics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2023-09-05

#### GET /emergency_contacts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `is_medical_provider` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.is_medical_provider` |

#### GET /events/athletics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_end_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_start_date` |

### 2023-09-01

#### GET /events/group_events

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_end_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_start_date` |

## August 2023

### 2023-08-22

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.last_modified_date` |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.last_modified_date` |

### 2023-08-10

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

#### GET /academics/student_assignments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `assignment.grading_period` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.assignment.grading_period` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `assignment.grading_period_id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.assignment.grading_period_id` |

### 2023-08-09

#### GET /academics/student_assignments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `assignment.grading_period` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.assignment.grading_period` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `grading_period` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `assignment.grading_period_id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `grading_period_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.assignment.grading_period_id` |

### 2023-08-08

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.class_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_teacher` |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.class_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_teacher` |

#### GET /academics/student_assignments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /extended_care/registrations

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.class_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_teacher` |

#### GET /extended_care/registrations/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.class_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_teacher` |

#### GET /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.class_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_teacher` |

#### GET /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.class_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_teacher` |

#### GET /report_card/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The query string request parameter `school_year` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `course_classification` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `person_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `student_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_teacher` |

#### GET /report_card/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_teacher` |

#### GET /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.class_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_teacher` |

#### GET /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.class_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_teacher` |

#### PATCH /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.class_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.primary_teacher` |

#### PATCH /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.class_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.primary_teacher` |

#### PATCH /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.class_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.primary_teacher` |

### 2023-08-07

#### GET /academics/student_assignments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## July 2023

### 2023-07-24

#### GET /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `suffix` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.first_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.suffix` |

#### GET /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `suffix` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.first_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.suffix` |

#### GET /behavior

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /behavior/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.first_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.last_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.suffix` |

#### PATCH /behavior/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.first_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.suffix` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.last_name` |

#### POST /behavior

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2023-07-20

#### POST /academics/rubric_criteria

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.scale_id` became optional |

#### POST /academics/rubrics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.category_id` became optional |

### 2023-07-05

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `campus.id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `campus_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus` |

### 2023-07-03

#### GET /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person_id` became read-only |

#### GET /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person_id` became read-only |

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `advisor_id`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `homeroom_teacher_id`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `homeroom`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `household_id`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `role`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `campus.id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.campus_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.campus` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `campus_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `role` to the `value_lists.items.fields.items` response property |

#### PATCH /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` became read-only |

#### POST /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API removed  |

#### POST /academics/enrollments/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API removed  |

#### POST /programs/enrollments/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API removed  |

#### POST /summer/enrollments/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## June 2023

### 2023-06-30

#### GET /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person_id` read-only status was removed |

#### GET /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person_id` read-only status was removed |

#### PATCH /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` read-only status was removed |

#### POST /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` became required |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` became required |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` read-only status was removed |

### 2023-06-29

#### GET /academics/rubric_categories

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/rubric_categories/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/rubric_criteria

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/rubric_criteria/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/rubric_scale_levels

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/rubric_scale_levels/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/rubric_scales

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/rubric_scales/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/rubrics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/rubrics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /athletics/sports

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /athletics/sports/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /athletics/teams

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /athletics/teams/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/rubric_categories/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/rubric_criteria/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/rubric_scale_levels/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/rubric_scales/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/rubrics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /athletics/sports/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /athletics/teams/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /academics/rubric_categories

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /academics/rubric_criteria

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /academics/rubric_scale_levels

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /academics/rubric_scales

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /academics/rubrics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /athletics/sports/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /athletics/teams

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2023-06-28

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `advisor_id`, the type/format was generalized from `integer` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `homeroom_teacher_id`, the type/format was generalized from `integer` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `homeroom`, the type/format was generalized from `integer` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `household_id`, the type/format was generalized from `integer` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `role`, the type/format was generalized from `integer` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `role` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `campus.id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `campus_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus` |

### 2023-06-27

#### GET /boarding/dorms/{internal_dorm_id}/students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.floor_number` |

#### GET /boarding/dorms/{internal_dorm_id}/students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.floor_number` |

#### PATCH /boarding/dorms/{internal_dorm_id}/students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.floor_number` |

### 2023-06-15

#### GET /events/athletics

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /events/athletics/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /events/group_events

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /events/group_events/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2023-06-05

#### GET /boarding/dorms/{internal_dorm_id}/students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.floor_number` |

#### GET /boarding/dorms/{internal_dorm_id}/students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.floor_number` |

#### PATCH /boarding/dorms/{internal_dorm_id}/students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.floor_number` |

#### POST /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.month_applying_for` became optional |

#### POST /admission/applications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.month_applying_for` became optional |

## May 2023

### 2023-05-12

#### GET /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.grade_level_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `grade_level_id` from the `value_lists.items.fields.items` response property |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.grade_level_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `grade_level_id` from the `value_lists.items.fields.items` response property |

#### GET /boarding/dorms

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /boarding/dorms/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /boarding/dorms/{internal_dorm_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /boarding/dorms/{internal_dorm_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /boarding/dorms/{internal_dorm_id}/students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /boarding/dorms/{internal_dorm_id}/students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `department.id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `subject.id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.department` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.subject` |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `department.id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `subject.id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.department` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.subject` |

#### GET /courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `department.id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.department` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.subject` |

#### GET /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `department.id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.department` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.subject` |

#### GET /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.grade_level_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `grade_level_id` from the `value_lists.items.fields.items` response property |

#### GET /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.grade_level_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `grade_level_id` from the `value_lists.items.fields.items` response property |

#### GET /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.grade_level_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `grade_level_id` from the `value_lists.items.fields.items` response property |

#### GET /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.grade_level_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `grade_level_id` from the `value_lists.items.fields.items` response property |

#### PATCH /academics/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.grade_level_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` became read-only |

#### PATCH /boarding/dorms/{internal_dorm_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /boarding/dorms/{internal_dorm_id}/students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.department` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.subject` |

#### PATCH /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.grade_level_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` became read-only |

#### PATCH /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.grade_level_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` became read-only |

#### POST /academics/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /academics/courses/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.grade_level_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.person_id` became read-only |

#### POST /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.grade_level_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.person_id` became read-only |

#### POST /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.grade_level_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.person_id` became read-only |

## March 2023

### 2023-03-31

#### GET /extended_care/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /extended_care/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /extended_care/classes/{internal_class_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /extended_care/classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /extended_care/classes/{internal_class_id}/meeting_times

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /extended_care/classes/{internal_class_id}/meeting_times/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /extended_care/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /extended_care/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /extended_care/registrations

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /extended_care/registrations/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /programs/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /programs/classes/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /report_card/classes/{internal_class_id}/curriculum

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/classes/{internal_class_id}/curriculum/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/classes/{internal_class_id}/teachers

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/classes/{internal_class_id}/teachers/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/documents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/documents/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/enrollments/{enrollment_id}/numeric_grades

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/enrollments/{enrollment_id}/numeric_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/enrollments/{enrollment_id}/qualitative_grades

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/enrollments/{enrollment_id}/qualitative_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/students/{person_id}/academic_classifications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/students/{person_id}/academic_classifications/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/students/{person_id}/gpas

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /report_card/students/{person_id}/gpas/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /summer/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /summer/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /summer/classes/{internal_class_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /summer/classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /summer/classes/{internal_class_id}/meeting_times

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /summer/classes/{internal_class_id}/meeting_times/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /summer/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /summer/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /extended_care/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /extended_care/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /summer/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /summer/classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /summer/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.month_applying_for` became required |

#### POST /admission/applications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.month_applying_for` became required |

#### POST /extended_care/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /extended_care/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /programs/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /programs/courses/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### POST /summer/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /summer/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2023-03-09

#### POST /programs/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.primary_grade_level_id` became optional |

### 2023-03-01

#### GET /programs/classes/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /programs/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /programs/classes/{internal_class_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /programs/classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /programs/classes/{internal_class_id}/meeting_times

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /programs/classes/{internal_class_id}/meeting_times/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /programs/courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /programs/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /programs/classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /programs/classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /programs/courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /programs/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /programs/classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /programs/courses/

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /programs/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## February 2023

### 2023-02-07

#### DELETE /academics/classes/{internal_class_id}/assignments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/assignments/{assignment_id}/grades

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/assignments/{assignment_id}/grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/classes/{internal_class_id}/assignments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/classes/{internal_class_id}/assignments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/assignments/{assignment_id}/grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/classes/{internal_class_id}/assignments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /academics/classes/{internal_class_id}/assignments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2023-02-01

#### GET /academics/numeric_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.enrollment_id` became read-only |

#### GET /academics/qualitative_grades

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.enrollment_id` became read-only |

#### PATCH /academics/numeric_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/qualitative_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## January 2023

### 2023-01-31

#### GET /academics/qualitative_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.rubric_criteria.description` response's property type/format changed from `integer` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `rubric_criteria.description` from the `value_lists.items.fields.items` response property |

### 2023-01-30

#### GET /emergency_contacts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `legal_custody`, the type/format was changed from `string` to `boolean` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `medical_notification`, the type/format was changed from `string` to `boolean` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `person_id`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `pick_up`, the type/format was changed from `string` to `boolean` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `relationship`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `student_id`, the type/format was changed from `string` to `integer` |

### 2023-01-24

#### GET /emergency_contacts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `legal_custody`, the type/format was generalized from `boolean` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `medical_notification`, the type/format was generalized from `boolean` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `person_id`, the type/format was generalized from `integer` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `pick_up`, the type/format was generalized from `boolean` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `relationship`, the type/format was generalized from `integer` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `student_id`, the type/format was generalized from `integer` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `student_role` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `student_role` |

## December 2022

### 2022-12-16

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.virtual_meeting_url` |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.virtual_meeting_url` |

### 2022-12-13

#### PATCH /academics/numeric_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API removed  |

#### PATCH /academics/qualitative_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API removed  |

## November 2022

### 2022-11-30

#### GET /academics/calendar_rotation_days

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/calendar_rotation_days/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/block_groups

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/block_groups/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/block_schedules

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/block_schedules/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/blocks

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/blocks/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/blocks_by_block_groups

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/blocks_by_block_groups/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/grading_periods

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/grading_periods/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/numeric_grades

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/numeric_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/permissions

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/permissions/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/qualitative_grades

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/qualitative_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/rooms

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/rooms/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/subjects

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/subjects/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/numeric_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/qualitative_grades/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2022-11-29

#### GET /academics/config/block_times

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/block_times/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/rotation_days

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/config/rotation_days/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/departments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/departments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## September 2022

### 2022-09-06

#### GET /parents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `household_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.username` |

#### GET /parents/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.username` |

#### GET /staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `role`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `role` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `household_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.household_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.username` |

#### GET /staff_faculty/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `role` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.household_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.username` |

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `household_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.household_id` |

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.household_id` |

## July 2022

### 2022-07-22

#### PATCH /admission/applications/{application_id}/checklists/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## May 2022

### 2022-05-24

#### GET /relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2022-05-17

#### GET /academics/classes/{internal_class_id}/meeting_times

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/classes/{internal_class_id}/meeting_times/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2022-05-16

#### DELETE /emergency_contacts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /emergency_contacts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /emergency_contacts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /emergency_contacts/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /emergency_contacts

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2022-05-12

#### GET /classes/{internal_class_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `block_description` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `block_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.block` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.end_time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.start_time` |

#### GET /classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.block` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.end_time` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.start_time` |

#### PATCH /classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.block` |

### 2022-05-05

#### GET /contact_info

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |

#### GET /contact_info/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

### 2022-05-02

#### GET /directory/configurations

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.value_list` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.options_json` |

#### GET /households

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

#### GET /people/{id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |

## March 2022

### 2022-03-04

#### GET /directory/preferences/household

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /directory/preferences/household/{household_id}/:id

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### GET /directory/preferences/household/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /directory/preferences/people

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /directory/preferences/people/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /directory/preferences/people/{person_id}/:id

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### PATCH /directory/preferences/household/{household_id}/:id

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

#### PATCH /directory/preferences/household/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /directory/preferences/people/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /directory/preferences/people/{person_id}/:id

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | API path removed  |

### 2022-03-03

#### GET /directory/configurations

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /directory/preferences/household/{household_id}/:id

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /directory/preferences/people/{person_id}/:id

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /directory/preferences/household/{household_id}/:id

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /directory/preferences/people/{person_id}/:id

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.student_id` became optional |

## February 2022

### 2022-02-11

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `currently_enrolled` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_withdrawn` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `internal_class_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `late_date_enrolled` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course_type` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `school_year` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `subject` to the `value_lists.items.fields.items` response property |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `currently_enrolled` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_withdrawn` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `internal_class_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `late_date_enrolled` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course_type` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `school_year` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `subject` to the `value_lists.items.fields.items` response property |

#### GET /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `applicant_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_of_birth` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `household_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `mobile_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `nick_name` from the `value_lists.items.fields.items` response property |

#### GET /admission/applicants/{applicant_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `applicant_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_of_birth` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `household_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `mobile_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `nick_name` from the `value_lists.items.fields.items` response property |

#### GET /admission/applicants/{applicant_id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `admissions_access` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `legal_custody` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `related_person_id` from the `value_lists.items.fields.items` response property |

#### GET /admission/applicants/{applicant_id}/relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `admissions_access` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `legal_custody` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `related_person_id` from the `value_lists.items.fields.items` response property |

#### GET /admission/applications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `admission_lead_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `applicant_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `application_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `application_decision_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `application_decision_response_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `application_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `inquiry_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `requesting_financial_aid` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `visit_date` from the `value_lists.items.fields.items` response property |

#### GET /admission/applications/{application_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `admission_lead_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `applicant_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `application_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `application_decision_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `application_decision_response_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `application_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `inquiry_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `requesting_financial_aid` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `visit_date` from the `value_lists.items.fields.items` response property |

#### GET /admission/applications/{application_id}/checklists

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `checklist_item_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `completed_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `completed` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `follow_up_complete_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `follow_up_complete` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `required` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `scheduled_date` from the `value_lists.items.fields.items` response property |

#### GET /admission/applications/{application_id}/checklists/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `checklist_item_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `completed_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `completed` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `follow_up_complete_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `follow_up_complete` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `required` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `scheduled_date` from the `value_lists.items.fields.items` response property |

#### GET /admission/citizenships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `is_primary` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `passport_expiration_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `passport_issue_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `passport_issuing_authority` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `passport_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |

#### GET /admission/citizenships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `is_primary` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `passport_expiration_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `passport_issue_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `passport_issuing_authority` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `passport_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |

#### GET /admission/config/years

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `available_for_inquiry` from the `value_lists.items.fields.items` response property |

#### GET /admission/config/years/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `available_for_inquiry` from the `value_lists.items.fields.items` response property |

#### GET /admission/config/years/{school_year}/checklists

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `category_id`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `abbreviation` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `applies_to_prospect` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `category` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `description` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `due_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `early_due_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `filter_by_group` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `required_for_application` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `required_for_review` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `required` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `sort_key` from the `value_lists.items.fields.items` response property |

#### GET /admission/config/years/{school_year}/checklists/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `abbreviation` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `applies_to_prospect` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `category` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `description` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `due_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `early_due_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `filter_by_group` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `required_for_application` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `required_for_review` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `required` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `sort_key` from the `value_lists.items.fields.items` response property |

#### GET /admission/households

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `address_1` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `address_2` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `address_3` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `city` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `county` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `postal_code` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `state` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `subdivision` from the `value_lists.items.fields.items` response property |

#### GET /admission/households/{household_id}/members

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_of_birth` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `nick_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |

#### GET /admission/households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `address_1` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `address_2` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `address_3` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `city` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `county` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `postal_code` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `state` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `subdivision` from the `value_lists.items.fields.items` response property |

#### GET /admission/languages

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `is_primary` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `spoken_at_home` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `years_studying` from the `value_lists.items.fields.items` response property |

#### GET /admission/languages/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `is_primary` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `spoken_at_home` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `years_studying` from the `value_lists.items.fields.items` response property |

#### GET /admission/relatives

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_of_birth` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_of_death` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `graduation_year` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `household_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `maiden_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `mobile_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `nick_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `place_of_birth` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `work_phone` from the `value_lists.items.fields.items` response property |

#### GET /admission/relatives/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_of_birth` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_of_death` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `graduation_year` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `household_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `maiden_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `mobile_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `nick_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `place_of_birth` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `work_phone` from the `value_lists.items.fields.items` response property |

#### GET /admission/relatives/{relative_id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `related_person_id` from the `value_lists.items.fields.items` response property |

#### GET /admission/relatives/{relative_id}/relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `related_person_id` from the `value_lists.items.fields.items` response property |

#### GET /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `captain` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `currently_enrolled` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_withdrawn` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `height` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `internal_class_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `jersey_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `late_date_enrolled` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `lettered` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `position` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `weight` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `school_year` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `sport` to the `value_lists.items.fields.items` response property |

#### GET /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `captain` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `currently_enrolled` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_withdrawn` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `height` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `internal_class_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `jersey_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `late_date_enrolled` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `lettered` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `position` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `weight` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `school_year` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `sport` to the `value_lists.items.fields.items` response property |

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `primary_teacher_id`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `room_id`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `class_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `course` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `description` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `primary_teacher` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `room` from the `value_lists.items.fields.items` response property |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `class_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `course` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `description` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `primary_teacher` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `room` from the `value_lists.items.fields.items` response property |

#### GET /classes/{internal_class_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `attendance_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `internal_class_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `student_id` from the `value_lists.items.fields.items` response property |

#### GET /classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `attendance_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `internal_class_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `student_id` from the `value_lists.items.fields.items` response property |

#### GET /contact_info

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `business_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email_1` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email_2` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `home_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `household_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `mobile_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `role` to the `value_lists.items.fields.items` response property |

#### GET /contact_info/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `business_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email_1` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email_2` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `home_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `household_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `mobile_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `role` to the `value_lists.items.fields.items` response property |

#### GET /courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `catalog_description` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `catalog_title` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `course_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `name` from the `value_lists.items.fields.items` response property |

#### GET /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `catalog_description` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `catalog_title` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `course_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `name` from the `value_lists.items.fields.items` response property |

#### GET /health/patients

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `allergies_symptoms` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `current_medications` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_of_birth` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `dental_group_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `dental_insurer` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `dental_subscriber_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `general_medical_notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `health_group_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `health_insurer` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `health_subscriber_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `height` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `medical_id_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `medications_allowed` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `preferred_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `roles` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `weight` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `role` to the `value_lists.items.fields.items` response property |

#### GET /health/patients/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `allergies_symptoms` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `current_medications` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_of_birth` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `dental_group_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `dental_insurer` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `dental_subscriber_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `general_medical_notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `health_group_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `health_insurer` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `health_subscriber_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `height` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `medical_id_number` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `medications_allowed` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `preferred_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `roles` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `weight` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `role` to the `value_lists.items.fields.items` response property |

#### GET /health/patients/{patient_id}/conditions

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `begin_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `critical` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `description` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `end_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `patient_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `patient_name` from the `value_lists.items.fields.items` response property |

#### GET /health/patients/{patient_id}/conditions/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `begin_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `critical` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `description` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `end_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `patient_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `patient_name` from the `value_lists.items.fields.items` response property |

#### GET /health/patients/{patient_id}/medications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `dosage_instruction` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `end_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `patient_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `start_date` from the `value_lists.items.fields.items` response property |

#### GET /health/patients/{patient_id}/medications/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `dosage_instruction` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `end_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `patient_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `start_date` from the `value_lists.items.fields.items` response property |

#### GET /households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `address_line_1` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `address_line_2` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `address_line_3` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `city` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `state_or_province` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `zip` from the `value_lists.items.fields.items` response property |

#### GET /master_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `attendance_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `early_dismissal_time` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `excused` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `late_arrival_time` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `return_time` from the `value_lists.items.fields.items` response property |

#### GET /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `attendance_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `early_dismissal_time` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `excused` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `late_arrival_time` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `return_time` from the `value_lists.items.fields.items` response property |

#### GET /parents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `include_deceased`, the type/format was changed from `string` to `boolean` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `role`, the type/format was generalized from `integer` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email_1` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_nick_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `head_of_household` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `household_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `preferred_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `roles` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `spouse` from the `value_lists.items.fields.items` response property |

#### GET /parents/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `address` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `business_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email_1` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email_2` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `employer` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_nick_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `head_of_household` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `home_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `household_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `job_title` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `mobile_phone` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `preferred_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `roles` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `spouse` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `address.country` to the `value_lists.items.fields.items` response property |

#### GET /people/{id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `custody_status` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `emergency` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `legal_custody` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `medical_notification` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `parent_portal_access` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `pick_up` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `profile_update_permission` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `receive_general_correspondence` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `receive_invoices` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `receive_other` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `receive_report_cards` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `resident` from the `value_lists.items.fields.items` response property |

#### GET /staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `role`, the type/format was generalized from `integer` to `string` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_hired` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_terminated` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email_1` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `job_title` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `preferred_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `roles` from the `value_lists.items.fields.items` response property |

#### GET /staff_faculty/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_hired` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_terminated` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email_1` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `job_title` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `preferred_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `roles` from the `value_lists.items.fields.items` response property |

#### GET /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `attendance_end_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `attendance_return_time` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `attendance_start_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `attendance_time` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `extended_care_arrival_time` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `extended_care_leave_time` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `extended_care_type` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `internal_notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_user` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `posted` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `response_notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `student_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `student_name` from the `value_lists.items.fields.items` response property |

#### GET /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `attendance_end_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `attendance_return_time` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `attendance_start_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `attendance_time` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `extended_care_arrival_time` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `extended_care_leave_time` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `extended_care_type` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `internal_notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_user` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `posted` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `response_notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `student_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `student_name` from the `value_lists.items.fields.items` response property |

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `advisor_id`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `homeroom_teacher_id`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `advisor` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `birthday` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email_1` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `entry_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `exit_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `graduation_year` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `homeroom_teacher` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `preferred_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `roles` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `username` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `role` to the `value_lists.items.fields.items` response property |

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `advisor` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `birthday` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `current_location` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `email_1` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `entry_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `exit_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `first_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `graduation_year` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `homeroom_teacher` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_modified_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `last_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `middle_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `preferred_name` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `username` from the `value_lists.items.fields.items` response property |

#### GET /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `currently_enrolled` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_withdrawn` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `internal_class_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `late_date_enrolled` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `school_year` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `subject` to the `value_lists.items.fields.items` response property |

#### GET /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `currently_enrolled` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_withdrawn` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `internal_class_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `late_date_enrolled` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `notes` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `person_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `school_year` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `subject` to the `value_lists.items.fields.items` response property |

## January 2022

### 2022-01-28

#### DELETE /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### GET /parents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `role`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `include_deceased` |

#### PATCH /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /admission/applicants/{applicant_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /admission/applicants/{applicant_id}/relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /admission/applications/{application_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /admission/citizenships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /admission/households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /admission/languages/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /admission/relatives/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /admission/relatives/{relative_id}/relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /health/patients/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /health/patients/{patient_id}/conditions/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /health/patients/{patient_id}/medications/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### PATCH /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `204` |

#### POST /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

#### POST /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

#### POST /admission/applicants/{applicant_id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

#### POST /admission/applications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

#### POST /admission/citizenships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

#### POST /admission/languages

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

#### POST /admission/relatives

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

#### POST /admission/relatives/{relative_id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

#### POST /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

#### POST /health/patients/{patient_id}/conditions

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

#### POST /health/patients/{patient_id}/medications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

#### POST /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

#### POST /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the success response with the status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added the success response with the status `201` |

## December 2021

### 2021-12-24

#### GET /health/patients

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /health/patients/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /health/patients/{patient_id}/conditions

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /health/patients/{patient_id}/conditions/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /health/patients/{patient_id}/medications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /health/patients/{patient_id}/medications/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /health/patients/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /health/patients/{patient_id}/conditions/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /health/patients/{patient_id}/medications/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /health/patients/{patient_id}/conditions

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /health/patients/{patient_id}/medications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2021-12-15

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `roles` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `role` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.roles` |

## October 2021

### 2021-10-29

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `course_type`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `school_year`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `subject`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.grade_level_id` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.level` response's property type/format changed from `string` to `integer` |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_level_id` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.level` response's property type/format changed from `string` to `integer` |

#### GET /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.current_grade` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.ethnicity` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.gender` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.name_prefix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.name_suffix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.pronouns` response's property type/format changed from `string` to `integer` |

#### GET /admission/applicants/{applicant_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.current_grade` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.ethnicity` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.gender` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_prefix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_suffix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.pronouns` response's property type/format changed from `string` to `integer` |

#### GET /admission/applicants/{applicant_id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.relationship` response's property type/format changed from `string` to `integer` |

#### GET /admission/applicants/{applicant_id}/relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.relationship` response's property type/format changed from `string` to `integer` |

#### GET /admission/applications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `application_status`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `year_applying_for`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.admission_source` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.application_decision_response` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.application_status` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.campus_applying_for` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.candidate_pool` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.grade_applying_for` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.month_applying_for` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.resident_status_applying_for` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.student_group_applying_for` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.year_applying_for` response's property type/format changed from `string` to `integer` |

#### GET /admission/applications/{application_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.admission_source` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.application_decision_response` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.application_status` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.campus_applying_for` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.candidate_pool` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_applying_for` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.month_applying_for` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.resident_status_applying_for` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.student_group_applying_for` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.year_applying_for` response's property type/format changed from `string` to `integer` |

#### GET /admission/citizenships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.country` response's property type/format changed from `string` to `integer` |

#### GET /admission/citizenships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.country` response's property type/format changed from `string` to `integer` |

#### GET /admission/config/years

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.id` response's property type/format changed from `string` to `integer` |

#### GET /admission/config/years/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.id` response's property type/format changed from `string` to `integer` |

#### GET /admission/config/years/{school_year}/checklists

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.checklist_type` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.filter_by_campus` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.filter_by_from_grade` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.filter_by_international` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.filter_by_resident_status` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.filter_by_to_grade` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.school_year` response's property type/format changed from `string` to `integer` |

#### GET /admission/config/years/{school_year}/checklists/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.checklist_type` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.filter_by_campus` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.filter_by_from_grade` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.filter_by_international` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.filter_by_resident_status` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.filter_by_to_grade` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.school_year` response's property type/format changed from `string` to `integer` |

#### GET /admission/households

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `country`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.country` response's property type/format changed from `string` to `integer` |

#### GET /admission/households/{household_id}/members

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.gender` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.name_prefix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.name_suffix` response's property type/format changed from `string` to `integer` |

#### GET /admission/households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.country` response's property type/format changed from `string` to `integer` |

#### GET /admission/languages

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.language` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.listening_proficiency` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.reading_proficiency` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.speaking_proficiency` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.writing_proficiency` response's property type/format changed from `string` to `integer` |

#### GET /admission/languages/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.language` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.listening_proficiency` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.reading_proficiency` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.speaking_proficiency` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.writing_proficiency` response's property type/format changed from `string` to `integer` |

#### GET /admission/relatives

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.ethnicity` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.gender` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.marital_status` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.name_prefix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.name_suffix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.pronouns` response's property type/format changed from `string` to `integer` |

#### GET /admission/relatives/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.ethnicity` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.gender` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.marital_status` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_prefix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_suffix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.pronouns` response's property type/format changed from `string` to `integer` |

#### GET /admission/relatives/{relative_id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.relationship` response's property type/format changed from `string` to `integer` |

#### GET /admission/relatives/{relative_id}/relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.relationship` response's property type/format changed from `string` to `integer` |

#### GET /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `school_year`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `sport`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.grade_level_id` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.jersey_size` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.level` response's property type/format changed from `string` to `integer` |

#### GET /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_level_id` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.jersey_size` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.level` response's property type/format changed from `string` to `integer` |

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.primary_grade_level` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.school_level` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.school_year` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.status` response's property type/format changed from `string` to `integer` |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.primary_grade_level` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.school_level` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.school_year` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.status` response's property type/format changed from `string` to `integer` |

#### GET /classes/{internal_class_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.status` response's property type/format changed from `string` to `integer` |

#### GET /classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.status` response's property type/format changed from `string` to `integer` |

#### GET /contact_info

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `role`, the type/format was changed from `string` to `integer` |

#### GET /courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.course_type` response's property type/format changed from `string` to `integer` |

#### GET /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.course_type` response's property type/format changed from `string` to `integer` |

#### GET /households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.country` response's property type/format changed from `string` to `integer` |

#### GET /master_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.attendance_category` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.day_of_week` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.faculty_attendance_status` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.grading_period` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.school_year` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.student_attendance_status` response's property type/format changed from `string` to `integer` |

#### GET /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_category` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.day_of_week` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.faculty_attendance_status` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grading_period` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.school_year` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.student_attendance_status` response's property type/format changed from `string` to `integer` |

#### GET /parents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.gender` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.name_prefix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.name_suffix` response's property type/format changed from `string` to `integer` |

#### GET /parents/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.address.country` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.gender` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_prefix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_suffix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.occupation` response's property type/format changed from `string` to `integer` |

#### GET /people/{id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `relationship`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.relationship` response's property type/format changed from `string` to `integer` |

#### GET /staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `campus`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `employee_code`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `faculty_type`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `role`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.campus` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.department` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.employee_code` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.faculty_type` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.gender` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.name_prefix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.name_suffix` response's property type/format changed from `string` to `integer` |

#### GET /staff_faculty/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.campus` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.department` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.employee_code` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.faculty_type` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.gender` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_prefix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_suffix` response's property type/format changed from `string` to `integer` |

#### GET /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.am_pm` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.attendance_type` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.bus_stop` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.status` response's property type/format changed from `string` to `integer` |

#### GET /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.am_pm` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_type` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.bus_stop` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.status` response's property type/format changed from `string` to `integer` |

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `homeroom`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.gender` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.grade_level` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.homeroom` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.school_level` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `date_of_birth` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.date_of_birth` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `birthday` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.birthday` |

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.campus` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.gender` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_level` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.homeroom` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_prefix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_suffix` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.school_level` response's property type/format changed from `string` to `integer` |

#### GET /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `school_year`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | For the query string request parameter `subject`, the type/format was changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.grade_level_id` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.level` response's property type/format changed from `string` to `integer` |

#### GET /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_level_id` response's property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.level` response's property type/format changed from `string` to `integer` |

#### PATCH /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_level_id` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.level` request property type/format changed from `string` to `integer` |

#### PATCH /admission/applicants/{applicant_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.current_grade` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.ethnicity` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.gender` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_prefix` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_suffix` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.pronouns` request property type/format changed from `string` to `integer` |

#### PATCH /admission/applicants/{applicant_id}/relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.relationship` request property type/format changed from `string` to `integer` |

#### PATCH /admission/applications/{application_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.admission_source` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.application_decision_response` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.application_status` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.campus_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.candidate_pool` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.month_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.resident_status_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.student_group_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.year_applying_for` request property type/format changed from `string` to `integer` |

#### PATCH /admission/citizenships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.country` request property type/format changed from `string` to `integer` |

#### PATCH /admission/households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.country` request property type/format changed from `string` to `integer` |

#### PATCH /admission/languages/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.language` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.listening_proficiency` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.reading_proficiency` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.speaking_proficiency` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.writing_proficiency` request property type/format changed from `string` to `integer` |

#### PATCH /admission/relatives/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.ethnicity` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.gender` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.marital_status` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_prefix` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_suffix` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.pronouns` request property type/format changed from `string` to `integer` |

#### PATCH /admission/relatives/{relative_id}/relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.relationship` request property type/format changed from `string` to `integer` |

#### PATCH /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_level_id` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.jersey_size` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.level` request property type/format changed from `string` to `integer` |

#### PATCH /classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.status` request property type/format changed from `string` to `integer` |

#### PATCH /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.course_type` request property type/format changed from `string` to `integer` |

#### PATCH /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_category` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.faculty_attendance_status` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grading_period` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.school_year` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.student_attendance_status` request property type/format changed from `string` to `integer` |

#### PATCH /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.am_pm` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_type` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.bus_stop` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.status` request property type/format changed from `string` to `integer` |

#### PATCH /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_level_id` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.level` request property type/format changed from `string` to `integer` |

#### POST /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_level_id` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.level` request property type/format changed from `string` to `integer` |

#### POST /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.admission_source` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.application_decision_response` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.application_status` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.campus_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.candidate_pool` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.country` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.current_grade` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.ethnicity` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.gender` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.month_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_prefix` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_suffix` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.pronouns` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.resident_status_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.student_group_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.year_applying_for` request property type/format changed from `string` to `integer` |

#### POST /admission/applicants/{applicant_id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.relationship` request property type/format changed from `string` to `integer` |

#### POST /admission/applications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.admission_source` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.application_decision_response` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.application_status` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.campus_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.candidate_pool` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.month_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.resident_status_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.student_group_applying_for` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.year_applying_for` request property type/format changed from `string` to `integer` |

#### POST /admission/citizenships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.country` request property type/format changed from `string` to `integer` |

#### POST /admission/languages

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.language` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.listening_proficiency` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.reading_proficiency` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.speaking_proficiency` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.writing_proficiency` request property type/format changed from `string` to `integer` |

#### POST /admission/relatives

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.country` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.ethnicity` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.gender` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.marital_status` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.name_prefix` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.pronouns` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.relationship` request property type/format changed from `string` to `integer` |

#### POST /admission/relatives/{relative_id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.relationship` request property type/format changed from `string` to `integer` |

#### POST /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_level_id` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.jersey_size` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.level` request property type/format changed from `string` to `integer` |

#### POST /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.am_pm` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.attendance_type` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.bus_stop` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.status` request property type/format changed from `string` to `integer` |

#### POST /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.grade_level_id` request property type/format changed from `string` to `integer` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.level` request property type/format changed from `string` to `integer` |

### 2021-10-28

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `date_of_birth` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.date_of_birth` |

### 2021-10-18

#### GET /parents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `email_1` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.email_1` |

#### GET /staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `email_1` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.email_1` |

#### GET /staff_faculty/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `email_1` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.email_1` |

### 2021-10-04

#### GET /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/applicants/{a_id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/applicants/{a_id}/relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/applicants/{applicant_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/applications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/applications/{app_id}/checklists

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/applications/{app_id}/checklists/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/applications/{application_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/citizenships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/citizenships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/config/years

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/config/years/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/config/years/{school_year}/checklists

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/config/years/{school_year}/checklists/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/households

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/households/{household_id}/members

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/languages

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/languages/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/relatives

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/relatives/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/relatives/{relative_id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /admission/relatives/{relative_id}/relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `primary_teacher_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.primary_teacher_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `primary_teacher` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `primary_teacher_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `room_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_teacher` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.room.abbreviation` |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `primary_teacher_id` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.primary_teacher_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `primary_teacher` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_teacher` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.room.abbreviation` |

#### PATCH /admission/applicants/{a_id}/relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /admission/applicants/{applicant_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /admission/applications/{application_id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /admission/citizenships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /admission/households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /admission/languages/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /admission/relatives/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /admission/relatives/{relative_id}/relationships/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /admission/applicants

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /admission/applicants/{a_id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /admission/applications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /admission/citizenships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /admission/languages

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /admission/relatives

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /admission/relatives/{relative_id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## September 2021

### 2021-09-30

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `primary_teacher_id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `room` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.primary_teacher_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.room` |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `primary_teacher_id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `room` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.primary_teacher_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.room` |

### 2021-09-16

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `internal_class_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `person_id` |

#### GET /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `internal_class_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `person_id` |

#### GET /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `internal_class_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `person_id` |

### 2021-09-14

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.course.id` |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.course.id` |

#### GET /parents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.spouse.id` |

#### GET /parents/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.address.address_1` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.address.address_2` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.address.address_3` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.address.city` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.address.postal_code` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.address.state_province` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.spouse.id` |

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.advisor.name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.homeroom_teacher.name` |

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.advisor.name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.homeroom_teacher.name` |

### 2021-09-07

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person_id` read-only status was removed |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person_id` read-only status was removed |

#### GET /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person_id` read-only status was removed |

#### GET /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person_id` read-only status was removed |

#### GET /parents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /parents/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /people/{id}/relationships

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `campus` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `date_hired` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `date_terminated` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `employee_code` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `campus` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `employee_code` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_date_hired` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_date_terminated` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_date_hired` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_date_terminated` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.campus` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.date_hired` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.date_terminated` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.employee_code` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |

#### GET /staff_faculty/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `campus` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `date_hired` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `date_terminated` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `employee_code` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.campus` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.date_hired` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.date_terminated` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.employee_code` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `entry_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `exit_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_entry_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_exit_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_entry_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_exit_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.entry_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.exit_date` |

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `entry_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `exit_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.entry_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.exit_date` |

#### GET /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person_id` read-only status was removed |

#### GET /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person_id` read-only status was removed |

#### PATCH /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` read-only status was removed |

#### PATCH /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` read-only status was removed |

#### PATCH /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` read-only status was removed |

#### POST /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` became required |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` became required |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` read-only status was removed |

#### POST /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` became required |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` became required |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` read-only status was removed |

#### POST /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` became required |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_class_id` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` became required |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.person_id` read-only status was removed |

## August 2021

### 2021-08-26

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /summer/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /summer/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## June 2021

### 2021-06-17

#### GET /contact_info

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /contact_info/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /households/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /staff_faculty

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /staff_faculty/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `advisor` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `gender` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `graduation_year` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `homeroom_teacher` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `homeroom` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `middle_name` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `preferred_name` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `username` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `advisor_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `homeroom_teacher_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `homeroom` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.advisor` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.gender` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.graduation_year` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.homeroom_teacher` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.homeroom` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.middle_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.preferred_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.username` |

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.advisor` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.homeroom_teacher` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.advisor` response's property type/format changed from `string` to `object` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.homeroom_teacher` response's property type/format changed from `string` to `object` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `birthday` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `gender` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `graduation_year` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `middle_name` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `name_prefix` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `name_suffix` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `preferred_name` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `username` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.advisor.id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.birthday` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.gender` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.graduation_year` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.homeroom_teacher.id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.middle_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.name_prefix` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.name_suffix` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.preferred_name` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.username` |

## May 2021

### 2021-05-13

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `value_lists.items.items.items.id` response's property type/format changed from `integer` to `string` |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `value_lists.items.items.items.id` response's property type/format changed from `integer` to `string` |

#### GET /classes/{internal_class_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `value_lists.items.items.items.id` response's property type/format changed from `integer` to `string` |

#### GET /classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `value_lists.items.items.items.id` response's property type/format changed from `integer` to `string` |

#### GET /courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `value_lists.items.items.items.id` response's property type/format changed from `integer` to `string` |

#### GET /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `value_lists.items.items.items.id` response's property type/format changed from `integer` to `string` |

#### GET /master_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `value_lists.items.items.items.id` response's property type/format changed from `integer` to `string` |

#### GET /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `value_lists.items.items.items.id` response's property type/format changed from `integer` to `string` |

#### GET /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `value_lists.items.items.items.id` response's property type/format changed from `integer` to `string` |

#### GET /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `value_lists.items.items.items.id` response's property type/format changed from `integer` to `string` |

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `value_lists.items.items.items.id` response's property type/format changed from `integer` to `string` |

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `value_lists.items.items.items.id` response's property type/format changed from `integer` to `string` |

## April 2021

### 2021-04-29

#### GET /master_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `update_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.update_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `on_or_after_update_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `on_or_before_update_date` |

#### GET /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `update_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.update_date` |

#### GET /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `input_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `input_user` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.input_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.input_user` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `on_or_after_input_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the query string request parameter `on_or_before_input_date` |

#### GET /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `input_date` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `input_user` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.input_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.input_user` |

#### PATCH /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.update_date` |

#### PATCH /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.input_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.input_user` |

#### POST /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.input_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.input_user` |

### 2021-04-15

#### GET /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_user` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_user` |

#### GET /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_user` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_user` |

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

### 2021-04-14

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

#### GET /classes/{internal_class_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |

#### GET /classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

#### GET /courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |

#### GET /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

### 2021-04-13

#### GET /master_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.attendance_category` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.excused` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_last_modified_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.last_modified_date` |

#### GET /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.attendance_category` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.excused` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `last_modified_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.last_modified_date` |

#### PATCH /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_category` read-only status was removed |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.excused` read-only status was removed |

### 2021-04-12

#### GET /master_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.attendance_category` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.excused` became read-only |

#### GET /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.attendance_category` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.excused` became read-only |

#### PATCH /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_category` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.excused` became read-only |

## March 2021

### 2021-03-30

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `value_lists` became read-only |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `value_lists` became read-only |

#### GET /classes/{internal_class_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.student_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `value_lists` became read-only |

#### GET /classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.student_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `value_lists` became read-only |

#### GET /courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `value_lists` became read-only |

#### GET /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `value_lists` became read-only |

#### GET /master_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.day_of_week` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.person` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `value_lists` became read-only |

#### GET /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.day_of_week` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.person` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `value_lists` became read-only |

#### GET /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.student_name` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `value_lists` became read-only |

#### GET /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.student_name` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `value_lists` became read-only |

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.items.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `value_lists` became read-only |

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.advisor` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.current_location` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.homeroom_teacher` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `value_lists` became read-only |

#### PATCH /classes/{internal_class_id}/attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_date` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.notes` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.status` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.internal_class_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.student_id` became read-only |

#### PATCH /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.catalog_description` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.catalog_title` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.course_id` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.course_type` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.name` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.id` became read-only |

#### PATCH /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_category` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_date` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.early_dismissal_time` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.excused` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.faculty_attendance_status` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.grading_period` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.late_arrival_time` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.notes` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.return_time` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.school_year` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.student_attendance_status` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.update_date` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.day_of_week` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.person_id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.person` became read-only |

#### PATCH /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.am_pm` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_end_date` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_return_time` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_start_date` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_time` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_type` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.bus_route` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.bus_stop` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.category` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.date` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.extended_care_arrival_time` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.extended_care_leave_time` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.extended_care_type` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.input_date` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.input_user` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_notes` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.notes` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.posted` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.reason` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.response_notes` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.status` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.student_id` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.transportation_method` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.student_name` became read-only |

#### POST /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.am_pm` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_end_date` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_return_time` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_start_date` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_time` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.attendance_type` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.bus_route` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.bus_stop` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.category` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.date` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.extended_care_arrival_time` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.extended_care_leave_time` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.extended_care_type` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.input_date` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.input_user` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_notes` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.notes` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.posted` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.reason` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.response_notes` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.status` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.transportation_method` became optional |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.id` became read-only |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The request required property `data.student_name` became read-only |

### 2021-03-26

#### GET /classes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.course` |

#### GET /classes/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `course` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.course` |

#### GET /classes/{internal_class_id}/attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `attendance_date` |

#### GET /courses

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /master_attendance

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `person_id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `update_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `attendance_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_update_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_update_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `person_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.person_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.update_date` |

#### GET /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `person_id` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `update_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.person_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.update_date` |

#### GET /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `input_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `input_user` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_after_input_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional query string request parameter `on_or_before_input_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.input_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.input_user` |

#### GET /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `input_date` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added enum value `input_user` to the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.input_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.input_user` |

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `role` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.role` |

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed enum value `role` from the `value_lists.items.fields.items` response property |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.role` |

#### PATCH /courses/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /master_attendance/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.person_id` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.update_date` |

#### PATCH /student_logistics_requests/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.input_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.input_user` |

#### POST /student_logistics_requests

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.input_date` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added required request property `data.input_user` |

### 2021-03-23

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

## December 2020

### 2020-12-07

Initial documentation published

## August 2020

### 2020-08-19

First Data API release

