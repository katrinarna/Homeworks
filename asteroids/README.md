# Asteroids CLI – Track Near-Earth Objects

Welcome to Asteroids CLI, a tool that fetches data about asteroids approaching Earth using NASA's public Near Earth Object API. Input a date, and find out which cosmics flew close to home.

## What It Does

Given a specific date, the app will return a list of asteroids that came near Earth within a 7-day window. For each asteroid, you'll get:

- Name (or ID)
- Estimated diameter (in meters)
- Distance from Earth (in kilometers)

## Example usage:

```bash
$ asteroids --date 2024-05-01

