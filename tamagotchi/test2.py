from app import*
from flask import Flask

def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"


"""



# create and initialize a new Flask app
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()

 """


 """

 # configuration
 DATABASE = "tutorial.db"

 # create and initialize a new Flask app
 app = Flask(__name__)

 # load the config
 app.config.from_object(__name__)


 @app.route("/")
 def hello():
     return "Hello, World!"


 if __name__ == "__main__":
     app.run()
"""

"""



def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"


def test_database():
    assert Path("tutorial.db").is_file()
 """

 