import { createClient, print } from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection errors
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Promisify the get function
const getAsync = promisify(client.get).bind(client);

/**
 * Set a new school in Redis
 * @param {string} schoolName - The key to set in Redis
 * @param {string} value - The value to set for the key
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

/**
 * Display the value of a school from Redis
 * @param {string} schoolName - The key to retrieve from Redis
 */
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err.message}`);
  }
}

// Call the functions with the specified arguments
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
