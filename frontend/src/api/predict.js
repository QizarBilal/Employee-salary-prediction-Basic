import axios from "axios";

const API_URL = "http://localhost:5000/predict"; // Change for deployment

async function predictSalary(data) {
  try {
    const response = await axios.post(API_URL, data);
    return response.data.prediction;
  } catch (error) {
    console.error("Prediction Error:", error);
    return "Error";
  }
}

export default predictSalary;