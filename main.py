import pdfkit
from flask import Flask, render_template, make_response, jsonify


app = Flask(__name__)



person = {
            'first_name':'John', 
            'last_name': 'Doe',
            'currency': 'Ksh',
            'amount_paid': 100.00,
            'amount_due': 900.00 
        }

title='Invoice 001'
@app.route('/')
def index():
    template = render_template('index.html', person=person, title=title)
    return template

@app.route('/pdf')
def view_pdf():
    template = render_template('pdf_template.html', person=person, title=title)
    pdf = pdfkit.from_string(template, False)

    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename='+title+'.pdf'
    return response


if __name__ == '__main__':
    app.run(debug=True)