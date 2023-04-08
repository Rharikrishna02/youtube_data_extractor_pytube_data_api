import React,{useState} from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './UInput.css';

function UInput(){
    const [mlink,setmLink]=useState('');
  const [mail,setmail]=useState('');
  const navigate=useNavigate();
  const send = ()=>{
    axios.post('http://127.0.0.1:5000',{
      ylink:mlink,
      umail:mail
    }).then((response)=>{
      console.log("Success");
      alert("Success");
    });
	navigate('/success');
    alert('Success');
  }
  return (
    <div>
<div class="container" id="container">
	<div class="form-container sign-in-container">
		<form onSubmit={send}>
			<h1>YouTube Data Extractor</h1>
			
			<span>Enter the video link of any channel you want to Search</span>
			<input type="url" onChange={(e)=>{setmLink(e.target.value);}} placeholder="Enter Video URL"/>
			<input type="email" onChange={(e)=>{setmail(e.target.value);}} placeholder="Enter Your Email" />
			
			<button type="submit">Submit</button>
		</form>
	</div>
	<div class="overlay-container">
		<div class="overlay">
			
			<div class="overlay-panel overlay-right">
				<h1>Guidelines</h1>
				<p>
					<ol>
						<li>Enter the URL of any YouTube video you want to search</li>
						<li>Enter your email id</li>
						<li>Just Click Submit</li>
						<li>Report about the Channel will be sent to the mail id you have entered</li>
					</ol>
				</p>
			</div>
		</div>
	</div>
</div>
<footer>
	<p>
		Created by      
		<a styles="margin-left:10px;" rel="noreferrer" target="_blank" href="https://www.linkedin.com/in/harikrishna-r-1a034a221/">HARIKRISHNA R</a>
		- Contact
		<a target="_blank" rel="noreferrer" href="mailto:rharikrishna02@gmail.com">here</a>.
	</p>
</footer>


    </div>
  );
}
export default UInput;