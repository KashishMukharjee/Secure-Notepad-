from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from .models import Note, User
from . import db
from datetime import datetime
from functools import wraps

notes = Blueprint('notes', __name__)


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated


@notes.route('/dashboard')
@login_required
def dashboard():
    user = User.query.get(session['user_id'])
    user_notes = Note.query.filter_by(user_id=user.id).order_by(Note.updated_at.desc()).all()
    return render_template('dashboard.html', user=user, notes=user_notes)


@notes.route('/notes/new', methods=['GET', 'POST'])
@login_required
def new_note():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()

        if not title or not content:
            flash('Title and content are required.', 'danger')
            return render_template('note_form.html', action='New', note=None)

        note = Note(title=title, content=content, user_id=session['user_id'])
        db.session.add(note)
        db.session.commit()
        flash('Note created successfully!', 'success')
        return redirect(url_for('notes.dashboard'))

    return render_template('note_form.html', action='New', note=None)


@notes.route('/notes/<int:note_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = Note.query.filter_by(id=note_id, user_id=session['user_id']).first_or_404()

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()

        if not title or not content:
            flash('Title and content are required.', 'danger')
            return render_template('note_form.html', action='Edit', note=note)

        note.title = title
        note.content = content
        note.updated_at = datetime.utcnow()
        db.session.commit()
        flash('Note updated successfully!', 'success')
        return redirect(url_for('notes.dashboard'))

    return render_template('note_form.html', action='Edit', note=note)


@notes.route('/notes/<int:note_id>/delete', methods=['POST'])
@login_required
def delete_note(note_id):
    note = Note.query.filter_by(id=note_id, user_id=session['user_id']).first_or_404()
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted.', 'info')
    return redirect(url_for('notes.dashboard'))


@notes.route('/notes/<int:note_id>/view')
@login_required
def view_note(note_id):
    note = Note.query.filter_by(id=note_id, user_id=session['user_id']).first_or_404()
    return render_template('view_note.html', note=note)
