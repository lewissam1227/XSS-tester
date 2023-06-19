This script sends an HTTP request to the URL, parses the response using BeautifulSoup, and finds all input and textarea tags. It then injects a simple XSS payload into each field and sends the form data back to the server. If the injected payload is reflected in the response HTML, it indicates a potential XSS vulnerability.

Again, this is a basic script for educational purposes. Comprehensive vulnerability scanning tools like OWASP ZAP or Burp Suite are recommended for more thorough XSS testing and detection. I only create these tools to learn more about Python scripting.

Remember to always obtain proper authorization before performing any security testing on websites or services.
