from flask import Flask, request, jsonify
from flask_cors import CORS
import pdfkit

app = Flask(__name__)
CORS(app)

@app.route('/convert-to-pdf', methods=['POST'])
def convert_to_pdf():
    # Check if a file is part of the request
    if 'html_file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['html_file']

    try:
        # Read HTML content from the file and decode it
        html_content = file.read().decode('utf-8')

        # Convert HTML to PDF
        pdf_data = pdfkit.from_string(html_content, False)
        return pdf_data, 200, {'Content-Type': 'application/pdf'}
    except Exception as e:
        # Log the error
        app.logger.error(f'wkhtmltopdf error: {str(e)}')

        # Return an error message
        return jsonify({'error': 'Internal server error. Please check the logs for details.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
