from flask import Flask, render_template, request, flash
import random


application = Flask(__name__)
application.secret_key = "love"
'''
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='images/favicon.png')
'''
@application.route('/')
def index():
    return render_template('index.html')
    

@application.route('/results', methods=["GET", "POST"])
def results():
    name1 = request.form['name1']
    name2 = request.form['name2']
    '''
    text1 = ("Sorry but keep looking.")
    text2 = ("You may have found the one.")
    text3 = ("Don't let this one get away.")
    '''
    
    first =(len(name1))
    second =(len(name2))
    rnd = random.randint(1,20)
    percentage = 100-(first*second)-rnd

    if percentage <= 60:
      print("Chances of true love together is "+str(percentage)+"%")
      print("Sorry but keep looking.")
    elif percentage <= 80:
      print("Chances of true love together is "+str(percentage)+"%")
      print("You may have found the one.")
    elif percentage >= 80:
      print("Chances of true love together is "+str(percentage)+"%")
      print("Don't let this one get away.")
    #flash("percentage")
    return render_template('results.html', percentage=percentage)


if __name__ == '__main__':
    application.run()

    

