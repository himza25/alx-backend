import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

/**
 * Send a notification
 * @param {string} phoneNumber - The phone number to send the notification to
 * @param {string} message - The message to send
 */
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs from the 'push_notification_code' queue
queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
