<h1> Session Authentication </h1>
This is a way the server verifies the permission of a client request by
returning a token in the form of a cookie to the client after the first authorization

<h1> The flow of the Session Authentication</h1>
<ul>
   <li> User submits login credentials e.g. email & password</li>
   <li>Server verifies the credentials against the Database</li>
   <li>Server creates a temporary user session</li>
   <li>Server issues a cookie with a session ID</li>
   <li>User sends the cookie with each request</li>
   <li>Server validates it against the session store & grants access</li>
   <li>When user logs out, server destroys the session & clears the cookie</li>
</ul>

<h1>Running the server on local terminal </h1>
In the first terminal:
    Create a new user with the necessary credentials in a main file
    Run: <code>API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth ./main_0.py </code>
    Then run the server using:
      <code>API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app</code>

In the second terminal:
Test different endpoint:
    <code>curl "http://0.0.0.0:5000/api/v1/status"</code>
    <code>curl "http://0.0.0.0:5000/api/v1/users"</code>
    <code>curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"</code>
    <code>curl "http://0.0.0.0:5000/api/v1/users/me" -H "Authorization: Basic Ym9iQGhidG4uaW86SDBsYmVydG9uU2Nob29sOTgh"</code>
