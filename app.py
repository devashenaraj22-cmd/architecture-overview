from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

# Initialize the Gemini client with your copied API key
client = genai.Client(api_key="AQ.Ab8RN6JVP9xEkc7OIh8ztOOXMEZpFamfcvWDCRyo48VAiLBc_g")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"answer": "Please enter a question."})

    try:
        # Call the Gemini model
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=question
        )
        answer = response.text
    except Exception as e:
        answer = f"Error: {str(e)}"

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)