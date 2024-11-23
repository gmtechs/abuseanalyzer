from flask import Flask, request, jsonify
from gradio_client import Client

app = Flask(__name__)

# Initialize the Gradio client
client = Client("art-manuh/Maliza_Uhalifu_Mtandaoni")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract the comment from the request JSON
        data = request.json
        comment = data.get("comment")
        if not comment:
            return jsonify({"error": "Missing 'comment' in request"}), 400

        # Use the Gradio client to send the comment to the API
        result = client.predict(
            comment=comment,
            api_name="/predict"
        )

        # Return the response
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
