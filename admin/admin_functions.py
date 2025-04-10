from flask import Blueprint, render_template
import firebase_admin
from firebase_admin import firestore

admin_bp = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates/admin')  # Define the Blueprint

db = firestore.client()  # Assuming you've initialized Firebase elsewhere

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