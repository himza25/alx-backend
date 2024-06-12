import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';
import kue from 'kue';

// Initialize variables
const initialAvailableSeats = 50;
let reservationEnabled = true;

// Create Redis client and promisify methods
const client = createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Function to reserve seats
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Function to get the current available seats
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats, 10) : null;
}

// Initialize available seats in Redis
async function initializeSeats() {
  await reserveSeat(initialAvailableSeats);
}
initializeSeats();

// Create Kue queue
const queue = kue.createQueue();

// Create Express server
const app = express();
const port = 1245;

// Route to get available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

// Route to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat')
    .save((err) => {
      if (!err) {
        return res.json({ status: 'Reservation in process' });
      } else {
        return res.json({ status: 'Reservation failed' });
      }
    });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

// Route to process the queue
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats();
    if (currentAvailableSeats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }

    const newAvailableSeats = currentAvailableSeats - 1;
    await reserveSeat(newAvailableSeats);

    if (newAvailableSeats === 0) {
      reservationEnabled = false;
    }

    done();
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
