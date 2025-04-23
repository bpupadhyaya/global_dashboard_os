# global_dashboard_os_api
Global Dashboard OS API.

Steps:
------

* In order to test the setup, define a function called `main` in `views.py`:
```
def main(request):
    return HttpResponse("Leadership Dashboard OS)
```

* Create `urls.py` file and link above main method to a url, it can be empty as well. If it is empty then it will be base url of the app.
* Next, link `/global_dashboard_os_api/urls.py` to `/global_dashboard_os/urls.py`


