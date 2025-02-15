from flask import Flask, render_template, request, session, jsonify
import pandas as pd
from Connect4 import *

app = Flask(__name__)
app.secret_key = 'MyCodedData'

@app.route('/')
def start():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        usr = session['user']
        return redirect(url_for('home', usr = usr))
    else:
        if request.method=='POST':
            usr = request.form['usrname']
            pswrd = request.form['pswrd']
            lg_data = pd.read_csv('login_data.csv')
            # try:
            if str(lg_data.iloc[lg_data[lg_data['username']==usr].index.values[0]]['password']) == pswrd:
                session['user'] = usr
                return redirect(url_for('home', usr = usr))
            else:
                print(type(lg_data.iloc[lg_data[lg_data['username']==usr].index.values[0]]['password']))
                print(type(pswrd))
                return render_template('login.html') 
            # except:
            #     return render_template('login.html') 
        else:
            return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup(usr):
    if request.method=='POST':
        usr = request.form['usrname']
        fname = request.form['fname']
        sname = request.form['sname']
        mail = request.form['mail']
        pswrd = request.form['pswrd']
        Cpswrd = request.form['Cpswrd']
        if len(pswrd)>7 and pswrd == Cpswrd:
            lg_cre = [[usr, fname, sname, mail, pswrd]]
            lg_data = pd.DataFrame(lg_cre)
            lg_data.to_csv('login_data.csv', mode='a', index=False, header=False)
            if True:
                return redirect(url_for('login'))
        else:
            return render_template('Signup.html')
    else:
        return render_template('Signup.html')

# if 'user' in session:
#     usr = session['user']

@app.route('/<usr>', methods=['GET', 'POST'])
def home(usr):
    if 'user' in session:
        usr = session['user']
        return render_template('Home.html', user=usr)
    else:
        return redirect(url_for('login'))

@app.route('/Connect4', methods=['GET', 'POST'])
def Connect4():
    global A
    A = Connect_4()
    return render_template('Connect4.html')

@app.route('/TicTac', methods=['GET', 'POST'])
def TicTac():
    return render_template('TicTacToe.html')

@app.route('/Profile', methods=['GET', 'POST'])
def Profile():
    return render_template('Profile.html')

@app.route('/Logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('home', usr = ""))

@app.route("/won<player>", methods = ['GET', 'POST'])
def Won(player):
    return render_template('Won.html', Player = player)

@app.route("/Turn/<ID>/<color>")
def Turns(ID, color):
    i = int(ID)
    x = i//7
    y = i%7
    if color == "red":
        key = A.P1Turn((x, y))
        A.show()
    else:
        key = A.P2Turn((x, y))
        A.show()
    if key in [1, 2]:
        return jsonify(dict(redirect=f'Player {key}'))
    return "aa"


if __name__ == '__main__':
    app.run(debug=True)