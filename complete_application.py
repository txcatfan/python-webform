from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import dotenv
import os 
from admin.admin_functions import admin_bp  # Import the Blueprint
import firebase_admin
from firebase_admin import credentials, firestore


cred_path = "./creds/mab-comercio-de-acciones-aeae38e733ed.json" #store the path
cred = credentials.Certificate(cred_path)
# Check if Firebase Admin is already initialized
if not firebase_admin._apps:
  firebase_admin.initialize_app(cred)

db = firestore.client(database_id="ctdr-adoption-applications")

print(db)
db.collection('Applications').list_documents()

app = Flask(__name__)
app.register_blueprint(admin_bp)  # Register the Blueprint

app.secret_key = os.environ.get("FLASK_SECRET_KEY")
if not app.secret_key:
    raise ValueError("No secret key set in environment variables.")

@app.route('/')  # Root route (the main page)
def index():
    session['firestore_document_id'] = None 
    return render_template('index.html')  # Render the HTML template

@app.route('/clear_answers', methods=['GET', 'POST'])
def clear_answers():
    # Clear the session data
    session.clear()
    session['firestore_document_id'] = None  # Reset the Firestore document ID
    # Redirect back to page1.html
    return redirect("/form/page1")

@app.route('/form/page1', methods=['GET', 'POST'])
def page1():
    if request.method == 'POST':
        session['page1_data'] = request.form
        print(session['page1_data'])

        if not session['firestore_document_id']:
            # Create a new document with a single field named 'page1_data'
            doc_ref = db.collection('Applications').document()  #Get a DocumentReference
            doc_ref.set({
                'page1_data': session['page1_data']
            })

            # Save the document ID to the session
            session['firestore_document_id'] = doc_ref.id
        else:
            # Update the existing document with the new data
            doc_ref = db.collection('Applications').document(session['firestore_document_id'])
            doc_ref.update({
                'page1_data': session['page1_data']
            })
        print(session)
        return redirect("/form/page2")
    page1_data = session.get('page1_data', {})
    print(session)

    return render_template('form/page1.html', page1_data=page1_data)

@app.route('/form/page2', methods=['GET', 'POST'])
def page2():
    if request.method == 'POST':
        session['page2_data'] = request.form
        print(session['page2_data'])

        if not session['firestore_document_id']:
            # Create a new document with a single field named 'page1_data'
            doc_ref = db.collection('Applications').document()  #Get a DocumentReference
            doc_ref.set({
                'page2_data': session['page2_data']
            })

            # Save the document ID to the session
            session['firestore_document_id'] = doc_ref.id
        else:
            # Update the existing document with the new data
            doc_ref = db.collection('Applications').document(session['firestore_document_id'])
            doc_ref.update({
                'page2_data': session['page2_data']
            })
        print(session)
        return redirect("/form/page3")  
    page2_data = session.get('page2_data', {})
    return render_template('form/page2.html', page2_data=page2_data)

@app.route('/form/page3', methods=['GET', 'POST'])
def page3():
    if request.method == 'POST':
        session['page3_data'] = request.form
        print(session['page3_data'])

        if not session['firestore_document_id']:
            # Create a new document with a single field named 'page1_data'
            doc_ref = db.collection('Applications').document()  #Get a DocumentReference
            doc_ref.set({
                'page3_data': session['page3_data']
            })

            # Save the document ID to the session
            session['firestore_document_id'] = doc_ref.id
        else:
            # Update the existing document with the new data
            doc_ref = db.collection('Applications').document(session['firestore_document_id'])
            doc_ref.update({
                'page3_data': session['page3_data']
            })
        print(session)
        return redirect("/form/page4") 
    page3_data = session.get('page3_data', {})
    return render_template('form/page3.html', page3_data=page3_data)

@app.route('/form/page4', methods=['GET', 'POST'])
def page4():
    if request.method == 'POST':
        session['page4_data'] = request.form
        print(session['page4_data'])

        if not session['firestore_document_id']:
            # Create a new document with a single field named 'page1_data'
            doc_ref = db.collection('Applications').document()  #Get a DocumentReference
            doc_ref.set({
                'page4_data': session['page4_data']
            })

            # Save the document ID to the session
            session['firestore_document_id'] = doc_ref.id
        else:
            # Update the existing document with the new data
            doc_ref = db.collection('Applications').document(session['firestore_document_id'])
            doc_ref.update({
                'page4_data': session['page4_data']
            })
        print(session)
        return redirect("/form/page5")
    page4_data = session.get('page4_data', {})
    return render_template('form/page4.html', page4_data=page4_data)

@app.route('/form/page5', methods=['GET', 'POST'])
def page5():
    if request.method == 'POST':
        session['page5_data'] = request.form
        print(session['page5_data'])

        if not session['firestore_document_id']:
            # Create a new document with a single field named 'page1_data'
            doc_ref = db.collection('Applications').document()  #Get a DocumentReference
            doc_ref.set({
                'page5_data': session['page5_data']
            })

            # Save the document ID to the session
            session['firestore_document_id'] = doc_ref.id
        else:
            # Update the existing document with the new data
            doc_ref = db.collection('Applications').document(session['firestore_document_id'])
            doc_ref.update({
                'page5_data': session['page5_data']
            })
        print(session)
        return redirect("/form/review")
    page5_data = session.get('page5_data', {})  
    return render_template('form/page5.html', page5_data=page5_data)

@app.route('/form/review', methods=['GET', 'POST'])
def review():
    print(session)
    return render_template('form/review.html', review_data=session)


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
