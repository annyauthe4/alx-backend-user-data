<h1> Basic Authentication </h1>
It is an HTTP authentication method where the client sends a username and password, encoded in base64, as part
of the HTTP request header.

<b><i> Base64 </i></b>: A method of encoding binary data into ASCII characters

In this project, you will learn what the authentication process means and implement a Basic Authentication on a simple API.

In the industry, you should not implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask: Flask-HTTPAuth). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Basic Usage
<code>
    import base64

    text = "username:password"

    // Convert to bytes
    txt_bytes = text.encode('utf-8')

    // Encode
    base64_bytes = base64.b64encode(txt_bytes).decode('utf-8')
    print(base64_bytes)
</code>

## Decode to string
