@myapp_obj.route("/")

def home():
  name = {'username':'Lisa'}
  city_names = ['Paris','London','Rome','Tahiti']
  
  return render_template('home.html', name=name, cities=city_names)
