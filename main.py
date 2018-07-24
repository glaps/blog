from app import apli, db
from app.models import User, Post

@apli.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


#if __name__=="__main__":
    #apli.run(debug=True)
