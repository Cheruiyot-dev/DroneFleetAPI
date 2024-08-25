# DroneFleetAPI

A RESTful web service built with Django REST Framework for managing drone categories, drones, and pilots. This API provides endpoints for creating, retrieving, updating, and deleting drone-related data, enabling seamless integration and management of drone fleets.

## Table of Contents

- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
  - [Drone Categories](#drone-categories)
  - [Drones](#drones)
  - [Pilots](#pilots)
  - [Competitions](#competitions)
- [Filters and Search](#filters-and-search)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Project Description

The **DroneFleetAPI** is designed to facilitate the management and tracking of drone operations, including drone categories, individual drones, pilots, and competitions. The API is structured to allow full CRUD (Create, Read, Update, Delete) operations on all models, with robust filtering, searching, and ordering capabilities.

## Tech Stack

- **Backend Framework:** Django
- **API Framework:** Django REST Framework (DRF)
- **Database:** PostgreSQL 
- **Filtering:** Django Filters
- **Environment Management:** Python `venv`
- **Testing:** Django Test Framework

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/DroneFleetAPI.git
   cd DroneFleetAPI
2. **Create and Activate a Virtual Environment:**
   python -m venv env
  source env/bin/activate  # On Windows, use `env\Scripts\activate`
3. **Install Dependencies:**
   pip install -r requirements.txt
4. **Configure the Database:**
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dronefleet_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
5. **Make and Apply Migrations:**
   python manage.py makemigrations
   python manage.py migrate

6. **Create a Superuser:**
   python manage.py createsuperuser
 
7. **Run the Development Server:**
   python manage.py runserver


## API Endpoints

| **Model**          | **Action**                      | **HTTP Method** | **Endpoint**                           |
|--------------------|---------------------------------|-----------------|----------------------------------------|
| **Drone Categories** | List All Drone Categories      | GET             | `/drone-categories/`                   |
|                    | Create a New Drone Category     | POST            | `/drone-categories/`                   |
|                    | Retrieve a Specific Drone Category | GET         | `/drone-categories/{id}/`              |
|                    | Delete a Specific Drone Category   | DELETE      | `/drone-categories/{id}/`              |
| **Drones**         | List All Drones                 | GET             | `/drones/`                             |
|                    | Create a New Drone              | POST            | `/drones/`                             |
|                    | Retrieve a Specific Drone       | GET             | `/drones/{id}/`                        |
|                    | Update a Specific Drone         | PUT / PATCH     | `/drones/{id}/`                        |
|                    | Delete a Specific Drone         | DELETE          | `/drones/{id}/`                        |
| **Pilots**         | List All Pilots                 | GET             | `/pilots/`                             |
|                    | Create a New Pilot              | POST            | `/pilots/`                             |
|                    | Retrieve a Specific Pilot       | GET             | `/pilots/{id}/`                        |
|                    | Update a Specific Pilot         | PUT / PATCH     | `/pilots/{id}/`                        |
|                    | Delete a Specific Pilot         | DELETE          | `/pilots/{id}/`                        |
| **Competitions**   | List All Competitions           | GET             | `/competitions/`                       |
|                    | Create a New Competition        | POST            | `/competitions/`                       |
|                    | Retrieve a Specific Competition | GET             | `/competitions/{id}/`                  |
|                    | Update a Specific Competition   | PUT / PATCH     | `/competitions/{id}/`                  |
|                    | Delete a Specific Competition   | DELETE          | `/competitions/{id}/`                  |


## Filters and Search

The API supports filtering, searching, and ordering on various fields across different models:

### Drones
- **Filterable Fields**: `name`, `drone_category`, `manufacturing_date`, `has_it_competed`
- **Searchable Fields**: `name`
- **Orderable Fields**: `name`, `manufacturing_date`

### Pilots
- **Filterable Fields**: `name`, `gender`, `races_count`
- **Searchable Fields**: `name`
- **Orderable Fields**: `name`, `races_count`

### Competitions
- **Filterable Fields**: `distance_in_feet`, `from_achievement_date`, `to_achievement_date`, `min_distance_in_feet`, `max_distance_in_feet`, `drone_name`, `pilot_name`
- **Orderable Fields**: `distance_in_feet`, `distance_achievement_date`
## Project Structure

- **dronefleet/**: Contains the Django app with models, views, and serializers.
- **dronefleet/urls.py**: Defines all the URL routes for the API.
- **dronefleet/models.py**: Defines the data models (`DroneCategory`, `Drone`, `Pilot`, `Competition`).
- **dronefleet/serializers.py**: Defines the serializers for the models.
- **dronefleet/views.py**: Contains the API views that handle the requests and responses.

## Models

- **DroneCategory**: Stores the categories to which drones can belong.
- **Drone**: Represents individual drones and their attributes.
- **Pilot**: Stores information about pilots who operate the drones.
- **Competition**: Records competitions in which drones participate.


