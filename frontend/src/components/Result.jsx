import React from "react";

function Result({ result }) {
  return (
    <div className="mt-10 text-center bg-[color:var(--card-bg)] border border-[color:var(--card-border)] p-6 rounded-xl shadow-lg transition-all duration-300">
      <h2 className="text-lg font-semibold text-[color:var(--text-color)] tracking-wide">
        Predicted Salary:
      </h2>
      <p
        className={`text-3xl font-extrabold mt-4 ${
          result === ">50K"
            ? "text-green-500"
            : "text-red-500"
        }`}
      >
        {result}
      </p>
    </div>
  );
}

export default Result;