from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

instructions = [

    {
        "id": 1,
        "name": "Paint a wall",
        "description": "Instructions how to paint a wall",
        "steps": [" Clean the wall", "Tape the trim",
                  "Roll the primer onto the wall",
                  "Paint the trim", "Remove the painter's tape"],
        "tools": ["painter's tape", "primer", "paint", "paint roller",
                  "paint tray", " paintbrush"],
        "cost": 100,
        "duration": 8
    },
    {
        "id": 2,
        "name": "Write text on paper",
        "description": "Instructions how to write on paper",
        "steps": ["Get a new paper", "Pick up a pencil",
                  "Hold the pencil in your arm",
                  "Press the pencil on the paper", "Use a eraser"],
        "tools": ["Paper", "Pencil", "Eraser", "Hand"],
        "cost": 10,
        "duration": 2
    }
]


@app.route('/instructions', methods=['GET'])
def get_instructions():
    return jsonify({'data': instructions})


@app.route('/instructions/<int:instruction_id>', methods=['GET'])
def get_instruction(instruction_id):
    instruction = next((instruction for instruction in instructions if instruction['id'] == instruction_id), None)
    if instruction:
        return jsonify(instruction)

    return jsonify({'message': 'instruction not found'}), HTTPStatus.NOT_FOUND


@app.route('/instructions/', methods=['POST'])
def create_instruction():
    data = request.get_json()

    name = data.get('name')
    description = data.get('description')

    instruction = {

        'id': len(instructions) + 1,
        'name': name,
        'description': description

    }
    instructions.append(instruction)
    return jsonify(instruction), HTTPStatus.CREATED


@app.route('/instructions/<int:instruction_id>', methods=['DELETE'])
def delete_instruction(instruction_id):
    instruction = next((instruction for instruction in instructions if instruction['id'] == instruction_id), None)

    if not instruction:
        return jsonify({'message': 'instruction not found'}), HTTPStatus.NOT_FOUND

    instructions.remove(instruction)

    return '', HTTPStatus.NO_CONTENT


if __name__ == '__main__':
    app.run()
