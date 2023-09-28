import React, { Component } from 'react';
import logo from './sev1tech-logo.png';
import './App.css';
import axios from 'axios';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      count: 0,
      persons: [],
      date: new Date()
    }
  }

  componentDidMount() {
    // Kubernetes nginx service endpoint
    let personServiceApiEndpoint = "http://localhost:30500"
    console.log(window.location.hostname)
    console.log(window.location.port)
    if (window.location.hostname === 'localhost' && window.location.port === '8000') {
      // Docker-compose nginx service endpoint
      personServiceApiEndpoint = "http://localhost:8000"
    }
    axios.get(`${personServiceApiEndpoint}/persons`)
      .then(res => {
        const persons = res.data;
        this.setState({ persons });
      })
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1>Sev1Tech Code Challenge</h1>

          <h3>Person Service Persons</h3>
          <ul>
            { this.state.persons.map(person => <li key={person.firstName}>{person.firstName} {person.lastName}</li>)}
          </ul>
          <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
        </header>
      </div>
    );
  }
}

export default App;
