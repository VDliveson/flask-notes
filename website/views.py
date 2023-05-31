from cmath import log
import json
from . import db
from flask import Blueprint, flash, jsonify, render_template,request
from flask_login import login_user, login_required, logout_user, current_user
from .models import Note


views= Blueprint('views', __name__)\
    
@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method=='GET':
        return  render_template('home.html',user=current_user)
    
    if request.method=='POST':
        note=request.form.get('note')
        if(len(note)<1):
            flash('Note too short',category='error')
        else:
            new_note=Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added',category='success')
        return render_template("home.html", user=current_user)
        
@views.route('/delete-note',methods=['POST'])
def delete_note():
    note=json.loads(request.data)
    noteId=note['noteId']
    note=Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note deleted',category='success')
            return jsonify({})

    