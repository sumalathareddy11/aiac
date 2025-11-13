import React, { useState } from "react";

// ✅ AI-Assisted Education Frontend Generator
// -------------------------------------------
// This component takes input from users (site details) and generates
// an HTML education layout using an AI-assisted (mock) generator.
// You can replace the mock logic with an actual AI API call.

export default function EduAIGenerator() {
  const [title, setTitle] = useState("My Course Platform");
  const [primaryColor, setPrimaryColor] = useState("#4f46e5");
  const [numSections, setNumSections] = useState(3);
  const [audience, setAudience] = useState("High school students");
  const [features, setFeatures] = useState("lessons, quizzes, progress tracking");
  const [outputHtml, setOutputHtml] = useState("");
  const [loading, setLoading] = useState(false);

  // --- Mock AI Generator Function ---
  function mockAIGenerate({ title, primaryColor, numSections, audience, features }) {
    const sections = [];
    for (let i = 1; i <= Math.max(1, Number(numSections)); i++) {
      sections.push(`
        <section style="padding:24px; border-bottom:1px solid #eee">
          <h3 style="margin:0 0 8px 0">Lesson ${i}</h3>
          <p>Tailored for ${audience}: engaging, interactive, and fun!</p>
          <button style="background:${primaryColor};color:#fff;border:none;padding:8px 12px;border-radius:8px;">
            Start Lesson ${i}
          </button>
        </section>`);
    }

    return (`<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title}</title>
<style>
  body {font-family: Inter, sans-serif; margin:0; background:#f8fafc;}
  header {background:${primaryColor}; color:white; padding:24px; text-align:center;}
  main {max-width:800px; margin:30px auto; background:white; padding:24px; border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);}
  h2 {color:${primaryColor};}
</style>
</head>
<body>
  <header>
    <h1>${title}</h1>
    <p>An educational experience for ${audience}</p>
    <small>Features: ${features}</small>
  </header>
  <main>
    <h2>Course Overview</h2>
    ${sections.join("\n")}
  </main>
</body>
</html>`);
  }

  // --- Generate HTML using AI ---
  const handleGenerate = async () => {
    setLoading(true);
    try {
      const html = mockAIGenerate({ title, primaryColor, numSections, audience, features });
      setOutputHtml(html);
    } catch (err) {
      setOutputHtml(`<pre>Error: ${err?.message || String(err)}</pre>`);
    } finally {
      setLoading(false);
    }
  };

  // --- Download Generated File ---
  const handleDownload = () => {
    if (!outputHtml) return;
    try {
      const blob = new Blob([outputHtml], { type: "text/html" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      const safeName = (title || "site").replace(/[^\w\d-_]+/g, "_").replace(/^_+|_+$/g, "");
      a.download = `${safeName || "site"}.html`;
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);
    } catch (err) {
      // eslint-disable-next-line no-console
      console.error("Download failed", err);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-2xl font-semibold mb-4 text-indigo-700">
          🎓 AI-Assisted Education Frontend Generator
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* Left: Input Form */}
          <div className="space-y-3">
            <label className="block">
              Site Title
              <input
                aria-label="Site title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                className="mt-1 w-full p-2 rounded border"
              />
            </label>

            <label className="block">
              Primary Color (hex)
              <input
                aria-label="Primary color"
                value={primaryColor}
                onChange={(e) => setPrimaryColor(e.target.value)}
                className="mt-1 w-full p-2 rounded border"
              />
            </label>

            <label className="block">
              Number of Sections
              <input
                type="number"
                min={1}
                value={numSections}
                onChange={(e) => setNumSections(Number(e.target.value) || 1)}
                className="mt-1 w-full p-2 rounded border"
              />
            </label>

            <label className="block">
              Target Audience
              <input
                aria-label="Target audience"
                value={audience}
                onChange={(e) => setAudience(e.target.value)}
                className="mt-1 w-full p-2 rounded border"
              />
            </label>

            <label className="block">
              Features
              <input
                aria-label="Features"
                value={features}
                onChange={(e) => setFeatures(e.target.value)}
                className="mt-1 w-full p-2 rounded border"
              />
            </label>

            <div className="flex gap-2">
              <button
                type="button"
                onClick={handleGenerate}
                disabled={loading}
                className="px-4 py-2 bg-indigo-600 text-white rounded"
              >
                {loading ? "Generating..." : "Generate"}
              </button>
              <button
                type="button"
                onClick={handleDownload}
                disabled={!outputHtml}
                className="px-4 py-2 border rounded"
              >
                Download HTML
              </button>
            </div>
          </div>

          {/* Right: Output Preview */}
          <div>
            <h2 className="font-medium text-gray-700">Generated Output (Preview)</h2>
            <div className="mt-2 h-96 overflow-auto border rounded bg-white p-3">
              {outputHtml ? (
                <iframe
                  title="preview"
                  srcDoc={outputHtml}
                  style={{ width: "100%", height: "100%", border: "none" }}
                />
              ) : (
                <p className="text-gray-400">No output yet — click Generate.</p>
              )}
            </div>
          </div>
        </div>

        <p className="mt-6 text-sm text-gray-500">
          💡 *This mock AI generator can be integrated with OpenAI GPT APIs to
          create real-time educational website layouts.*
        </p>
      </div>
    </div>
  );
}
