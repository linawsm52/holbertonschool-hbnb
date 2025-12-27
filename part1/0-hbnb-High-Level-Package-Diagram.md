# 0. High-Level Package Diagram

## Objective
This document describes the high-level package architecture of the HBnB application.
It illustrates the three-layer architecture and the use of the Facade pattern to manage communication between layers.

---

## Architecture Overview

The application is structured into three main layers:

- Presentation Layer
- Business Logic Layer
- Persistence Layer

The Facade pattern is used to provide a single entry point from the Presentation Layer to the Business Logic Layer.

---

## Package Structure

### Presentation Layer
- APIController  
Responsible for handling incoming API requests and forwarding them to the Business Logic Layer.

---

### Business Logic Layer
- HBnBFacade  
- UserService  
- PlaceService  
- ReviewService  
- AmenityService  

Contains the core application logic and business rules.
The HBnBFacade acts as an intermediary between the Presentation Layer and the internal services.

---

### Persistence Layer
- UserRepository  
- PlaceRepository  
- ReviewRepository  
- AmenityRepository  
- Database  

Responsible for data storage and retrieval.
Repositories abstract database access from the business logic.

---

## Communication Flow

1. The Presentation Layer receives client requests.
2. Requests are forwarded to the Business Logic Layer through the HBnBFacade.
3. The Facade delegates operations to the appropriate service.
4. Services interact with repositories in the Persistence Layer.
5. Data is stored or retrieved from the database.
6. The response flows back to the client.

---

## Design Pattern Used

- Facade Pattern  
Used to simplify communication between the Presentation Layer and the Business Logic Layer by exposing a unified interface.

## Package Diagram

![High-Level Package Diagram](High-Level-Package-Diagram.png)

