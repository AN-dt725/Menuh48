
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_excel("data.xlsx")  # đọc file excel

@app.route("/", methods=["GET", "POST"])
def index():
    ket_qua = None  # mặc định là không có kết quả
    keyword = ""    # mặc định từ khóa trống

    if request.method == "POST":
        keyword = request.form["keyword"].strip().lower()
        if keyword:
            # Lọc dữ liệu theo từ khóa
            ket_qua = df[df["Tên mặt hàng"].str.lower().str.contains(keyword)]

    return render_template("index.html", ket_qua=ket_qua, keyword=keyword)

if __name__ == "__main__":
    app.run()


