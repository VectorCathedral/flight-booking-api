from flask import Flask,request,jsonify
import json
from json import dumps
from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

password=os.getenv('password')

con_string = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=MOTHEOSHP\\SQLEXPRESS;"
    "Database=AREYENG_FLIGHTS;"
    "uid=Admin;"
    f"pwd={password};"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)




con =pyodbc.connect(con_string)
cursor=con.cursor()



app=Flask(__name__)
app.config["DEBUG"]=True

@app.route("/add_customer",methods=["POST"])

def post():
    _json=request.json
    idNum=_json['idNum']
    email=_json['email']
    phone=_json['phone']
    fName=_json['fName']
    lName=_json['lName']
    postalAddress=_json['postalAddress']
    status='Registered'
    age=_json['age']

    data={
        "idNum":idNum,
        "email":email,
        "phone":phone,
        "fName":fName,
        "lName":lName,
        "postalAddress":postalAddress,
        "status":status,
        "age":age
        }


    json_data=json.dumps([data])

    insert_querry ="INSERT INTO Customers SELECT idNum,email,phone," \
    "fName,lName,postalAddress,status,age " \
    "FROM OPENJSON (@JSONString) " \
    "WITH (idNum VARCHAR(13),email NVARCHAR(50),phone VARCHAR(15), " \
    "fName VARCHAR(50),lName VARCHAR(50)," \
    "postalAddress VARCHAR(50), status VARCHAR(15),age INT)"
    querry=f"DECLARE @JSONString NVARCHAR(MAX)='{json_data}' {insert_querry}"


    if idNum and email and phone and fName and lName and postalAddress and status and age and request.method == "POST":

    
        cursor.execute(querry)
        cursor.commit()

        message={
            "message":"user added successfully",
            "status":200
        }

        resp=jsonify(message)
        resp.status_code=200

        return resp
    else:
        return not_found()
    
@app.route('/reservations/<int:resID>/<custID>',methods=['GET'])

def get(resID,custID):
    querry=f"SELECT * FROM Reservations WHERE resID = ?  AND custID =?"
    cursor.execute(querry,(resID,custID))  
    row =cursor.fetchone()

    if row :
            
        columns=[col[0]for col in cursor.description]
        result=dict(zip(columns,row))
        return jsonify(result)


           
    else:
        return not_found()
        


@app.route('/delete_reservation/<int:resID>/<custID>',methods=['DELETE'])
def delete(custID,resID):
    querry=f"DELETE  FROM Reservations WHERE resID = ? AND custID =?"
    cursor.execute(querry,(resID,custID))  
    cursor.commit()
    message={
            "message":"user deleted successfully",
            "status":200
        }

    resp=jsonify(message)
    resp.status_code=200

    return resp




@app.errorhandler(404)
def not_found(error=None):
    message={
        "status":404,
        "message":f'error {error}'
    }

    resp=jsonify(message)

    resp.status_code=404

    return resp
    
    
    
      

 
   
if __name__ == "__main__":
    app.run(debug=True)

 
