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
