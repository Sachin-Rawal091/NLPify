<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>NLPify</title>

<style>
    body {
        margin: 0;
        font-family: 'Segoe UI', sans-serif;
        background: #0f172a;
        color: #e2e8f0;
    }

    .container {
        width: 85%;
        margin: auto;
        padding: 20px;
    }

    h1 {
        text-align: center;
        font-size: 40px;
        background: linear-gradient(90deg, #38bdf8, #6366f1);
        -webkit-background-clip: text;
        color: transparent;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 40px;
    }

    .card {
        background: #1e293b;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 25px;
        transition: 0.3s;
        box-shadow: 0 5px 15px rgba(0,0,0,0.4);
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.6);
    }

    h2 {
        color: #38bdf8;
        border-bottom: 1px solid #334155;
        padding-bottom: 5px;
    }

    ul {
        padding-left: 20px;
        line-height: 1.8;
    }

    code {
        background: #020617;
        padding: 6px 10px;
        border-radius: 6px;
        color: #38bdf8;
    }

    .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
    }

    .badge {
        display: inline-block;
        background: #334155;
        padding: 6px 12px;
        margin: 5px;
        border-radius: 20px;
        font-size: 14px;
    }

    .footer {
        text-align: center;
        margin-top: 40px;
        color: #64748b;
        font-size: 14px;
    }
</style>
</head>

<body>

<div class="container">

    <h1>NLP Multi Analyzer</h1>
    <p class="subtitle">
        Smart NLP-powered text analysis with a clean GUI — built for extensibility
    </p>

    <div class="card">
        <h2>Overview</h2>
        <p>
            A desktop-based Natural Language Processing (NLP) application built with Python and Tkinter.
            It enables users to analyze text using multiple NLP techniques in an intuitive interface.
        </p>
        <p>
            The system is modular and designed for future expansion with advanced NLP capabilities.
        </p>
    </div>

    <div class="card">
        <h2>Core Features</h2>
        <div class="grid">
            <div class="badge">User Authentication</div>
            <div class="badge">Sentiment Analysis</div>
            <div class="badge">Emotion Detection</div>
            <div class="badge">NER</div>
            <div class="badge">GUI Interface</div>
            <div class="badge">API Integration</div>
        </div>
    </div>

    <div class="card">
        <h2>Technology Stack</h2>
        <ul>
            <li>Python</li>
            <li>Tkinter GUI</li>
            <li>Custom Database Module</li>
            <li>NLP APIs</li>
        </ul>
    </div>

    <div class="card">
        <h2>Project Structure</h2>
<pre>
NLPAPP/
│
├── main.py
├── mydb.py
├── myapi.py
├── Resource/
└── README
</pre>
    </div>

    <div class="card">
        <h2>Run Application</h2>
        <p>Execute the following command:</p>
        <code>python main.py</code>
    </div>

    <div class="card">
        <h2>Future Scope</h2>
        <ul>
            <li>Text Summarization</li>
            <li>Language Translation</li>
            <li>Chatbot Integration</li>
            <li>Offline NLP Models</li>
        </ul>
    </div>

    <div class="card">
        <h2>Author</h2>
        <p>Sachin Rawal</p>
    </div>

    <div class="footer">
        <p>Built for learning, experimentation, and future NLP innovation.</p>
    </div>

</div>

</body>
</html>
