// import React from 'react';
// import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react'; 
import Header from './Header';

function MyForm() {
  // Define state variables for each form field
  const [name, setName] = useState('');
  const [selectedOption, setSelectedOption] = useState('');
  const [selectedDate, setSelectedDate] = useState('');

  // Handle form submission
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    // Do something with the form data (e.g., submit it to a server)
    console.log({ name ,selectedOption, selectedDate});
    // Clear the form fields
    setName('');
    setSelectedOption('');
    setSelectedDate('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Task:
        <input
          type="text"
          value={name}
          onChange={(event) => setName(event.target.value)}
        />
      </label>
      <br />
      <label>
        Select Option:
        <select
          value={selectedOption}
          onChange={(event) => setSelectedOption(event.target.value)}
        >
          <option value="">--Select--</option>
          <option value="option1">Option 1</option>
          <option value="option2">Option 2</option>
          <option value="option3">Option 3</option>
          <option value="option4">Option 4</option>
          <option value="option5">Option 5</option>
        </select>
      </label>
      <br />
      <label>
        Select Date:
        <input
          type="date"
          value={selectedDate}
          onChange={(event) => setSelectedDate(event.target.value)}
        />
      </label>
      <br />
      <button type="submit">Submit</button>
    </form>
  );
}

function App() {
  return (
    <div className='bColor'>
    <div className="App">
      <Header title="cosmos1"></Header>
    </div>
    <MyForm /> {/* Render the MyForm component here */}
    </div>
  );
}



export default App;
