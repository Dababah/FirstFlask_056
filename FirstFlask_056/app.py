from flask import Flask, request, render_template_string

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1E1E2F; /* Warna background gelap */
            color: #EAEAEA; /* Warna teks terang */
            margin: 20px;
        }

        h1 {
            color: #FFD700; /* Warna emas untuk heading */
            text-align: center; /* Pusatkan heading */
            font-size: 2.5em;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.7); /* Efek bayangan */
        }

        form {
            margin-top: 20px;
            padding: 20px;
            background-color: #29293D; /* Background form lebih gelap */
            border-radius: 8px; /* Sudut membulat */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.6); /* Efek bayangan */
            max-width: 400px;
            margin-left: auto;
            margin-right: auto;
        }

        label {
            margin-right: 10px;
            font-weight: bold;
            color: #C0C0C0; /* Warna label lebih terang */
        }

        input {
            padding: 10px;
            margin-right: 10px;
            border: 1px solid #444; /* Border input */
            border-radius: 4px; /* Sudut input membulat */
            background-color: #222; /* Warna input */
            color: #EAEAEA; /* Warna teks input */
        }

        button {
            padding: 10px 20px;
            background-color: #4CAF50; /* Warna hijau cerah */
            color: #FFF; /* Warna teks putih */
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease; /* Animasi saat hover */
        }

        button:hover {
            background-color: #45A049; /* Warna hijau lebih gelap saat hover */
        }

        p {
            margin-top: 20px;
            font-size: 1.2em;
            text-align: center;
            color: #FFF; /* Warna teks putih */
        }

        input:focus {
            outline: none; /* Hilangkan outline bawaan */
            border-color: #FFD700; /* Border warna emas saat fokus */
            box-shadow: 0 0 5px #FFD700; /* Efek cahaya */
        }
    </style>
</head>
<body>
    <h1>Flask Parameter Form</h1>
    <form method="POST" action="/submit">
        <label for="user_input">Input:</label>
        <input type="text" id="user_input" name="user_input" required>
        <button type="submit">Submit</button>
    </form>
    {% if result %}
        <p>{{ result }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_code)

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    result = f"You entered: {user_input}"
    return render_template_string(html_code, result=result)

if __name__ == '__main__':
    app.run(debug=True)
