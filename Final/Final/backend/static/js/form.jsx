import React, { useState } from 'react';
import './App.css'; // Import your CSS file

function App() {
  const [formData, setFormData] = useState({
    X2: '',
    X3: '',
    X4: '',
    X5: '11th',
    X6: '',
    X7: 'No',
    X8: 'No',
    X9: 'No change',
    X10: 'No',
    X11: 'No',
    X12: 'No',
    X13: 'No',
    X14: 'No',
    X15: 'No change',
    X16: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission here
    console.log(formData); // For testing, you can log the form data
  };

  return (
    <div className="App">
      <header>
        <h1>Student Mental Wellness Survey</h1>
      </header>
      <main>
        <p>Welcome to our Student Mental Health Prediction AI project! We're working on creating an AI model to predict
          mental health issues among students. Your participation in this survey will greatly assist us in developing a
          tool that can identify signs of depression and anxiety early on. Rest assured, all information you provide
          will be kept strictly confidential. Your responses will help us understand the challenges students face and
          improve mental health support services. Thank you for taking the time to contribute to this important
          endeavor!</p><br /><br />

        <form id="surveyForm" onSubmit={handleSubmit}>
          <label htmlFor="X2">1. Age:</label>
          <input type="number" id="X2" name="X2" value={formData.X2} onChange={handleChange} required /><br /><br />

          <label htmlFor="X3">2. Which state are you from?</label>
          <input type="text" id="X3" name="X3" value={formData.X3} onChange={handleChange} required /><br /><br />

          <label>3. Gender:</label><br />
          <input type="radio" id="male" name="X4" value="Male" onChange={handleChange} required />
          <label htmlFor="male">Male</label>
          <input type="radio" id="female" name="X4" value="Female" onChange={handleChange} required />
          <label htmlFor="female">Female</label>
          <input type="radio" id="other" name="X4" value="Others" onChange={handleChange} required />
          <label htmlFor="others">Others</label>
          <input type="radio" id="preferNotToSay" name="X4" value="Prefer Not To Say" onChange={handleChange} required />
          <label htmlFor="preferNotToSay">Prefer not to say</label><br /><br />

          <label htmlFor="X5">4. Grade Level/Year in School:</label>
          <select id="X5" name="X5" value={formData.X5} onChange={handleChange} required>
            <option value="11th">11th</option>
            <option value="12th">12th</option>
            <option value="Bachelor's 1st Year">Bachelor's 1st Year</option>
            <option value="Bachelor's 2nd Year">Bachelor's 2nd Year</option>
            <option value="Bachelor's 3rd Year">Bachelor's 3rd Year</option>
            <option value="Bachelor's 4th Year">Bachelor's 4th Year</option>
            <option value="Others">Others</option>
          </select><br /><br />

          <label htmlFor="X6">5. What are you currently studying?</label>
          <input type="text" id="X6" name="X6" value={formData.X6} onChange={handleChange} /><br /><br />

          

            <label for="X7">6. How often have you been feeling sad or hopeless in the past two weeks?</label>
            <select id="X7" name="X7" required>
                <option value="No">No</option>
                <option value="Rarely">Rarely</option>
                <option value="Sometimes">Sometimes</option>
                <option value="Often">Often</option>
                <option value="Everyday">Everyday</option>
            </select><br /><br />

            <label for="X8">7. How often have you been feeling nervous, anxious, or on edge in the past two
                weeks?</label>
            <select id="X8" name="X8" required>
                <option value="No">No</option>
                <option value="Rarely">Rarely</option>
                <option value="Sometimes">Sometimes</option>
                <option value="Often">Often</option>
                <option value="Everyday">Everyday</option>
            </select><br /><br />

            <label for="X9">8. Have you experienced changes in your appetite or weight in the past two weeks?</label>
            <select id="X9" name="X9" required>
                <option value="No change">No Change</option>
                <option value="Increased appetite">Increased Appetite</option>
                <option value="Decreased appetite">Decreased Appetite</option>
                <option value="Weight gain">Weight Gain</option>
                <option value="Weight loss">Weight Loss</option>
            </select><br /><br />

            <label for="X10">9. Have you had trouble sleeping in the past two weeks?</label>
            <select id="X10" name="X10" required>
                <option value="No">No</option>
                <option value="Rarely">Rarely</option>
                <option value="Sometimes">Sometimes</option>
                <option value="Often">Often</option>
                <option value="Everyday">Everyday</option>
            </select><br /><br />

            <label for="X11">10. Have you been feeling unusually fatigued or lacking in energy in the past two weeks?</label>
            <select id="X11" name="X11" required>
                <option value="No">No</option>
                <option value="Rarely">Rarely</option>
                <option value="Sometimes">Sometimes</option>
                <option value="Often">Often</option>
                <option value="Everyday">Everyday</option>
            </select><br /><br />

            <label for="X12">11. Have you had trouble concentrating in the past two weeks?</label>
            <select id="X12" name="X12" required>
                <option value="No">No</option>
                <option value="Rarely">Rarely</option>
                <option value="Sometimes">Sometimes</option>
                <option value="Often">Often</option>
                <option value="Everyday">Everyday</option>
            </select><br /><br />

            <label for="X13">12. Have you had recurring thoughts of death or suicide in the past two weeks?</label>
            <select id="X13" name="X13" required>
                <option value="No">No</option>
                <option value="Rarely">Rarely</option>
                <option value="Sometimes">Sometimes</option>
                <option value="Often">Often</option>
                <option value="Everyday">Everyday</option>
            </select><br /><br />

            <label for="X14">13. Have you experienced any physical symptoms in the past two weeks?</label>
            <select id="X14" name="X14" required>
                <option value="No">No</option>
                <option value="Rarely">Rarely</option>
                <option value="Sometimes">Sometimes</option>
                <option value="Often">Often</option>
                <option value="Everyday">Everyday</option>
            </select><br /><br />

            <label for="X15">14. Have you noticed any changes in your academic performance or attendance due to
                emotional distress in the past two weeks?</label>
            <select id="X15" name="X15" required>
                <option value="No change">No Change</option>
                <option value="Slight decline">Slight Decline</option>
                <option value="Significant decline">Significant Decline</option>
            </select><br /><br />

            <label for="X16">15. Is there anything else you would like to share about your emotional well-being
                or any concerns you have?</label>
            <textarea id="X16" name="X16" rows="4" cols="50"></textarea><br /><br />

            <input type="submit" value="Submit" />

          
        </form>
        <div id="predictionDiv"></div>
      </main>
    </div>
  );
}

export default App;
