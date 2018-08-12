from flask import Flask, jsonify


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)
    # Load config first
    app.config.from_object('config.settings')
    if settings_override:
        app.config.update(settings_override)
    register_routes(app)
    return app


def register_routes(app):
    @app.route('/directory/software-statement/<statement_id>/<key_type>/jwk_uri', methods=['GET'])
    def get_jwks(statement_id, key_type):
        try:
            conf = app.config['DIR_CONFIG']
            jwks = conf['config']['statements'][statement_id]['jwks'][key_type]['jwk']
            print(jwks)
        except Exception as ex:
            return jsonify(
                {
                    'code': 500,
                    'message': str(ex)
                }
            ), 500

        return jwks, 200
