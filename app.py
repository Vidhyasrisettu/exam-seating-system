from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_excel("students1.xlsx")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Clean register number column
df["reg no"] = df["reg no"].astype(str).str.strip()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        reg_no = request.form["reg_no"].strip()

        result = df[df["reg no"] == reg_no]

        if result.empty:
            result = None

    return render_template("index.html", data=result)

if __name__ == "__main__":
    app.run(debug=True)