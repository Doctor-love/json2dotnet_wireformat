# json2dotnet_wireformat - Convert JSON to ASP.NET MVC wire format

## Introduction
Small utiliy developed in Python 3 to convert JSON data to ASP.NET MVC wire format, used for model binding.  
  
"Why would I ever need this?!", you may say.  
Cross-Site Request Forgery attacks is one answer.  

Applications that use JSON in POST requests are typically protected by enforcing usage of the "application/json" content type.  
ASP.NET applications does however have a nasty habbit of also accepting URL encoded forms, which are not typically protected by CORS.  
If the data structure is simple, such as "{"foo": "bar"}, it can be converted to "foo=bar", but if nested lists and dictionaries are involved things get a bit more complicated.  
  
Thanks to the [ASP.NET MVC wire format](https://www.hanselman.com/blog/ASPNETWireFormatForModelBindingToArraysListsCollectionsDictionaries.aspx), it is however possible to represent these complex structures in forms.  
  
This lousy little utily tries to do just that - convert JSON to the wire format.  


## Examples
```
$ echo '{"user": "jann3", "privs": [{"module": "banking", "admin": true}, {"module": "orders", "admin": false}]}' | ./json2dotnet_wireformat.py

privs[0].admin=true&privs[0].module=banking&privs[1].admin=false&privs[1].module=orders&user=jann3
```
  
```
[...]

from json2dotnet_wireformat import process_json

data = process_json(json_data)
```
