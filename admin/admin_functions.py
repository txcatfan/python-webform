from flask import Blueprint, render_template
import firebase_admin
from firebase_admin import credentials, firestore

admin_bp = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates/admin')  # Define the Blueprint

cred_path = "./creds/mab-comercio-de-acciones-aeae38e733ed.json" #store the path
cred = credentials.Certificate(cred_path)
# Check if Firebase Admin is already initialized
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client(database_id="Applications")

@admin_bp.route('/active_applications')
def active_applications():
    active_applications = []
    applications_ref = db.collection('applications')
    query = applications_ref.where('status', '==', 'active')
    docs = query.get()
    for doc in docs:
        active_applications.append(doc.to_dict())
    return render_template('active_applications.html', applications=active_applications)

# Add other admin routes here (e.g., /users, /edit_application)