Snapchat Dashboard
===================

My first taste of Django was making a Snapchat Dashboard.

This is it.

I used a Snapchat library lovingly made by [niothiel](https://github.com/niothiel).

There are probably better ways to do this, but hey. It's my first time.

#Running it

Install the following (might need to `sudo`):

```
pip install Django
pip install requests
easy_install pycrypto

```

Change the following line in `views.py`:

```py
s.login('YOUR_SNAPCHAT_USERNAME', 'YOUR_SNAPCHAT_PASSWORD')
```

And then just run the server to check it out in your browser:

```
python manage.py runserver 8080
```
