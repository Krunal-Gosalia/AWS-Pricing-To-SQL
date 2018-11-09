import sqlalchemy
import pymssql
import dbconfig
import awsToSQL as awsToSQL
from crontab import CronTab
from flask import Flask



conn_string = dbconfig.getConn()
engine = sqlalchemy.create_engine(conn_string)

# awsToSQL.s3ToSQL(engine)
# awsToSQL.ec2ToSQL(engine)

# app = Flask(__name__)

# @app.route('/')
def bathProcess():
    print("DB Bulk Insertion Process Begins:")
    try:
        flag_1 = awsToSQL.ec2ToSQL(engine)
        flag_2 = awsToSQL.s3ToSQL(engine)
        if(flag_1 and flag_2):
            # awsToSQL.AWSVendorUpdate(engine)
            print("DB Bulk Insertion Process Completed")
        else:
            print("Error in flags")
    except:
        print("Failed")
# if __name__ == "__main__":
#     app.run(port=8000)

bathProcess()
