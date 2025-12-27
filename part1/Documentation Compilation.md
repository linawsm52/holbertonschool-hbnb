# HBnB Evolution – Technical Design Document

## 1. Introduction
This part focuses on creating comprehensive technical documentation for the HBnB Evolution application. The goal is to provide a clear and detailed blueprint that will guide the implementation phases in later parts of the project.  

This documentation describes the system architecture, business logic design, and interactions between components using UML diagrams.

### 1.a Scope
This documentation covers:  
- System architecture design  
- Business logic modeling  
- Documentation of entities and relationships  

**Purpose:**  
To provide developers with a clear reference for how the system is structured, how components interact, and how business rules are enforced.  

---

## 2. High-Level Architecture

### 2.a Architecture Overview
The application follows a **three-layer architecture**:

1. **Presentation Layer:**  
   - Handles user interactions and API requests.  
   - Example: Receiving HTTP requests from a web or mobile client.

2. **Business Logic Layer:**  
   - Contains core models, entities, and business rules.  
   - Example: Validating user inputs, managing bookings, calculating ratings.

3. **Persistence Layer:**  
   - Responsible for data storage and retrieval.  
   - Example: Storing user accounts, listings, and reviews in the database.  

**Benefits of this architecture:**  
- Separation of concerns  
- Easier maintenance and testing  
- Scalability and modularity  

### 2.b High-Level Package Diagram
<img width="1536" height="1024" alt="High-Level Package Diagram" src="https://github.com/user-attachments/assets/853fba1a-6765-4e11-aff6-d05b96ac0c33" />

### Purpose
This high-level package diagram provides an overview of the HBnB system architecture.  
It illustrates how the application is structured into layers and how responsibilities are separated to ensure maintainability and scalability.

### Why This Diagram Is Important
- Helps understand the overall system structure before diving into implementation.
- Clearly separates concerns between presentation, business logic, and data persistence.
- Simplifies communication between layers by enforcing architectural boundaries.
- Serves as a reference for future development and team collaboration.

### How It Works
1. The **Presentation Layer** receives client requests through API endpoints.
2. Requests are forwarded to the **Business Logic Layer** via the `HBnBFacade`.
3. The facade delegates operations to the appropriate service.
4. Services interact with repositories in the **Persistence Layer**.
5. Repositories handle data storage and retrieval from the database.
6. Results are returned through the same flow to the client.

### Notes
- The Facade pattern is used to provide a single entry point between the Presentation and Business Logic layers.
- The Business Logic layer does not directly access the database.
- All database interactions are handled exclusively by the Persistence layer.

 

---

## 3. Business Logic Layer
### Class Diagram
This layer contains the core business models and rules for managing **users, places, reviews, and amenities**. 

### Key Entities
- **User:** Represents system users.
- **Place:** Represents properties.  
- **Review:** Stores feedback and ratings for places.  
- **Amenity:** Represents features available at places.

*<img width="842" height="617" alt="لقطة شاشة 2025-12-22 143549" src="https://github.com/user-attachments/assets/ef49d6c9-c370-4ce8-964c-d6e25214cacb" />
* 



**Notes:**  
 ### Relationships
| Relationship | Description |
|--------------|-------------|
| User 1 --- * Place | A user can own multiple places |
| User 1 --- * Review | A user can write multiple reviews |
| Place 1 --- * Review | A place can have multiple reviews |
| Place * --- * Amenity | Many-to-many; a place can have multiple amenities |

---

## 4. API Interaction Flow

<img width="1232" height="1302" alt="user_registration" src="https://github.com/user-attachments/assets/df60cff6-bdc6-4f72-8dac-12447b0d7384" />

1. User Registration

Describes the process of registering a new user.

The user sends a request to the API.

The service validates the user data.

User data is saved in the database.

A successful response (201 Created) is returned to the user.

<img width="1212" height="802" alt="place_creation" src="https://github.com/user-attachments/assets/dcb5f63d-ef16-4eae-bf97-48eedf1db9f3" />
 
2. Place Creation

Describes the creation of a new place.

The user sends a create place request to the API.

The service validates place data.

Place data is stored in the database.

A success response (201 Created) is returned.
 
<img width="1242" height="802" alt="review_submission" src="https://github.com/user-attachments/assets/91a89f41-2d1f-40f8-a686-241b44f5fc95" />
 
3. Review Submission

Describes submitting a review for a place.

The user sends a review request through the API.

The service validates the review data.

The review is saved in the database.

A Success response is returned to the user.
  
<img width="1272" height="822" alt="fetch_places" src="https://github.com/user-attachments/assets/80025aa1-1d15-4563-aeaa-2f826eeaf2a4" />
 
4. Fetching a List of Places

Describes fetching a list of places.

The user sends a request to retrieve places.

The service fetches data from the database.

A list of places is returned to the user.  

**Notes**
Each diagram shows the interaction flow between system layers:
User → API → Service → Database
The diagrams focus on request flow rather than implementation details.
---

  
