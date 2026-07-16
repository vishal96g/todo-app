from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/todo", methods=["GET"])
def todo_page():
    return '''
        <h2>To-Do Page</h2>
        <form action="/submittodoitem" method="POST">

            <label>Item ID:</label>
            <input type="text" name="itemId" />
            
            <label>Item UUID:</label>
            <input type="text" name="itemUuid" />

            <label>Item Hash:</label>
            <input type="text" name="itemHash" />

            <label>Item Name:</label><br>
            <input type="text" name="itemName"><br><br>
            
            <label>Item Description:</label><br>
            <textarea name="itemDescription"></textarea><br><br>
            
            <button type="submit">Submit</button>
        
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)

