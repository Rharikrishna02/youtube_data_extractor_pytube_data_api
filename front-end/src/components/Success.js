import React from 'react';
import {Link} from 'react-router-dom';

function Success(){
    return(
        <div>
            <div id="container">
  <div id="success-box">
    <div class="dot"></div>
    <div class="dot two"></div>
    <div class="face">
      <div class="eye"></div>
      <div class="eye right"></div>
      <div class="mouth happy"></div>
    </div>
    <div class="shadow scale"></div>
    <div class="message"><h1 class="alert">Success!</h1><p>The report will be mailed to you within 30 minutes</p></div>
    <Link to="/"><button class="button-box"><h1 class="green">Return</h1></button></Link>
  </div></div>
        </div>
    )
}
export default Success;