from app import app, db
from app.models import Voter, Answer

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Voter': Voter,
        'Answer': Answer,
    }