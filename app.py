from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.document import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_document = request.form['id_docuemnt']
    title_docuement = request.form['title_docuement']
    number_page = request.form['number_page']
    category = request.form['category']
    Autor = request.form['Autor']

    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    p = Person(id_person=id_person, name=first_name, last_name=last_name)

    b = Document(id_document=id_document, title_docuement=title_docuement, number_page=number_page,
                 category=category, Autor=Autor[p])

    model.append(b)
    return render_template('person_detail.html', value=b)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)


if __name__ == '__main__':
    app.run()
