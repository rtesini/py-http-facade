# py-http-facade



My take on a simple HTTP Façade for easy request making.

## Examples

Simple get:

```python
    Response r = HttpFacade("www.google.com").get();
    r.status() // 200
    r.content() // <html>...
```

More complex request:

```python
    HttpFacade("luan.xyz/api/people")
        .header("key", "value")
        .body("{ id: 42, name: \"Luan\" }")
    .post();
```
