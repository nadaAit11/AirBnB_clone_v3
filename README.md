# AirBnB clone - The console

![hbnb_stack](https://github.com/nadaAit11/AirBnB_clone_v2/assets/121446147/3a3b1952-4fd4-4999-9e7c-1344e927a6ad)

## Desciption 
AirBnB clone is a featuring database storage, a back-end API, and front-end interfacing in a clone of AirBnB. The project currently implements the back-end console.


## Classes 🆑
HBnB utilizes the following classes:
- BaseModel
- FileStorage
- User
- State
- City
- Amenity
- Place
- Review

### PUBLIC INSTANCE ATTRIBUTES
- id
- created_at
- updated_at


### PUBLIC INSTANCE METHODS
- save
- to_dict
- all
- new
- save
- reload

### PUBLIC CLASS ATTRIBUTES
- email
- password
- first_name
- last_name
- name
- state_id
- name
- city_id
- user_id
- name
- description
- number_rooms
- number_bathrooms
- max_guest
- price_by_night
- latitude
- longitude
- amenity_ids
- place_id
- user_id
- text

### PRIVATE CLASS ATTRIBUTES
- file_path
- objects

## Storage 🛄
The above classes are managed by the abstracted storage engine defined in the FileStorage class. The storage object is loaded/re-loaded from the JSON file file.json as class instances are created, updated, or deleted.

## Console 💻
The console is a command-line interpreter for managing the backend of HolbertonBnB. It can handle and manipulate all classes utilized by the application through calls on the storage object defined above.

## Console Commands
The HBNB console supports the following commands:
- create
- show
- destory
- all
- count
- update

## How to use : 
Your shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Testing 📏
Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:
```bash
$ python3 -m unittest discover tests
```
## Authors ✒️
- NAZIH TOUIH (NEAZYIT)
- NADA AIT KIDAR (nadaAit11) 
