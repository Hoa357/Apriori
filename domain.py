from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder="static")

@app.route("/")
def home():
    return render_template("indexTD.html")

# Route để phục vụ tất cả file trong thư mục "static"
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# Route riêng để lấy JSON ảnh nếu cần
@app.route("/product_images.json")
def get_product_images():
    return send_from_directory(os.path.join(app.root_path, "static"), "product_images.json")

if __name__ == "__main__":
    app.run(debug=True)
