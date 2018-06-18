# Simple API

Simple api project is simple.

## Requirements

Assume for all operations that we expect a REST API. We want to add to add
some features to our application laid out in the features section. Besides
those features you should keep in mind a few principals.

1. This project should have tests
2. This project should follow the style guideline

### Capabilities

- You must be able to create a metadata item.
- You must be able to update a metadata item.
- You must be able to delete a metadata item.
- You should be able to paginate all metadata item.
- You should be able to make bulk request for metadata items, limit up to 200.
- You should be able to filter items by kind, category (multiple)

### Data schema

The goal of this project is to allow the storage of metadata. All metadata
follows this form. We should ensure that this data is validated at all times.

Name       | Required            | Description
-----------|---------------------|---------------------------------------------------------
pk         | required for update | the primary key for this metadata
title      | Yes                 | A descriptive title, limited to 500 chars
url        | No                  | An optional url, max_length 1000 chars
kind       | Yes                 | One of three kinds 1:Abstract, 2:Presentation, 3:Dataset
categories | Yes                 | A list of strings min 1, max 5. String limit is 50.
created_at | n/a                 | Datetime of creation, not writeable.
updated_at | n/a                 | Datetime of update, not writable.


Here is an example JSON object.

```
{
  "pk": 1,
  "title": "This is a title",
  "url": "http://google.com",
  "kind": 1,
  "categories": ["simple", "api"]
  "created_at": "2018-04-26T18:10:28Z",
  "updated_at": "2018-04-26T18:10:28Z",
}
```
