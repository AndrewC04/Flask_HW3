from flask import Flask

myapp_obj = Flask(__name__)

@myapp_obj.route("/")

name = {'username':'Lisa'}
city_names = ['Paris','London','Rome','Tahiti']

def home():
    for city in range(len(city_names)):
        return '''
        <!DOCTYPE html>
        <html>
            <body>
                <h1> Welcome ''' + name['username'] + '''! </h1>
                <p> <a href="http://www.google.com/"> not google </a> </p>
            <ul>
                 <li> ''' + city_names[city] + ''' </li>
                 <li> ''' + city_names[city+1] + ''' </li>
                 <li> ''' + city_names[city+2] + ''' </li>
                 <li> ''' + city_names[city+3] + ''' </li>
            </ul>
            </body>
        </html> '''
    
if __name__ == "__main__":
    myapp_obj.run(debug=True)
