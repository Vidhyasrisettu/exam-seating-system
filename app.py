from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Load student data from Excel (support both filename variants)
_excel_file = 'students.xlsx' if os.path.exists('students.xlsx') else 'students1.xlsx'
df = pd.read_excel(_excel_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        reg_no = request.form.get('reg_no', '').strip()
        match = df[df['Register Number'].astype(str).str.strip() == reg_no]
        if not match.empty:
            result = match.iloc[0].to_dict()
        else:
            error = f"No record found for Register Number: {reg_no}"
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
