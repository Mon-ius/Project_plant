from app import create_app, cli
from ext import mongo as db,
import os


app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db}


if __name__ =='__main__':
    app.run(host=os.getenv('IP', 'localhost'),
        port=int(os.getenv('PORT', 4444)))
