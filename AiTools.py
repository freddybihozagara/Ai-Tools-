import os
import pyperclip
from flask import Flask, jsonify, request, render_template
from datetime import datetime
from AiTools.server import connection
from AiTools.forms import aitoolsForm, updateForm, adduserForm
from dotenv import load_dotenv
from dotenv import dotenv_values
from AiTools.forms import aitoolsForm
from AiTools.config import init_env



# Initialize environment variables
config = init_env()

app = Flask(__name__)


SEC_KEY = os.environ.get("KEY")
app.config['SECRET_KEY'] = SEC_KEY
app.config['WTF_CSRF_ENABLED'] = True



@app.route('/pyperclip', methods = ['GET', 'POST'])
def copy(a):
        pyperclip.copy(a)
        pyperclip.paste()
        if request.method == 'GET':
            return render_template('success.html', title='copied to clipboard!!!')
        else:
            return render_template('success.html', title='invalid request!!!')



@app.route("/")
@app.route('/home', methods=['POST','GET'])
def home():
    if request.method == 'GET':
        return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        message='Welcome to AiTools & More!')
    else:
        return render_template('success.html', title='invalid request!!!')
    

@app.route('/about', methods=['POST','GET'])
def about():
    if request.method == 'GET':
        return render_template(
        'about.html',
        title='About Page',
        year=datetime.now().year,
        message='Welcome to AiTools & More.')
    else:
        return render_template('success.html', title='invalid request!!!')
    
@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method == 'GET':
        return render_template(
        'contact.html',
        title='Ai Tools & more',
        year=datetime.now().year,
        message='This is the contact page of AiTools!')
    else:
        return render_template('success.html', title='invalid request!!!')
    
@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'GET':
        name = None
        form = aitoolsForm()
        if form.validate_on_submit():
           name = form.name.data
           url = form.url.data
           category = form.category.data
        return render_template('form.html', title='AiTools& more Form', name=name, form=form)
    elif request.method == 'POST':
        name = request.form['name']
        url = request.form['url']
        category = request.form['category']
        cur = connection.cursor()
        cur.execute('''INSERT INTO aitools (name, url, category) VALUES (%s, %s, %s)''', (name, url, category))
        connection.commit()
        cur.close()
        return render_template('success.html', title='new ai tool successfully added!!!')
    else:
          return render_template('success.html', title='invalid request!!!')


def get_aitools():
    
    form = updateForm()
    cur = connection.cursor()
    try:
        cur.execute('''SELECT * FROM aitools''')
        result = cur.fetchall()
        cur.close()
        msg = jsonify(result)
        return render_template('aitoolslist.html', title='Ai Tools& more', results=result, message=msg, form=form)
        
    except Exception as e:
        cur.close()
        return str(e), 500



@app.route('/aitools', methods = ['POST','GET'])
def addtools():
    form = updateForm()
    if request.method == 'GET':
        
        return get_aitools()

    elif request.method == 'POST':
        name = None
        form = aitoolsForm()
        if form.validate_on_submit():
            name = form.name.data
            url = form.url.data
            form = updateForm()
            category = form.category.data
            cur = connection.cursor()
            cur.execute('''INSERT INTO aitools (name, url, category) VALUES (%s, %s, %s)''', (name, url, category))
            connection.commit()
            cur.close()
            return render_template('success.html', title='new ai tool successfully added!!!')
        
 





@app.route('/delete', methods = ['POST'])
def delete():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        url = request.form['url']
        cur = connection.cursor()
        cur.execute('''DELETE FROM aitools WHERE id = %s OR name = %s OR url = %s''', (id, name, url))
        connection.commit()
        cur.close()
        return render_template('success.html', title='ai tool successfully deleted!!!')
    else:
        return render_template('success.html', title='invalid request!!!')




@app.route('/update', methods = ['GET', 'POST'])
def update():
    form = updateForm()
    if request.method == 'GET':
        name = None
   
        if form.validate_on_submit():
           name = form.name.data
           url = form.url.data
           category = form.category.data
        return render_template('updateform.html', title='AiTools& more Form', name=name, url=url, category=category, form=form)
    elif request.method == 'POST':
        id = form.id.data
        name = form.name.data
        url = form.url.data
        category = form.category.data
        cur = connection.cursor()
        cur.execute('''UPDATE aitools SET id=%s, name=%s, url=%s, category=%s WHERE id = %s''', (id, name, url, category, id))
        connection.commit()
        cur.close()
        return render_template('success.html', title='ai tool successfully updated!!!')
    else:
        return render_template('success.html', title='invalid request!!!')
    

@app.route('/trinkets', methods=['POST','GET'])
def trinkets():
    """Renders the trinkets page."""
    if request.method == 'GET':
        return render_template(
        'adhoc.html',
        title='Trinket',
        year=datetime.now().year,
        message='code snippets:'
        )
    else:
        return render_template('success.html', title='invalid request!!!')
    


if __name__ == '__main__':
    app.run(debug=True)