package com.geocent.services.person.controllers;

import com.geocent.services.person.models.Person;
import com.geocent.services.person.repos.PersonRepository;
import java.util.ArrayList;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PersonController {
    
    @Autowired
    PersonRepository personRepository;

    @GetMapping(path = "/persons")
    public ArrayList<Person> getPersons() {
        return personRepository.findAll();
    }
}
