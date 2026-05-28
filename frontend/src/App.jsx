
import { useState } from "react";
import "./App.css";

function App() {
  const [code, setCode] = useState("");
  const [result, setResult] = useState("");

  const explainCode = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/explain", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          code: code,
        }),
      });

      const data = await response.json();
      setResult(data.explanation);
    } catch (error) {
      console.error(error);
      setResult("Error connecting to backend");
    }
  };

  return (
    <div className="container">
      <h1>AI Code Explainer</h1>

      <textarea
        rows="12"
        placeholder="Paste your code here..."
        value={code}
        onChange={(e) => setCode(e.target.value)}
      />

      <button onClick={explainCode}>Explain Code</button>

      <div className="result">
        <h2>Explanation</h2>
        <p>{result}</p>
      </div>
    </div>
  );
}

export default App;