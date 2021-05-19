from flask import Flask, render_template, request, redirect, url_for
import csv

# render_templeate allows to send html files

# Free html / css templates: http://www.mashup-template.com/templates.html
# css and html from the initial exercises below were copied to _old
# new templates and static folders contain the html / css files from the above
# website

# Other cool templates: https://html5up.net/

app = Flask(__name__)
print(__name__)

# to tun this you need to do in the command line:
# export FLASK_APP=server.py  to set the environment variable
# flask run
# Response:
# flask run
# * Serving Flask app "server.py"
# * Environment: production
#   WARNING: This is a development server. Do not use it in a production deployment.
#   Use a production WSGI server instead.
# * Debug mode: off
# server
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# the http above is the local URL (the address of the laptop you are working on)
# it you copy the URL in a browser, you'll see the hello world output

# to set up the debug environment do:
# Note this is not working, using the app.run(debug=True) above
# export FLASK_ENV = development

# double curly brackets in flask e.g. {{ expression }} are evaluated using 'jinja'
# as python expressions: {{ 4 + 5 }} will print 9
# to test this, do:


# @app.route('/')
# def hello_world():
# return 'Hello, World, this is me again!'
# fort the render template to find index, the file needs to be in a 'templates' folder
# available in the directory where this file is
#print(url_for('static', filename='earth.ico'))
# return render_template('index.html')

# The <username> is passed to the function below, using e.g. 127.0.0.1:5000/bob
# prints bob
# @app.route('/<username>')
# def hello_world(username=None):

#    return render_template('index.html', name=username)

# see flask docs: we can also pass an integer (requested to be integer with int:)

@app.route('/')
def my_home():
    return render_template('index.html')
    # @app.route('/index.html')
    # def index():

    #    return render_template('index.html')


# @app.route('/index.html')
# def index():
#    return render_template('index.html')


# @app.route('/works.html')
# def work():
 #   return render_template('works.html')


# @app.route('/about.html')
# def about():
#    return render_template('about.html')


# @app.route('/contact.html')
# def contact():
#    return render_template('contact.html')


# @app.route('/components.html')
# def components():
#    return render_template('components.html')

# we can do the above automatically


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# for thsi to work, line 75 of contact.html was changed to have action="submit_form"
# with method="post". This will get actioned when the button "Send" is pushed
# Also, all the input data <input in contact.html need to be given a name attribute
# so that the information can be used / captured using python


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
        # write_to_file(data)
            print(data)
    #    if valid_login(request.form['username'],
    #                   request.form['password']):
    #        return log_the_user_in(request.form['username'])
    #    else:
    #        error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)
        # return 'form submitted!'
            return redirect('thankyou.html')
        except:
            return 'Something is wrong, could not save to database'
    else:
        return 'something went wrong, try again'


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

# the newline option below create a new line when adding the file, so that
# the headers (typed manually) are not in the same line as the first entry


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


app.run(debug=True)      # setting the development flag somehow does not work
