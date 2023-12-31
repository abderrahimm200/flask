from flask import Flask, request, jsonify
from flask_cors import CORS
import pdfkit

app = Flask(__name__)
CORS(app)

@app.route('/convert-to-pdf', methods=['POST'])
def convert_to_pdf():
    html_content = request.form.get('html_content')

    try:
        options = {
            'encoding': "UTF-8",
            'custom-header' : [
                ('Accept-Encoding', 'gzip')
            ]
        }
        # Convert HTML to PDF
        pdf_data = pdfkit.from_string(html_content, False, options=options)
        return pdf_data, 200, {'Content-Type': 'application/pdf; charset=UTF-8'}
    except Exception as e:
        # Log the error
        app.logger.error(f'wkhtmltopdf error: {str(e)}')

        # Return an error message
        return jsonify({'error': 'Internal server error. Please check the logs for details.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
