const faqs = {
    "ai general chatbot": "chatgpt.com",
    "ai specialized about a youtube video or websites or your content": "notebooklm.google"
};


function tokenize(text) {
    return text.toLowerCase().split(/\W+/).filter(Boolean);
}

function getTF(tokens) {
    const tf = {};
    tokens.forEach(token => {
        tf[token] = (tf[token] || 0) + 1;
    });
    return tf;
}

const faqVectors = {};
const faqTokens = {};
Object.keys(faqs).forEach(question => {
    const tokens = tokenize(question);
    faqTokens[question] = tokens;
    faqVectors[question] = getTF(tokens);
});

function cosineSimilarity(vecA, vecB) {
    const allTokens = new Set([...Object.keys(vecA), ...Object.keys(vecB)]);
    let dotProduct = 0;
    let magA = 0;
    let magB = 0;
    allTokens.forEach(token => {
        const a = vecA[token] || 0;
        const b = vecB[token] || 0;
        dotProduct += a * b;
        magA += a * a;
        magB += b * b;
    });
    if (magA === 0 || magB === 0) return 0;
    return dotProduct / (Math.sqrt(magA) * Math.sqrt(magB));
}

function findWebsite() {
    const userInput = document.getElementById('questionInput').value.trim();
    if (!userInput) {
        document.getElementById('answer').innerText = "please enter a question";
        return;
    }
    const s = document.getElementById('questionInput').value = "";
    const userTokens = tokenize(userInput);
    const userTF = getTF(userTokens);

    let maxSim = 0;
    let bestQuestion = null;

    Object.keys(faqs).forEach(question => {
        const sim = cosineSimilarity(userTF, faqVectors[question]);
        if (sim > maxSim) {
            maxSim = sim;
            bestQuestion = question;
        }
    });

    if (maxSim > 0.3) {
        document.getElementById('answer').innerText = faqs[bestQuestion];
    } else {
        document.getElementById('answer').innerText = "Sorry, I don't know that yet.";
    }
}



const input = document.getElementById('questionInput');

input.addEventListener('keydown', function(event) {
if (event.key === 'Enter') {
    event.preventDefault();
    findWebsite();
}
});

