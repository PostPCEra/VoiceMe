# VoiceMe

Flask Tutorial -- good one: 
 + covers step by step of each topic : [Templates, Forms, Ajax, etc..](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
 + In this tutorial  having 'app' folder and 'router.py', __init__.py is confusing, so just juse one file for routes and to start/run server.
 +

**ngrok :**
```
1. start you flask webserver , note the port number
2. find ngrok executable as ~/Downloads/ngrok
3. $ln ~/Downloads/ngrok .   # this establishing a symbloic link

4. login to ngrok.com with github credentials, it shows authtoken code , execute it
5. $ ./ngrok authtoken <TOKENCODE>


6. ./ngrok http PORT   # same port as flask webserver

you have url available for whole world

```


