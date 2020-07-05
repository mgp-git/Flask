from flask import render_template, url_for, redirect, Blueprint, flash, request
from flask_login import login_required, current_user
from flask_table import Table, Col
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime
from app import db, login_manager
from ..models.models import Match
from ..forms.match_form import MatchForm


class UsersSubTable(Table):
    pass
    #user_id = Col()

class MatchesTable(Table):
    #id = Col('id', show=False)     --> not to show column
    id = Col('Match ID')
    date = Col('Date')
    team_a = Col('Home team')
    team_b = Col('Visiting team')
    venue = Col('Venue')
    #result = Col('result')
    #for_team_a = Col('for_team_a')
    #for_team_b = Col('for_team_b')

matches = Blueprint('matches', __name__)

@matches.route('/past')
def past_matches():
    page = request.args.get('page', 1, type=int)
    matches = Match.query.filter(Match.date<datetime.now().date()).paginate(page=page, per_page=5, error_out=True)
    #table = MatchesTable(matches, border=True)
    return render_template('past_matches.html', matches=matches)

@matches.route('/current')
def current_matches():
    results = Match.query.filter(Match.date==datetime.now().date()).all()
    #print(results)
    table = MatchesTable(results, border=True)
    return render_template('matches.html', table=table)

@matches.route('/upcoming')
def upcoming_matches():
    matches = Match.query.filter(Match.date>datetime.now().date()).all()
    user_id = current_user.get_id()
    results = []    

    #page = request.args.get(get_page_parameter(), type=int, default=1)
    #pagination = Pagination(page=page, total=len(matches), search=False, record_name='matches')
    return render_template('matches.html', matches=matches)

@matches.route('/add', methods=['GET', 'POST'])
def add_matches():
    form = MatchForm()
    if form.validate_on_submit():
        match = Match(date=form.date.data, venue=form.venue.data, team_a=form.team_a.data, team_b=form.team_b.data)
        db.session.add(match)
        db.session.commit()
        #flash("Added the match to DB")
        return redirect(url_for('matches.add_matches'))
    #for fieldName, errorMessages in form.errors.items():
    #    flash(errorMessages, "danger")
    return render_template('add_match.html', form=form)




