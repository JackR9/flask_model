from flask import Flask, jsonify, request, render_template
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String
# import os
# from flask_marshmallow import Marshmallow
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open('code/model.pickle', 'rb'))

# base_dir = os.path.abspath(os.path.dirname(__file__))
# db_path = os.path.join(base_dir, 'fifa.db')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
# db = SQLAlchemy(app)
# ma = Marshmallow(app)


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/get_player')
# def get_player():
#    position = request.args.get('position', 'unknown')
#    age = request.args.get('age', 0)
#
#    if position == 'unknown':
#        player_details = Player.query.filter_by(Age=age).all()
#        result = player_schemas.dump(player_details)
#    else:
#        player_details = Player.query.filter_by(Position=position).all()
#        result = player_schema.dump(player_details)

#    return player_details


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    result = int(model.predict(final_features))
    return render_template('index.html', prediction_text=f'The players potential overall rating is {result}')


# class Player(db.Model):
#    __tablename__ = 'fifa_players'
#    field1 = Column(Integer, primary_key=True)
#    ID = Column(Integer)
#    Name = Column(String)
#    Age = Column(String)
#    Photo = Column(String)
#    Nationality = Column(String)
#    Position = Column(String)

# class PlayerSchema(ma.Schema):
#    class Meta:
#        fields = ('field1','ID', 'Name', 'Age', 'Photo', 'Nationality','Position')


# player_schema = PlayerSchema()
# player_schemas = PlayerSchema(many=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)