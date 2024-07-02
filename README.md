# UML Class Diagram
+-----------------+
|     Engine      |    (Abstract)
+-----------------+
| - mileage       |
+-----------------+
| + needs_service() : bool |
+-----------------+
       ^
       |
+-----------------+        +-------------------+
|  CapuletEngine  |        | WilloughbyEngine  |
+-----------------+        +-------------------+
| + needs_service() : bool | + needs_service() : bool |
+-----------------+        +-------------------+
       ^
       |
+-----------------+
| SternmanEngine  |
+-----------------+
| + needs_service() : bool |
+-----------------+

+-----------------+
|     Battery     |    (Abstract)
+-----------------+
| - last_service_date |
+-----------------+
| + needs_service() : bool |
+-----------------+
       ^
       |
+-----------------+        +-----------------+
| SpindlerBattery |        | NubbinBattery   |
+-----------------+        +-----------------+
| + needs_service() : bool | + needs_service() : bool |
+-----------------+        +-----------------+

+-----------------+
|      Car        |
+-----------------+
| - engine        |
| - battery       |
+-----------------+
| + needs_service() : bool |
+-----------------+

+-----------------+
| ServiceCriteria |
+-----------------+
| + evaluate(engine) : bool |
| + evaluate(battery) : bool |
+-----------------+


[![Model Answer](https://img.shields.io/badge/Lyft-Answer)](https://github.com/vagabond-systems/forage-lyft-task-2-model-answer)

