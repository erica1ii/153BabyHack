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
  const [hoursNeeded, setSelectedHours] = useState(0);

  // Handle form submission
  const handleSubmit = async(event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    //han
    const formData = new FormData();
    formData.append('title', name);
    formData.append('priority', selectedOption);
    formData.append('date', selectedDate);
    formData.append('hours', String(hoursNeeded));

    

    try {
      // Send form data to the Flask backend
      const response = await fetch('/add_tasks', {
        method: 'POST',
        body: formData
      });

      // Check if request was successful
      if (response.ok) {
        console.log('Form data sent successfully');
        // Clear form fields
        setName('');
        setSelectedOption('');
        setSelectedDate('');
        setSelectedHours(0);
      } else {
        console.error('Failed to send form data:', response.statusText);
      }
    } catch (error) {
      console.error('Error sending form data:', error);
    }
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
          <option value="option1">Priority 1</option>
          <option value="option2">Priority 2</option>
          <option value="option3">Priority 3</option>
          <option value="option4">Priority 4</option>
          <option value="option5">Priority 5</option>
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
      <label>
        Hours:
        <input
          type="number" // Use type "number" for integer input
          value={hoursNeeded}
          onChange={(event: React.ChangeEvent<HTMLInputElement>) => setSelectedHours(parseInt(event.target.value))}
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
