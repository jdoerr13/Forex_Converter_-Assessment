### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  1. primary usage- python is general purpose, backend programming, data analysis, and used with web development frameworks liek Django and Flask. - while JS is mainly used for front end, client side (with browers) web development and is essential for creating interactive web pages and web applications
  2. The syntax is quite different- python emphasizes readability with an indention block structure which JS does not enforce this and uses curly braces to define code blocks verses :. JS allows for more flexibility.
  

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
1. you can use the get() method in python.  
value = my_dict.get("c", -1)
print(value)  # Output: -1
2. you can use a try and except approach
  

- What is a unit test?
in python it test one 'unit' of functionality- typically one function or method (individual test in isolation). writting as unittest - part of python standard library. It is often used in classes.


- What is an integration test?
testing in Pythond that focuses on testing the interactions between different components or modules of a software application and verifies that components work together.


- What is the role of web application framework, like Flask?
Flask provides a structured and organized way to build web applications acting as a foundation that simplifies the development process (offering tools, libraries) handling common web dev tasks such as routing, request and response using HTTP.  Provides templates like jinja, session and cookie management, error handling.


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
1.  Use a parameter in a route URL when displaying detailed info about a specific product- like a subject of a page. But must be careful that a limited number of parameters can be included in the route before it becomes too long and less readable.
2.  use Query Parameter when the info is optional of non-essential and does not significantly affect the content of a page. such as filtering and sorting results on a search page - extra infor about a page. Often used then coming from form.
   

- How do you collect data from a URL placeholder parameter using Flask?
1. define a route with a URL placeholder paramenter @app.route().  
2. the route contails a URL placeholder parameter named for example <food_type>
3. when a request is made to a URL like /foods/pretzels, flask captures the value pretzel from URL and passes it as an argument to the view function- which will then process the captured value and return a response string if applicable. 
4. you can make a GET request using curl, URL, or HTML form(name=)


- How do you collect data from the query string using Flask?
using request.args object in the view function. such as: 
food_type = request.args.get('type')

GET /foods?type=pizza  when the app.route('/foods')


- How do you collect data from the body of the request using Flask?
    - create a flask application, define a route that handles the desired HTTP method - POST,  then collect the data in the request body using request.form.get('data').
    - you can then process the data in a few different ways, such as a response string showing the data has been received or test functionality with an HTML form when a POST request is make

- What is a cookie and what kinds of things are they commonly used for?
Cookies are a way to store small bits of info on the client(browser)- also meaning that they save 'state'. they are a name/string-value pair stored by the client (browser). the server tells the client to store these and the client sends the cookies to the server with each request. they are just strings, limited by how much info you can store (4kb) and They are commonly used for things with: personalization - user prefereances and settings, shopping carts, tracking and analytics, targeted advertising, security, tracking user progress, and working with sessions

- What is the session object in Flask?
The sessions are stored in the browser as a cookie.  They are serialized and signed so users could see, but can't change their actual session data- only Flask can.  Typically sessions are easier to work with then cookies. They are also refered to as a 'magic dictionary' in Flask, contain infor for the current browser, they preseve the type (list stay list).

- What does Flask's `jsonify()` do?
it simplifies the process of returning JSON responses from a Flask view function.  It takes python objects (dic or list) as inputs and converts them into JSON formatted response.  The purpose is to serialize Python data and set the 'content-type' header in the response to indicate that the data being returned in JSON format making it easier for web browser or other applications to understand and process the data. 
- when GET request is make to a specific route the view function returns a JSON reponse using something like:  return jsonify(data)
- this will eliminate the need to manually convert Python dictionaries to list to JSON strings.
