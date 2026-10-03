# Value Lists

Many fields in the Data API are "value lists". These are fields where appropriate values are from a separate list. The options for value list fields are found in a corresponding `value_list` key of the response object.

When using value list fields for parameters or in data updates the `id` of the value list object must be provided for the field's value.

### School Customization

Many value lists in Veracross can be customized by each school individually. School specific customizations can apply to any property of a value list item (id, description, etc).

<!-- theme: warning -->
> Value lists will be consistent across different API requests that include the same field, but **shouldn't** be shared between different schools.

### Request/Response

| Request Header | Default | Allowed Values | Optional/Required |
|---|---|---|---|
| `X-API-Value-Lists` | no value | `include` | Optional; when this header is set to `include`, the `value_list` field will be provided in the response |

| Response | |
|---|---|
| fields | An array of field names from `data` that this value list goes with |
| items | An array of value list items whose `id` field matches the value in the response data |
| categories | An array of "category" objects, which allow you to partition the value list items according to their category field |

| Items | |
|---|---|
| id | This value corresponds to field data. It can be a string or a number |
| description | The label for this value in the user interface |
| category | A category id value that corresponds to the "category" items |
| sort_key | A value used for ordering value list items in a UI |

| Categories | |
|---|---|
| id | The category's id, to be used for correlation with an item category |
| description | The label for this category in the UI |
| sort_key | A value used for ordering categories in the UI |

### Example

On the Students endpoint there's a field called `grade_level`. While JSON property itself is a number, in Veracross this field is a value list type.

The corresponding value list options are also provided in the response. You can match which option goes with each data field by finding the name of the data field in the value list's "fields" array.

```json
// example Students API response
{
  "data": [{
    // (other fields omitted)
    // "20" correspond to an item in the value list "items" array
    "grade_level": 20,
  }, {
    // (other students omitted)
  }],

  "value_lists": [{
    "fields": [
      // This entry applies to the "grade_level" field
      "grade_level"
    ],
    // here are the list of possible values:
    "items": [{
      "id": 0,
      "description": "None",
      "category": 0,
      "sort_key": 1
    }, {
      // this object's id field is 20, same as in the response data,
      // so we know that student's grade level is Kindergarten
      "id": 20,
      "description": "Kindergarten",
      "category": 0,
      "sort_key": 2
    }, {
      // ...
    }],
    // some value lists are categorized,
    // although this one has all the values together
    "categories": [{
      "id": 0,
      "description": "&lt;None&gt;",
      "sort_key": 0
    }],
  }, {
    // ...
  }
}
```
