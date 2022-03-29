from flask import Flask

myapp_obj = Flask(__name__)

@myapp_obj.route("/")

def home():
    name = {'username':'Lisa'}
    city_names = ['Paris','London','Rome','Tahiti']

    return '''
    <!DOCTYPE html>
    <html>
        <body>
            <h1> Welcome ''' + name['username'] + '''! </h1>
            <p> <a href="http://www.google.com/"> not google </a> </p>
            <ul>
                <li>Paris</li>
                <li>London</li>
                <li>Rome</li>
                <li>Tahiti</li>
            </ul>
        </body>
    </html> '''

if __name__ == '__main__':
