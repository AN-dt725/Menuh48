
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Đọc file Excel
df = pd.read_excel("data.xlsx")

@app.route("/", methods=["GET", "POST"])
def index():
    ket_qua = None
    keyword = ""
    if request.method == "POST":
        keyword = request.form["keyword"].strip().lower()
        if keyword:
            # Tìm trong cả "Tên mặt hàng" và "Loại hàng"
            ket_qua = df[
                df["Tên mặt hàng"].str.lower().str.contains(keyword) |
                df["Loại hàng"].str.lower().str.contains(keyword)
            ]
    return render_template("index.html", ket_qua=ket_qua, keyword=keyword)

if __name__ == "__main__":
    app.run()
