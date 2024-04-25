# Madlibs

Given a question with a set of questions:
 - user inputs an answer for each question

 ```
plural_noun: turnips
verb: juggle
 ```

Build a story template of that puts together the questions and answers
```
I love to {verb} {plural_noun}.
```

Create a story
```
I love to juggle turnips.
```

## Story Class

### constructor method
- takes in:
    - self
    - words
    - text
- outputs:
    - sets self.prompts and self.template

### get_result_text method
- takes in:
    - self
    - answers
        - the answer values are from a result dictionary (request.args)
            - `ans = {"verb": "eat", "noun": "mango"}`
            - `.get_result_text(ans)`


app.py
- endpoints are the same for GET and POST

1. GET request - Route (/)
- when someone enters website for first time
- fn:
    - generate plain html form

2. GET request - Route (/)
- when someone presses submit on the form
- do GET request to the server
- fn:
    - get user's input
    - `ans = {"verb": "eat", "noun": "mango"}`
    - `.get_result_text(ans)`
        - calling the .get_results_text method to put answer into story format
    - save the results from `.get_result_text(ans)` into `results.jinja`

Why did GET work?
- bc the form had action /results, that is the endpoint we are listening to for a GET request

POST request if we wanted to save the result for the form, etc.


## Allow User to Pick Story

1 - add a dropdown to homepage of story templates

```html
<div class="dropdown show">
  <a class="btn btn-secondary dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Dropdown link
  </a>

  <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
    <a class="dropdown-item" href="#">Action</a>
    <a class="dropdown-item" href="#">Another action</a>
    <a class="dropdown-item" href="#">Something else here</a>
  </div>
</div>
```


2 - update `generate_template` fn to update `words` based on the story that was selected
    - get the story template selection
    - add an if statement
