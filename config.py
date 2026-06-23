"""
Centralised error handling.

Registers friendly HTML error pages for common HTTP error codes so the
user never sees a raw Flask traceback or a bare "Not Found" text page.
"""

from flask import render_template


def register_error_handlers(app):
    """Attach 404 and 500 error handlers to the given Flask app."""

    @app.errorhandler(404)
    def handle_not_found(error):
        return render_template("error.html", code=404, message="Page not found."), 404

    @app.errorhandler(500)
    def handle_server_error(error):
        return render_template(
            "error.html", code=500, message="Something went wrong on our end."
        ), 500
