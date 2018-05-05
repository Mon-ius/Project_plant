import os

from app import cli, create_app
from ext import mongo


app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': mongo.db}


if __name__ =='__main__':
    app.run(host=os.getenv('IP', 'localhost'),
        port=int(os.getenv('PORT', 4444)))
