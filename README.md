# Smart Searcher 🔎

👧🏻 SHEHACK-2019 Hackathon Project 🛠️

Frontend : https://github.com/Nancy-Chauhan/smart-searcher-frontend 

## Pre-requisites

1. Python 3.7 🐍
2. Pipenv

## Getting Started

1. 🖥️ Launch `pipenv shell` to start-up a virtual environment
2. ⚡ Run `pipenv install` to install required dependencies

## Data

1. All data is stored inside `data` sub-directory.
2. `data/images` should contain images with files `1000.jpg`, `2000.jpg` etc.
3. `data/images.csv` is supposed to be a listing of all images

### Generating embeddings for image similarity

1. Run `python -m smartsearcher.generate_embeddings data/images`

### Preparing the DB

1. Run `./sanitize.sh data/images.csv`
1. Run `python -m smartsearcher.generate_embeddings data/images.csv` to load seed data into the app DB.

## Starting the server

1. ⚡ Run `./server.sh dev` to start a development server
