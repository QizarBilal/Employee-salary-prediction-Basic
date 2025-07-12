import React from "react";
import Form from "./components/Form";
import Result from "./components/Result";
import { useState } from "react";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="w-full max-w-xl bg-white rounded-2xl shadow-lg p-6 space-y-6">
        <h1 className="text-2xl font-bold text-center">Employee Salary Prediction</h1>
        <Form setResult={setResult} />
        {result && <Result result={result} />}
      </div>
    </div>
  );
}

export default App;