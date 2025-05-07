from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def card_form():
    if request.method == "POST":
        card_number = request.form.get("cardNumber")
        card_holder = request.form.get("cardHolder")
        expiry = request.form.get("expiry")
        cvv = request.form.get("cvv")

        # In ra console (terminal)
        print("=== Thông tin thẻ nhận được ===")
        print("Số thẻ:", card_number)
        print("Chủ thẻ:", card_holder)
        print("Hết hạn:", expiry)
        print("CVV:", cvv)
        print("==============================")

        # Trả lại thông báo cho người dùng
        return f"<h2>Đã nhận thông tin thẻ của {card_holder}</h2>"

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)



