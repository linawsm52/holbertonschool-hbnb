# High-Level Package Diagram

This diagram illustrates the high-level layered architecture of the HBnB application.
It shows how the Presentation, Business Logic, and Persistence layers interact using
the Facade pattern.

```mermaid
flowchart LR
    Presentation[Presentation Layer]
    Business[Business Logic Layer<br/>Facade]
    Persistence[Persistence Layer]

    Presentation --> Business
    Business --> Persistence

Explanation

The Presentation layer handles client requests and communicates with the Business
Logic layer through a Facade.

The Business Logic layer contains the core application logic and coordinates
interactions with the Persistence layer.

The Persistence layer is responsible for data storage and retrieval.
