from flask import Flask


def create_app():
    app = Flask(__name__)

    from .controllers.index import bp_index
    app.register_blueprint(bp_index)

    from .controllers.phasediagram import bp_phasediagram
    app.register_blueprint(bp_phasediagram)

    from .controllers.phaseopen import bp_phaseopen
    app.register_blueprint(bp_phaseopen)

    from .controllers.plotphase import bp_plotphase
    app.register_blueprint(bp_plotphase)

    return app
