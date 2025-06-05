# Gemeente Den Haag – Digital Parking System

This project simulates a digital parking management platform for The Hague municipality. It covers parking zone validation, license plate registration, and integration with DigiD authentication.

## Features
- REST API for parking zone validation
- Parking pass verification via DigiD (mock)
- License plate check-in/out
- Designed for citizen use via mobile or kiosk

## Tech Stack
- FastAPI (Python)
- Docker + Docker Compose
- Mock DigiD integration
- OpenAPI spec defined

## Structure
- `/api` – OpenAPI spec
- `/backend` – Main controller logic
- `/integration` – DigiD mock endpoint
- `/scripts` – Database init and setup

