# Integrating with Admission Endpoints

Veracross offers a wide range of API endpoints for the purpose of integrating with the Veracross Admission module. These endpoints provide you with the ability to create, read, and update all the critical admission-related records housed in Veracross.

## Using this Guide

Veracross stores admission data in a specific way with a variety of interconnected records. The way in which these records are interconnected requires a specific order of operations to ensure the data is inserted correctly.

The purpose of this guide is to share best practices for using the Veracross Admission endpoints. We've included perspectives from the Veracross Product Team and partners/vendors who have used these endpoints for their own integrations. We expect to update this guide over time as best practices evolve. It remains your responsibility to decide the best way to use our Admission API endpoints for your integration.

Please direct questions/feedback about the admission endpoints and/or this guide to Veracross Product Manager, [Thad White](mailto:thad.white@veracross.com).

## Before You Begin

If you haven't done so already, please review the Concepts section of our API documentation - there is a lot of information that will be helpful as you familiarize yourself with the Veracross API. In addition, [Making a Data API Request](../guides/making-a-data-api-request.md) guide is very helpful for walking you through your first time making a request to the Data API. This guide will assume you already know how to integrate with the Data API. Here's a tip from that documentation that is particularly useful when interacting with the admission endpoints:

Set `X-API-Value-Lists = Include` in your response header to receive value lists for certain fields with your response - this is particularly helpful when mapping values from your system to their equivalent in Veracross.

Veracross Admission module works most effectively for schools when we can avoid duplicate records as early as possible. Therefore before creating admission records, we recommend always checking for possible duplicates first.

## Creating or Updating an Applicant

All admission functionality in Veracross begins with and builds upon an applicant's person record. This person record is composed of all the demographic data points the school has gathered about the person. In Veracross, this record persists beyond the admission process and acts as the source of truth for this person's demographic information throughout their relationship with the school.

Creating a person record or identifying an existing person record is always the first step in integrating with Veracross Admission data. Given the critical nature of the one-record architecture, it is strongly advised that any process tasked with inserting new people into the database be preempted with a search to see if the person already exists in the database.

### 1. Check if the Applicant Already Exists

#### Step 1: Check if the applicant exists using the admission applicants endpoint

[list Admission: Applicants records](../../reference/Data-API.yaml/paths/~1admission~1applicants/get)

You can check to see if the applicant already exists based on a number of criteria, including first and last name:

`/admission/applicants?last_name=abbott&first_name=john`

If the applicant exists, continue on to STAGE 2.

#### Step 2: If no applicant exists, check to see if a household already exists for this family using the admission households endpoint

[list Admission: Households records](../../reference/Data-API.yaml/paths/~1admission~1households/get)

You can check to see if the household exists based on the address:

`/admission/households?address_1=401&city=wakefield`

If there are multiple households that match the address, check to see if there are any known relatives in the household:

[list Admission: Household Members records](../../reference/Data-API.yaml/paths/~1admission~1households~1%7Bhousehold_id%7D~1members/get)

You can check to see if a known relative exists based on their first and last name:

`/admission/households/41566/members?first_name=Test&last_name=A`

### 2. Create a New Applicant

#### Option A: No Household/No Applicant

Use this option if you have determined that no matching applicant already exists in the system AND no family members with whom this new person resides (via the same household/Address) exist in the system. Applicants must reside within a household record. To create a new household record, exclude the `household_id` field from the data object of the create applicant endpoint.

<!-- theme: warning -->
> #### Warning
>
> Failure to identify existing person or household records will result in the creation of duplicate records that must be manually cleaned up by the school.

[create Admission: Applicant record](../../reference/Data-API.yaml/paths/~1admission~1applicants/post)

#### Option B: Household exists, but no Applicant

Use this option if you have determined that NO matching applicant exists in the system but you have found parents and/or siblings who reside in the correct household (address) record.

<!-- theme: warning -->
> #### Warning
>
> Failure to identify existing person or household records will result in the creation of duplicate records that must be manually cleaned up by the school.

[create Admission: Applicant record](../../reference/Data-API.yaml/paths/~1admission~1applicants/post)

### 3. Update an Applicant

Any demographic-related changes to an applicant's record can be synched to Veracross using a patch request.

[patch Admission: Applicant record](../../reference/Data-API.yaml/paths/~1admission~1applicants~1%7Bapplicant_id%7D/patch)

## Creating or Updating an Application

Now that you have identified the applicant's existing person record or created a new person record for them, the next step is to get the details of their admission candidacy into the system via an application record. The application record encapsulates all of the year-specific data points for an applicant.

Applicants who have applied to the school multiple times should have multiple application records - one for each year - but it is a best practice to maintain only one application record per year.

### 1. Check if an Application Record Exists

Use the admission applications endpoint to determine if a specific applicant has an existing application record for the year they are applying for.

[list Admission: Application records](../../reference/Data-API.yaml/paths/~1admission~1applications/get)

Use `applicant_id` and `year_applying_for` to look for a specific applicant/year pairing:

`/admission/applications?applicant_id=21580&year_applying_for=2014`

### 2. Create an Application Record

Use this option if you have determined that no matching application already exists in the system for a specific applicant.

<!-- theme: warning -->
> #### Warning
>
> Failure to identify existing person or household records will result in the creation of duplicate records that must be manually cleaned up by the school.

[create Admission: Application record](../../reference/Data-API.yaml/paths/~1admission~1applications/post)

### 3. Update an Application Record

Any application-related changes to an applicant's record can be synched to Veracross using a patch request.

[update Admission: Application record](../../reference/Data-API.yaml/paths/~1admission~1applications~1%7Bapplication_id%7D/patch)

## Creating or Updating a Relative

It's very common to collect information about an applicant's parents and siblings as part of the admission process. Veracross has the ability to house this information as well as information about extended family members and family friends who are stakeholders in the applicant's admission process. As with applicant person records, these records persist beyond the admission process and act as the source of truth for the person's demographic information throughout their relationship with the school.

In the case of relatives who already exist in the database, we advise extreme caution when considering patch requests beyond defining the relationship between them and the applicant. For example, if the applicant's uncle is the Head of School, it's a bad idea to send a patch request to change their email address on file.

### 1. Check if Relative Person Records Exist

Parents and siblings are the most common relatives synced between systems, so it's a good idea to start by looking for existing members of the applicant's household. Follow the same steps outlined in the “Check if the Applicant Already Exists” section above to check if a household already exists for the relative you want to sync.

### 2. Create a Relative Person Record

Ensure that there is not already a relative in the system that matches the person you are trying to create. It is possible that that household that this relative should be apart of already exists, so specify the `household_id` if that value is known. Otherwise, the relative will be created in a new household.

<!-- theme: warning -->
> #### Warning
>
> Failure to identify existing person or household records will result in the creation of duplicate records that must be manually cleaned up by the school.

[create Admission: Relative record](../../reference/Data-API.yaml/paths/~1admission~1relatives/post)

This will return a valid “person_id” for the newly created person. Repeat this process as many times as necessary to create parents/guardians, siblings, grandparents, and any other relatives as needed.

## Upcoming Guide Updates

* Details/best practices for viewing and mapping applicant checklists
