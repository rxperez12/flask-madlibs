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

3. POST request - Route (/results)
- posting everything from `results.jinja`

