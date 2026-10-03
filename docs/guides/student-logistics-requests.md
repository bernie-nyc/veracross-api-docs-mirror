# Student Logistics Requests

Student Logistics Requests are a way for a parent to indicate a change to their students daily attendance, transportation plan, or extended care schedules.

### Creating a new Student Logistics Request

Student Logistics Requests are created for a student by a parent. The type of logistics request is indicated by the `request_category`. `request_category` is a Value List with values: Attendance, Transportation to School, Transportation from School, Extended Care, or Multi-Day Absence. Depending on the type of request certain fields should be populated in specific ways. See the below table for details.

<!-- theme: info -->
> Note: fields that are required for insert are marked as such.

|Field Name|Description|Field Details|
|---|---|---|
|student_id|The id of the student this request is for|**required**|
|request_date|The date this request is for|**required**|
|request_category|Value List indicating what type of request this is|**required**|
|request_status_completion_date|Date the request was completed|Default to the date the request was submitted|
|request_reason|Value List indicating the reason for the request||
|request_notes|Additional details about the request||
|attendance_type|Value List indicating what type of attendance change this request is for|Default to 0 if none specified|
|attendance_start_date|If this is an attendance request, the start date the attendance change will take affect for the student|If the request_category is Attendance or Multi-Day Attendance and the start date is not blank use the attendance_start_date otherwise use request_date|
|attendance_end_date|If this is an attendance request, the end date the attendance change will take affect for the student|If the request_category is Attendance or Multi-Day Attendance and the end date is not blank use the attendance_end_date otherwise use request_date<br>if this is an attendance request, the start date the attendance change will take affect<br>if the request_category is Attendance or Multi-Day Attendance and the start date is not blank use the attendance_start_date otherwise use request_date|
|attendance_time|If this is an attendance request, the time of day the student is expected to leave school||
|attendance_return_time|If this is an attendance request, the time of day the student is expected to return to school||
|extended_care_type|Indicates what type of extended care change this request is for||
|extended_care_arrival_time|If this is an extended care request, the time the student is expected to arrive for extended care||
|extended_care_leave_time|If this is an extended care request, the time the student is expected to leave extended care||
|am_pm|Value List indicating if a transportation request is for a morning or the evening schedule change|If the request_category is "transportation to school" the value should be "AM", if the request_category is "transportation from school" or "extended care" the values should be "PM". Otherwise specify as "Both".|
|transportation_method|If this is a transportation request, Value List indicating the new transportation method this student will take to get home||
|bus_route|If this is a transportation request and the transportation method is "bus", Value List indicating the new bus route the student will take home|Only populate if the transportation_method is "Bus"|
|bus_stop|If this is a transportation request and the transportation method is "bus", Value List indicating the new bus stop the student will take home|Only populate if the transportation_method is "Bus"|
|posted|Indicates if this record is locked for further edits||


### Updating a Student Logistics Request

The following fields are available for update:

|Field Name|Description|Field Details|
|---|---|---|
|request_status|Value List indicating the whether the request was approved or denied|Approved requests have additional logic in Veracross to update related child tables with the approval in real time|
|request_notes|Additional details about the request||
|response_notes|Additional details about the response for the request (i.e. reason why the request was denied)||
|internal_notes|Internal notes about the request||

To mark a Student Logistic Request as approved or denied, update the `request_status`. `request_status` is a Value List with the following values:

<!-- theme: info -->
> Note: All options for Value List fields are available for any API request. For details, see [Value Lists](../concepts/value-lists.md)

|request_status|Description|
|---|---|
|Approved|Request was approved, no automatic email through Veracross is sent|
|Approved - send Email|Request was approved, Veracross will automatically send a confirmation email to the requestor (i.e. the parent)|
|Denied|Request was not approved, no automatic email through Veracross is sent|
|Denied - send Email|Request was denied, Veracross will automatically send a declined email to the requestor (i.e. the parent)|

<!-- theme: info -->
> Note: for sandbox purposes use the Approved and Denied values only
