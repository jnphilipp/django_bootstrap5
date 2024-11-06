# django bootstrap5 app

![Linting & Tests](https://github.com/jnphilipp/django_bootstrap5/actions/workflows/tests.yml/badge.svg)


## Included versions

* [Bootstrap](https://github.com/twbs/bootstrap) (bundle): 5.3.3
* [jQuery](https://github.com/jquery/jquery): 3.7.1
* [jQuery UI](https://github.com/jquery/jquery-ui): 1.14.1
* [Select2](https://github.com/select2/select2): 4.0.13


## Usage

### Basics

Load with `{% load bootstrap %}` and include CSS/JS with:

```html
<head>
  {% bootstrap_css %}
  {% bootstrap_js %}
</head>
```

### iFrame modal

Simple modal with an iFrame, designed for usage with forms.

Add modal with `{% iframe_form_modal %}`, with options:
* **iframe_min_height**: `iframe_min_height="500px"` set minimum height of iframe
* **iframe_max_height**: `iframe_max_height="500px"` set maximum height of iframe
* **static_backdrop**: `static_backdrop=False` static backdrop of the model, defaults to `True`

Open link with:
```html
<a href="{% url SOME_FORM %}" title="{% trans "Modal title" %}" data-bs-toggle="modal" data-bs-target="#iframeFormModal">open modal form</a>
```

The URL will be loaded in the iFrame and the title will be set as the modal title.
