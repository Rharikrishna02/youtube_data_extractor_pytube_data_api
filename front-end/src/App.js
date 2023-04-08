import React from 'react';
import UInput from './components/UInput';
import {BrowserRouter as Router,Routes, Route } from "react-router-dom";
import Success from './components/Success';

function App() {
  return (
    <>
		{
        <Router>
          <Routes>
          <Route path="/" exact element={<UInput />} />
          <Route path="/success" element={<Success />} />
          
          </Routes>
        </Router>
        }
	</>
  );
}

export default App;
