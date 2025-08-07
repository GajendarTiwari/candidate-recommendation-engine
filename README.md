# 🔍 Candidate Recommendation Engine

A powerful AI-driven recruitment tool that automatically matches job descriptions with candidate resumes using advanced NLP techniques and generates personalized summaries and interview insights.

## ✨ Features

- **Smart Resume Matching**: Uses TF-IDF vectorization and cosine similarity to rank candidates
- **AI-Powered Candidate Summaries**: Generates intelligent 3-4 sentence summaries explaining why each candidate is a great fit for the role using Google's Gemini AI
- **Personalized Interview Questions**: Automatically creates 3 tailored, insightful interview questions for each candidate based on their resume and the job requirements
- **Multi-Format Support**: Handles PDF, DOCX, and TXT resume formats
- **User-Friendly Interface**: Clean Streamlit web interface with custom styling
- **Real-Time Processing**: Instant candidate ranking and analysis

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Gemini API key
- Required Python packages (see requirements below)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/sproutsai-candidate-engine.git
cd sproutsai-candidate-engine
```

2. Install dependencies:
```bash
pip install streamlit scikit-learn google-generativeai python-dotenv sentence-transformers PyMuPDF python-docx
```

3. Set up environment variables:
```bash
# Create a .env file in the project root
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
```

4. Run the application:
```bash
streamlit run main.py
```

## 📁 Project Structure

```
sproutsai-candidate-engine/
├── app.py                 # Main Streamlit application
├── gemini_summary.py       # AI summary and question generation
├── utils.py      # Document processing utilities
├── style.css              # Custom UI styling
├── .env                   # Environment variables (create this)
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🛠️ Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
GEMINI_API_KEY=your_google_gemini_api_key
```

### CSS Styling

The application uses custom CSS styling located in `style.css`. The path is already configured for GitHub deployment. The styling provides:
- Modern color scheme with professional blues and grays
- Hover effects for interactive elements
- Clean typography using Segoe UI font family
- Responsive button styling with smooth transitions

## 📋 Usage

1. **Start the Application**: Run `streamlit run main.py`
2. **Enter Job Description**: Paste the job requirements in the text area
3. **Upload Resumes**: Upload multiple candidate resumes (supports .txt, .pdf, .docx)
4. **Get Recommendations**: Click "🚀 Recommend Candidates" to process and rank candidates
5. **Review Results**: View similarity scores, AI-generated summaries, and interview questions for top 5 candidates

## 🔧 Key Components

### Resume Matching Algorithm

**TF-IDF (Term Frequency-Inverse Document Frequency) Vectorization:**
- **Term Frequency (TF)**: Measures how frequently a term appears in a document (resume or job description)
- **Inverse Document Frequency (IDF)**: Reduces the weight of common words that appear across many documents
- **Vectorization Process**: Converts text documents into numerical vectors where each dimension represents the TF-IDF score of a specific term
- **Benefits**: Automatically identifies important keywords while filtering out common stop words, creating meaningful numerical representations of text content

**Cosine Similarity Computation:**
- **Mathematical Foundation**: Measures the cosine of the angle between two vectors in multi-dimensional space
- **Range**: Produces similarity scores from 0 (completely different) to 1 (identical)
- **Advantage**: Focuses on the angle between vectors rather than magnitude, making it ideal for text comparison regardless of document length
- **Implementation**: Compares the job description vector against each resume vector to quantify semantic similarity
- **Ranking**: Candidates are ranked by their cosine similarity scores, with higher scores indicating better matches

**Why This Approach Works:**
- **Keyword Matching**: Identifies resumes containing relevant technical skills, tools, and industry terms
- **Context Awareness**: TF-IDF considers term importance across the entire corpus
- **Scalability**: Efficiently processes multiple resumes simultaneously
- **Objectivity**: Provides quantifiable, bias-free similarity measurements

### AI Integration & Analysis

- **Google Gemini AI Integration**: Powers intelligent candidate analysis and content generation
- **Contextual Candidate Summaries**: Analyzes job requirements against resume content to generate detailed fit assessments
- **Dynamic Interview Question Generation**: Creates role-specific, candidate-tailored interview questions that help recruiters identify the best matches
- **Natural Language Processing**: Understands context and nuances in both job descriptions and candidate profiles

### Document Processing

- **Multi-Format Support**: PDF, DOCX, and TXT file handling
- **Text Extraction**: Clean text extraction from various document formats
- **Encoding Handling**: Robust text encoding for international resumes

## 📊 Output Features

For each top candidate, the system provides:
- **Similarity Score**: Numerical match percentage based on TF-IDF and cosine similarity
- **AI-Generated Summary**: Intelligent 3-4 sentence assessment explaining why this candidate is an excellent fit for the role
- **Personalized Interview Questions**: 3 custom interview questions tailored to the candidate's background and job requirements

## 🔒 Security & Privacy

- Environment variables for secure API key storage
- Local file processing (no data sent to external servers except AI summaries)
- Temporary file handling with automatic cleanup

## 📈 Future Enhancements

- [ ] Add more AI models for comparison
- [ ] Implement candidate skill extraction
- [ ] Add email integration for automated outreach
- [ ] Include diversity and inclusion metrics
- [ ] Export results to various formats

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Google Gemini AI for intelligent text processing
- Streamlit for the amazing web framework
- scikit-learn for machine learning capabilities
- The open-source community for various libraries used

---

**Streamlit Deployment Link**: https://candidate-recommendation-engine-etuhohwsalajnbdfteknzt.streamlit.app/

