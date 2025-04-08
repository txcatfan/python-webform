from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import dotenv
import os 

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY")
if not app.secret_key:
    raise ValueError("No secret key set in environment variables.")

@app.route('/')  # Root route (the main page)
def index():
    return render_template('index.html')  # Render the HTML template

@app.route('/clear_answers', methods=['GET', 'POST'])
def clear_answers():
    # Clear the session data
    session.clear()
    # Redirect back to page1.html
    return redirect("/form/page1")

@app.route('/form/page1', methods=['GET', 'POST'])
def page1():
    if request.method == 'POST':
        # Process data from page 1
        # For example:
        #session['page1_data'] = request.get_json()
        #print (session['page1_data'])
        session['page1_data'] = request.form
        print(session['page1_data'])
        return redirect("/form/page2")  # Redirect to the route for page 2
    page1_data = session.get('page1_data', {})
    return render_template('form/page1.html', page1_data=page1_data)

@app.route('/form/page2', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        # Process data from page 2
        # For example:
        session['page2_data'] = request.form
        print(session['page2_data'])
        print(session)
        return redirect("/form/page3")  # Redirect to the route for page 3
    page2_data = session.get('page2_data', {})
    return render_template('form/page2.html', page2_data=page2_data)

@app.route('/form/page3', methods=['GET', 'POST'])
def page3():
    if request.method == 'POST':
        # Process data from page 2
        # For example:
        session['page3_data'] = request.form
        print(session['page3_data'])
        print(session)
        return redirect("/form/page1")  # Redirect to the route for page 3
    page3_data = session.get('page3_data', {})
    return render_template('form/page3.html', page3_data=page3_data)

# @app.route('/submit-application', methods=['POST'])
# def submit_application():
#   try:
#     data = request.get_json()  # Parse JSON from request body
#     # Now 'data' is a Python dictionary containing your form data
#     print(data)

#     # Example: Accessing values
#     name = data.get('name')
#     email = data.get('email')
#     print(name, email)

#     # Your further processing here (e.g., save to database, send emails)
#     # Process values and send them along to other processes

#     return jsonify({'message': 'Application received successfully!'}), 200  # Respond with success message

#   except Exception as e:
#     print(f"Error processing application: {e}")
#     return jsonify({'error': 'Failed to process application'}), 500  # Respond with error message

if __name__ == '__main__':
  app.run(debug=True)
