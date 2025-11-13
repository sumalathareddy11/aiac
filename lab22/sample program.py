# app.py
import os
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# ----- AI integration stub -----
def call_ai_generate_component(prompt: str, framework: str = "react", accessibility: bool = True) -> dict:
    """
    Replace this stub with a real call to an LLM (OpenAI, Anthropic, local model).
    The function returns a dict containing keys: code (string), css (string), usage (string).
    """
    # Example simulated output for demo purposes:
    if "quiz" in prompt.lower():
        code = \"\"\"import React, {useState} from 'react';

export default function QuizCard({question, options, onAnswer}) {
  const [selected, setSelected] = useState(null);
  const [submitted, setSubmitted] = useState(false);

  function handleSubmit() {
    setSubmitted(true);
    if (onAnswer) onAnswer(selected);
  }

  return (
    <section role="region" aria-labelledby="quiz-title" className="quiz-card">
      <h2 id="quiz-title">Quiz</h2>
      <p>{question}</p>
      <ul role="list" aria-label="options" className="options">
        {options.map((o, i) => (
          <li key={i}>
            <label>
              <input
                type="radio"
                name="quiz"
                value={i}
                checked={selected === i}
                onChange={() => setSelected(i)}
                aria-checked={selected === i}
              />
              {o}
            </label>
          </li>
        ))}
      </ul>
      <button onClick={handleSubmit} disabled={selected === null} aria-disabled={selected === null}>
        Submit
      </button>
      {submitted && <div aria-live="polite">Answer received.</div>}
    </section>
  );
}
\"\"\"
        css = \".quiz-card{max-width:420px;margin:1rem;padding:1rem;border:1px solid #ccc}\n.options{list-style:none;padding:0}\n@media (max-width:480px){.quiz-card{padding:.5rem}}\"\n
        usage = \"\"\"// Usage example\n// <QuizCard question={'What is 2+2?'} options={['1','2','3','4']} onAnswer={(i)=>console.log(i)} />\"\"\"
        return {"code": code, "css": css, "usage": usage}
    # fallback simple card
    return {"code": "<div>Generated component</div>", "css": "", "usage": ""}

# ----- Endpoint -----
@app.route("/generate", methods=["POST"])
def generate():
    payload = request.get_json(force=True)
    prompt = payload.get("prompt", "")
    framework = payload.get("framework", "react")
    accessibility = payload.get("accessibility", True)
    # call AI (stub)
    result = call_ai_generate_component(prompt, framework, accessibility)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)