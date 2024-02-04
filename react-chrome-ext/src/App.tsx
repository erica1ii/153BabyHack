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

  const [allSubmissions, setAllSubmissions] = useState<{ title: string; priority: string; date: string; hours: number; }[]>([]);

  // Handle form submission
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    // if (isNaN(hoursNeeded)) {
    //   console.error('Please enter a valid number for hours');
    //   return; // Prevent submission if hoursNeeded is NaN
    // }

    const newSubmission = {
      title: name,
      priority: selectedOption,
      date: selectedDate,
      hours: hoursNeeded
    };

    setAllSubmissions([...allSubmissions, newSubmission]);

    setName('');
    setSelectedOption('');
    setSelectedDate('');
    setSelectedHours(0);
  };

  const handleFinalSubmit = async () => {
    // try {
    //   // Send all submissions to the backend
    //   const response = await fetch('/scheduling_tasks', {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify(allSubmissions)
    //   });
    //   // Check if request was successful
    //   if (response.ok) {
    //     console.log('All form data sent successfully');
    //     // Clear all submissions after successful upload
    //     setAllSubmissions([]);
    //   } else {
    //     console.error('Failed to send form data:', response.statusText);
    //   }
    // } catch (error) {
    //   console.error('Error sending form data:', error);
    // }
    try {
      // Send all submissions to the backend
      await fetch('http://localhost:4000/scheduling_tasks', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(allSubmissions)
      });
      console.log('All form data sent successfully');
      // Clear all submissions after successful upload
      setAllSubmissions([]);
    } catch (error) {
      console.error('Error sending form data:', error);
    }
  };


  return (
    <div>
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
            <option value="option1">Need to be done ASAP</option>
            <option value="option2">Very Important!</option>
            <option value="option3">Important</option>
            <option value="option4">Not Important</option>
            <option value="option5">Not a Rush</option>
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
            type="number"
            step="1"
            value={hoursNeeded}
            onChange={(event: React.ChangeEvent<HTMLInputElement>) => setSelectedHours(parseInt(event.target.value))}
          />
        </label>
        <br />
        <button type="submit">Add Task</button>
      </form>

      {allSubmissions.length > 0 && (
        <button onClick={handleFinalSubmit}>Schedule All Tasks</button>
      )}
    </div>
  );
}

function App() {
  return (
    <div className='bColor'>
      <div className="App">
        <Header title="cosmos"></Header>
        <p>Enter tasks as needed. For each task, input the name, priority where 1
          is the highest, date the task is due, and number of expected hours the
          task should take.
        </p>
      </div>
      <MyForm /> {/* Render the MyForm component here */}
    </div>
  );
}



export default App;
