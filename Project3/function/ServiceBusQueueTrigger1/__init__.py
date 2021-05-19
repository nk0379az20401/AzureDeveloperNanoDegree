import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)

    dbConnection = psycopg2.connect(database="techconfdb", user='Karthikeya@nk1240pgsqlproject3', password='Ishaan@4949', host='nk1240pgsqlproject3.postgres.database.azure.com', port= '5432')

    try:
        cursor = dbConnection.cursor()
        
        notification = cursor.execute("SELECT message, subject FROM notification WHERE id = {};".format(notification_id))

        cursor.execute("SELECT first_name, email FROM attendee;")
        attendees = cursor.fetchall()

        for attendee in attendees:
            Mail('{}, {}, {}'.format({'info@techconf.com'}, {attendee[1]}, {notification}))

        completed_date = datetime.utcnow()

        status = 'Notified {} attendees'.format(len(attendees))

        update_query = cursor.execute("UPDATE notification SET status = '{}', completed_date = '{}' WHERE id = {};".format(status, completed_date, notification_id))

        dbConnection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        dbConnection.rollback()
    finally:
        cursor.close()
        dbConnection.close()
