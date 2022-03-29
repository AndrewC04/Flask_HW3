from flask import Flask

myapp_obj = Flask(__name__)

@myapp_obj.route("/")

def home():
    name = {'username':'Lisa'}
    city_names = ['Paris','London','Rome','Tahiti']

    return f'''
    <!DOCTYPE html>
    <html>
        <body>
            <h1> Welcome {name["username"]}! </h1>
            <p> <a href="http://www.google.com/"> not google </a> </p>
            <ul>
                {% for city in city_names %}
                <li> {{ city }} </li>
                {% endfor %}
            </ul>
        </body>
    </html> '''

if __name__ == '__main__':
    myapp_obj.run(debug=True)
