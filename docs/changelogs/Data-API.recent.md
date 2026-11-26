# Data API - Recent Changelog

## November 2026

### 2026-11-25

#### DELETE /ancestral_affiliations/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /ancestral_affiliations

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /ancestral_affiliations/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /ancestral_affiliations/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /ancestral_affiliations

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-11-23

#### GET /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.exclude_from_report_card` to the response with the `200` status |

#### GET /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.exclude_from_report_card` to the response with the `200` status |

#### GET /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.exclude_from_report_card` to the response with the `200` status |

#### GET /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.exclude_from_report_card` to the response with the `200` status |

#### PATCH /academics/enrollments/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.exclude_from_report_card` |

#### PATCH /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.exclude_from_report_card` |

#### POST /academics/enrollments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.exclude_from_report_card` |

#### POST /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.exclude_from_report_card` |

### 2026-11-18

#### GET /academics/qualitative_grades

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.rubric_criteria.description` response property's maxlength was set to `800` for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | The `data.items.rubric_criteria.description` response's property `type` changed from `integer` to `string` for status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed the `rubric_criteria.description` enum value from the `value_lists.items.fields.items` response property for the response status `200` |

### 2026-11-12

#### GET /students

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.home_languages` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.place_of_birth` to the response with the `200` status |

#### GET /students/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.home_languages` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.place_of_birth` to the response with the `200` status |

### 2026-11-11

#### GET /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.preferred_name` to the response with the `200` status |

#### GET /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.preferred_name` to the response with the `200` status |

#### PATCH /athletics/rosters/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.preferred_name` |

#### POST /athletics/rosters

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.preferred_name` |

### 2026-11-10

#### Other Changes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | A breaking change was detected but the version is still `3.0.0` |

#### GET /academics/student_assignments

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added `publish_status` enum value to the `value_lists.items.fields.items` response property for the response status `200` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added optional `query` request parameter `publish_status` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.publish_status` to the response with the `200` status |

#### GET /athletics/teams/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Response property `data.internal_sport_id` became read-only for the status `200` |

#### GET /student_logistics/reasons

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.lock_attendance_on_approval` to the response with the `200` status |

#### PATCH /athletics/teams/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_sport_id` became read-only |

#### POST /athletics/teams

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.internal_sport_id` became read-only |

#### POST /exams/qualifications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Request property `data.awarding_body_id` became optional |

## October 2026

### 2026-10-29

#### DELETE /exams/sessions/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/awarding_bodies

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/awarding_bodies/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/candidates

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/candidates/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/entries

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/entries/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/incidents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/incidents/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/qualification_components

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/qualification_components/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/qualifications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/qualifications/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/seasons

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/seasons/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/sessions

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### GET /exams/sessions/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /exams/awarding_bodies/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /exams/candidates/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /exams/entries/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /exams/incidents/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /exams/qualification_components/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /exams/qualifications/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /exams/seasons/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### PATCH /exams/sessions/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /exams/awarding_bodies

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /exams/incidents

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /exams/qualification_components

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /exams/qualifications

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /exams/seasons

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

#### POST /exams/sessions

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Endpoint added |

### 2026-10-21

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.external_invoice_number` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.items.external_invoice_url` to the response with the `200` status |

#### GET /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.external_invoice_number` to the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added property `data.external_invoice_url` to the response with the `200` status |

#### PATCH /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.external_invoice_number` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.external_invoice_url` |

#### POST /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.external_invoice_number` |
| <img src='https://assets.veracross.com/_documentation/api/icons/plus.svg' alt='plus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Added request property `data.external_invoice_url` |

### 2026-10-20

#### Other Changes

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/info.svg' alt='info' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | A breaking change was detected but the version is still `3.0.0` |

#### GET /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.external_po_number` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.items.external_po_url` from the response with the `200` status |

#### GET /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.external_po_number` from the response with the `200` status |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed property `data.external_po_url` from the response with the `200` status |

#### PATCH /finance/ap_invoices/{id}

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.external_po_number` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.external_po_url` |

#### POST /finance/ap_invoices

|    | Description |
|----|-------------|
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.external_po_number` |
| <img src='https://assets.veracross.com/_documentation/api/icons/minus.svg' alt='minus' width='16' height='16' style='max-width: 16px; padding-top: 4px; pointer-events: none;'> | Removed request property `data.external_po_url` |

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

### Older updates

For older updates, please refer to the [full changelog history](./docs/changelogs/Data-API.full.md).

