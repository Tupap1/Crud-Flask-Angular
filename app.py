from flask import Flask, session, request,jsonify
from sqlalchemy import Column, Integer, ForeignKey,Date, Float,String, create_engine, Date, Time
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/crud'
app.config['MYSQL_SSL_DISABLED'] = True
engine = create_engine('mysql://root:@localhost/crud')
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'connect_args': {
        'ssl': {'ssl_disabled': True}
    }
}
bcrypt = Bcrypt(app)
db = SQLAlchemy(app) 


class usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column (db.String(1000))
    email = db.Column (db.String(1000))

with app.app_context():
    db.create_all()
    print("Tablas creadas")

@app.route("/signup", methods=["POST"])
def signup():
    try:    
        email = request.json["email"]
        nombres = request.json ["nombres"]

    except KeyError as e:
            print(jsonify({"error": f"Missing key: {e.args[0]}"}), 400) 
    
    user_exists = usuario.query.filter_by(email=email).first() is not None
    
    
    if user_exists:
        return jsonify({"error": "Ya existe un usuario con este email"}), 409


    nuevousuario = usuario(email = email,  nombre = nombres)
    db.session.add(nuevousuario)
    db.session.commit()


 
    return jsonify({
        "iduser": nuevousuario.id,
        "nombres": nuevousuario.nombre,
        "email": nuevousuario.email
    })


@app.route('/editarusuario/<int:id>', methods =["PUT"])
def editarusuario(id):
    data = request.get_json()
    user = usuario.query.get(id)
    if user:
        user.email = data['email']
        user.nombre = data['nombres']
        db.session.commit()
        return jsonify({'message': 'datos actualizados correctamente'}), 200
    else:
        return jsonify({'error': 'datos no encontrados'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')