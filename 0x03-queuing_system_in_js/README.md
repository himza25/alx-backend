# Queuing System in JavaScript

This project implements a queuing system in JavaScript using Redis and Kue. The system includes various tasks to manage products, reservations, and notifications. Below are the details of each task.

## Table of Contents

1. [Installation](#installation)
2. [Tasks](#tasks)
   - [0. Install a Redis Instance](#0-install-a-redis-instance)
   - [1. Node Redis Client](#1-node-redis-client)
   - [2. Node Redis Client and Basic Operations](#2-node-redis-client-and-basic-operations)
   - [3. Node Redis Client and Async Operations](#3-node-redis-client-and-async-operations)
   - [4. Node Redis Client and Advanced Operations](#4-node-redis-client-and-advanced-operations)
   - [5. Node Redis Client Publisher and Subscriber](#5-node-redis-client-publisher-and-subscriber)
   - [6. Create the Job Creator](#6-create-the-job-creator)
   - [7. Create the Job Processor](#7-create-the-job-processor)
   - [8. Track Progress and Errors with Kue](#8-track-progress-and-errors-with-kue)
   - [9. Track Progress and Errors with Kue: Job Processor](#9-track-progress-and-errors-with-kue-job-processor)
   - [10. Writing the Job Creation Function](#10-writing-the-job-creation-function)
   - [11. Writing the Test for Job Creation](#11-writing-the-test-for-job-creation)
   - [12. In Stock?](#12-in-stock)
   - [13. Can I Have a Seat?](#13-can-i-have-a-seat)

## Installation

1. Clone the repository.
2. Install the necessary dependencies using `npm install`.
3. Ensure Redis is installed and running on your system.
