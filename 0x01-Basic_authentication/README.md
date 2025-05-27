<h1> Basic Authentication </h1>
It is an HTTP authentication method where the client sends a username and password, encoded in base64, as part
of the HTTP request header.

<b><i> Base64 </i></b>: A method of encoding binary data into ASCII characters

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
