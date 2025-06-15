<h1> Personal Data (Personal Identifiable Information (PII)) </h1>
Personally Identifiable Information (PII) refers to any data that can be used to identify a specific individual.
Examples include:
<ul>
    <li> Full Name</li>
    <li> Home Address</li>
    <li> Email Address</li>
    <li> Phone Number</li>
    <li> Date of Birth</li>
    <li> Social Security Number (SSN)</li>
    <li> Driver's License Number</li>
    <li> Passport Number</li>
    <li> Biometric Data (e.g. fingerprints, facial recognition)</li>
    <li> Credit Card or Bank Account Number</li> etc
</ul>

<h2> Steps to Obfuscate PII in Logs </h2>
<ol>
    <li> Define which fields are PII</li>
    <li> Create a function to mask PII values</li>
    <li> Custom Logging filter or formatter</li>
    <li> Setup the logger</li>
    <li> Test the logger</li>
</ol>

Tips: For production purpose use structured logging libraries like structlog, loguru, or json-logger for better control.
