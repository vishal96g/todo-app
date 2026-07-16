from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/todo", methods=["GET"])
def todo_page():
    return '''
        <h2>To-Do Page</h2>
        <form action="/submittodoitem" method="POST">
            <label>Item Name:</label><br>
            <input type="text" name="itemName"><br><br>
            <label>Item Description:</label><br>
            <textarea name="itemDescription"></textarea><br><br>
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

