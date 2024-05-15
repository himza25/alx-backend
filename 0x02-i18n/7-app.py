#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask import Flask, render_template, request, g, session
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Flask app config
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id):
    """
    Mock logging in
    """
    return users.get(int(id))


@app.before_request
def before_request():
    """
    Mock logging in
    """
    id = request.args.get('login_as', None)
    g.user = get_user(id)


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    languages = app.config['LANGUAGES']
    local = request.args.get("locale")
    if local in languages:
        return local

    if g.user:
        local = g.user.get('locale')
        if local in languages:
            return local

    preferred_local = request.headers.get('Accept-Language')
    if preferred_local:
        for entry in preferred_local.split(',')[1:]:
            lang = entry.split(';')[0]
            if lang in languages:
                return lang

    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """
    Infer appropriate time zone
    """
    tzp = request.args.get('timezone')
    if tzp:
        try:
            pytz.timezone(tzp)
            return tzp
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        tzp = g.user.get('timezone')
        if tzp:
            try:
                pytz.timezone(tzp)
                return tzp
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def main():
    """
    Outputs Welcome to Holberton
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
