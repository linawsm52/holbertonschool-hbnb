@startuml
skinparam packageStyle rectangle
left to right direction

package "Presentation Layer" {
  class APIController
}

package "Business Logic Layer" {
  class HBnBFacade
  class UserService
  class PlaceService
  class ReviewService
  class AmenityService
}

package "Persistence Layer" {
  class UserRepository
  class PlaceRepository
  class ReviewRepository
  class AmenityRepository
  class Database
}

APIController ..> HBnBFacade : uses (Facade)

HBnBFacade ..> UserService
HBnBFacade ..> PlaceService
HBnBFacade ..> ReviewService
HBnBFacade ..> AmenityService

UserService ..> UserRepository
PlaceService ..> PlaceRepository
ReviewService ..> ReviewRepository
AmenityService ..> AmenityRepository

UserRepository ..> Database
PlaceRepository ..> Database
ReviewRepository ..> Database
AmenityRepository ..> Database

@enduml
