from flask import Flask , render_template,url_for,request,redirect
import csv
app = Flask(__name__)



@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)
def write_to_csv(data):
    with open(r'database.csv',mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',' ,quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

def write_to_file(data):
    with open('database.txt',mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database2.write(f'\n{email},{subject},{message}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # data = request.form['email']
        try:
          data = request.form.to_dict()
        # print(url_for('static/assets','favicon.ico'))
          write_to_csv(data)
        # write_to_file(data)
          return redirect('/thankyou.html')
        except:
            return 'do not save to database'
    else:
        return 'something went wrong'