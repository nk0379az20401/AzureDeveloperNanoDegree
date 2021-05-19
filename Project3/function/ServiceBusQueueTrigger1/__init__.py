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

    # TODO: Get connection to database
    dbConnection = psycopg2.connect(database="techconfdb", user='Karthikeya@nk1240pgsqlproject3', password='Ishaan@4949', host='nk1240pgsqlproject3.postgres.database.azure.com', port= '5432')

    try:
        cursor = dbConnection.cursor()
        
        # TODO: Get notification message and subject from database using the notification_id
        notification = cursor.execute("SELECT message, subject FROM notification WHERE id = {};".format(notification_id))

        # TODO: Get attendees email and name
        cursor.execute("SELECT first_name, email FROM attendee;")
        attendees = cursor.fetchall()

        # TODO: Loop through each attendee and send an email with a personalized subject
        for attendee in attendees:
            Mail('{}, {}, {}'.format({'info@techconf.com'}, {attendee[1]}, {notification}))

        # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified

        completed_date = datetime.utcnow()

        status = 'Notified {} attendees'.format(len(attendees))

        update_query = cursor.execute("UPDATE notification SET status = '{}', completed_date = '{}' WHERE id = {};".format(status, completed_date, notification_id))

        dbConnection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        logging.error(error)
        dbConnection.rollback()
    finally:
        # TODO: Close connection
        cursor.close()
        dbConnection.close()
