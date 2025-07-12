import React, { useState } from "react";
import predictSalary from "../api/predict";

const initialState = {
  age: "",
  workclass: "",
  fnlwgt: "",
  education: "",
  "education-num": "",
  "marital-status": "",
  occupation: "",
  relationship: "",
  race: "",
  sex: "",
  "capital-gain": "",
  "capital-loss": "",
  "hours-per-week": "",
  "native-country": "",
};

function Form({ setResult }) {
  const [formData, setFormData] = useState(initialState);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const res = await predictSalary(formData);
    setResult(res);
    setLoading(false);
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="grid grid-cols-1 md:grid-cols-2 gap-4 bg-[color:var(--card-bg)] p-6 rounded-2xl shadow-xl border border-[color:var(--card-border)] transition-all duration-300"
    >
      {Object.keys(initialState).map((key) => (
        <div key={key} className="flex flex-col">
          <label
            htmlFor={key}
            className="mb-1 text-sm font-medium text-[color:var(--text-color)]"
          >
            {key.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase())}
          </label>
          <input
            id={key}
            name={key}
            value={formData[key]}
            onChange={handleChange}
            placeholder={key}
            required
            className="p-2 rounded-lg bg-[color:var(--input-bg)] text-[color:var(--input-text)] border border-[color:var(--input-border)] focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
          />
        </div>
      ))}

      <div className="md:col-span-2 text-center mt-4">
        <button
          type="submit"
          disabled={loading}
          className="bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white py-2 px-6 rounded-full shadow-md transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? "Predicting..." : "Predict Salary"}
        </button>
      </div>
    </form>
  );
}

export default Form;